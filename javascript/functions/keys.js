/**
 * This algorithm works though a pattern in how Braille dots are arranged per character.
 * The bottom two dots indicate a "row", where the alphabet may be divided up into 3 rows: A-J, K-T, U-Z. 
 * Within each row, this is a periodic set of 10 patterns on the upper four dots;
 * A particular row and column combination indicates a specific character.
 */

// For converting English to Braille, an array is used to instantly retrieve the Braille translation.
const ROW_TO_BRAILLE = ['..', 'O.', 'OO'];
const COLUMN_TO_BRAILLE = ['O...', 'O.O.', 'OO..', 'OO.O', 'O..O', 'OOO.', 'OOOO', 'O.OO', '.OO.','.OOO'];

// For converting Braille to English, an object is used to instantly retrieve the character index.
const BRAILLE_TO_ROW = {};
ROW_TO_BRAILLE.forEach((braille, index) => {
    BRAILLE_TO_ROW[braille] = index;
});

const BRAILLE_TO_COLUMN = {};
COLUMN_TO_BRAILLE.forEach((braille, index) => {
    BRAILLE_TO_COLUMN[braille] = index;
});

// Does not contain 'w'.
const ALPHABET = 'abcdefghijklmnopqrstuvxyz'; 

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

