const {
    BRAILLE_LETTERS_TO_ENGLISH, 
    BRAILLE_NUMBERS_TO_ENGLISH, 
    BRAILLE_SYMBOLS_TO_ENGLISH,
    ENGLISH_LETTERS_TO_BRAILLE, 
    ENGLISH_SYMBOLS_TO_BRAILLE,
    CAPITAL_FOLLOWS, 
    DECIMAL_FOLLOWS, 
    NUMBER_FOLLOWS,  } = require('../constants');

const translateBrailleToEnglish = (sentence) => {
    let translatedSentence = '';

    let doesCapitalFollow = false;
    let doesNumberFollow = false;

    for (let i = 0; i < sentence.length; i+=6) {
        const brailleChar = sentence.slice(i, i+6);

        // Follows
        if (brailleChar === CAPITAL_FOLLOWS) {
            doesCapitalFollow = true;
        } else if (brailleChar === NUMBER_FOLLOWS) {
            doesNumberFollow = true;
        } else if (brailleChar === DECIMAL_FOLLOWS) {
            translatedSentence += '.'
        } 
        // Numbers
        else if (doesNumberFollow) { 
            if (brailleChar === ENGLISH_LETTERS_TO_BRAILLE[' ']) {
                translatedSentence += ' ';
                doesNumberFollow = false;
            } else if (brailleChar === ENGLISH_SYMBOLS_TO_BRAILLE['>']) {
                translatedSentence += '>';
            } else
                translatedSentence += BRAILLE_NUMBERS_TO_ENGLISH[brailleChar];
        } 
        // Letters and symbols
        else { 
            let char = BRAILLE_LETTERS_TO_ENGLISH[brailleChar] ?? BRAILLE_SYMBOLS_TO_ENGLISH[brailleChar];
            if (doesCapitalFollow) char = char.toUpperCase();
            doesCapitalFollow = false;
            translatedSentence += char;
        }
    }
    console.log(translatedSentence);
};

module.exports = { translateBrailleToEnglish };
