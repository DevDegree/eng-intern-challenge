const { ROW_TO_BRAILLE: ROWS, COLUMN_TO_BRAILLE: COLUMNS, 
    ALPHABET, W_BRAILLE, CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE } = require('./keys');

let NUMERIC_FLAG = false;

const toBraille = (input) => {
    let result = '';

    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        if (char === ' ') {
            result += SPACE;
        } else {
            result += parseEnglish(char);
        }
    }

    return result;
}

const parseEnglish = (char) => {

    // 'w' and 'W' are special cases
    if (char === 'w') { return W_BRAILLE; }
    if (char === 'W') { return CAPITAL_FOLLOWS + W_BRAILLE; }

    let result = '';

    const isNumber = !ALPHABET.includes(char) && !ALPHABET.includes(char.toLowerCase());
    if (isNumber) {
        if (!NUMERIC_FLAG) {
            result += NUMBER_FOLLOWS;
        }

        NUMERIC_FLAG = true;
        return result + `${COLUMNS[char - 1]}${ROWS[0]}`;
    }

    NUMERIC_FLAG = false;

    const isUpperCase = !ALPHABET.includes(char); 
    if (isUpperCase) {
        result += CAPITAL_FOLLOWS;
    }
    
    const charIndex = ALPHABET.indexOf(char.toLowerCase());
    const column = charIndex % 10;
    const row = Math.trunc(charIndex / 10);

    return result + `${COLUMNS[column]}${ROWS[row]}`;
}

module.exports = toBraille;