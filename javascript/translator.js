const brailleToEnglish = {
    "O.....": "a", "O.....": "b", "O.O...": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number",
    ".O....": "1", ".OO...": "2", "O..O..": "3", "O..OO.": "4", "O..OOO": "5",
    "OOO...": "6", "O.OO..": "7", "O.OOO.": "8", ".O.O..": "9", ".O.OO.": "0",
    "......": " ", ".O..O.": ".", "..O.O.": ",", "..O...": "!", "..OO..": "?",
    "..OOO.": "'", "....O.": "-", "....OO": "/", "..OO.O": ":", "..OO..": ";",
    ".O.OO.": "<", ".OO.O.": ">", "....O.": "(", "....O.": ")", ".": "..."
};

const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "O..OO.", "5": "O..OOO",
    "6": "OOO...", "7": "O.OO..", "8": "O.OOO.", "9": ".O.O..", "0": ".O.OO.",
    " ": "......", ".": ".O..O.", ",": "..O.O.", "!": "..O...", "?": "..OO..",
    "'": "..OOO.", "-": "....O.", "/": "....OO", ":": "..OO.O", ";": "..OO..",
    "<": ".O.OO.", ">": ".OO.O.", "(": "....O.", ")": "....O.", ".": "..OO.O",
};

const capitalIndicator = ".....O";
const numberIndicator = ".O.OOO";

// Create reverse mapping for faster lookups
const reverseBrailleToEnglish = Object.fromEntries(
    Object.entries(brailleToEnglish).map(([k, v]) => [v, k])
);

function translateToBraille(text) {
    let brailleText = [];
    let numberMode = false;
    let capitalMode = false;

    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        
        if (char === ' ') {
            brailleText.push("......");
            numberMode = capitalMode = false;
            continue;
        }

        const isUpperCase = char >= 'A' && char <= 'Z';
        const isNumber = char >= '0' && char <= '9';

        if (isUpperCase) {
            if (!capitalMode) {
                brailleText.push(capitalIndicator);
                capitalMode = true;
            }
        } else if (isNumber) {
            if (!numberMode) {
                brailleText.push(numberIndicator);
                numberMode = true;
            }
        } else {
            numberMode = false;
        }

        brailleText.push(englishToBraille[char.toLowerCase()] || "......");
        capitalMode = false;
    }
    return brailleText.join("");
}

function translateToEnglish(braille) {
    let englishText = [];
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const symbol = braille.slice(i, i + 6);
        
        if (symbol === capitalIndicator) {
            isCapital = true;
            continue;
        } else if (symbol === numberIndicator) {
            isNumber = true;
            continue;
        }

        let char = reverseBrailleToEnglish[symbol] || " ";
        
        if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        } else if (isNumber) {
            isNumber = false;
        }
        
        englishText.push(char);
    }
    return englishText.join("");
}

const args = process.argv.slice(2);
if (args.length === 0) {
    console.log("Usage: node translator.js <input string>");
    process.exit(1);
}

const input = args.join(" ");
console.log(input.includes('.') || input.includes('O') ? translateToEnglish(input) : translateToBraille(input));
