// Braille mappings: English to Braille
const brailleMapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
};

// Numbers 1-9 and 0 are represented by letters "a" to "j"
const numberMapping = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
};

// Reverse mappings for Braille to English conversion
const brailleToEnglish = {};
const numberToEnglish = {};

Object.keys(brailleMapping).forEach(key => {
    brailleToEnglish[brailleMapping[key]] = key;
});
Object.keys(numberMapping).forEach(num => {
    numberToEnglish[numberMapping[num]] = num;
});

// Convert English text to Braille
const convertEnglishToBraille = (input) => {
    let result = "";
    let inNumberMode = false;

    for (const char of input) {
        let brailleChar = "";

        // Handle spaces separately
        if (char === ' ') {
            result += brailleMapping[' '];
            inNumberMode = false;
            continue;
        }

        // Handle numbers with a number indicator
        if (!isNaN(char)) {
            if (!inNumberMode) {
                result += brailleMapping['number'];
                inNumberMode = true;
            }
            brailleChar = brailleMapping[numberMapping[char]];
        } else {
            // Handle capital letters with a capitalization marker
            if (char === char.toUpperCase()) {
                result += brailleMapping['capital'];
                brailleChar = brailleMapping[char.toLowerCase()];
            } else {
                brailleChar = brailleMapping[char];
            }
            inNumberMode = false; // Reset number mode for non-numeric characters
        }

        result += brailleChar;
    }

    return result;
};

// Convert Braille text to English
const convertBrailleToEnglish = (input) => {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleSegment = input.slice(i, i + 6);

        // Handle capitalization and number markers
        if (brailleSegment === brailleMapping['capital']) {
            isCapital = true;
            continue;
        }
        if (brailleSegment === brailleMapping['number']) {
            isNumber = true;
            continue;
        }

        // Handle spaces
        if (brailleSegment === brailleMapping[' ']) {
            result += ' ';
            continue;
        }

        // Translate based on number mode or normal letters
        let char = brailleToEnglish[brailleSegment];
        if (isNumber) {
            char = numberToEnglish[char] || '?'; // Fallback in case of invalid Braille
            isNumber = false;
        } else if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        }

        result += char;
    }

    return result;
};

// Determine if input is Braille
const detectBraille = (input) => /^[O.]+$/.test(input);

// Main translation function
const translate = (input) => detectBraille(input) ? convertBrailleToEnglish(input) : convertEnglishToBraille(input);

// Get input from command-line arguments
const userInput = process.argv.slice(2).join(' ');
const translation = translate(userInput);
console.log(translation);
