const { BRAILLE_TO_ROW: ROWS, BRAILLE_TO_COLUMN: COLUMNS, 
    ALPHABET, W_BRAILLE, CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE } = require('./keys');

const BRAILLE_CHAR_LEN = 6;
let CAPITAL_FLAG = false, NUMBER_FLAG = false;

const toEnglish = (brailleString) => {
    let result = "";

    for (let i = 0; i < brailleString.length; i += BRAILLE_CHAR_LEN) {
        const brailleChar = brailleString.substring(i, i + BRAILLE_CHAR_LEN);

        if (brailleChar === CAPITAL_FOLLOWS) { 
            CAPITAL_FLAG = true; 
        } else if (brailleChar === NUMBER_FOLLOWS) {
             NUMBER_FLAG = true; 
        } else if (brailleChar === SPACE) {
            if (NUMBER_FLAG) { NUMBER_FLAG = false }
            result += " ";
        } else { 
            result += parseBraille(brailleChar); 
        }
    }

    return result;
}

const parseBraille = (char) => {    

    // 'w' is a special case
    if (char === W_BRAILLE) { return 'w'; } 
    
    const row = ROWS[char.substring(4, 6)];
    const column = COLUMNS[char.substring(0, 4)];
    
    if (NUMBER_FLAG) {
        return `${(column + 1)}`;
    }
    
    const letter = ALPHABET.charAt(column + (row * 10))
    
    if (CAPITAL_FLAG) {
        CAPITAL_FLAG = false;
        return letter.toUpperCase();
    } 

    return letter;
}

module.exports = toEnglish;