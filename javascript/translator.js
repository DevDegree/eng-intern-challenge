// Braille to English and English to Braille Translator

// Braille mapping for the alphabet and numbers
const brailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", // Space
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "capital": ".....O", // Capitalization symbol
    "number": ".O.OOO"  // Number follows symbol
};

// Reverse mapping for Braille to English
const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([key, value]) => [value, key])
);

// Function to translate English to Braille
function englishToBraille(text) {
    let brailleText = '';
    let isNumber = false;

    for (let char of text) {
        if (char.match(/[A-Z]/)) {
            brailleText += brailleMap['capital'] + brailleMap[char.toLowerCase()];
        } else if (char.match(/[0-9]/) && !isNumber) {
            brailleText += brailleMap['number'] + brailleMap[char];
            isNumber = true;
        } else if (char.match(/[0-9]/)) {
            brailleText += brailleMap[char];
        } else if (char === ' ') {
            brailleText += brailleMap[' '];
            isNumber = false;
        } else {
            brailleText += brailleMap[char];
            isNumber = false;
        }
    }

    return brailleText;
}

// Function to translate Braille to English
function brailleToEnglish(brailleText) {
    let englishText = '';
    let i = 0;
    let isCapital = false;
    let isNumber = false;

    while (i < brailleText.length) {
        let brailleChar = brailleText.substring(i, i + 6);

        if (brailleChar === brailleMap['capital']) {
            isCapital = true;
            i += 6;
        } else if (brailleChar === brailleMap['number']) {
            isNumber = true;
            i += 6;
        } else {
            let englishChar = reverseBrailleMap[brailleChar];
            if (isCapital) {
                englishChar = englishChar.toUpperCase();
                isCapital = false;
            }
            if (isNumber) {
                englishText += englishChar;
            } else {
                englishText += englishChar;
            }
            i += 6;
        }
    }

    return englishText;
}

// Main function to determine input type and translate
function translate(input) {
    // Check if the input is Braille or English
    if (input.match(/^[O.]+$/)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

// Get the input from command line arguments
const input = process.argv.slice(2).join(' ');

// Output the translated result
console.log(translate(input));