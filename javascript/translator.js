#!/usr/bin/env node

// Access the arguments passed during runtime
const args = process.argv.slice(2);

// Check if a string to translate is passed
if (args.length === 0) {
    console.log("Please provide a string to translate.");
    process.exit(1); // Exit with a failure code
}

const textToTranslate = args[0];

const brailleTexts = {
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
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
};

// Create the reverse map (braille -> english)
const brailleToEnglishMap = {};
for (const key in brailleTexts) {
    brailleToEnglishMap[brailleTexts[key]] = key;
}

function isBraille(input) {
    for (let i = 0; i < input.length; i++) {
        if (input[i] !== "O" && input[i] !== ".") {
            return false;
        }
    }
    return input.length % 6 === 0;
}

function translateToBraille(input) {
    let output = "";
    let isNumberMode = false;

    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        if (char === " ") {
            output += brailleTexts[" "];
        } else if (!isNaN(char) && char !== " ") {
            // If it's a number
            if (!isNumberMode) {
                output += brailleTexts["number follows"];
                isNumberMode = true;
            }
            output += brailleTexts[char];
        } else if (char === ".") {
            // If it's a period, prepend the "decimal follows"
            output += brailleTexts["decimal follows"] + brailleTexts["."];
        } else if (char >= "A" && char <= "Z") {
            // If it's an uppercase letter
            output +=
                brailleTexts["capital follows"] +
                brailleTexts[char.toLowerCase()];
            isNumberMode = false; // exit number mode when encountering letters
        } else if (char in brailleTexts) {
            // If it's a lowercase letter or punctuation
            output += brailleTexts[char];
            isNumberMode = false; // exit number mode when encountering letters
        }
    }

    return output;
}

function translateToEnglish(input) {
    let output = "";
    let isCapital = false;
    let isNumberMode = false;
    let isDecimalMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleTexts["capital follows"]) {
            isCapital = true;
        } else if (brailleChar === brailleTexts["number follows"]) {
            isNumberMode = true;
        } else if (brailleChar === brailleTexts["decimal follows"]) {
            isDecimalMode = true;
        } else {
            let translatedChar;

            if (isNumberMode) {
                translatedChar = Object.keys(brailleTexts).find(
                    (key) => brailleTexts[key] === brailleChar && !isNaN(key)
                );
            } else {
                translatedChar = brailleToEnglishMap[brailleChar];
            }

            if (!translatedChar) {
                translatedChar = brailleChar; // Default to raw braille if not found
            }

            if (isCapital) {
                translatedChar = translatedChar.toUpperCase();
                isCapital = false;
            }

            if (isDecimalMode) {
                translatedChar = "."; // Add a period for decimal
                isDecimalMode = false;
            }

            output += translatedChar;
        }
    }

    return output;
}

function translate(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

console.log(translate(textToTranslate));
