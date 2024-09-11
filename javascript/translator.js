/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */
const readline = require('readline-sync');

const brailleToEnglish = (brailleString) => {
    const englishString = "";

    const BRAILLE_CHAR_LEN = 6;

    let capitalFlag = false, decimalFlag = false, numberFlag = false;

    for (let i = 0; i < brailleString.length; i += BRAILLE_CHAR_LEN) {
        const brailleChar = brailleString.substring(i, i + BRAILLE_CHAR_LEN);
        parseBraille(brailleChar, capitalFlag, decimalFlag, numberFlag);
    }
}

const parseBraille = (char, cF, nF) => {
    parseAlphaNumericBraille(char, false);
}

// TO DO: Ensure that argument is indeed alphanumeric
const parseAlphaNumericBraille = (char, numberFlag) => {
    const alphabet = 'abcdefghijklmnopqrstuvxyz' // Does not contain 'w'!
    let result = '';

    // if (char[4] === '.' && char[5] === '.') { row = 1; }
    // else if (char[4] === '0' && char[5] === '.') { row = 2; }
    // else if (char[4] === '0' && char[5] === '0') { row = 3; }
    // else { result = 'w'; }

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
    
    console.log("Bottom Two: " + char.substring(4, 6));
    console.log("Top Four: " + char.substring(0, 4));

    row = rowValues[char.substring(4, 6)];
    column = columnValues[char.substring(0, 4)];

    if (numberFlag) {
        return `${(column + 1)}`;
    }

    console.log("Column: " +  column);
    console.log("Row: " + row);

    console.log(alphabet.charAt(column + (row * 10)));
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
