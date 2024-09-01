const {
    ENGLISH_LETTERS_TO_BRAILLE, 
    ENGLISH_SYMBOLS_TO_BRAILLE,
    ENGLISH_NUMBERS_TO_BRAILLE,
    CAPITAL_FOLLOWS, 
    DECIMAL_FOLLOWS, 
    NUMBER_FOLLOWS,  } = require('../constants');

const translateEnglishToBraille = (words) => {
    let translatedSentence = '';

    let writingNumbers = false;
    for (let i = 0; i < words.length; i++) {
        for (let char of words[i]) {

            // Numbers
            if ('0' <= char && char <= '9') {
                if (!writingNumbers) translatedSentence += NUMBER_FOLLOWS;
                translatedSentence += ENGLISH_NUMBERS_TO_BRAILLE[char];
                writingNumbers = true;
            }
            else if (char === '.' && writingNumbers)
                translatedSentence += DECIMAL_FOLLOWS;
            else if (char === '>' && writingNumbers)
                translatedSentence += ENGLISH_SYMBOLS_TO_BRAILLE['>'];

            // Letters and Symbols
            else {
                if (char === char.toUpperCase()) translatedSentence += CAPITAL_FOLLOWS;
                translatedSentence += ENGLISH_LETTERS_TO_BRAILLE[char.toLowerCase()] ?? ENGLISH_SYMBOLS_TO_BRAILLE[char.toLowerCase()];                
            }
        }

        // Spaces
        if (i+1 < words.length) translatedSentence += ENGLISH_LETTERS_TO_BRAILLE[' '];
        writingNumbers = false;
    }
    console.log(translatedSentence);
};

module.exports = { translateEnglishToBraille };
