// Braille alphabet mapping
const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'CAPITAL': '.....O', 'NUMBER': '.O.OOO'
};

// Number mapping for Braille
const numberMapping = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
};

// Reverse mappings for translation
const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([k, v]) => [v, k])
);

const letterToNumber = Object.fromEntries(
    Object.entries(numberMapping).map(([k, v]) => [v, k])
);

/**
 * Translates text to Braille
 * @param {string} text - The input text to translate
 * @returns {string} The Braille representation of the input text
 */
function translateToBraille(text) {
    let result = '';
    let isNumber = false;

    for (const char of text) {
        if (char === ' ') {
            result += brailleAlphabet[' '];
            isNumber = false;
        } else if (/\d/.test(char)) {
            if (!isNumber) {
                result += brailleAlphabet['NUMBER'];
                isNumber = true;
            }
            result += brailleAlphabet[letterToNumber[char]];
        } else {
            isNumber = false;
            if (char.toUpperCase() !== char.toLowerCase() && char === char.toUpperCase()) {
                result += brailleAlphabet['CAPITAL'];
            }
            result += brailleAlphabet[char.toLowerCase()] || '';
        }
    }

    return result;
}

/**
 * Translates Braille to English
 * @param {string} braille - The input Braille to translate
 * @returns {string} The English representation of the input Braille
 */
function translateToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
    const cells = braille.match(/.{1,6}/g) || [];

    for (const cell of cells) {
        if (cell === brailleAlphabet['CAPITAL']) {
            isCapital = true;
        } else if (cell === brailleAlphabet['NUMBER']) {
            isNumber = true;
        } else if (cell === brailleAlphabet[' ']) {
            result += ' ';
            isNumber = false;
        } else {
            let letter = reverseBrailleAlphabet[cell];
            if (isNumber) {
                letter = numberMapping[letter];
                isNumber = false;
            }
            if (isCapital) {
                letter = letter.toUpperCase();
                isCapital = false;
            }
            result += letter || '';
        }
    }

    return result;
}

/**
 * Determines the input type and translates accordingly
 * @param {string} input - The input string to translate
 * @returns {string} The translated output
 */
function translate(input) {
    const isBraille = /^[O\.]+$/.test(input.replace(/\s/g, ''));
    return isBraille ? translateToEnglish(input) : translateToBraille(input);
}

// Main execution
const input = process.argv.slice(2).join(' ');
console.log(translate(input));
