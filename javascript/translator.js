//Charlie Zhang, Sep 9, 2024.

// Mapping of English characters to their Braille representation
const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "capital_follows": ".....O", // Indicates that the next letter should be capitalized
    "decimal_follows": ".O...O", // Indicates that the next character is a decimal
    "number_follows": ".O.OOO", // Indicates that the next characters are numbers
    " ": "......" // Braille representation of a space
};

// Mapping of numbers to their Braille representation
const numbersToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Create reverse mappings for translating Braille back to English and numbers
let brailleToEnglish = {};
let brailleToNumbers = {};

// Populate reverse mappings
for (let [key, value] of Object.entries(englishToBraille)) {
    brailleToEnglish[value] = key;
}
for (let [key, value] of Object.entries(numbersToBraille)) {
    brailleToNumbers[value] = key;
}

// Determine if the input string is in English or Braille
function isEnglish(input) {
    for (let char of input) {
        let lowerChar = char.toLowerCase();
        // Check if the character is a letter (excluding 'O') or a digit
        if ((lowerChar >= 'a' && lowerChar <= 'z' && char !== 'O') || (char >= '0' && char <= '9')) {
            return true;
        }
    }
    return false;
}

// Translate English text to Braille
function translateToBraille(input) {
    let insideNumber = false;

    for (let char of input) {
        // Handle capitalization
        if (char === char.toUpperCase() && isNaN(char)) {
            process.stdout.write(englishToBraille["capital_follows"]);
        }

        // Handle numbers
        if (insideNumber && char === ' ') {
            insideNumber = false;
        }
        if (!isNaN(char) && char !== ' ') {
            if (!insideNumber) {
                process.stdout.write(englishToBraille["number_follows"]);
                insideNumber = true;
            }
            process.stdout.write(numbersToBraille[char]);
            continue;
        }

        // Translate to Braille
        const braille = englishToBraille[char.toLowerCase()];
        process.stdout.write(braille || " "); // Write a space if character not found in Braille map
    }

    console.log(); // Move to the next line after translation
}

// Translate Braille text to English
function translateToEnglish(input) {
    let characters = [];
    // Split input into 6-character Braille cells
    for (let i = 0; i < input.length; i += 6) {
        characters.push(input.slice(i, i + 6));
    }

    let capitalFollows = false;
    let numberFollows = false;

    for (let char of characters) {
        // Check for capitalization and number indicators
        if (char === englishToBraille["capital_follows"]) {
            capitalFollows = true;
            continue;
        }
        if (char === englishToBraille["number_follows"]) {
            numberFollows = true;
            continue;
        }

        // Translate Braille to English
        let englishChar = brailleToEnglish[char];
        if (numberFollows) {
            englishChar = brailleToNumbers[char];
        }

        // Handle numbers and capitalization
        if (numberFollows && englishChar >= "a" && englishChar <= "j") {
            englishChar = String.fromCharCode('1'.charCodeAt(0) + (englishChar.charCodeAt(0) - 'a'.charCodeAt(0)));
        } else if (capitalFollows) {
            englishChar = englishChar.toUpperCase();
            capitalFollows = false;
        }

        process.stdout.write(englishChar);

        // Reset number follows on space
        if (englishChar === " ") {
            numberFollows = false;
        }
    }

    console.log(); // Move to the next line after translation
}

// Get input from command-line arguments
const input = process.argv.slice(2).join(" ");

// Determine if input is English or Braille and translate accordingly
if (isEnglish(input)) {
    translateToBraille(input);
} else {
    translateToEnglish(input);
}
