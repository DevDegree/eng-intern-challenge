const { ROW_TO_BRAILLE: ROWS, COLUMN_TO_BRAILLE: COLUMNS, 
    ALPHABET, W_BRAILLE, CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE } = require('./keys');

let NUMBER_FLAG = false;

const toBraille = (input) => {
    let result = '';

    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        if (char === ' ') { // Adds a space.
            result += SPACE;
        } else { // Converts alphanumeric English character to Braille.
            result += parseEnglish(char);
        }
    }

    return result;
}

const parseEnglish = (char) => {

    // 'w' and 'W' are special cases.
    if (char === 'w') { return W_BRAILLE; }
    if (char === 'W') { return CAPITAL_FOLLOWS + W_BRAILLE; }

    let result = '';

    const isNumber = !ALPHABET.includes(char) && !ALPHABET.includes(char.toLowerCase());
    if (isNumber) {
        if (!NUMBER_FLAG) {
            result += NUMBER_FOLLOWS; // Prepend with number follows character.
        }

        NUMBER_FLAG = true; // Raise number flag so succeeding numbers won't be prepended with a number follows character.

        // A number is equivalent to its column, with its bottom two dots the same as row 1. 
        return result + `${COLUMNS[char - 1]}${ROWS[0]}`;
    }

    NUMBER_FLAG = false; // Remove number flag if character is no longer a number. 

    const isUpperCase = !ALPHABET.includes(char); 
    if (isUpperCase) {
        result += CAPITAL_FOLLOWS; // If capital, prepend with capital follows character.
    }
    
    const charIndex = ALPHABET.indexOf(char.toLowerCase());

    /**
     * Once a character is converted to an integer, 
     * we use the ones decimal place to signify the "column",
     * and the tens decimal place to signify the "row".
     * E.g., 'S' -> 18 -> row 1, column 8
     */
    const column = charIndex % 10;
    const row = Math.trunc(charIndex / 10);

    return result + `${COLUMNS[column]}${ROWS[row]}`;
}

module.exports = toBraille;