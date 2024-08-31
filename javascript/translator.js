//Using the braille.jpg and mapped all the characters to braille
const brailleMap = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
  "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
  "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
  "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
  "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
  "cap": ".....O", "dec": ".O....", "num": ".O.OOO",
  ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", 
  ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".O.O.O", ">": "O.O..0", 
  "(": "O.O..O", ")": ".O.OO.", " ": "......"
};

// Reverse mapping from Braille patterns to characters, used for translating Braille back to text.
const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([key, value]) => [value, key])
);

// Function to check if a given input is a Braille string (contains only 'O' and '.').
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Function to translate a text string to Braille.
function translateToBraille(text) {
    let result = '';
    let isNumberMode = false;

    for (let char of text) {
        // Handle capitalization by adding the 'cap' indicator before capital letters.
        if (/[A-Z]/.test(char)) {
            result += brailleMap['cap'];  // Add the capitalization indicator
            char = char.toLowerCase();    // Convert to lowercase to get the correct Braille character
        }

        // Handle numbers by adding the 'num' indicator before digits.
        if (/\d/.test(char)) {
            if (!isNumberMode) {
                result += brailleMap['num'];  // Add the number indicator
                isNumberMode = true;
            }
        } else {
            isNumberMode = false;  // Exit number mode for non-numeric characters
        }

        // Add the corresponding Braille pattern for the character.
        result += brailleMap[char];  
    }
    return result; // Return the final Braille string.
}

// Function to translate a Braille string back to text.
function translateToEnglish(text) {
    let result = '';
    let isCapital = false;
    let isNumberMode = false;

    // Iterate over the Braille string in chunks of 6 characters (1 Braille character).
    for (let i = 0; i < text.length; i += 6) {
        let brailleChar = text.slice(i, i + 6);

        // Check if the current Braille character is a capitalization indicator.
        if (brailleChar === brailleMap['cap']) {
            isCapital = true;
            continue;
        }
        // Check if the current Braille character is a number indicator.
        if (brailleChar === brailleMap['num']) {
            isNumberMode = true;
            continue;
        }
        // Find the corresponding English character from the Braille pattern.
        let char = reverseBrailleMap[brailleChar];

        // If the pattern is unrecognized, add a placeholder character.
        if (!char) {
            result += '?';  // In case of an unrecognized pattern
            continue;
        }
        // Handle number mode, ensuring digits are interpreted correctly.
        if (isNumberMode) {
            if (/[a-j]/.test(char)) {
                // Convert letter to corresponding digit based on Braille number mode mapping
                let digit = 'abcdefghij'.indexOf(char) + 1;
                result += digit;
            } else {
                isNumberMode = false; // Exit number mode if the character is not a digit
                // After exiting number mode, we continue to handle the character normally
                if (isCapital) {
                    char = char.toUpperCase();
                    isCapital = false;
                }
                result += char;
            }
        } else {
            // Handle capitalization.
            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }
            result += char;
        }
    }
    return result; // Return the final translated text.
}

// Main execution: process input based on whether it's Braille or regular text.
const input = process.argv.slice(2).join(' ');

if (isBraille(input)) {
    console.log(translateToEnglish(input)); // Translate Braille to English
} else {
    console.log(translateToBraille(input)); // Translate English to Braille
}