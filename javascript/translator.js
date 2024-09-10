const EnglishToBrailleCharacterAndSymbols = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    
    ' ': '......',
    '.': '..OO.0', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
};

const EnglishToBrailleNumbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const capitalPrefix = '.....O';
const numberPrefix = '.O.OOO';
const decimalPrefix = '.O...O';

const BrailleToEnglishCharacterAndSymbol = {};
for (const [key, value] of Object.entries(EnglishToBrailleCharacterAndSymbols)) {
    BrailleToEnglishCharacterAndSymbol[value] = key;
}

const BrailleToEnglishNumbers = {};
for (const [key, value] of Object.entries(EnglishToBrailleNumbers)) {
    BrailleToEnglishNumbers[value] = key;
}

function isBraille(input) {
    return input.includes('O') || input.includes('.');
}

function englishToBraille(input) {
    let output = '';
    let isNumberMode = false;
    let isDecimalMode = false;

    for (let i = 0; i < input.length; i++) {
        let char = input[i];

        if (char >= 'A' && char <= 'Z') {
            output += capitalPrefix;
            char = char.toLowerCase();
        }
        else if(char === " "){
            isNumberMode = false;
        }

        if (char >= '0' && char <= '9') {
            if (!isNumberMode) {
                output += numberPrefix;
                isNumberMode = true;
            }

            if (i + 1 < input.length && input[i + 1] === '.') {
                output += decimalPrefix;
                isDecimalMode = true;
                continue;
            }
        } 
        else {
            isNumberMode = false;
            isDecimalMode = false;
        }

        if (!isNumberMode && EnglishToBrailleCharacterAndSymbols[char]) {
            output += EnglishToBrailleCharacterAndSymbols[char];
        }
        else if (isNumberMode && EnglishToBrailleNumbers[char]) {
             output += EnglishToBrailleNumbers[char];
        }
    }

    return output;
}

let isNumberModebrailleToEnglish = false;
function brailleToEnglish(input) {
    let output = '';
    let i = 0;
    let isCapitalMode = false;
    let isDecimalMode = false;

    while (i < input.length) {
        let brailleChar = input.substr(i, 6);

        if (brailleChar === capitalPrefix) {
            isCapitalMode = true;
            i += 6;
            continue;
        }

        if (brailleChar === numberPrefix) {
            isNumberModebrailleToEnglish = true;
            i += 6;
            continue;
        }

        if (brailleChar === '......') {
            isNumberModebrailleToEnglish = false;
            isDecimalMode = false;
        }

        if (brailleChar === decimalPrefix) {
            isDecimalMode = true;
            i += 6;
            continue;
        }

        if (BrailleToEnglishCharacterAndSymbol[brailleChar]) {
            let char = BrailleToEnglishCharacterAndSymbol[brailleChar];

            if (isCapitalMode) {
                char = char.toUpperCase();
                isCapitalMode = false;
            }

            if (isNumberModebrailleToEnglish) {
                char = BrailleToEnglishNumbers[brailleChar];
                if (isDecimalMode) {
                    char = '.' + char;
                    isDecimalMode = false;
                }
            }

            output += char;
        }

        i += 6;
    }

    return output;
}

function translate(input) {
    if (isBraille(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
}

const inputArgs = process.argv.slice(2);
const input = inputArgs.join(' '); // Combine arguments into a single string
console.log("Received input:", input);

if (input) {
    translate(input);
} else {
    console.log("Please provide a string to translate.");
}