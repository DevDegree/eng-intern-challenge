/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */

const toEnglish = require('./functions/toEnglish');
const toBraille = require('./functions/toBraille');
const isEnglish = require('./functions/isEnglish');

const validateInput = (input) => {
    // Program only supports alphanumeric, ., and space characters.
    if (/[^A-Za-z0-9 .]/.test(input)) { throw new Error('Invalid input.'); } 
}

const validateBrailleInputLength = (input) => {
    // A Braille input must be divisible by 6.
    if (input.length % 6 !== 0) { throw new Error('Invalid input.'); }
}

function main() {
    if (process.argv.length < 3) { return }
      
    const input = process.argv.slice(2).join(' ');
    validateInput(input);

    let output = '';
    if (isEnglish(input)) {
        output = toBraille(input);
    } else {
        validateBrailleInputLength(input);
        output = toEnglish(input);
    }

    console.log(output);
}
main();
