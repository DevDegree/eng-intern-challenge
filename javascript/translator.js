const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..OO.O', ',': '..O...', '?': '..O.O.', '!': '..OOO.', ':': 'O..O..',
    ';': 'O..O.O', '-': '..O.OO', '/': '..OOO.', '(': '.O..OO', ')': 'O.OOOO'
};

// Reverse map for Braille to English
const reverseBrailleMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

const capitalizeFollow = '.....O'; // Braille code to capitalize
const numberFollow = '.O.OOO';   // Braille code for numbers

function translateToBraille(text) {
    let braille = '';
    let isNumber = false;

    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        if (/[A-Z]/.test(char)) {
            braille += capitalizeFollow + brailleMap[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                braille += numberFollow;
                isNumber = true;
            }
            braille += brailleMap[char];
        } else {
            braille += brailleMap[char];
            isNumber = false; // reset number mode after a non-number
        }
    }
    return braille;
}

function translateToEnglish(brailleText) {
    let english = '';
    let isCapital = false;
    let isNumber = false;
    let i = 0;

    while (i < brailleText.length) {
        const brailleChar = brailleText.slice(i, i + 6);

        if (brailleChar === capitalizeFollow) {
            isCapital = true;
            i += 6;
            continue;
        } else if (brailleChar === numberFollow) {
            isNumber = true;
            i += 6;
            continue;
        }

        let translatedChar = reverseBrailleMap[brailleChar];
        if (isCapital) {
            translatedChar = translatedChar.toUpperCase();
            isCapital = false;
        }

        if (isNumber) {
            if (/[a-j]/.test(translatedChar)) {
                translatedChar = (translatedChar.charCodeAt(0) - 'a'.charCodeAt(0) + 1).toString();
            }
            isNumber = false;
        }

        english += translatedChar;
        i += 6;
    }
    return english;
}

function isBraille(text) {
    // Check if the text consists of only 'O' and '.' and is of valid length
    return text.match(/^[O.]+$/) && text.length % 6 === 0;
}

function main() {
    const args = process.argv.slice(2);
    if (args.length === 0) {
        console.error("Please provide a string to translate.");
        return;
    }

    const input = args.join(' ');

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();
