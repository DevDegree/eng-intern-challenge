/**
 * Neil Dominic V. Torres
 * neildominictorres@gmail.com
 * Shopify eng-intern-challenge
 */
const readline = require('readline-sync');

function main() {
    const input = readline.question('Input: ');
    console.log(`Output: ${parseInput(input)}`);
}
main();

function parseInput(input) {
    return input;
}

