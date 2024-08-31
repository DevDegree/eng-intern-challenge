
// constants that keep track of translator's internal state

const SPACE_CONSTANT = ' ';
const CAPSLOCK_CONSTANT = 'CAPSLOCK';
const INT_CONSTANT = 'INT';
const brailleBook = {};
const inverseBook = {};

// mapped patterns
const patterns = [
    'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..',
    'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.',
    'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO', '......', '.....O', '.O.OOO',
    '.OOO..', 'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...'
];

// accepted english translator chars
const characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', SPACE_CONSTANT, CAPSLOCK_CONSTANT, INT_CONSTANT,
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
];


// build the braille book and the inverse book for translation
for (let i = 0; i < characters.length; i++) {
    brailleBook[characters[i]] = patterns[i];
    inverseBook[patterns[i]] = characters[i];
}

/**
 * a char converter to decide which function should be handled for given English char type
 * @param {*} char read in string char from input
 * @param {*} isNumber boolean value to indicate if the char is a number 
 * @returns mapped char with post and pre extra braille pattern mappings 
 */
function convertCharToBraille(char, isNumber) {
    if (char >= 'A' && char <= 'Z') {
        return handleUppercase(char);
    } else if (char >= '0' && char <= '9') {
        return handleNumber(char, isNumber);
    } else if (char === ' ') {
        return handleSpace();
    } else {
        return brailleBook[char];
    }
}

/**
 * handle upper case from char to braille
 * @param {*} char read in string char from input
 * @returns braille mapped chars
 */
function handleUppercase(char) {
    return brailleBook[CAPSLOCK_CONSTANT] + brailleBook[char.toLowerCase()];
}

/**
 * handle the number case when to post map the braille constant
 * @param {*} char read in string char from input
 * @param {*} isNumber running isNumber state
 * @returns braille number mapped chars
 */
function handleNumber(char, isNumber) {
    if (!isNumber) {
        return brailleBook[INT_CONSTANT] + brailleBook[char];
    } else {
        return brailleBook[char];
    }
}

/**
 * handles the space element
 * @returns the space constant braille book mapping
 */
function handleSpace() {
    return brailleBook[SPACE_CONSTANT];
}

/**
 * do English to Braille conversion processing on the given text 
 * @param {*} text input string from terminal
 * @returns the converted string
 */
function convertEnglishToBr(text) {
    let res = '';
    let isInt = false;

    for (const char of text) {
        const brailleChar = convertCharToBraille(char, isInt);

        if (char === SPACE_CONSTANT) {
            isInt = false;
        } else if (char >= '0' && char <= '9') {
            isInt = true;
        }

        res += brailleChar;
    }

    return res;
}

/**
 * a char converter to decide which function should be handled for given Braille char type
 * @param {*} brailleChar the braille char
 * @param {*} capitalizeNext pre mapping to see when to do capital next
 * @returns the braille to English char
 */
function convertBrailleCharToText(brailleChar, capitalizeNext) {
    if (brailleChar === brailleBook[CAPSLOCK_CONSTANT]) {
        return handleCapitalIndicator();
    } else if (brailleChar === brailleBook[INT_CONSTANT]) {
        return handleNumberIndicator();
    } else if (brailleChar === brailleBook[SPACE_CONSTANT]) {
        return handleSpaceBraille();
    } else {
        let char = inverseBook[brailleChar];
        if (capitalizeNext) {
            char = char.toUpperCase();
        }
        return { result: char };
    }
}

/**
 *  Function to handle capital letter indicator
 * @returns capital indicator values
 */
function handleCapitalIndicator() {
    return { capitalizeNext: true, result: '' };
}

/**
 * Function to handle number indicator
 * @returns number indicator values
 */
function handleNumberIndicator() {
    return { isNumber: true, result: '' };
}


/**
 * // Function to handle space in Braille
 * @returns space indicator values
 */
function handleSpaceBraille() {
    return { isNumber: false, result: ' ' };
}
/**
 * do Braille to English translation on given braille input
 * @param {*} braille braille input from the terminal
 * @returns the converted string
 */
function convertBrToEnglish(braille) {
    let result = '';
    let i = 0;
    let capitalizeNext = false;
    let isNumber = false;

    while (i < braille.length) {
        const brailleChar = braille.substring(i, i + 6);
        i += 6;

        const { result: charResult, capitalizeNext: newCapitalizeNext, isNumber: newIsNumber } =
            convertBrailleCharToText(brailleChar, capitalizeNext);

        capitalizeNext = newCapitalizeNext !== undefined ? newCapitalizeNext : capitalizeNext;
        isNumber = newIsNumber !== undefined ? newIsNumber : isNumber;
        result += charResult;
    }

    return result;
}

/**
 * a helper function to process the terminal input and check if a string is braille
 * @param {*} input terminal string input
 * @returns boolean value indicating if the string is a braille string
 */
function isBrailleInput(input) {
    const brailleChars = Object.values(brailleBook);
    for (let i = 0; i < input.length; i += 6) {
        const segment = input.substring(i, i + 6);
        if (!brailleChars.includes(segment)) {
            return false;
        }
    }
    return true;
}

/**
 * helper function to be smart enough if text is braille or english and process the input properly
 * @param {*} input the terminal string value
 * @returns the translator function's converted string
 */
function processInput(input) {
    if (isBrailleInput(input)) {
        return convertBrToEnglish(input);
    } else {
        return convertEnglishToBr(input);
    }
}

/**
 * the entry point of the terminal CLI
 */
function main() {
    const input = process.argv.slice(2).join(' ');
    const result = processInput(input);
    console.log(result);
}

main();
