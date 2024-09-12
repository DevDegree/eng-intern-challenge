const ROW_TO_BRAILLE = ['..', 'O.', 'OO'];
const COLUMN_TO_BRAILLE = ['O...', 'O.O.', 'OO..', 'OO.O', 'O..O', 'OOO.', 'OOOO', 'O.OO', '.OO.','.OOO'];

const BRAILLE_TO_ROW = {};
ROW_TO_BRAILLE.forEach((braille, index) => {
    BRAILLE_TO_ROW[braille] = index;
});

const BRAILLE_TO_COLUMN = {};
COLUMN_TO_BRAILLE.forEach((braille, index) => {
    BRAILLE_TO_COLUMN[braille] = index;
});

const ALPHABET = 'abcdefghijklmnopqrstuvxyz'; // Does not contain 'w'

const W_BRAILLE = '.OOO.O';
const CAPITAL_FOLLOWS = '.....O';
const NUMBER_FOLLOWS = '.O.OOO';
const SPACE = '......';

module.exports = {
    ROW_TO_BRAILLE,
    COLUMN_TO_BRAILLE,
    BRAILLE_TO_ROW,
    BRAILLE_TO_COLUMN,
    ALPHABET,
    W_BRAILLE,
    CAPITAL_FOLLOWS,
    NUMBER_FOLLOWS,
    SPACE
}

