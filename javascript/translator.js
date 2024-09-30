const { ALPHABET_TO_BRAILLE, NUMBER_TO_BRAILLE, BRAILLE_TO_ALPHABET, BRAILLE_TO_NUMBER } = require('./constants');

/**
 * Translate Braille to English
 * @param {string} input - Braille input string
 * @returns {string} Translated English output
 */
const translateToEnglish = (input) => {
    let index = 0, output = "", isCaps = false, isNumber = false;

    while (index < input.length) {
        const brailleChar = input.substring(index, index + 6);
        let value = BRAILLE_TO_ALPHABET[brailleChar];

        if (value === 'CAP') {
            isCaps = true;
        } else if (value === 'NUM') {
            isNumber = true;
        } else {
            if (isNumber) {
                value = handleNumberMode(value, brailleChar);
                if (value === null) isNumber = false;
            } else if (isCaps) {
                value = value.toUpperCase();
                isCaps = false;
            }
            output += value;
        }
        index += 6;
    }
    return output;
};

/**
 * Handle numbers in Braille translation
 * @param {string} value - Current character value
 * @param {string} brailleChar - Current Braille character
 * @returns {string|null} - Translated number or special character or null if not a number
 */
const handleNumberMode = (value, brailleChar) => {
    // Space is used to break number mode
    if (value === ' ') return null;
    if (value === 'DEC') return '.';
    // Special case for greater than
    if (brailleChar === 'O..OO.') return '>';  
    return BRAILLE_TO_NUMBER[brailleChar] || value;
};

/**
 * Translate English to Braille
 * @param {string} input - English input string
 * @returns {string} Translated Braille output
 */
const translateToBraille = (input) => {
    let output = "", isNumber = false;

    for (const char of input) {
        if (char === ' ') {
            isNumber = false;
            output += ALPHABET_TO_BRAILLE[char];
            continue;
        }

        if (isDigit(char)) {
            //Char is number
            if (!isNumber) output += ALPHABET_TO_BRAILLE['NUM'];
            output += NUMBER_TO_BRAILLE[char];
            isNumber = true;
        } else {
            //Char is alphabet/special character
            if (isNumber && char === '.') {
                output += ALPHABET_TO_BRAILLE['DEC'];
            } else {
                if (isUpperCase(char)) output += ALPHABET_TO_BRAILLE['CAP'];
                output += ALPHABET_TO_BRAILLE[char.toLowerCase()];
            }
            isNumber = false;
        }
    }

    return output;
};

/**
 * Helper to determine if a character is a digit
 * @param {string} char - Single character string
 * @returns {boolean} True if char is a digit
 */
const isDigit = (char) => !isNaN(char);

/**
 * Determine if a character is uppercase
 * @param {string} char - Single character string
 * @returns {boolean} True if char is uppercase
 */
const isUpperCase = (char) => char === char.toUpperCase();

/**
 * Transform input to either English or Braille based on format
 * @param {string} input - Input string to be translated
 * @returns {string} Translated output
 */
const transform = (input) => {
    input = input.trim();
    // Remove spaces, O and . to check if any other characters exist
    const temp = input.replace(/ /g, "").replace(/O/g, "").replace(/\./g, "");

    // If input length is a multiple of 6 and contains only valid Braille characters, translate to English
    return temp.length === 0 && input.length % 6 === 0 
        ? translateToEnglish(input)
        : translateToBraille(input);
};

const args = process.argv.slice(2);
const inputText = args.join(' ');
const out = transform(inputText);
console.log(out);
