const brailleLetters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
};

const brailleNumbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleIndicators = {
    'CAP': '.....O',  // Capitalization indicator
    'NUM': '.O.OOO',  // Number indicator
    'SPACE': '......' // Space
};

// Create the reverse mappings
const reverseBrailleLetters = Object.keys(brailleLetters).reduce((acc, key) => {
    acc[brailleLetters[key]] = key;
    return acc;
}, {});

const reverseBrailleNumbers = Object.keys(brailleNumbers).reduce((acc, key) => {
    acc[brailleNumbers[key]] = key;
    return acc;
}, {});

const reverseBrailleIndicators = {
    '.....O': 'CAP',
    '.O.OOO': 'NUM',
    '......': 'SPACE'
};

const isBraille = (input) => {
    return /^[O.]+$/.test(input);
};

const translateToBraille = (input) => {
    let output = '';
    let isNumber = false;

    for (const char of input) {
        if (/[A-Z]/.test(char)) {
            output += brailleIndicators['CAP']; // Capital indicator
            output += brailleLetters[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                output += brailleIndicators['NUM']; // Number indicator
                isNumber = true;
            }
            output += brailleNumbers[char];
        } else if (/[a-z]/.test(char)) {
            isNumber = false;
            output += brailleLetters[char];
        } else if (char === ' ') {
            isNumber = false;
            output += brailleIndicators['SPACE'];
        }
    }

    return output;
};

const translateToEnglish = (input) => {
    let output = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleIndicators['CAP']) {
            isCapital = true;
        } else if (brailleChar === brailleIndicators['NUM']) {
            isNumber = true;
        } else if (brailleChar === brailleIndicators['SPACE']) {
            isNumber = false;
            output += ' ';
        } else {
            let translatedChar;
            if (isNumber) {
                translatedChar = reverseBrailleNumbers[brailleChar];
            } else {
                translatedChar = reverseBrailleLetters[brailleChar];
                if (isCapital) {
                    translatedChar = translatedChar.toUpperCase();
                    isCapital = false;
                }
            }
            output += translatedChar;
        }
    }

    return output;
};

// Driver
const main = () => {
    const input = process.argv.slice(2).join(' ');
    const result = isBraille(input) ? translateToEnglish(input) : translateToBraille(input);
    console.log(result);
};

main();
