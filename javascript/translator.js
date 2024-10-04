// translator.js

// Define the Braille dictionary
const brailleDict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

function findKeyFromValue(obj, value, isNumber = false) {
    for (const [key, val] of Object.entries(obj)) {
        // Check if the key is a string representation of a number
        const isKeyNumber = !isNaN(key) && key.trim() !== '';

        // If we want to find a key that's a number or a letter
        if (val === value && isKeyNumber === isNumber) {
            return key;
        }
    }

    return null;
}

function isValidBrailleString(str) {
    // Check if the string contains only '0' and '.' and is divisible by 6
    const isValidCharacters = /^[0.]+$/.test(str);
    const isValidLength = str.length % 6 === 0;

    return isValidCharacters && isValidLength;
}

function brailleToEnglish(input) {
    const symbolLength = 6;
    let isCapital = false;
    let isNumber = false;
    let inEnglish = '';

    for (let i = 0; i < input.length; i += symbolLength) {
        let currentSymbol;

        if (isNumber) {
            currentSymbol = findKeyFromValue(brailleDict, input.slice(i, i + symbolLength), true);
        } else {
            currentSymbol = findKeyFromValue(brailleDict, input.slice(i, i + symbolLength));
        }

        if (currentSymbol === 'number') {
            isNumber = true;
        } else if (currentSymbol === 'capital') {
            isCapital = true;
        } else if (currentSymbol === ' ') {
            isNumber = false;
        }

        if (currentSymbol !== 'capital' && currentSymbol !== 'number' && currentSymbol !== 'decimal') {
            if (isCapital) {
                inEnglish += currentSymbol.toUpperCase();
                isCapital = false;
            } else {
                inEnglish += currentSymbol;
            }
        }
    }

    return inEnglish;
}

function englishToBraille(input) {
    let inBraille = '';
    let isFirstNum = true;

    for (let char of input) {
        if (char === ' ') {
            isFirstNum = true;
        }  else if (!isNaN(parseInt(char)) && isFirstNum) {
            inBraille += brailleDict['number'];
            isFirstNum = false;
        } else if (isNaN(parseInt(char)) && char === char.toUpperCase()) {
            inBraille += brailleDict['capital'];
        }
        inBraille += brailleDict[char.toLowerCase()];

    }

    return inBraille;
}

// Access command-line argments
const args = process.argv.slice(2); // Get arguments after the script name
if (args.length > 0) {
    const input = args.join(' '); // Join arguments to form the input string
    if (isValidBrailleString(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
} else {
    console.log("No input provided.");
}
