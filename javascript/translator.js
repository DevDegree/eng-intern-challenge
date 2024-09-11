/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */
const readline = require('readline-sync');

const brailleToEnglish = (brailleString) => {
    const result = "";

    const BRAILLE_CHAR_LEN = 6;

    let capitalFlag = false, numberFlag = false;

    for (let i = 0; i < brailleString.length; i += BRAILLE_CHAR_LEN) {
        const brailleChar = brailleString.substring(i, i + BRAILLE_CHAR_LEN);

        if (brailleChar = '.....O') { capitalFlag = true; }
        else if (brailleChar = '.O.OOO') { numberFlag = true; } 
        else { result += parseBraille(brailleChar, capitalFlag, numberFlag); }
    }
}

const parseBraille = (char, capitalFlag, numberFlag) => {
    parseAlphaNumericBraille(char, capitalFlag, numberFlag);
}

// TO DO: Ensure that argument is indeed alphanumeric
const parseAlphaNumericBraille = (char, numberFlag) => {    
    const rowValues = {
        '..' : 0,
        'O.' : 1,
        'OO' : 2
    }
    
    const columnValues = {
        'O...' : 0,
        'O.O.' : 1,
        'OO..' : 2,
        'OO.O' : 3,
        'O..O' : 4,
        'OOO.' : 5,
        'OOOO' : 6,
        'O.OO' : 7,
        '.OO.' : 8,
        '.OOO' : 9,
    }
    
    row = rowValues[char.substring(4, 6)];
    column = columnValues[char.substring(0, 4)];
    
    if (numberFlag) {
        return `${(column + 1)}`;
    }
    
    const alphabet = 'abcdefghijklmnopqrstuvxyz' // Does not contain 'w'!
    return alphabet.charAt(column + (row * 10));
}

const isEnglish = (input) => {
    // TO DO
    return false;
}

const parseInput = (input) => {
    if (isEnglish(input)) {
        return englishToBraille(input);
    }

    return brailleToEnglish(input);
}

function main() {
    const input = readline.question('Input: ');
    // TO DO: type checking for input

    console.log(`Output: ${parseInput(input)}`);
}
main();
