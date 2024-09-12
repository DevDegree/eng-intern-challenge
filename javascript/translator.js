/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * 
 * September 11, 2024
 * 
 * Shopify eng-intern-challenge
 */

const toEnglish = require('./functions/toEnglish');
const toBraille = require('./functions/toBraille');
const isEnglish = require('./functions/isEnglish');
const { validateInput, validateBrailleInputLength } = require('./functions/validators');

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
