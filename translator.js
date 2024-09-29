// Braille mappings
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', 
    // Special symbols
    'capital': '.....O', 'number': 'O.OOOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

// Translate English to Braille
function englishToBraille(text) {
    let result = '';
    let numberMode = false;

    for (let char of text) {
        if (char === ' ') {
            result += brailleMap[' '];
            numberMode = false;
        } else if (/[A-Z]/.test(char)) {
            result += brailleMap['capital'] + brailleMap[char.toLowerCase()];
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                result += brailleMap['number'];
                numberMode = true;
            }
            result += brailleMap[char];
        } else {
            result += brailleMap[char];
            numberMode = false;
        }
    }
    return result;
}

// Translate Braille to English
function brailleToEnglish(braille) {
    let result = '';
    let capitalMode = false;
    let numberMode = false;
    
    for (let i = 0; i < braille.length; i += 6) {
        let symbol = braille.slice(i, i + 6);

        if (symbol === brailleMap['capital']) {
            capitalMode = true;
        } else if (symbol === brailleMap['number']) {
            numberMode = true;
        } else if (symbol === brailleMap[' ']) {
            result += ' ';
            numberMode = false;
        } else {
            let char = englishMap[symbol];
            if (numberMode && /\d/.test(char)) {
                result += char;
            } else if (capitalMode) {
                result += char.toUpperCase();
                capitalMode = false;
            } else {
                result += char;
            }
        }
    }
    return result;
}

// Detect input type and translate
function translate(input) {
    if (/^[O.]+$/.test(input)) {
        // Input is Braille
        return brailleToEnglish(input);
    } else {
        // Input is English
        return englishToBraille(input);
    }
}

// Get the input from the command line
const input = process.argv[2];  // e.g., "Hello" or "O.....O.O..."

// Output the result
console.log(translate(input));
