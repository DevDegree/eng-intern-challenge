// Define Braille alphabet for letters and numbers
const brailleAlphabet = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..",
    f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.",
    p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......", "#": ".O.OOO", cap: ".....O"
};

// Reverse the braille alphabet for decoding
const englishAlphabet = {};
for (const [key, value] of Object.entries(brailleAlphabet)) {
    englishAlphabet[value] = key;
}

// Function to translate from English to Braille
function englishToBraille(text) {
    let result = "";
    let numberMode = false;
    for (const char of text) {
        if (/[A-Z]/.test(char)) {
            result += brailleAlphabet['cap'] + brailleAlphabet[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!numberMode) {
                result += brailleAlphabet['#'];
                numberMode = true;
            }
            result += brailleAlphabet[char];
        } else if (char === ' ') {
            numberMode = false;
            result += brailleAlphabet[' '];
        } else {
            numberMode = false;
            result += brailleAlphabet[char];
        }
    }
    return result;
}

// Function to translate from Braille to English
function brailleToEnglish(braille) {
    let result = "";
    let numberMode = false;
    let capitalize = false;
    for (let i = 0; i < braille.length; i += 6) {
        const symbol = braille.slice(i, i + 6);
        if (symbol === brailleAlphabet['cap']) {
            capitalize = true;
        } else if (symbol === brailleAlphabet['#']) {
            numberMode = true;
        } else {
            let letter = englishAlphabet[symbol];
            if (capitalize) {
                letter = letter.toUpperCase();
                capitalize = false;
            }
            if (numberMode) {
                numberMode = false; // Reset number mode after translating
            }
            result += letter;
        }
    }
    return result;
}

// Main function to detect and translate input
function translate(input) {
    if (/[O.]/.test(input)) {
        // Assume input is Braille if it contains O or .
        return brailleToEnglish(input);
    } else {
        // Otherwise, translate from English to Braille
        return englishToBraille(input);
    }
}

// Capture all command-line arguments without needing quotes and join them into a string
const input = process.argv.slice(2).join(' ');
console.log(translate(input));
