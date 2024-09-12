/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */

const toEnglish = require('./functions/toEnglish');
const toBraille = require('./functions/toBraille');
const isEnglish = require('./functions/isEnglish');

const validateInput = (input, isEnglishString) => {
    if (/[^A-Za-z0-9 .]/.test(input)) { throw new Error('Invalid input.'); }
    if (!isEnglishString && (input.length % 6 !== 0)) { throw new Error('Invalid input.'); }
    return input;
}

function main() {
    if (process.argv.length < 3) { return }
    
    const input = process.argv.slice(2).join(' ');
    const isEnglishString = isEnglish(input);
    validateInput(input, isEnglishString);

    const output = isEnglish(input) ? toBraille(input) : toEnglish(input);
    console.log(output);
}
main();
