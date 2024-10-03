const brailleAlphabetMapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
};

const brailleNumbersMapping = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleSpecialCharsMapping = {
    'capital': '.....O', 'number': '.O.OOO', 'space': '......'
};

function checkForBraille(input) {
    return /^[O.]+$/.test(input);
}


// Function to translate English to Braille
function convertToBraille(input) {
    let result = '';
    let isNumber = false;

    for (let char of input) {
        if (char === ' ') {
            result += brailleSpecialCharsMapping['space'];
            isNumber = false;
        } else if (/[A-Z]/.test(char)) {
            result += brailleSpecialCharsMapping['capital'];
            result += brailleAlphabetMapping[char.toLowerCase()];
            isNumber = false;
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result += brailleSpecialCharsMapping['number'];
                isNumber = true;
            }
            result += brailleNumbersMapping[char];
        } else {
            result += brailleAlphabetMapping[char];
            isNumber = false;
        }
    }

    return result;
}

// Function to translate Braille to English
function convertToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleSpecialCharsMapping['capital']) {
            isCapital = true;
        } else if (brailleChar === brailleSpecialCharsMapping['number']) {
            isNumber = true;
        } else if (brailleChar === brailleSpecialCharsMapping['space']) {
            result += ' ';
            isCapital = false;
            isNumber = false;
        } else {
            let char;
            if (isNumber) {
                char = Object.keys(brailleNumbersMapping).find(key => brailleNumbersMapping[key] === brailleChar);
            } else {
                char = Object.keys(brailleAlphabetMapping).find(key => brailleAlphabetMapping[key] === brailleChar);
            }

            if (isCapital && char) {
                result += char.toUpperCase();
                isCapital = false;
            } else if (char) {
                result += char;
            }
        }
    }

    return result;
}

// Main function to handle input and determine translation direction
function translateInput(input) {
    if (checkForBraille(input)) {
        return convertToEnglish(input);
    } else {
        return convertToBraille(input);
    }
}

// System process starts here
const input = process.argv[2];  // Input from the command line
console.log(translateInput(input));