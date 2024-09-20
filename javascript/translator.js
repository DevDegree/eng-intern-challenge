const brailleDictionary = {
    a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..', e: 'O..O..',
    f: 'OOO...', g: 'OOOO..', h: 'O.OO..', i: '.OO...', j: '.OOO..',
    k: 'O...O.', l: 'O.O.O.', m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.',
    p: 'OOO.O.', q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.',
    u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO', y: 'OO.OOO',
    z: 'O..OOO',
    'capital': '.....O', 
    ' ': '......', 
    'number': '.O.OOO', 
};

const brailleNum = {
    1: 'O.....', 2: 'O.O...', 3: 'OO....', 4: 'OO.O..', 5: 'O..O..',
    6: 'OOO...', 7: 'OOOO..', 8: 'O.OO..', 9: '.OO...', 0: '.OOO..',
};

const brailleToLetters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '......': ' ', '.O.OOO': 'number',
};

const brailleToNumbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
};

function convertToLetters(braille) {
    let result = '';
    let isCapital = false;
    let isNumberMode = false;
    
    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.slice(i, i + 6);
        
        if (brailleChar === brailleDictionary['capital']) {
            isCapital = true;
        } else if (brailleChar === brailleDictionary['number']) {
            isNumberMode = true;
        } else if (brailleChar === brailleDictionary[' ']) {
            result += ' ';
            isNumberMode = false;
        } else if (isNumberMode) {
            result += brailleToNumbers[brailleChar];
        } else {
            let char = brailleToLetters[brailleChar];
            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }
            result += char;
        }
    }

    return result;
}

function convertToBraille(text) {
    let result = '';
    let isNumberMode = false;
    
    for (const char of text) {
        if (char === ' ') {
            result += brailleDictionary[' ']; // Space
            isNumberMode = false;
        } else if (!isNaN(char)) {
            if (!isNumberMode) {
                result += brailleDictionary['number']; // Switch to number mode
                isNumberMode = true;
            }
            result += brailleNum[char];
        } else if (char === char.toUpperCase()) {
            result += brailleDictionary['capital'];
            result += brailleDictionary[char.toLowerCase()];
            isNumberMode = false;
        } else {
            result += brailleDictionary[char];
            isNumberMode = false;
        }
    }

    return result;
}




function checkAndTranslate(input) {
    const isBraille = /^[O.]+$/.test(input); 
    if (isBraille) {
        return convertToLetters(input);
    } else {
        return convertToBraille(input);
    }
}


const input = process.argv.slice(2).join(' ');
if (input) {
    console.log(checkAndTranslate(input));
} else {
    console.log('Missing input text');
}