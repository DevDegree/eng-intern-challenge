/**
 * English to Braille mapping for alphabet letters, numbers, and special characters.
 * Each key represents an English character, and the corresponding value represents its Braille encoding.
 */
const englishToBrailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', // space
    ',': '..O...', // comma
    '.': '..OO.O', // period
    '?': '..O.OO', 
    '!': '..OOO.', 
    ':': '..OO..', 
    ';': '..O.O.', 
    '-': '....OO', // dash
    '/': '.O..O.', 
    '(': 'O.O..O', 
    ')': '.O.OO.', 
    '<': '.OO..O', 
};


/**
 * Number to Braille mapping. Each digit (as a string) corresponds to its Braille encoding.
 */

const numberMap = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO.',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};



/**
 * Braille to English mapping.
 * 
 * Maps 6-dot Braille patterns ('O' for raised, '.' for flat) to English characters.
 * Includes letters, numbers, and punctuation.
 */
const brailleToEnglishMap = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g',
    'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n',
    'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', //space
    '..O...': ',', //comma
    '..OO.O': '.', //period
    '..O.OO': '?',
    '..OOO.': '!', 
    '..OO..': ':', 
    '..O.O.': ';', 
    '....OO': '-', //dash
    '.O..O.': '/', 
    'O.O..O': '(', 
    '.O.OO.': ')', 
    '.OO..O': '<', 
    'O..OO.': '>', 
   
};

/**
 * Braille encoding for capital letters.
 * When this appears before a letter, it indicates that the letter is uppercase.
 * It applies specifically to the next character only.
 */
const capitalIndicator = '.....O';
/**
 * Braille encoding for numbers.
 * When this appears before a sequence, it indicates that the following characters are numbers.
 */
const numberIndicator = '.O.OOO';

/**
 * Function to detect if the input is in Braille format.
 * @param {string} input - The string to be checked.
 * @returns {boolean} Returns true if the input is in Braille, false otherwise.
 */
function isBraille(input) {
    return /^[O.]+$/.test(input.replace(/\s+/g, '')); 
}


/**
 * Converts a Braille string to its corresponding English text.
 * 
 * This function handles both letters and numbers, as well as special cases
 * such as capitalization and number indicators. The input Braille string
 * is divided into words, and each 6-character Braille block is translated
 * into its corresponding English character.
 * 
 * @param {string} braille - The Braille string to be translated into English.
 * @returns {string} The translated English text.
 */

function brailleToEnglish(braille) {
    const words = braille.trim().split(/\s+/); // Split on spaces
    let english = '';
    let isNumberMode = false;
    let isCapitalMode = false;

    words.forEach(word => {
        for (let i = 0; i < word.length; i += 6) {
            const brailleChar = word.slice(i, i + 6);

            if (brailleChar === capitalIndicator) {
                isCapitalMode = true;
                continue;
            }
            if (brailleChar === numberIndicator) {
                isNumberMode = true;
                continue;
            }

            let char = brailleToEnglishMap[brailleChar] || '';

            if (isNumberMode) {
                char = Object.keys(numberMap).find(key => numberMap[key] === brailleChar);
                if (!char) isNumberMode = false; // Reset after finding a non-number char
            }

            if (isCapitalMode) {
                char = char.toUpperCase();
                isCapitalMode = false;
            }

            english += char;
        }
       
    });

    return english.trim();
}


/**
 * Converts an English string to its Braille equivalent.
 * Handles letters, numbers, and capitalization.
 * 
 * @param {string} english - The English string to be translated into Braille.
 * @returns {string} The Braille translation of the input English string.
 */

function englishToBraille(english) {
    let braille = '';
    let isNumberMode = false;

    for (let char of english) {
        if (/[0-9]/.test(char))  //Number character
        {
            if (!isNumberMode) {
                braille += numberIndicator;
                isNumberMode = true;
            }
            braille += numberMap[char];
        } else 
        {
            if (isNumberMode) {
                isNumberMode = false;
            }
            if (/[A-Z]/.test(char)) { //uppercase character
                braille += capitalIndicator;
                char = char.toLowerCase();
            }
            braille += englishToBrailleMap[char] || '';
        }
    }

    return braille.trim();
}
/**
 * Determines whether the input is Braille or English and translates accordingly.
 * 
 * @param {string} input - The input string to be translated (either Braille or English).
 * @returns {string} The translated string.
 */
function translate(input) {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}




/**
 * Command-line execution. This block runs when the script is executed directly via the command line.
 * It captures the input string, determines the mode, and translates it to Braille or English.
 */
if (require.main === module) {
    const input = process.argv.slice(2).join(' ');
    if (!input) {
        console.error('Please provide a string to translate.');
        process.exit(1);
    }

    const translated = translate(input);
    console.log(translated);
}
