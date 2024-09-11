/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */

const toEnglish = require('./translators/toEnglish');
const toBraille = require('./translators/toBraille');
const readline = require('readline-sync');

const isEnglish = (input) => {
    // TO DO
    return true;
}

const parseInput = (input) => {
    if (isEnglish(input)) {
        return toBraille(input);
    }

    return toEnglish(input);
}

function main() {
    const input = readline.question('Input: ');
    // TO DO: type checking for input

    console.log(`Output: ${parseInput(input)}`);
}
main();
