const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'capital': '.....O', 
    'number': '.O.OOO', 
};

const brailleToEnglish = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

function isBraille(input) {
    return /^[O.]+$/.test(input);
}

function encodeToBraille(input) {
    let output = '';
    const chars = input.split('');
    let numberMode = false;

    chars.forEach((char, index) => {
        if (/[A-Z]/.test(char)) {
            output += brailleAlphabet['capital']; 
            char = char.toLowerCase();
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                output += brailleAlphabet['number']; 
                numberMode = true;
            }
        } else {
            numberMode = false; 
        }

        if (brailleAlphabet[char]) {
            output += brailleAlphabet[char];
        }
    });

    return output;
}

function decodeFromBraille(input) {
    let output = '';
    let chars = [];
    let numberMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);
        if (brailleChar === brailleAlphabet['capital']) {
            // Next character is capitalized
            continue;
        } else if (brailleChar === brailleAlphabet['number']) {
            // Next characters are numbers
            numberMode = true;
            continue;
        } else if (brailleChar === brailleAlphabet[' ']) {
            output += ' ';
            numberMode = false;
            continue;
        }

        const decodedChar = brailleToEnglish[brailleChar];
        if (decodedChar) {
            if (numberMode && /\d/.test(decodedChar)) {
                output += decodedChar;
            } else {
                output += numberMode ? decodedChar : decodedChar.toLowerCase();
                numberMode = false;
            }
        }
    }

    return output;
}

function translate(input) {
    if (isBraille(input)) {
        return decodeFromBraille(input);
    } else {
        return encodeToBraille(input);
    }
}

// Read user input from command-line arguments and translate
const userInput = process.argv.slice(2).join(' ');
const translation = translate(userInput);
console.log(translation);
