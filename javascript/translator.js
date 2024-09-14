// Code by Chaitanya Santosh Tekane
// Email: chaitanyatekne5@gmail.com

// Dictionaries for translation
const BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' ',
    '..O...': ',', '..O.O.': ';', '..OO..': ':', '..OOO.': '!', '..O.OO': '?',
    '..OO.O': '.', '....OO': '-', '.O..O.': '/', 'O.O..O': '(', '.O.OO.': ')',
    '.OO..O': '<', '.O.OO.': '>'
};

// Create reversed dictionary for English to Braille translation
const ENGLISH_TO_BRAILLE = Object.fromEntries(
    Object.entries(BRAILLE_TO_ENGLISH).map(([k, v]) => [v, k])
); 

// Numbers are like a-j but with the number symbol in front
const NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

/**
 * Detect whether the input string is Braille or English.
 * @param {string} inputStr - The input string to detect.
 * @returns {string} - Returns 'braille' if the input contains Braille characters, 'english' otherwise.
 */

function detectInputType(inputStr) {
    return /[O.]/.test(inputStr) ? 'braille' : 'english';
}

/**
 * Translate a Braille string to English.
 * @param {string} brailleStr - The Braille string to translate.
 * @returns {string} - The translated English string.
 */

function translateBrailleToEnglish(brailleStr) {
    let englishOutput = [];
    let capitalizeNext = false;
    let numberMode = false;

    // Process Braille input in chunks of 6 characters

    for (let i = 0; i < brailleStr.length; i += 6) {
        let symbol = brailleStr.slice(i, i + 6);
        
        if (symbol === '.....O') { // Capital symbol
            capitalizeNext = true;
            continue;
        } else if (symbol === '.O.OOO') { // Number symbol
            numberMode = true;
            continue;
        }

        // Translate Braille symbol to English character

        let char = BRAILLE_TO_ENGLISH[symbol] || '?'; // Handle unknown symbols

        if (numberMode) {
            if (char === ' ') {
                numberMode = false; // End number mode
            } else {
                // Translate number symbols
                char = Object.keys(NUMBERS).find(k => NUMBERS[k] === symbol) || '?';
            }
        }

        if (capitalizeNext && char !== ' ') {
            char = char.toUpperCase(); // Capitalize next character
            capitalizeNext = false;
        }

        englishOutput.push(char);
    }

    return englishOutput.join('');
}

/**
 * Translate an English string to Braille.
 * @param {string} englishStr - The English string to translate.
 * @returns {string} - The translated Braille string.
 */

function translateEnglishToBraille(englishStr) {
    let brailleOutput = [];
    let numberMode = false;

    for (let char of englishStr) {
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            brailleOutput.push(ENGLISH_TO_BRAILLE['capital']); // Add capital symbol
            char = char.toLowerCase();
        }
        if (/\d/.test(char)) {
            if (!numberMode) {
                brailleOutput.push(ENGLISH_TO_BRAILLE['number']); // Add number symbol
                numberMode = true;
            }
            brailleOutput.push(NUMBERS[char]); // Add Braille representation of number
        } else {
            if (numberMode) {
                numberMode = false; // End number mode
            }
            brailleOutput.push(ENGLISH_TO_BRAILLE[char] || '......'); // Handle non-recognized characters
        }
    }

    return brailleOutput.join('');
}

// Main logic
const inputStr = process.argv.slice(2).join(' ') || '';

// Detect input type and perform the appropriate translation
const translationFunction = detectInputType(inputStr) === 'braille'
    ? translateBrailleToEnglish
    : translateEnglishToBraille;

    // Output the translation result

console.log(translationFunction(inputStr));

