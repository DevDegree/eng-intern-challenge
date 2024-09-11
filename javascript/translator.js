// 1. Define mappings for English to Braille and Braille to English
// 2. Implement a function to detect if input is Braille or English
// 3. Implement a function to translate English to Braille
// 4. Implement a function to translate Braille to English
// 5. Get the input string
// 6. Detect input type and call appropriate translation function
// 7. Output the translated string in terminal

const brailleMap = {
    'a': 'O.....',
    'b': 'O.O....',
    'c': 'OO.....',
    'd': 'OO.O...',
    'e': 'O..O...',
    'f': 'OOO....',
    'g': 'OOOO...',
    'h': 'O.OO...',
    'i': '.OO....',
    'j': '.OOO...',
    'k': 'O...O..',
    'l': 'O.O.O..',
    'm': 'OO..O..',
    'n': 'OO.OO..',
    'o': 'O..OO..',
    'p': 'OOO.O..',
    'q': 'OOOOO..',
    'r': 'O.OOO..',
    's': '.OO.O..',
    't': '.OOOO..',
    'u': 'O...OO.',
    'v': 'O.O.OO.',
    'w': '.OOO.O.',
    'x': 'OO..OO.',
    'y': 'OO.OOO.',
    'z': 'O..OOO.',
    '1': 'O.....',
    '2': 'O.O....',
    '3': 'OO.....',
    '4': 'OO.O...',
    '5': 'O..O...',
    '6': 'OOO....',
    '7': 'OOOO...',
    '8': 'O.OO...',
    '9': '.OO....',
    '0': '.OOO...',
    'capital': '.....O',
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
    ' ': '......',
};

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

function isBraille(input) {
    return /^[O.]{6}$/.test(input);
}

function translateToBraille(input) {
    let result = '';
    for (let char of input) {
        if (char >= 'A' && char <= 'Z') {
            result += brailleMap['capital'] + brailleMap[char.toLowerCase()];
        } else if (char >= '0' & char <= '9') {
            result += brailleMap['number'] + brailleMap[char];
        } else {
            result += brailleMap[char];
        }
    }
    return result;
}