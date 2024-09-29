/*
 *  Author: Kaleb Jubar
 *  Created: 28 Sep 2024, 2:49:59 PM
 *  Last update: 29 Sep 2024, 12:16:26 PM
 *  Copyright (c) 2024 Kaleb Jubar
 */

// English-to-Braille dictionary object
const englishToBraille = {
    // letters
    a: "O.....",
    b: "O.O...",
    c: "OO....",
    d: "OO.O..",
    e: "O..O..",
    f: "OOO...",
    g: "OOOO..",
    h: "O.OO..",
    i: ".OO...",
    j: ".OOO..",
    k: "O...O.",
    l: "O.O.O.",
    m: "OO..O.",
    n: "OO.OO.",
    o: "O..OO.",
    p: "OOO.O.",
    q: "OOOOO.",
    r: "O.OOO.",
    s: ".OO.O.",
    t: ".OOOO.",
    u: "O...OO",
    v: "O.O.OO",
    w: ".OOO.O",
    x: "OO..OO",
    y: "OO.OOO",
    z: "O..OOO",

    // numbers
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO..",

    // special indicators
    capital: ".....O",
    number: ".O.OOO",
    " ": "......",
};

// Braille-to-English dictionary object
// build automatically from the English-to-Braille dictionary so I don't have to write it out twice
// TODO: figure out number handling
const brailleToEnglish = {};
for (const letter in englishToBraille) {
    const brailleChar = englishToBraille[letter];
    brailleToEnglish[brailleChar] = letter;
}

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
    // could use .reduce() here but it makes the code harder to read and doesn't simplify anything
    let input = process.argv[2];
    for (let i = 3; i < process.argv.length; i++) {
        input += ` ${process.argv[i]}`;
    }
    console.debug("Input", input);

    // determine if input is in English or Braille
    // we can use .reduce() on something that is not an array by using .call() to apply to any
    // arbitrary "this" object that is iterable, including strings
    // using .reduce() helps simplify a lot of this logic and eliminate loops and flags and such
    // more worth it here than for parsing program input, IMO
    const inputInBraille = Array.prototype.reduce.call(
        input,
        (allBraille, curChar) => (
            // check if char is one of O or .
            allBraille && (curChar === "O" || curChar === ".")
        ),
        true    // start reducing with true so we can use &&
    ) && input.length % 6 === 0;    // also check if length is divisible by 6, because we can't translate if it's not
    console.debug("In Braille?", inputInBraille);

    // do translation
    let output = "";
    if (inputInBraille) {
        // parse Braille string
        let parseNum = false, parseCapital = false;
        for (let i = 0; i < input.length; i += 6) {
            const char = brailleToEnglish[input.slice(i, i + 6)];

            // reset flags on space
            if (char === " ") {
                parseNum = false;
                parseCapital = false;
                output += char;
            }
            // set flags
            else if (char === "capital") {
                parseCapital = true;
            }
            else if (char === "number") {
                parseNum = true;
            }
            // parse normal character
            else {
                // capital set
                if (parseCapital) {
                    output += char.toUpperCase();
                    parseCapital = false;   // flag only applies to next letter
                }
                // number set
                else if (parseNum) {
                    // TODO: handle numbers, Braille goes from 1-9 then 0 but ASCII is 0-9
                    output += char;
                }
                // no flag, just append character
                else {
                    output += char;
                }
            }
        }
    } else {
        // parse English string
        let numFlagAdded = false;
        for (const char of input) {
            // reset number flag on space
            if (char === " ") {
                numFlagAdded = false;
                output += englishToBraille[char];
            }
            // char is a number, handle number parsing
            else if (!Number.isNaN(+char)) {
                // add number flag to output if it hasn't been already
                if (!numFlagAdded) {
                    output += englishToBraille.number
                    numFlagAdded = true;
                }

                output += englishToBraille[char];
            }
            // char is a capital letter
            else if (char === char.toUpperCase()) {
                output += englishToBraille.capital;
                output += englishToBraille[char.toLowerCase()];
            }
            // char is a lowercase letter
            else {
                output += englishToBraille[char];
            }
        }
    }

    // print translated string
    console.log(output);
}

// invoke main
main();