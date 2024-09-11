const ALPHABET = 'abcdefghijklmnopqrstuvxyz';

const ROW = ['..', 'O.', 'OO'];
const COLUMN = ['O...', 'O.O.', 'OO..', 'OO.O', 'O..O', 'OOO.', 'OOOO', 'O.OO', '.OO.','.OOO'];

let NUMERIC_FLAG = false;

const toBraille = (input) => {
    let result = '';

    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        if (char === ' ') {
            result += '......';
        } else {
            result += parseEnglish(char);
        }
    }

    return result;
}

const parseEnglish = (char) => {
    if (char === 'w') { return '.OOO.O'; }
    if (char === 'W') { return '.....O' + '.OOO.O'; }

    let result = '';

    const isNumber = !ALPHABET.includes(char) && !ALPHABET.includes(char.toLowerCase());
    if (isNumber) {
        if (!NUMERIC_FLAG) {
            result += '.O.OOO';
        }

        NUMERIC_FLAG = true;
        return result + `${COLUMN[char - 1]}${ROW[0]}`;
    }

    NUMERIC_FLAG = false;

    const isUpperCase = !ALPHABET.includes(char); 
    if (isUpperCase) {
        result += '.....O';
    }


    const charIndex = ALPHABET.indexOf(char.toLowerCase());
    const column = charIndex % 10;
    const row = Math.trunc(charIndex / 10);

    return result + `${COLUMN[column]}${ROW[row]}`;
}

module.exports = toBraille;