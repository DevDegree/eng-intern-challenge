const brailleAlphabet = {
    A: "O.....",
    B: "O.O...",
    C: "OO....",
    D: "OO.O..",
    E: "O..O..",
    F: "OOO...",
    G: "OOOO..",
    H: "O.OO..",
    I: ".OO...",
    J: ".OOO..",
    K: "O...O.",
    L: "O.O.O.",
    M: "OO..O.",
    N: "OO.OO.",
    O: "O..OO.",
    P: "OOO.O.",
    Q: "OOOOO.",
    R: "O.OOO.",
    S: ".OO.O.",
    T: ".OOOO.",
    U: "O...OO",
    V: "O.O.OO",
    W: ".OOO.O",
    X: "OO..OO",
    Y: "OO.OOO",
    Z: "O..OOO",
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
    capital: ".....O",
    decimal: ".O...O",
    number: ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": "..O.O.",
    "<": "..O...",
    ">": "..O...",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
};

// Reverse lookup for Braille Alphabet
const reverseBrailleAlphabet = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z"
}

const reverseBrailleNumbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
};

const reverseSymbols = {
    ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number",
}

const reverseBrailleSpecialPunctuation = {
    "..OO.O": ".",
    ".O....": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.OO..": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
};

//Determine the string is English or Braille
function isBraille(str) {
    // Regular expression to match only 'O' and '.'
    const validChars = /^[O.]+$/;

    // Test the string against the regular expression
    return validChars.test(str);
}

//Translator: from English to Braille
function translateToBraille(engStr) {
    let braStr = "";
    let isNumberMode = false;  // A flag to track if number mode

    for (let i = 0; i < engStr.length; i++) {
        let char = engStr[i];

        // Check if the current character is a space
        if (char === " ") {
            braStr += brailleAlphabet[" "]; // Add Braille space
            isNumberMode = false;  // Reset number mode after a space
        }
        // Check if the current character is a number
        else if (!isNaN(char)) {
            if (!isNumberMode) {
                braStr += brailleAlphabet.number; // Add Braille number
                isNumberMode = true; // Turn number mode true
            }
            braStr += brailleAlphabet[char];  // Translate number to Braille
        }
        // Check if the current character is an uppercase letter
        else if (char === char.toUpperCase() && isNaN(char)) {
            braStr += brailleAlphabet.capital;  // Add Braille capital symbol
            braStr += brailleAlphabet[char];    // Add the letter's Braille
            isNumberMode = false;  // Reset number mode after a letter
        }
        // Check if the current character is a decimal point
        else if (char === "." && i > 0 && i < engStr.length - 1) {
            let beforeChar = engStr[i - 1];
            let afterChar = engStr[i + 1];

            // Only consider it as a decimal point if both before and after are numbers
            if (!isNaN(beforeChar) && !isNaN(afterChar)) {
                braStr += brailleAlphabet.decimal;  // Add Braille decimal symbol
            } else {
                // Otherwise treat it as a regular period
                braStr += brailleAlphabet["."];
            }
        }
        // Check if the current character is a special character
        else if (brailleAlphabet[char]) {
            braStr += brailleAlphabet[char]; // Add Braille for special characters
            isNumberMode = false;  // Reset number mode after special characters
        }
        // Handle lowercase letters
        else {
            braStr += brailleAlphabet[char.toUpperCase()]; // Add the letter's Braille
            isNumberMode = false;  // Reset number mode after a letter
        }
    }

    return braStr;
}

//Translator: from Braille to English
function translateToEnglish(braStr) {
    let engStr = "";
    let isNumberMode = false; // Track whether in number mode
    let isCapitalMode = false;
    // Split the Braille string into 6-character chunks
    let brailleChars = braStr.match(/.{1,6}/g);
    for (let i = 0; i < brailleChars.length; i++) {

        let brailleChar = brailleChars[i];

        // if braille is number, then change number mode then continue
        if (brailleChar === brailleAlphabet.number) {
            isNumberMode = true;
            continue;
        }

        // if braille is capital, then change capital mode then continue
        if (brailleChar === brailleAlphabet.capital) {
            isCapitalMode = true;
            continue;
        }
        if (brailleChar === reverseBrailleSpecialPunctuation[" "]) {
            engStr += " "; // Add a space
            isNumberMode = false; // Reset mode after space
            continue;
        }

        // if is number, then add number
        if (isNumberMode) {
            // if it is decimal
            if (reverseSymbols[brailleChar] === "decimal") {
                engStr += ".";
                continue;
            }
            engStr += reverseBrailleNumbers[brailleChar];
            continue;
        }

        // if is capital, then add to output otherwise add lower case
        if (isCapitalMode) {
            engStr += reverseBrailleAlphabet[brailleChar];
            isCapitalMode = false;
            continue;
        }

        try {
            engStr += reverseBrailleAlphabet[brailleChar].toLowerCase();
        } catch (TypeError) {
            // if cannot lower, it must be special punctuation
            engStr += reverseBrailleSpecialPunctuation[brailleChar];
        }
    }
    return engStr;
}

// Main function that determines which translation to use
function translate(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

// Main function
function main() {
    const args = process.argv.slice(2).join(" ");
    const translatedBraille = translate(args);
    console.log(translatedBraille);
}

if (require.main === module) {
    main();
}
