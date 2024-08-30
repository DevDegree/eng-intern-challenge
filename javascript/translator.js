const {
    BRAILLE_LETTERS_TO_ENGLISH, 
    BRAILLE_NUMBERS_TO_ENGLISH, 
    BRAILLE_SYMBOLS_TO_ENGLISH,
    ENGLISH_LETTERS_TO_BRAILLE, 
    ENGLISH_SYMBOLS_TO_BRAILLE,
    ENGLISH_NUMBERS_TO_BRAILLE,
    CAPITAL_FOLLOWS, 
    DECIMAL_FOLLOWS, 
    NUMBER_FOLLOWS,  } = require('./constants');

// English or Braille
const args = process.argv.slice(2);
const regexBrailleStart = /^O{0,5}.(.*)$/;
const isBraille = args.length <= 1 && args[0].length % 6 === 0 && regexBrailleStart.test(args[0]);

let translatedSentence = '';

// From Braille to English
if (isBraille) {
    const sentence = args[0];

    let doesCapitalFollow = false;
    let doesNumberFollow = false;

    for (let i = 0; i < sentence.length; i+=6) {
        const brailleChar = sentence.slice(i, i+6);

        // Follows
        if (brailleChar === CAPITAL_FOLLOWS) {
            doesCapitalFollow = true;
            continue;
        } else if (brailleChar === NUMBER_FOLLOWS) {
            doesNumberFollow = true;
            continue;
        } else if (brailleChar === DECIMAL_FOLLOWS) {
            translatedSentence += '.'
            continue;
        }

        // Numbers
        if (doesNumberFollow) {
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
}
// From English to Braille
else {
    let writingNumbers = false;
    for (let i = 0; i < args.length; i++) {
        for (let char of args[i]) {
            
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
        if (i+1 < args.length) translatedSentence += ENGLISH_LETTERS_TO_BRAILLE[' '];
        writingNumbers = false;
    }
}

console.log(translatedSentence);
