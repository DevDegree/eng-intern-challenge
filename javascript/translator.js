
const engToBraille = {
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
    'w': '.OOOO.',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOOO.',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOOO',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
};

const capitalFollows = '.....O';
const decimalFollows = '.O...O'; 
const numberFollows = '.O.OOO';  



function translateEngToBraille(input) {
    let output = '';
    let numberMode = false;

    for (const char of input) {
        if (char >= '0' && char <= '9') {
            if (!numberMode) {
                output += numberFollows;
                numberMode = true;
            }
            output += engToBraille[char];
        } else {
            numberMode = false;
            if (char >= 'A' && char <= 'Z') {
                output += capitalFollows + engToBraille[char.toLowerCase()];
            } else if (char === '.') {
                output += decimalFollows;
            } else {
                output += engToBraille[char] || '......'; 
            }
        }   
    }
    return output;
}




const brailleToEng = {
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
    '.OOOO.': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOOO': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
};



function translateBrailleToEng(input) {
    let output = '';
    let mode = 'normal'; 
    let currentPattern = '';

    for (const char of input) {
        currentPattern += char;


        if (currentPattern.length === 6) {
            if (currentPattern === numberFollows) {
                mode = 'number';
                currentPattern = ''; 
                continue; 
            } else if (currentPattern === decimalFollows) {
                mode = 'decimal';
                currentPattern = ''; 
                continue; 
            } else if (currentPattern === capitalFollows) {
                mode = 'capital';
                currentPattern = ''; 
                continue; 
            }

   
            let char = brailleToEng[currentPattern];
            if (char === undefined) {
                console.warn(`Braille pattern '${currentPattern}' not found in brailleToEng.`);
            } else {
                if (mode === 'capital') {
                    char = char.toUpperCase();
                    mode = 'normal'; 
                } else if (mode === 'number') {
                    mode = 'normal'; 
                } else if (mode === 'decimal') {
                    mode = 'normal'; 
                }
                output += char;
            }
            currentPattern = ''; 
        }
    }

    if (currentPattern.length === 6) {
        let char = brailleToEng[currentPattern];
        if (char === undefined) {
            console.warn(`Braille pattern '${currentPattern}' not found in brailleToEng.`);
        } else {
            if (mode === 'capital') {
                char = char.toUpperCase();
            }
            output += char;
        }
    }

    return output;
}


console.log(translateEngToBraille("Abc 123 xYz"));


