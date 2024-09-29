const readline = require('readline');

// Braille translation mapping
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', 
    '<': 'O.O..O', '>': '.O.OO.'
};

// Prefixes for capital, numbers, and decimals
const capitalFollows = '.....O';
const numberFollows = '.O.OOO';
const decimalFollows = '.O...O';

// Reverse map for Braille to English translation
const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

// Function to translate English to Braille with special follows
function englishToBraille(input) {
    let brailleOutput = '';
    let isNumber = false;

    for (let char of input) {
        if (/[A-Z]/.test(char)) {
            brailleOutput += capitalFollows + brailleMap[char.toLowerCase()]; // No space here
        } else if (/[0-9]/.test(char)) {
            brailleOutput += numberFollows + brailleMap[char]; // No space here
        } else if (char === '.') {
            brailleOutput += decimalFollows; // No space here
        } else {
            brailleOutput += brailleMap[char.toLowerCase()]; // No space here
        }
    }

    return brailleOutput; // No need to trim, as spaces are managed
}

// Function to translate Braille to English considering follows
function brailleToEnglish(input) {
    const brailleArray = input.match(/.{1,6}/g); // Split input into chunks of 6 characters (Braille cell)
    let englishOutput = '';
    let isCapital = false;
    let isNumber = false;

    for (let braille of brailleArray) {
        if (braille === capitalFollows) {
            isCapital = true;
        } else if (braille === numberFollows) {
            isNumber = true;
        } else if (braille === decimalFollows) {
            englishOutput += '.';
            isNumber = false;
        } else {
            let char = englishMap[braille];
            if (char) {
                if (isCapital) {
                    char = char.toUpperCase();
                    isCapital = false; // Reset capital flag
                }
                if (isNumber) {
                    if (/[a-j]/.test(char)) {
                        char = (char.charCodeAt(0) - 96).toString(); // 'a' -> '1', 'b' -> '2', etc.
                    }
                    isNumber = false;  // Reset number flag after processing
                }
                englishOutput += char;
            }
        }
    }

    return englishOutput;
}

// Main function to handle command-line input
function main() {
    const input = process.argv.slice(2).join(' ');

    // Check if input is Braille (contains 'O' and '.' characters)
    const isBraille = /^[O.o]+$/.test(input);
    
    if (isBraille) {
        // Translate from Braille to English
        console.log(brailleToEnglish(input));
    } else {
        // Translate from English to Braille
        console.log(englishToBraille(input));
    }
}

main();
