// Braille mappings (O for raised, . for unraised)
const BRAILLE_ALPHABET = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    " ": "......",  // Space character
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Reverse mapping from Braille to English
const ENGLISH_ALPHABET = Object.entries(BRAILLE_ALPHABET).reduce((obj, [key, value]) => {
    obj[value] = key;
    return obj;
}, {});

// Special symbols
const CAPITAL_PREFIX = ".....O";  // Capital letter indicator
const NUMBER_PREFIX = ".O.OOO";   // Number indicator

// Detect if input is English or Braille
function detectInputType(input) {
    return /^[O.]+$/.test(input) ? 'braille' : 'english';
}

// Translate English to Braille
function englishToBraille(text) {
    let result = '';
    let isNumber = false;
    
    for (const char of text) {
        if (/[A-Z]/.test(char)) {
            result += CAPITAL_PREFIX + BRAILLE_ALPHABET[char.toLowerCase()];
        } else if (/\d/.test(char)) {
            if (!isNumber) {
                result += NUMBER_PREFIX;
                isNumber = true;
            }
            result += BRAILLE_ALPHABET[char];
        } else if (char === " ") {
            result += BRAILLE_ALPHABET[char];
            isNumber = false; // Reset number mode after a space
        } else {
            result += BRAILLE_ALPHABET[char] || '';
            isNumber = false; // Reset number mode for non-numeric characters
        }
    }
    
    return result;
}

// Translate Braille to English
function brailleToEnglish(braille) {
    let result = '';
    let i = 0;
    let isNumberMode = false;

    while (i < braille.length) {
        const brailleChar = braille.slice(i, i + 6);

        if (brailleChar === CAPITAL_PREFIX) {
            i += 6;
            const nextBrailleChar = braille.slice(i, i + 6);
            const capitalLetter = ENGLISH_ALPHABET[nextBrailleChar];
            if (capitalLetter) {
                result += capitalLetter.toUpperCase();
            } else {
                throw new Error("Invalid Braille sequence.");
            }
        } else if (brailleChar === NUMBER_PREFIX) {
            isNumberMode = true;
            i += 6;
        } else {
            const englishChar = ENGLISH_ALPHABET[brailleChar];
            if (englishChar) {
                result += isNumberMode && /\d/.test(englishChar) ? englishChar : englishChar;
            } else {
                throw new Error("Invalid Braille sequence.");
            }
            if (isNumberMode && englishChar === " ") {
                isNumberMode = false;
            }
        }
        i += 6;
    }

    return result;
}

// Main function to translate based on the input type
function translator(input) {
    const inputType = detectInputType(input);
    if (inputType === 'english') {
        console.log(englishToBraille(input));
    } else {
        console.log(brailleToEnglish(input));
    }
}

// Example usage (node script.js "Hello" or node script.js ".....OO.OO..O..O..O.O.O.O.O.O.O..OO")
const input = process.argv.slice(2).join(" ");
translator(input);
