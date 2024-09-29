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
            // Capital letter
            brailleOutput += capitalFollows + ' ' + brailleMap[char.toLowerCase()] + ' ';
            isNumber = false; // Reset number flag
        } else if (/[0-9]/.test(char)) {
            // Number follows before each digit
            brailleOutput += numberFollows + ' ' + brailleMap[char] + ' ';
            isNumber = true;  // Stay in number mode until non-number encountered
        } else if (char === '.') {
            // Decimal point
            brailleOutput += decimalFollows + ' ';
            isNumber = false; // Reset number flag
        } else {
            // Regular character
            brailleOutput += brailleMap[char.toLowerCase()] + ' ';
            isNumber = false; // Reset number flag
        }
    }

    return brailleOutput.trim();
}

// Function to translate Braille to English considering follows
function brailleToEnglish(input) {
    let brailleArray = input.split(' ');
    let englishOutput = '';
    let isCapital = false;
    let isNumber = false;

    for (let braille of brailleArray) {
        if (braille === capitalFollows) {
            // Handle capital follows
            isCapital = true;
        } else if (braille === numberFollows) {
            // Handle number follows
            isNumber = true;
        } else if (braille === decimalFollows) {
            // Handle decimal point
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
                        // Convert a-j to 1-0 (Braille number representation)
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

// Set up readline interface for command-line input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to start the app
function startApp() {
    rl.question('Choose translation mode (1: English to Braille, 2: Braille to English): ', (mode) => {
        if (mode === '1') {
            rl.question('Enter English text to translate to Braille: ', (input) => {
                const braille = englishToBraille(input);
                console.log('Braille translation:', braille);
                rl.close();
            });
        } else if (mode === '2') {
            rl.question('Enter Braille text to translate to English (use spaces between Braille characters): ', (input) => {
                const english = brailleToEnglish(input);
                console.log('English translation:', english);
                rl.close();
            });
        } else {
            console.log('Invalid option. Please choose 1 or 2.');
            startApp();  // Restart if invalid input
        }
    });
}

// Start the app
startApp();
