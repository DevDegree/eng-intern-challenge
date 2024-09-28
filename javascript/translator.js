/*
 *  Author: Kaleb Jubar
 *  Created: 28 Sep 2024, 2:49:59 PM
 *  Last update: 28 Sep 2024, 3:11:51 PM
 *  Copyright (c) 2024 Kaleb Jubar
 */

// English-to-Braille object
const englishToBraille = {
    a: "O.....",
};
console.log(englishToBraille);

// Braille-to-English object
// build automatically from the English-to-Braille object so I don't have to write it out twice
const brailleToEnglish = {};
for (const letter in englishToBraille) {
    const brailleChar = englishToBraille[letter];
    brailleToEnglish[brailleChar] = letter;
}
console.log(brailleToEnglish);

/**
 * Main function for the Braille translator.
 * Takes a string on the command line in either English or Braille and translates to the opposite.
 * 
 * This technically could just be written straight into the file since it's being executed via Node,
 * but making a function allows for early returns if necessary (like during argument validation).
 */
function main() {
    // check for arguments
    if (process.argv.length < 3) {
        console.error("No arguments provided.");
        return;
    }

    // assemble input string, as arguments are split on spaces
    let input = process.argv[2];
    for (let i = 3; i < process.argv.length; i++) {
        input += ` ${process.argv[i]}`;
    }

    console.log("Input:", input);
}

main();