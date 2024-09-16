
// Braille Alphabet Mapping
const brailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......",
    "capital": ".....O", "number": ".O.OOO",
    ".": ".O..OO", ",": ".O....", "?": ".O.O.O", "!": ".OO.O.", "-": "......"
};

// Reverse mapping for Braille to English
const reverseBrailleMap = Object.fromEntries(Object.entries(brailleMap).map(([k, v]) => [v, k]));

// Function to detect if the string is Braille
function isBraille(input) {
    return input.trim().startsWith('O') || input.trim().startsWith('.');
}

// Function to translate English to Braille
function englishToBraille(input) {
    let braille = '';
    let isNumber = false;

    for (const char of input) {
        if (char >= 'A' && char <= 'Z') {
            braille += brailleMap['capital'] + brailleMap[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            if (!isNumber) {
                braille += brailleMap['number'];
                isNumber = true;
            }
            braille += brailleMap[char];
        } else {
            isNumber = false;
            braille += brailleMap[char] || "......";
        }
    }
    return braille;
}

// Function to translate Braille to English
function brailleToEnglish(input) {
    const brailleChars = input.match(/.{1,6}/g);
    let english = '';
    let isCapital = false;
    let isNumber = false;

    brailleChars.forEach(char => {
        if (char === brailleMap['capital']) {
            isCapital = true;
        } else if (char === brailleMap['number']) {
            isNumber = true;
        } else {
            let letter = reverseBrailleMap[char] || ' ';
            if (isCapital) {
                letter = letter.toUpperCase();
                isCapital = false;
            }
            if (isNumber) {
                isNumber = false;
            }
            english += letter;
        }
    });
    return english;
}


const input = process.argv.slice(2).join(' ');

if (!input){
    console.error("No input provided. Please enter a string to translate.");
    process.exit(1);
}

let result
if (isBraille(input)) {
    result = brailleToEnglish(input);
} else {
    result = englishToBraille(input);
}

console.log(result);