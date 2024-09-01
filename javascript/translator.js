const brailleMapping = {
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
    ' ': '......',  // Space character
    'CAPITAL': '.....O',  // Capital sign
    'NUMBER': '.O.OOO',  // Number sign
    ',': '.O....',
    ';': '.OO...',
    ':': '.O.O..',
    '.': '.O..O.',
    '!': '.OOO.O',
    '?': '.O.OO.',
    "'": '.O.O..',
    '-': '.OO.O.',
    '(': '.O.OO.',
    ')': '.OOO.O',
    '"': '.OOO.O'
};

// Number mapping after the number sign
const numberMapping = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
};

// Convert Braille to text
function translateBrailleToText(brailleString) {
    let textOutput = '';
    let isNextCapital = false;
    let isInNumberMode = false;

    for (let i = 0; i < brailleString.length; i += 6) {
        const brailleChar = brailleString.substring(i, i + 6);

        if (brailleChar === brailleMapping['CAPITAL']) {
            isNextCapital = true;
        } else if (brailleChar === brailleMapping['NUMBER']) {
            isInNumberMode = true;
        } else {
            let translatedChar;
            if (isInNumberMode) {
                translatedChar = Object.keys(numberMapping).find(key => numberMapping[key] === brailleChar) || '?';
                if (!translatedChar) {
                    isInNumberMode = false; // Exit number mode if no number is found
                }
            } else {
                translatedChar = Object.keys(brailleMapping).find(key => brailleMapping[key] === brailleChar) || '?';
                if (isNextCapital) {
                    translatedChar = translatedChar.toUpperCase();
                    isNextCapital = false;
                }
            }

            if (translatedChar !== '?') {
                textOutput += translatedChar;
            } else if (brailleChar === '......') {
                textOutput += ' ';
                isInNumberMode = false;
                isNextCapital = false;
            }
        }
    }

    return textOutput;
}

// Convert English text to Braille
function translateTextToBraille(textString) {
    let brailleOutput = [];
    let isInNumberMode = false;

    for (let character of textString) {
        if (character.match(/[0-9]/)) {
            if (!isInNumberMode) {
                brailleOutput.push(brailleMapping['NUMBER']);  // Number sign in Braille
                isInNumberMode = true;
            }
            brailleOutput.push(numberMapping[character] || '......');
        } else {
            if (isInNumberMode) {
                isInNumberMode = false;
            }
            if (character.match(/[A-Z]/)) {
                brailleOutput.push(brailleMapping['CAPITAL']);  // Capital sign in Braille
                character = character.toLowerCase();
            }
            brailleOutput.push(brailleMapping[character] || '......');  // Default to empty if character not found
        }
    }

    return brailleOutput.join('');
}

// Check if given input is Braille or alphabets
function isInputBraille(input) {
    if (input.length % 6 !== 0) {
        return false;
    }
    return /^[.O]+$/.test(input);
}

const arguments = process.argv.slice(2);
const userInput = arguments.join(' ');

const isBrailleInput = isInputBraille(userInput);
let output;

if (isBrailleInput) {
    output = translateBrailleToText(userInput);
} else {
    output = translateTextToBraille(userInput);
}

console.log(output); 
