// Complete mappings based on the Braille alphabet and numbers
const brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '..OO.O': '.', '..O...': ',', '..O.OO': '?',
    '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '..O..O': '-', '....OO': '<', 
    'OO....': '>', '.O..OO': '(', '.O.OOO': 'number', '.....O': 'capital',
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'
};

const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '..O..O', '<': '....OO', 
    '>': 'OO....', '(': '.O..OO', ')': '.O..OO', 'number': '.O.OOO', 'capital': '.....O',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};


function isBraille(input) {
    return /^[O.]+$/.test(input);
}


function brailleToText(braille) {
    let result = '';
    let isCapital = false;
    let isNumberMode = false;

    const brailleNumbers = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    };
    
    for (let i = 0; i < braille.length; i += 6) {
        const chunk = braille.slice(i, i + 6);
        if (chunk === '.....O') {
            isCapital = true;
        } else if (chunk === '.O.OOO') {
            isNumberMode = true;
        } else if (chunk === '......') {
            result += ' ';
            isNumberMode = false;  
        } else {
            let letter = brailleToEnglish[chunk];
            if (isNumberMode) {
                letter = brailleNumbers[chunk] || letter;
            } else if (isCapital) {
                letter = letter ? letter.toUpperCase() : '';
                isCapital = false;
            }
            result += letter || '';
        }
    }
    
    return result;
}
function textToBraille(text) {
    let brailleOutput = '';
    let isNumberMode = false;

    for (const char of text) {
        if (/[0-9]/.test(char)) {
            if (!isNumberMode) {
                brailleOutput += englishToBraille['number']; 
                isNumberMode = true;
            }
            brailleOutput += englishToBraille[char];
        } else if (char === ' ') {
            brailleOutput += englishToBraille[' '];
            isNumberMode = false;  
        } else {
            if (isNumberMode) {
                isNumberMode = false;
            }
            if (/[A-Z]/.test(char)) {
                brailleOutput += englishToBraille['capital'];
            }
            brailleOutput += englishToBraille[char.toLowerCase()];
        }
    }

    return brailleOutput;
}


function main() {
    const input = process.argv[2]; 

    if (isBraille(input)) {
        console.log(brailleToText(input));
    } else {
        console.log(textToBraille(input));
    }
}

main();
