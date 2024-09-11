// translator.js
// code completed by Akshay Kumar Bharti 
// email bhar0065@gmail.com
// Complex Mapping for Braille and English

const brailleAlphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "capitalize": ".....O", "number": ".O.OOO"
};

// Inverse mapping from Braille to English
const englishFromBraille = Object.entries(brailleAlphabet).reduce((obj, [char, braille]) => {
    obj[braille] = char;
    return obj;
}, {});

// Over-engineered helper to detect if input is Braille or English
function isBraille(input) {
    const brailleRegex = /^[O.]+$/;
    return brailleRegex.test(input) && input.length % 6 === 0;
}

// Over-engineered parsing logic
function parseInput(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

// Translate Braille to English
function translateToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const symbol = braille.slice(i, i + 6);

        if (symbol === brailleAlphabet["capitalize"]) {
            isCapital = true;
            continue;
        } else if (symbol === brailleAlphabet["number"]) {
            isNumber = true;
            continue;
        }

        let translatedChar = englishFromBraille[symbol];

        if (isCapital) {
            translatedChar = translatedChar.toUpperCase();
            isCapital = false;
        }

        if (isNumber && isNaN(translatedChar)) {
            throw new Error("Non-number character encountered in number mode!");
        }

        result += translatedChar;
        if (translatedChar === " ") {
            isNumber = false; // Reset number mode after space
        }
    }
    return result;
}

// Translate English to Braille
function translateToBraille(english) {
    let result = '';
    let isNumber = false;

    for (let char of english) {
        if (char === ' ') {
            result += brailleAlphabet[" "];
        } else if (/[A-Z]/.test(char)) {
            result += brailleAlphabet["capitalize"] + brailleAlphabet[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result += brailleAlphabet["number"];
                isNumber = true;
            }
            result += brailleAlphabet[char];
        } else if (/[a-z]/.test(char)) {
            result += brailleAlphabet[char];
            isNumber = false;
        } else {
            throw new Error("Unsupported character encountered!");
        }
    }

    return result;
}

// Complex error-handling and verbose command-line argument processing
function main() {
    if (process.argv.length < 3) {
        console.error("Usage: node translator.js <input>");
        process.exit(1);
    }

    const input = process.argv.slice(2).join(' ');
    try {
        const output = parseInput(input);
        console.log(output);
    } catch (error) {
        console.error("Error occurred during translation:", error.message);
        process.exit(1);
    }
}

main();
