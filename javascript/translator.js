const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Braille patterns for alphabet, numbers, and punctuation
const brailleAlphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    
    // Punctuation and symbols
    ",": ".O....", ".": ".O.O..", "?": ".O..O.", "!": ".OOO.O", ";": ".O.O..", ":": ".O..O.",
    "-": "....OO", "/": ".O..O.", "<": "OO....", ">": "OO.O..", "(": "O.OOO.", ")": ".OOO..", " ": "......"
};

const brailleNumbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Special Braille patterns
const brailleCapital = ".....O";
const brailleNumber = ".O.OOO";
const brailleSpace = "......";

// Reverse dictionaries for quick lookup
const reverseBrailleAlphabet = Object.fromEntries(Object.entries(brailleAlphabet).map(([k, v]) => [v, k]));
const reverseBrailleNumbers = Object.fromEntries(Object.entries(brailleNumbers).map(([k, v]) => [v, k]));

// Check if the input string is valid Braille
function isBraille(inputString) {
    return [...inputString].every(char => "O. ".includes(char));
}

// English to Braille translator
function englishToBraille(text) {
    let braille = [];
    for (let char of text) {
        if (char === " ") {
            braille.push(brailleSpace);
        } else if (char.toUpperCase() !== char.toLowerCase() && char === char.toUpperCase()) {
            // Capital letter
            braille.push(brailleCapital);
            braille.push(brailleAlphabet[char.toLowerCase()] || "......");
        } else if (/\d/.test(char)) {
            // Number
            braille.push(brailleNumber);
            braille.push(brailleNumbers[char]);
        } else {
            // Normal letter or punctuation
            braille.push(brailleAlphabet[char] || "......");
        }
    }
    return braille.join(" ");
}

// Braille to English translator
function brailleToEnglish(brailleText) {
    let english = [];
    let isNumberMode = false;
    let i = 0;

    while (i < brailleText.length) {
        let symbol = brailleText.slice(i, i + 6);

        if (symbol === brailleSpace) {
            english.push(" ");
            isNumberMode = false;
        } else if (symbol === brailleCapital) {
            // Capital letter follows
            i += 6;
            let capitalLetter = reverseBrailleAlphabet[brailleText.slice(i, i + 6)] || "";
            english.push(capitalLetter.toUpperCase());
        } else if (symbol === brailleNumber) {
            // Number mode
            isNumberMode = true;
        } else if (isNumberMode) {
            let number = reverseBrailleNumbers[symbol] || "";
            english.push(number);
        } else {
            let letter = reverseBrailleAlphabet[symbol] || "";
            english.push(letter);
        }

        i += 6;
    }

    return english.join("");
}

// Main function to allow user to choose translation direction
function main() {
    rl.question("Choose mode: [1] English to Braille, [2] Braille to English: ", function (mode) {
        if (mode === "1") {
            rl.question("Enter English text: ", function (inputText) {
                const translatedText = englishToBraille(inputText);
                console.log("\nTranslated to Braille:");
                console.log(translatedText);
                rl.close();
            });
        } else if (mode === "2") {
            rl.question("Enter Braille (separate characters by spaces): ", function (inputText) {
                const translatedText = brailleToEnglish(inputText.replace(/ /g, ""));
                console.log("\nTranslated to English:", translatedText);
                rl.close();
            });
        } else {
            console.log("Invalid option. Please try again.");
            rl.close();
        }
    });
}

// To test the code
main();
