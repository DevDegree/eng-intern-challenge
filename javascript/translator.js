// Command line input
const userInput = process.argv.slice(2).join(' ');

// Defines mappings from English characters to Braille representations
const brailleChart = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'uppercase': '.....O', 'numeric': '.O.OOO'
};

// Defines Braille representations for digits, separate from letters
const numbersInBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Checks if the given string is in Braille format based on expected characters
function checkBraille(input) {
    return /^[O\.]+$/.test(input);
}

// Converts Braille input to English text, handling capitalization and numeric sequences
function brailleToEnglish(brailleInput) {
    let output = '';
    let isCapital = false; // Tracks if the next character is uppercase
    let isNumber = false; // Tracks if the current sequence is numeric

    for (let index = 0; index < brailleInput.length; index += 6) {
        const segment = brailleInput.slice(index, index + 6);

        if (segment === brailleChart['uppercase']) { // Check for uppercase indicator
            isCapital = true;
            continue;
        }
        if (segment === brailleChart['numeric']) { // Check for numeric indicator
            isNumber = true;
            continue;
        }
        if (segment === '......') { // Treat '......' as a space and resets number mode
            output += ' ';
            isNumber = false;
            continue;
        }

        let characterMap = isNumber ? numbersInBraille : brailleChart;
        let character = Object.keys(characterMap).find(key => characterMap[key] === segment);

        if (character) {
            output += isCapital ? character.toUpperCase() : character;
            isCapital = false; // Reset uppercase mode after use
            isNumber = /\d/.test(character); // Continue numeric mode if character is a digit
        }
    }
    return output;
}

// Converts English text to Braille, handling digits and capital letters
function englishToBraille(englishInput) {
    let result = '';
    let currentIsNumeric = false; // Tracks numeric mode to manage numeric indicators

    for (let character of englishInput) {
        if (/[A-Z]/.test(character)) { // Add uppercase indicator for capital letters
            result += brailleChart['uppercase'];
            character = character.toLowerCase();
        }
        if (/\d/.test(character)) { // Handle digits with/without preceding numeric indicator
            if (!currentIsNumeric) {
                result += brailleChart['numeric'];
                currentIsNumeric = true;
            }
            result += numbersInBraille[character];
        } else {
            currentIsNumeric = false; // Reset numeric mode for non-digits
            result += brailleChart[character] || '......'; // Add Braille code/handle unknown characters
        }
    }
    return result;
}

// Determine if input is Braille or English 
if (checkBraille(userInput)) {
    console.log(brailleToEnglish(userInput));
} else {
    console.log(englishToBraille(userInput));
}
