// Maps each letter, number, and special character to its Braille representation.
const BRAILLE_ALPHABET = {
    // Letters a-z
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",
    // Numbers 1-0
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    // Special symbols
    space: "......",      // Space
    capital: ".....O",    // Capital follows
    number: ".O.OOO"      // Number follows
};

// Creates reverse lookup from Braille to text.
const REVERSE_BRAILLE_ALPHABET = Object.fromEntries(Object.entries(BRAILLE_ALPHABET).map(([key, value]) => [value, key]));

// Checks if the input contains only Braille characters ("O" and ".").
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Converts text to Braille, including handling numbers and capital letters.
function translateToBraille(text) {
    let brailleOutput = '';
    let numberMode = false;

    for (const char of text) {
        if (char === ' ') {
            brailleOutput += BRAILLE_ALPHABET.space;
        } else if (/[0-9]/.test(char)) {
            if (!numberMode) {
                brailleOutput += BRAILLE_ALPHABET.number;
                numberMode = true;
            }
            brailleOutput += BRAILLE_ALPHABET[char];
        } else if (/[A-Z]/.test(char)) {
            brailleOutput += BRAILLE_ALPHABET.capital + BRAILLE_ALPHABET[char.toLowerCase()];
            numberMode = false;
        } else if (/[a-z]/.test(char)) {
            brailleOutput += BRAILLE_ALPHABET[char];
            numberMode = false;
        }
    }

    return brailleOutput;
}

// Maps Braille back to its corresponding text (letters, numbers, etc.)
function mapBrailleToChar(brailleChar, capitalMode, numberMode) {
    let letter = REVERSE_BRAILLE_ALPHABET[brailleChar];

    if (numberMode) {
        const numbersMap = { a: '1', b: '2', c: '3', d: '4', e: '5', f: '6', g: '7', h: '8', i: '9', j: '0' };
        letter = numbersMap[letter];
    }

    if (capitalMode) {
        letter = letter.toUpperCase();
    }

    return letter;
}

// Converts Braille back into plain text, handling numbers and capital letters.
function translateToEnglish(brailleText) {
    let englishOutput = '';
    let capitalMode = false;
    let numberMode = false;

    for (let i = 0; i < brailleText.length; i += 6) {
        const brailleChar = brailleText.slice(i, i + 6);

        if (brailleChar === BRAILLE_ALPHABET.space) {
            englishOutput += ' ';
            numberMode = false;
        } else if (brailleChar === BRAILLE_ALPHABET.capital) {
            capitalMode = true;
        } else if (brailleChar === BRAILLE_ALPHABET.number) {
            numberMode = true;
        } else {
            englishOutput += mapBrailleToChar(brailleChar, capitalMode, numberMode);
            capitalMode = false;
        }
    }

    return englishOutput;
}

// Main function to decide whether to translate to Braille or English based on input type.
function main() {
    const input = process.argv.slice(2).join(' ');

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

// Execute the main function when the script is run
main();
