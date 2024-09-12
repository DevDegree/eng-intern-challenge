/**
 * @file        translator.js
 * @description This script provides functionality to convert English text into Braille
 *              and Braille back into English. It supports translation of both
 *              alphabetic characters and numeric digits, as well as handling capitalization.
 * 
 * @author      Jaydipsinh Padhiyar
 * @version     1.0.0
 * @date        September 12 2024
 * 
 * Problem:     The challenge was to create a bidirectional translator between
 *              English text and Braille, supporting the translation of both
 *              letters and numbers. The solution should be optimized for performance
 *              and handle edge cases such as capitalization and switching between
 *              letters and numbers.
 * 
 * Time Complexity:
 *              - `convertToEnglish`: O(n), where n is the length of the Braille string
 *              - `convertToBraille`: O(n), where n is the length of the English string
 *              - `isBraille`: O(n), where n is the length of the input
 *              - Overall complexity: O(n)
 * 
 */

/* Map to map English characters and Handler Character and Braille characters */
const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'capital': '.....O',
    'number': '.O.OOO'
};

/* Map to map Number and Braille numbers*/
const numbersToBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
};

/* Braille to English mapping */
const brailleToEnglish = Object.fromEntries(Object.entries(englishToBraille).map(([k, v]) => [v, k]));
/* Braille to Numbers mapping */
const brailleToNumbers = Object.fromEntries(Object.entries(numbersToBraille).map(([k, v]) => [v, k]));

/* Function to convert lowercase letter to uppercase letter */
function toLowercaseLetter(char) {
    return String.fromCharCode(char.charCodeAt(0) + 32);
}

/* Function to convert uppercase letter to lowercase letter */
function toUppercaseLetter(char) {
    return String.fromCharCode(char.charCodeAt(0) - 32);
}

/* Function to convert Braille to English */
function convertToEnglish(brailleStr) {
    if (!brailleStr) return '';

    const listOfBraille = brailleStr.match(/.{1,6}/g) || [];
    let englishLetters = [];
    let capitalize = false;
    let number = false;

    for (const braille of listOfBraille) {
        let letter = brailleToEnglish[braille];

        if (letter === 'capital') {
            capitalize = true;
        } else if (letter === 'number') {
            number = true;
        } else if (letter === ' ') {
            number = false;
            englishLetters.push(letter);
        } else if (capitalize) {
            capitalize = false;
            englishLetters.push(toUppercaseLetter(letter));
        } else if (number) {
            englishLetters.push(brailleToNumbers[braille]);
        } else {
            englishLetters.push(letter);
        }
    }

    return englishLetters.join('');
}

/* Function to convert English to Braille */
function convertToBraille(englishStr) {
    if (!englishStr) return '';

    let brailleLetters = [];
    let number = false;

    for (const letter of englishStr) {
        const charCode = letter.charCodeAt(0);

        if (charCode >= 65 && charCode <= 90) {
            brailleLetters.push(englishToBraille['capital']);
            brailleLetters.push(englishToBraille[toLowercaseLetter(letter)]);
        } else if (charCode >= 48 && charCode <= 57) { 
            if (!number) {
                brailleLetters.push(englishToBraille['number']);
                number = true;
            }
            brailleLetters.push(numbersToBraille[letter]);
        } else { 
            brailleLetters.push(englishToBraille[letter]);
            if (letter === ' ') number = false;
        }
    }

    return brailleLetters.join('');
}

/* Function to check if the input is Braille */
function isBraille(input) {
    return /^[O.]{6,}$/.test(input);
}

/* Main function to handle input and output */
function translator() {
    const input = process.argv.slice(2).join(' ');

    if (!input) {
        console.log('Input is empty. Please provide a valid string.');
        return;
    }

    if (isBraille(input)) {
        console.log(convertToEnglish(input));
    } else {
        console.log(convertToBraille(input));
    }
}

/* Run the translator */
translator();
