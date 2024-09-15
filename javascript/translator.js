const brailleMap = {
    // Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    // Numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
    // Symbols
    ' ': '......', // Space
    'cap': '.....O', // Capitalization prefix
    'num': '.O.OOO', // Number prefix
};

const reverseBrailleMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));

function isBraille(input) {
    return /^[O\.]+$/.test(input);
}

function translateToBraille(text) {
    let result = '';
    let inNumberMode = false;

    for (const char of text) {
        if (char === ' ') {
            result += brailleMap[' '];
            inNumberMode = false;
        } else if (!isNaN(char)) {
            if (!inNumberMode) {
                result += brailleMap['num'];
                inNumberMode = true;
            }
            result += brailleMap[char] || '';
        } else {
            if (char.toUpperCase() !== char.toLowerCase() && char === char.toUpperCase()) {
                result += brailleMap['cap'];
            }
            result += brailleMap[char.toLowerCase()] || '';
            inNumberMode = false;
        }
    }

    return result;
}

function translateToEnglish(braille) {
    const chars = braille.match(/.{1,6}/g); // Divide the input into Braille cells with six characters.
    let result = '';
    let inNumberMode = false;
    let capitalizeNext = false;

    for (const cell of chars) {
        if (cell === brailleMap['num']) {
            inNumberMode = true;
            continue;
        }
        if (cell === brailleMap['cap']) {
            capitalizeNext = true;
            continue;
        }
        if (cell === brailleMap[' ']) {
            result += ' ';
            inNumberMode = false;
            continue;
        }

        const translated = reverseBrailleMap[cell] || '';
        result += inNumberMode ? translated : capitalizeNext ? translated.toUpperCase() : translated;
        capitalizeNext = false;
        inNumberMode = false;
    }

    return result;
}

function main() {
    const input = process.argv.slice(2).join(' ');

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();
