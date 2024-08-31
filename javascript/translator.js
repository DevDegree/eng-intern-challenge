// need a dictionary to store key paired values for english to braille
const brailleMap = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    'capitalFollows': '.....O', 'decimalFollows': '.O...O', 'numberFollows': 'O.....', 
    ' ': '......', '.': '..O.OO', ',': '..O...', '?': '..OO.O',
    '!': '..OOO.', ':': '..OO..', ';': '..OOO.', '-': '..O..O', 
    '/': '..O.O.', '<': '..O.O.', '>': '..OOO.', '(': '...O..', ')': '...OO.'
}

const brailleToEnglish = Object.entries(brailleMap).reduce((obj, [key, value]) => {
    obj[value] = key;
    return obj;
}, {});

const capitalFollows = brailleMap['capitalFollows'];
const numberFollows = brailleMap['numberFollows'];

function isBraille(input) {
    return /^[O\.]+$/.test(input);
}

function translateToBraille(text) {
    let result = '';
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if(/[A-Z]/.test(char)) {
            result += capitalFollows;
        } else if (/[0-9]/.test(char)) {
            result += numberFollows;
        }
        result += brailleMap[char.toUpperCase()];
    }
    return result;
}

function translateToEnglish(braille) {
    let result = '';
    let capital = false;
    let number = false;
    for (let i = 0; i < braille.length; i += 6) {
        let symbol = braille.slice(i, i + 6);
        if (symbol === capitalFollows) {
            capital = true;
            continue;
        }

        let char = brailleToEnglish[symbol];
        if (capital) {
            char = char.toUpperCase();
            capital = false;
        } else {
            char = char.toLowerCase();
        }
        result += char;
    }
    return result;
}

function brailleTranslator(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
console.log(brailleTranslator(input));