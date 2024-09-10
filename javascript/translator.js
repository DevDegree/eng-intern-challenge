const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..OO..', '!': '..O.O.', ':': '..OO..',
    '-': '..O..O', '/': '.O..O.', '(': '.O.O..', ')': '.O.OO.'
};

const CAPITAL_SIGN = '.....O';
const NUMBER_SIGN = '.O.O..';

const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([char, braille]) => [braille, char])
);

function convertToBraille(text) {
    return Array.from(text).map(char => {
        if (char === char.toUpperCase() && char !== ' ') {
            return CAPITAL_SIGN + brailleMap[char.toLowerCase()] || '';
        }
        if (!isNaN(char)) {
            return NUMBER_SIGN + brailleMap[char] || '';
        }
        return brailleMap[char] || '';
    }).join('');
}


function convertToEnglish(brailleText) {
    const result = [];
    let index = 0;
    const textLength = brailleText.length;
    let isCapital = false;
    let isNumber = false;

    while (index < textLength) {
        const brailleChar = brailleText.slice(index, index + 6);

        if (brailleChar === CAPITAL_SIGN) {
            isCapital = true;
            index += 6;
            continue;
        }
        if (brailleChar === NUMBER_SIGN) {
            isNumber = true;
            index += 6;
            continue;
        }

        const englishChar = reverseBrailleMap[brailleChar];
        if (englishChar) {
            if (isNumber) {
                result.push(englishChar);
            } else if (isCapital) {
                result.push(englishChar.toUpperCase());
            } else {
                result.push(englishChar);
            }
        } else {
            result.push(''); 
        }


        isCapital = false;
        isNumber = false;
        index += 6;
    }

    return result.join('');
}

function processInput(inputText) {
    let isBraille = true;
    
    for (const char of inputText) {
        if (char !== 'O' && char !== '.' && char !== ' ') {
            isBraille = false;
            break;
        }
    }

    if (isBraille) {
        console.log(convertToEnglish(inputText));
    } else {
        console.log(convertToBraille(inputText));
    }
}

const inputText = process.argv.slice(2).join(' ');
 
if (inputText) {
    processInput(inputText);
} else {
    console.log("Please provide input text.");
}
