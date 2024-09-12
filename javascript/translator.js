// Define a function that returns Braille mapping based on input type
function createBrailleMapping(letters, patterns) {
    const mapping = {};
    for (let i = 0; i < letters.length; i++) {
        mapping[letters[i]] = patterns[i];
    }
    return mapping;
}

// Define the characters and their Braille patterns separately
const letterKeys = 'abcdefghijklmnopqrstuvwxyz '.split('');
const letterBraille = [
    'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..',
    '.OO...', '.OOO..', 'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 'OOO.O.',
    'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO',
    'OO.OOO', 'O..OOO',
    '......'  // Space
];

const numberKeys = '1234567890'.split('');
const numberBraille = [
    'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..',
    '.OO...', '.OOO..'
];

// Create mappings using the function
const brailleLetters = createBrailleMapping(letterKeys, letterBraille);
const brailleNumbers = createBrailleMapping(numberKeys, numberBraille);

// Add capital and number indicators
const specialBraille = {
    'capital': '.....O',
    'number': '.O.OOO'
};

// Reverse mapping from Braille to English letters/numbers
const englishLetters = Object.fromEntries(Object.entries(brailleLetters).map(([key, value]) => [value, key]));
const englishNumbers = Object.fromEntries(Object.entries(brailleNumbers).map(([key, value]) => [value, key]));

// Function to detect if input is Braille
function isBraille(input) {
    return /^[O. ]+$/.test(input);
}

// Function to translate English to Braille
function translateToBraille(input) {
    let result = [];
    let isNumber = false;
    
    for (let char of input.trim()) {
        if (char >= 'A' && char <= 'Z') {
            result.push(specialBraille['capital']);
            result.push(brailleLetters[char.toLowerCase()] || '......');
        } else if (char >= '0' && char <= '9') {
            if (!isNumber) {
                result.push(specialBraille['number']);
                isNumber = true;
            }
            result.push(brailleNumbers[char] || '......');
        } else {
            result.push(brailleLetters[char] || '......');
            isNumber = false;
        }
    }
    
    return result.join('');
}

// Function to translate Braille to English
function translateToEnglish(input) {
    let result = [];
    let isCapital = false;
    let isNumber = false;

    const chunks = input.match(/.{1,6}/g) || []; // Split Braille into 6-character blocks

    for (let chunk of chunks) {
        if (chunk === specialBraille['capital']) {
            isCapital = true;
            continue;
        }
        if (chunk === specialBraille['number']) {
            isNumber = true;
            continue;
        }

        if (chunk === '......') { // Handle space explicitly
            result.push(' ');
            isNumber = false;
            continue;
        }

        if (isNumber) {
            let number = englishNumbers[chunk] || '?';
            result.push(number);
        } else {
            let letter = englishLetters[chunk] || '?';
            result.push(isCapital ? letter.toUpperCase() : letter);
            isCapital = false;
        }

        if (chunk === brailleLetters[' ']) {
            isNumber = false;
        }
    }
    
    return result.join('');
}


// Function to handle translation
function brailleTranslator(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

// Process command-line arguments and run translation
const input = process.argv.slice(2).join(' ');
console.log(brailleTranslator(input));
