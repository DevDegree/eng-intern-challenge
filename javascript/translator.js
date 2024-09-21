const ASCII_CODE_A = 'a'.charCodeAt(0);
const ASCII_CODE_J = 'j'.charCodeAt(0);

const brailleToEnglish = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
    '.....O': 'capital', 
    '.O...O': '.',
    '.O.OOO': 'number', 
};

const EnglsihToBraille = {
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
    ' ': '......', 
    'capital': '.....O', 
    'number': '.O.OOO', 
    '.': '.O...O',
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

function letterToNumber(character) {
    if (brailleToEnglish[character].charCodeAt(0) === ASCII_CODE_J) {
        return '0';
    }
    return String(brailleToEnglish[character].charCodeAt(0) - ASCII_CODE_A + 1)
}


function isValidBraillePattern(pattern) {    
    return pattern.length % 6 === 0 && /^[O.]+$/.test(pattern);
}

function translateToEnglish(characters) {
    let isCapital = false;
    let isInNumberMode = false;
    let translatedText = '';

    characters.forEach((character) => {
        const translation = brailleToEnglish[character];
        if (translation === 'capital') {
            isCapital = true;
        } else if (translation === 'number') {
            isInNumberMode = true;
        } else if (translation === ' ') {
            isInNumberMode = false;
            translatedText += ' ';
        } else {
            if (isInNumberMode) {
                translatedText += letterToNumber(character);
            } else {
                translatedText += isCapital ? translation.toUpperCase() : translation;
                isCapital = false;
            }
        }
    });

    return translatedText;
}

function translateToBraille(characters) {
    let isInNumberMode = false; 
    let translatedText = '';
    
    characters.split('').forEach((char)=> {
        if(char === ' ') {
            isNumber = false;
            translatedText += EnglsihToBraille[char];
        } else if(!isNaN(char)) {
            if(!isInNumberMode) {
                translatedText += EnglsihToBraille['number'];
                isInNumberMode = true;
            }
            translatedText += EnglsihToBraille[char];
        } else if(char.toUpperCase() === char) {
            translatedText += EnglsihToBraille['capital'];
            translatedText += EnglsihToBraille[char.toLowerCase()];
        } else {
            translatedText += EnglsihToBraille[char]; 
        }
    });

    return translatedText;
}

let textToTranslate = process.argv.slice(2).join(' ');

if(isValidBraillePattern(textToTranslate.toUpperCase())) {
    const letters = [];
    for(let i = 0; i < textToTranslate.length; i+= 6) {
        letters.push(textToTranslate.toUpperCase().slice(i, i+6));
    }
    console.log(translateToEnglish(letters));
}
else {
    console.log(translateToBraille(textToTranslate));
}
