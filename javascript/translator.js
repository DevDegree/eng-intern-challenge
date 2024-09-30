// key value pairs
const ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
};

const BRAILLE_NUMBERS = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
};

const BRAILLE_CAPITAL = '.....O';
const BRAILLE_NUMBER = '.O.OOO';
const BRAILLE_SPACE = '......';

// for reverse mapping
const BRAILLE_TO_ENGLISH = Object.entries(ENGLISH_TO_BRAILLE).reduce((obj, [letter, braille]) => {
    obj[braille] = letter;
    // console.log("This is the object: ", obj);
    return obj;
}, {});


// You must include the entire English alphabet, the ability to capitalize letters, add spaces, and the numbers 0 through 9 as well.
// based off this, im assuming sentences will be separated by spaces, and no periods will be used.
function isBraille(input) {
    return input.includes('.');
}


function translateBrailleToEnglish(input) {
    let result = '';

    // flags for detecting capital letters and numbers
    let capitalizeNext = false;
    let numberMode = false;

    // each braille is 6 segments long
    for (let i = 0; i < input.length; i += 6) {
        const char = input.substring(i, i + 6);

        if (char === BRAILLE_CAPITAL) {
            capitalizeNext = true;
        } else if (char === BRAILLE_NUMBER) {
            numberMode = true;
        } else if (char === BRAILLE_SPACE) {
            result += ' ';
            numberMode = false;
        } else {
            let translatedChar = numberMode ? BRAILLE_NUMBERS[BRAILLE_TO_ENGLISH[char]] : BRAILLE_TO_ENGLISH[char] || 'Unknown input';

            if (capitalizeNext && !numberMode) {
                translatedChar = translatedChar.toUpperCase();
                capitalizeNext = false;
            }

            result += translatedChar;
        }
    }

    return result;
}


function translateEnglishToBraille(input) {
    let result = '';
    let numberMode = false;

    for (const char of input) {
        if (char === ' ') {
            result += BRAILLE_SPACE;
            numberMode = false;
            // upper case test, found Regex for this on stackoverflow
        } else if (/[A-Z]/.test(char)) {
            result += BRAILLE_CAPITAL + ENGLISH_TO_BRAILLE[char.toLowerCase()];
            // number case
        } else if (/[0-9]/.test(char)) {
            if (!numberMode) {
                result += BRAILLE_NUMBER;
                numberMode = true;
            }
            // a is reference
            const letter = String.fromCharCode('a'.charCodeAt(0) + (parseInt(char) - 1));
            // console.log("This is the letter: ", letter);
            result += ENGLISH_TO_BRAILLE[letter];
        } else {
            result += ENGLISH_TO_BRAILLE[char];
        }
    }

    return result;
}


function translator(input) {
    if (isBraille(input)) {
        return translateBrailleToEnglish(input);
    } else {
        return translateEnglishToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
console.log(translator(input));