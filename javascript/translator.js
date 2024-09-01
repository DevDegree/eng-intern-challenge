// Define Braille alphabet and numbers mapping with 'O' for raised dots and '.' for period
const cpBrailleText = {
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
const cpBrailleNumbers = {
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

// convert braille to text
function cpBrailleToText(brailleString) {
    let text = '';
    let capitalizeNext = false;
    let numberMode = false;

    // Process the Braille string in chunks of 6 characters
    for (let i = 0; i < brailleString.length; i += 6) {
        const char = brailleString.substring(i, i + 6);

        if (char === cpBrailleText['CAPITAL']) {
            capitalizeNext = true;
        } else if (char === cpBrailleText['NUMBER']) {
            numberMode = true;
        } else {
            let letter;
            if (numberMode) {
                letter = Object.keys(cpBrailleNumbers).find(key => cpBrailleNumbers[key] === char) || '?';
                if (!letter) {
                    numberMode = false; // Exit number mode if no number is found
                }
            } else {
                letter = Object.keys(cpBrailleText).find(key => cpBrailleText[key] === char) || '?';
                if (capitalizeNext) {
                    letter = letter.toUpperCase();
                    capitalizeNext = false;
                }
            }

            if (letter !== '?') {
                text += letter;
            } else if (char === '......') {
                // Handle space correctly by adding a space and resetting modes
                text += ' ';
                numberMode = false;
                capitalizeNext = false;
            }
        }
    }

    return text;
}

// Function to convert English text to Braille
function cpTextToBraille(textString) {
    const braille = [];
    let numberMode = false;

    for (let char of textString) {
        if (char.match(/[0-9]/)) {
            if (!numberMode) {
                braille.push(cpBrailleText['NUMBER']);  // Number sign in Braille
                numberMode = true;
            }
            braille.push(cpBrailleNumbers[char] || '......');
        } else {
            if (numberMode) {
                numberMode = false;  // Exit number mode after encountering a non-numeric character
            }
            if (char.match(/[A-Z]/)) {
                braille.push(cpBrailleText['CAPITAL']);  // Capital sign in Braille
                char = char.toLowerCase();
            }
            braille.push(cpBrailleText[char] || '......');  // Default to empty if character not found
        }
    }

    return braille.join('');
}

// check if given input is braille or alphabets
function cpIsBraille(input) {
    // Check if the string length is a multiple of 6 (for 6-dot Braille)
    const brailleLength = 6;
    if (input.length % brailleLength !== 0) {
        return false;
    }

    // Check if the string contains only '.' and 'O'
    return /^[.O]+$/.test(input);
}

const args = process.argv.slice(2);
const input = args.join(' ');

const cpBrailleOutput = cpIsBraille(input);
let output;

if (cpBrailleOutput) {
    output = cpBrailleToText(input);
} else {
    output = cpTextToBraille(input);
}

console.log(output); // Log output
