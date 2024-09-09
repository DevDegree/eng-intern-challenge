// const inputVal = process.argv.slice(2);
// console.log(inputVal);
let inputVal = '';
for (i = 2; i < process.argv.length; i++) {
    if (i === 2) {
        inputVal += process.argv[i];
    }
    else {
        inputVal += " " + process.argv[i];
    }
}

function isBraille(inputVal) {
    if (inputVal.length % 6 !== 0) {
        return false;
    }
    for (let i = 0; i < inputVal.length; i += 6) {
        const splitInput = inputVal.slice(i, i + 6);
        if (splitInput.length !== 6) {
            return false;
        }
        for (const char of splitInput) {
            if (char !== 'O' && char !== '.') {
                return false;
            }
        }
    }
    return true;
}

const brailleAlphabet = {

    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    'A': '.....OO.....', 'B': '.....OO.O...', 'C': '.....OOO....', 'D': '.....OOO.O..', 'E': '.....OO..O..',
    'F': '.....OOOO...', 'G': '.....OOOOO..', 'H': '.....OO.OO..', 'I': '.....O.OO...', 'J': '.....O.OOO..',
    'K': '.....OO...O.', 'L': '.....OO.O.O.', 'M': '.....OOO..O.', 'N': '.....OOO.OO.', 'O': '.....OO..OO.',
    'P': '.....OOOO.O.', 'Q': '.....OOOOOO.', 'R': '.....OO.OOO.', 'S': '.....O.OO.O.', 'T': '.....O.OOOO.',
    'U': '.....OO...OO', 'V': '.....OO.O.OO', 'W': '.....O.OOO.O', 'X': '.....OOO..OO', 'Y': '.....OOO.OOO',
    'Z': '.....OO..OOO',

    // Space
    ' ': '......',

    // Numbers (0-9)
    '1': '.O.O..O.....', '2': '.O.O..O.O...', '3': '.O.O..OO....', '4': '.O.O..OO.O..', '5': '.O.O..O..O..',
    '6': '.O.O..OOO...', '7': '.O.O..OOOO..', '8': '.O.O..O.OO..', '9': '.O.O...OO...', '0': '.O.O...OOO..',

    'CAPITAL': '.....O',
    'NUMBER': '.O.O..'
}

function brailleToText(inputVal) {
    let outputVal = '';
    for (let i = 0; i < inputVal.length; i += 6) {
        const splitInput = inputVal.slice(i, i + 6);
        if (splitInput === '......') {
            outputVal += ' ';
        } else if (splitInput === '.....O') {
            const letterPattern = inputVal.slice(i, i + 12);
            const value = Object.keys(brailleAlphabet).find(key => brailleAlphabet[key] === letterPattern);
            outputVal += value;
            i += 6;
        } else if (splitInput === '.O.O..') {
            const numPattern = inputVal.slice(i, i + 12);
            const value = Object.keys(brailleAlphabet).find(key => brailleAlphabet[key] === numPattern);
            outputVal += value;
            i += 6;
        } else {
            const value = Object.keys(brailleAlphabet).find(key => brailleAlphabet[key] === splitInput);
            outputVal += value ? value : 'Enter valid braille character';
        }
    }
    console.log(outputVal)
}


function textToBraille(inputVal) {
    let outputVal = '';

    for (const char of inputVal) {
        if (char === ' ') {
            outputVal += '......';
        } else if (brailleAlphabet[char] !== undefined) {
            outputVal += brailleAlphabet[char];
        } else {
            console.log('Enter valid alphabet');
            outputVal += '......';
        }
    }
    console.log(outputVal);
}

function determineTextOrBraille(inputVal) {
    if (isBraille(inputVal) === true) {
        brailleToText(inputVal);
    } else {
        textToBraille(inputVal);
    }
}
determineTextOrBraille(inputVal);