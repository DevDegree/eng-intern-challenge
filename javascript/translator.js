/*
 *  Author: Kaleb Jubar
 *  Created: 28 Sep 2024, 2:49:59 PM
 *  Last update: 28 Sep 2024, 3:42:52 PM
 *  Copyright (c) 2024 Kaleb Jubar
 */

// English-to-Braille object
// TODO: figure out if it's better to index on ASCII number or character
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
    decimal: ".O...O",
    number: ".O.OOO",

    // special characters
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
};

// Braille-to-English object
// build automatically from the English-to-Braille object so I don't have to write it out twice
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
    let input = process.argv[2];
    for (let i = 3; i < process.argv.length; i++) {
        input += ` ${process.argv[i]}`;
    }
    console.debug("Input", input);

    // determine if input is in English or Braille
    // we can use the reduce higher-order function on something that is not an array by using .call() to apply to any
    // arbitrary "this" object that is iterable, including strings
    // using reduce helps simplify a lot of this logic and eliminate loops and flags and such
    const inputInBraille = Array.prototype.reduce.call(
        input,
        (allBraille, curChar) => (
            allBraille && (curChar === "O" || curChar === ".")
        ),
        true
    ) && input.length % 6 === 0;    // also check if length is divisible by 6, because we can't translate if it's not
    console.debug("In Braille?", inputInBraille);
}

main();