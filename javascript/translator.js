const brailleAlphabet = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO',
    'decimal': '.O.O.O',
    '.': '.O.O.O',    ',': '.O....',    '?': '.O..O.',    '!': '.O.OO.',
    ':': '.OO...',    ';': '.O.O..',    '-': '.O..O.',    '/': '.O.O..',
    '<': 'O..O.O',    '>': '.OOO..',    '(': 'O..OOO',    ')': '.OO..O'
};

const numberMapping = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
};

const reverseBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

function englishToBraille(text) {
    let result = '';
    let isNumber = false;

    for (let char of text) {
        const lowerChar = char.toLowerCase();
        if (/[1-9]/.test(char)) {
            if (!isNumber) {
                result += brailleAlphabet['number'];
                isNumber = true;
            }
            result += brailleAlphabet[Object.keys(numberMapping).find(key => numberMapping[key] === char)];
        } else if (char === '0') {
            if (!isNumber) {
                result += brailleAlphabet['number'];
                isNumber = true;
            }
            result += brailleAlphabet['j'];
        } else if (char === '.') {
            if (isNumber) {
                result += brailleAlphabet['decimal'];
            } else {
                result += brailleAlphabet[char];
            }
        } else {
            if (isNumber && !/[0-9]/.test(char)) {
                isNumber = false;
            }
            if (char !== lowerChar) {
                result += brailleAlphabet['capital'];
            }
            result += brailleAlphabet[lowerChar] || brailleAlphabet[char] || '';
        }
    }
    return result;
}

function brailleToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const char = braille.slice(i, i + 6);
        if (char === brailleAlphabet['capital']) {
            isCapital = true;
        } else if (char === brailleAlphabet['number']) {
            isNumber = true;
        } else if (char === brailleAlphabet['decimal']) {
            result += '.';
        } else {
            let translated = reverseBrailleAlphabet[char];
            if (isNumber && numberMapping[translated]) {
                translated = numberMapping[translated];
            } else if (isCapital && translated) {
                translated = translated.toUpperCase();
                isCapital = false;
            }
            if (translated && !/[0-9]/.test(translated)) {
                isNumber = false;
            }
            result += translated || '';
        }
    }
    return result;
}

function translate(input) {
    return input.includes('.') || input.includes('O') ? brailleToEnglish(input) : englishToBraille(input);
}

const input = process.argv.slice(2).join(' ');

if (input) {
    console.log(translate(input));
} else {
    console.error('No input provided. Usage: node translator.js Your input here');
}