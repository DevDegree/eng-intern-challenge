// 1. Define mappings for English to Braille and Braille to English
// 2. Implement a function to detect if input is Braille or English
// 3. Implement a function to translate English to Braille
// 4. Implement a function to translate Braille to English
// 5. Get the input string
// 6. Detect input type and call appropriate translation function
// 7. Output the translated string in terminal

const brailleMap = {
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
    'number': '.O.OOO',
    'decimal': '.O...O',
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
    ' ': '......',
};

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

function isBraille(input) {
    if (input.length % 6 !== 0)
        return false;
    for (let i = 0; i < input.length; i += 6) {
        if (!/^[O.]{6}$/.test(input.slice(i, i + 6))) {
            return false;
        }
    }
    return true;
}

function translateToBraille(input) {
    let result = '';
    let inNumberSequence = false;

    for (let i = 0; i < input.length; i++) {
        let char = input[i];
        if (char >= 'A' && char <= 'Z') {
            result += brailleMap['capital'] + brailleMap[char.toLowerCase()];
            inNumberSequence = false;
        } else if (char >= '0' && char <= '9') {
            if (!inNumberSequence) {
                result += brailleMap['number'];
                inNumberSequence = true;
            }
            result += brailleMap[char];
        // } else if (char === '.' && i > 0 && input[i - 1] >= '0' && input[i - 1] <= '9' && i < input.length - 1 && input[i + 1] >= '0' && input[i + 1] <= '9') {
        //     result += brailleMap['decimal'];
        //     inNumberSequence = true;
        } else {
            result += brailleMap[char];
            inNumberSequence = false;
        }
    }
    return result;
}


function translateToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        let brailleChar = input.slice(i, i + 6);

        // Handle capital letters
        if (brailleChar === brailleMap['capital']) {
            isCapital = true;
            continue;
        }

        // Handle number mode
        if (brailleChar === brailleMap['number']) {
            isNumber = true;
            continue;
        }

        // Handle decimal point
        if (brailleChar === brailleMap['decimal']) {
            result += '.';
            continue;
        }

        let char = englishMap[brailleChar];
        
        // Handle capitalization
        if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        }

        // Handle number translation
        if (isNumber) {
            if (char >= 'a' && char <= 'j') {
                char = String.fromCharCode(char.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0)); // Convert a-j to 1-0
            }
            if (!char.match(/[0-9]/)) {
                isNumber = false;
            }
        }

        result += char;

        // Exit number mode if the current character is not a digit
        if (char === ' ') {
            isNumber = false;
        }
    }
    
    return result;
}

const input = process.argv.slice(2).join(' ');
if (!input) {
    console.error('Please provide an input string');
    process.exit(1);
}

const output = isBraille(input) ? translateToEnglish(input) : translateToBraille(input);
console.log(output);