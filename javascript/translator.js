// Braille to English mappings
const brailleToEnglishLetters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'cap', '.O.OOO': 'num', '.O...O': '.',
    '......': ' ', // space

};

const brailleToEnglishNumbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '......': ' ', // space
};

// English to Braille mappings
const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', '.': '.O...O',
    ' ': '......', // space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

function isBraille(input) {
    return /^[O.]+$/.test(input);
}

function translateToEnglish(braille) {
    let output = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.substring(i, i + 6);

        if (brailleChar === '.....O') { // Capitalization indicator
            isCapital = true;
            continue;
        }

        if (brailleChar === '.O.OOO') { // Number mode indicator
            isNumber = true;
            continue;
        }

        let translatedChar;

        if (isNumber) {
            translatedChar = brailleToEnglishNumbers[brailleChar] || '';
        } else {
            translatedChar = brailleToEnglishLetters[brailleChar] || '';
        }

        if (isCapital) {
            translatedChar = translatedChar.toUpperCase();
            isCapital = false; // Reset capitalization after applying it
        }

        output += translatedChar;

        // Reset number mode when a space is encountered
        if (brailleChar === '......') {
            isNumber = false;
        }
    }

    return output;
}


function translateToBraille(english) {
    let output = '';
    let isNumber = false;

    for (let i = 0; i < english.length; i++) {
        const char = english[i];
        if (/[A-Z]/.test(char)) {
            output += englishToBraille['cap'];
            output += englishToBraille[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                output += englishToBraille['num'];
                isNumber = true;
            }
            output += englishToBraille[char];
        } else {
            output += englishToBraille[char] || '';
            isNumber = false; // Reset number flag for non-number characters
        }
    }

    return output;
}

function main() {
    const input = process.argv[2];

    if (!input) {
        console.log("Please provide a string to translate.");
        return;
    }

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();

