// Define mappings for English to Braille
const brailleMap = {
    letters: {
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
    },
    numbers: {  
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
    },
    symbols: {
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
    }
};

// Define mappings for Braille to English
const englishMap = Object.fromEntries(
    Object.entries({ ...brailleMap.letters, ...brailleMap.numbers, ...brailleMap.symbols})
    .map(([key, value]) => [value, key])
);

// Implement a function to detect if input is Braille or English
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

// Implement a function to translate English to Braille
function translateToBraille(input) {
    let result = '';
    let inNumberSequence = false;

    for (const char of input) {
        if (char >= 'A' && char <= 'Z') {
            result += brailleMap.symbols['capital'] + brailleMap.letters[char.toLowerCase()];
            inNumberSequence = false;
        } else if (char >= '0' && char <= '9') {
            if (!inNumberSequence) {
                result += brailleMap.symbols['number'];
                inNumberSequence = true;
            }
            result += brailleMap.numbers[char];
        } else {
            result += brailleMap.symbols[char] || brailleMap.letters[char] || '';
            inNumberSequence = false;
        }
    }
    return result;
}

// Implement a function to translate Braille to English
function translateToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleMap.symbols['capital']) {
            isCapital = true;
            continue;
        }

        if (brailleChar === brailleMap.symbols['number']) {
            isNumber = true;
            continue;
        }

        if (brailleChar === brailleMap.symbols['decimal']) {
            result += '.';
            continue;
        }

        const char = englishMap[brailleChar];
        
        if (isCapital) {
            result += char ? char.toUpperCase() : '';
            isCapital = false;
        } else if (isNumber) {
            if (char >= 'a' && char <= 'j') {
                result += char ? String.fromCharCode(char.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0)) : '';
            } else {
                result += char || '';
                isNumber = false; 
            }
        } else {
            result += char || '';
        }
    }
    return result;
}

// Get the input string
const input = process.argv.slice(2).join(' ');
if (!input) {
    console.error('Please provide an input string');
    process.exit(1);
}

// Detect input type and call appropriate translation function
const output = isBraille(input) ? translateToEnglish(input) : translateToBraille(input);
// Output the result
console.log(output);