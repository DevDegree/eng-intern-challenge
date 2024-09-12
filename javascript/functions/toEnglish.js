const { BRAILLE_TO_ROW: ROWS, BRAILLE_TO_COLUMN: COLUMNS, 
    ALPHABET, W_BRAILLE, CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE } = require('./keys');

const BRAILLE_CHAR_LEN = 6;
let CAPITAL_FLAG = false, NUMBER_FLAG = false;

const toEnglish = (brailleString) => {
    let result = "";

    for (let i = 0; i < brailleString.length; i += BRAILLE_CHAR_LEN) {
        const brailleChar = brailleString.substring(i, i + BRAILLE_CHAR_LEN);

        if (brailleChar === CAPITAL_FOLLOWS) { // Raises capital flag.
            CAPITAL_FLAG = true; 
        } else if (brailleChar === NUMBER_FOLLOWS) { // Raises number flag.
             NUMBER_FLAG = true; 
        } else if (brailleChar === SPACE) { // Adds a space. If capital flag is raised, removes capital flag as well.
            if (NUMBER_FLAG) { NUMBER_FLAG = false }
            result += " ";
        } else { // Convert alphanumeric Braille character to English. 
            result += parseBraille(brailleChar); 
        }
    }

    return result;
}

const parseBraille = (char) => {    

    // 'w' is a special case.
    if (char === W_BRAILLE) { return 'w'; } 
    
    // The row is represented by the bottom two dots.
    const row = ROWS[char.substring(4, BRAILLE_CHAR_LEN)];

    // The column is represented by the upper four dpts.
    const column = COLUMNS[char.substring(0, 4)];
    
    if (NUMBER_FLAG) {
        return `${(column + 1)}`; // A number is equivalent to its column.
    }

    /**
     * Once row and column have been obtained,
     * the integer value of the character is calculated.
     */
    const letter = ALPHABET.charAt(column + (row * 10))
    
    if (CAPITAL_FLAG) {
        CAPITAL_FLAG = false;
        return letter.toUpperCase();
    } 

    return letter;
}

module.exports = toEnglish;