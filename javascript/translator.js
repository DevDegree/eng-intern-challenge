// To run the code, use the command: node translator.js "your input here"

// Dictionary to map each English letter, number, and special symbol to its corresponding Braille representation.
const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', 'space': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

// Create a reverse mapping to translate Braille back to English characters.
const brailleToEnglishDict = Object.fromEntries(
    Object.entries(brailleDict).map(([char, braille]) => [braille, char])
);

// Function to check if the input string is written in Braille.
function isBraille(input) {
    return /^[O.]+$/.test(input.trim());
}

// Function to translate a given English text to Braille.
function translateToBraille(text) {
    let brailleOutput = [];  // Array to store the resulting Braille symbols.
    let numberMode = false;   // Track if we are in number mode for translating digits.

    for (let char of text) {
        if (char === ' ') {
            // Add a space symbol in Braille for spaces in the input.
            brailleOutput.push(brailleDict['space']);
        } else if (/\d/.test(char)) {
            // If we encounter a digit, enter number mode if we aren't already.
            if (!numberMode) {
                brailleOutput.push(brailleDict['num']);
                numberMode = true; // Switch to number mode.
            }
            // Add the corresponding Braille representation for the digit.
            brailleOutput.push(brailleDict[char]);
        } else {
            // Check for unsupported characters
            if (!brailleDict[char.toLowerCase()]) {
                console.warn(`Warning: Character "${char}" is not supported for translation.`);
                continue; // Skip unsupported characters
            }

            // Check if the character is uppercase.
            if (char === char.toUpperCase()) {
                // Add a capitalization marker for the next letter.
                brailleOutput.push(brailleDict['cap']);
            }
            // Add the Braille representation for the lowercase character.
            brailleOutput.push(brailleDict[char.toLowerCase()]);
            numberMode = false; // Reset number mode after processing a letter.
        }
    }
    // Join the Braille symbols into a single string and return.
    return brailleOutput.join('');
}


// Function to translate Braille text back to English.
function translateFromBraille(brailleText) {
    let englishOutput = [];  // Array to store the resulting English characters.
    let numberMode = false;  // Track if we are in number mode.
    let capitalizeNext = false; // Flag to indicate if the next letter should be capitalized.

    // Process the Braille text in chunks of 6 characters.
    for (let i = 0; i < brailleText.length; i += 6) {
        let symbol = brailleText.slice(i, i + 6); // Extract the current Braille symbol.

        // Check for the number marker to switch to number mode.
        if (symbol === brailleDict['num']) {
            numberMode = true; // Activate number mode.
            continue;
        }

        // Check for the capitalization marker.
        if (symbol === brailleDict['cap']) {
            capitalizeNext = true; // Set the flag to capitalize the next character.
            continue;
        }

        // Check for space.
        if (symbol === brailleDict['space']) {
            englishOutput.push(' '); // Add a space to the output.
            numberMode = false; // Reset number mode on encountering space.
            continue;
        }

        let char = brailleToEnglishDict[symbol]; // Translate the Braille symbol to English.

        // Handle number mode.
        if (numberMode) {
            if (char >= 'a' && char <= 'j') {
                // Convert Braille letters (a-j) to digits (1-9).
                let number = (char.charCodeAt(0) - 'a'.charCodeAt(0) + 1).toString();
                englishOutput.push(number); // Add the corresponding number.
            } else if (char === 'j') {
                englishOutput.push('0'); // 'j' corresponds to 0 in number mode.
            }
            continue; // Skip to the next iteration after processing number.
        } 
        
        // Handle capitalization.
        if (capitalizeNext) {
            englishOutput.push(char.toUpperCase()); // Capitalize the letter.
            capitalizeNext = false; // Reset the capitalization flag.
        } else {
            englishOutput.push(char); // Add the letter as is.
        }
    }

    // Join the English characters into a complete string and return.
    return englishOutput.join('');
}

// Get the input from the command line arguments.
const input = process.argv.slice(2).join(' ');

// Determine whether to translate the input to Braille or from Braille based on the input.
if (isBraille(input)) {
    console.log(translateFromBraille(input)); // Translate from Braille to English.
} else {
    console.log(translateToBraille(input)); // Translate English to Braille.
}

// Export the functions for testing
module.exports = {
    translateToBraille,
    translateFromBraille,
    isBraille
};