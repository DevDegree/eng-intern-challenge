// Define mappings for English to Braille and Braille to English
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

const brailleToEnglish = Object.fromEntries(Object.entries(brailleMap).map(([k, v]) => [v, k]));

// Function to determine if input is Braille or English
function isBraille(input) {
    return /^[O.]+$/.test(input) && input.length % 6 === 0;
}

// Function to translate English to Braille
function translateToBraille(text) {
    let result = '';
    let inNumberMode = false;

    for (const char of text) {
        if (char >= 'A' && char <= 'Z') {
            result += brailleMap['cap'] + brailleMap[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            if (!inNumberMode) {
                result += brailleMap['num'];
                inNumberMode = true;
            }
            result += brailleMap[char];
        } else {
            inNumberMode = false;
            result += brailleMap[char] || '';  // Handle unexpected characters gracefully
        }
    }
    return result;
}

// Function to translate Braille to English
function translateToEnglish(braille) {
    let result = '';
    let i = 0;
    let inNumberMode = false;

    while (i < braille.length) {
        const symbol = braille.substring(i, i + 6);
        if (symbol === brailleMap['cap']) {
            const nextSymbol = braille.substring(i + 6, i + 12);
            result += brailleToEnglish[nextSymbol].toUpperCase();
            i += 12;
        } else if (symbol === brailleMap['num']) {
            inNumberMode = true;
            i += 6;
        } else {
            result += brailleToEnglish[symbol];
            i += 6;
            if (inNumberMode && /\D/.test(result[result.length - 1])) {
                inNumberMode = false;
            }
        }
    }
    return result;
}

// Main function to handle input and perform translation
function main() {
    const input = process.argv.slice(2).join(' ');

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();
