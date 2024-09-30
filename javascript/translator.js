#!/usr/bin/env node

// Braille Dictionary as per image provided in the Git hub link
const brailleDict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO"
};

// Reverse dictionary for Braille to English conversion
const englishDict = Object.fromEntries(Object.entries(brailleDict).map(([k, v]) => [v, k]));

function isBraille(input) {
    // checking if patterns "O","." exists, then categorizing it as Braille
    return /^[O.]+$/.test(input);
}

// Function to convert English to Braille
function englishToBraille(input) {
    let brailleOutput = "";
    let numberMode = false;

    for (let char of input) {
        if (char >= "A" && char <= "Z") {
            // Handling capital letters
            brailleOutput += brailleDict["capital"];
            brailleOutput += brailleDict[char.toLowerCase()];
        } else if (char >= "0" && char <= "9" && !numberMode) {
            // Handling numbers with "number" mode
            brailleOutput += brailleDict["number"];
            numberMode = true;
            brailleOutput += brailleDict[char];
        } else if (char === " ") {
            // Handling spaces
            brailleOutput += brailleDict[" "];
            numberMode = false;
        } else {
            // Handling lowercase letters
            brailleOutput += brailleDict[char];
        }
    }

    return brailleOutput;
}

// Function to convert Braille to English
function brailleToEnglish(input) {
    let englishOutput = "";
    let capitalNext = false;
    let numberMode = false;

    for (let i = 0; i < input.length; i = i+6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleDict["capital"]) {
            // Handling capital letter indicator
            capitalNext = true;
            continue;
        } else if (brailleChar === brailleDict["number"]) {
            // Handling number indicator
            numberMode = true;
            continue;
        }

        let englishChar = englishDict[brailleChar];

        if (capitalNext) {
            englishChar = englishChar.toUpperCase();
            capitalNext = false;
        }

        if (numberMode && /^[a-z]$/.test(englishChar)) {
            // Handle number mode conversion
            englishChar = "1234567890"["abcdefghij".indexOf(englishChar)];
        }

        if (englishChar === " ") {
            numberMode = false; // Reset number mode after space
        }

        englishOutput += englishChar;
    }

    return englishOutput;
}

function main() {
    const args = process.argv.slice(2);
    const input = args.join(" ");

    if (isBraille(input)) {
        // If input is Braille, translating to English
        console.log(brailleToEnglish(input));
    } else {
        // If input is English, translating it to Braille
        console.log(englishToBraille(input));
    }
}

main();
