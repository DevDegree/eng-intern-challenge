// Braille to English mapping
const brailleToEnglish = {
    "O.....": "a", ".O....": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", ".O..O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", ".O..OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "#", ".....O": "#", ".O.OO.": "cap"
};

// English to Braille mapping
const englishToBraille = {
    "a": "O.....", "b": ".O....", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": ".O..O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": ".O..OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "cap": ".O.OO.", "#": ".....O"
};

const numberMap = {
    "1": "O.....", "2": ".O....", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Function to detect if input is Braille or English using some Simple RegEX
function isBraille(input) {
    return /^[O\.]+$/.test(input);
}

// Translate Braille to English
function translateBrailleToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
    const symbols = input.match(/.{1,6}/g); // Split into groups of 6
    
    symbols.forEach(symbol => {
        if (symbol === ".....O") {
            isNumber = true;
        } else if (symbol === ".O.OO.") {
            isCapital = true;
        } else {
            let letter = isNumber ? Object.keys(numberMap).find(key => numberMap[key] === symbol) : brailleToEnglish[symbol];
            if (isCapital) {
                letter = letter.toUpperCase();
                isCapital = false;
            }
            result += letter;
            if (isNumber && letter === " ") {
                isNumber = false; // Numbers end after a space
            }
        }
    });
    
    return result;
}

// Translate English to Braille
function translateEnglishToBraille(input) {
    let result = '';
    let isNumber = false;
    
    for (let i = 0; i < input.length; i++) {
        const char = input[i];
        
        if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result += englishToBraille["#"]; // Start of numbers
                isNumber = true;
            }
            result += numberMap[char];
        } else if (char === char.toUpperCase() && /[A-Z]/.test(char)) {
            result += englishToBraille["cap"]; // Capital indicator
            result += englishToBraille[char.toLowerCase()];
        } else {
            result += englishToBraille[char.toLowerCase()];
        }
        
        if (char === " ") {
            isNumber = false; // Reset numbers after space
        }
    }
    
    return result;
}

// Main function
function main() {
    const input = process.argv.slice(2).join(' ').trim();

    if (isBraille(input)) {
        console.log(translateBrailleToEnglish(input));
    } else {
        console.log(translateEnglishToBraille(input));
    }
}
