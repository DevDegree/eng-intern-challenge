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
    ".O.OO.": "<", ".OO.O.": ">", "....O.": "(", "....O.": ")", ".": "..."  // Adjust punctuation if needed
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
    "<": ".O.OO.", ">": ".OO.O.", "(": "....O.", ")": "....O.", ".": "..OO.O",  // Adjust punctuation if needed
};
//"capital":".....O","number":".O.OOO",
// // Braille capital follows
 const capitalIndicator = ".....O";
// // Braille number follows
 const numberIndicator = ".O.OOO";

// function translateToBraille(text) {
//     let brailleText = [];
//     for (let char of text) {
//         if (char === ' ') {
//             brailleText.push("......");
//             continue;
//         }
//         if (char.match(/[A-Z]/)) {
//             brailleText.push(capitalIndicator);
//             char = char.toLowerCase();
//         }
//         if (char.match(/[0-9]/)) {
//             //brailleText.push(numberIndicator);
//         }
//         brailleText.push(englishToBraille[char] || "......");

//     }
//     return brailleText.join("");
// }
function translateToBraille(text) {
    let brailleText = [];
    let numberMode = false;
    let capitalMode = false;

    for (let char of text) {
        if (char === ' ') {
            brailleText.push("......");  // Space in Braille
            numberMode = false;         // Reset number mode when encountering a space
            capitalMode = false;        // Reset capital mode when encountering a space
            continue;
        }

        if (char.match(/[A-Z]/)) {
            // If the capital mode is active, push the capital indicator and set the mode to true for the next character
            if (!capitalMode) {
                brailleText.push(capitalIndicator);
                capitalMode = true;
            }
            char = char.toLowerCase(); // Convert to lowercase for lookup
        } else if (char.match(/[0-9]/)) {
            // If not already in number mode, push number indicator and set the mode to true
            if (!numberMode) {
                brailleText.push(numberIndicator);
                numberMode = true;
            }
        } else {
            // Reset number mode when a non-number character is encountered
            if (numberMode) {
                numberMode = false;
            }
        }

        // Reset capital mode after processing one character if it was set
        if (capitalMode) {
            capitalMode = false;
        }

        brailleText.push(englishToBraille[char] || "......");  // Default to space if not found
    }
    return brailleText.join("");
}


function translateToEnglish(braille) {
    let englishText = [];
    let index = 0;
    let isCapital = false;
    let isNumber = false;

    while (index < braille.length) {
        let symbol = braille.substring(index, index + 6);
        if (symbol === capitalIndicator) {
            isCapital = true;
            index += 6;
            continue;
        } else if (symbol === numberIndicator) {
            isNumber = true;
            index += 6;
            continue;
        }
        let char = brailleToEnglish[symbol] || " ";
        if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        } else if (isNumber) {
            char = char;  // The char remains the same for numbers
            isNumber = false;
        }
        englishText.push(char);
        index += 6;
    }
    return englishText.join("");
}

const args = process.argv.slice(2);
if (args.length === 0) {
    console.log("Usage: node translator.js <input string>");
    process.exit(1);
}

const input = args.join(" ");
if (input.match(/^[O.]+$/)) {
    console.log(translateToEnglish(input));
} else {
    console.log(translateToBraille(input));
}
