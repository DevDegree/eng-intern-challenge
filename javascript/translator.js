
const engToBraille = {
    'a': '0.....',
    'b': '0.0...',
    'c': '00....',
    'd': '00.0..',
    'e': '0..0..',
    'f': '000...',
    'g': '0000..',
    'h': '0.00..',
    'i': '.00...',
    'j': '.000..',
    'k': '0...0.',
    'l': '0.0.0.',
    'm': '00..0.',
    'n': '00.00.',
    'o': '0..00.',
    'p': '000.0.',
    'q': '00000.',
    'r': '0.000.',
    's': '.00.0.',
    't': '.0000.',
    'u': '0...00',
    'v': '0.0.00',
    'w': '.000.0',
    'x': '00..00',
    'y': '00.000',
    'z': '0..000',
    '1': '0.....',
    '2': '0.0...',
    '3': '00....',
    '4': '00.0..',
    '5': '0..0..',
    '6': '000...',
    '7': '0000..',
    '8': '0.00..',
    '9': '.00...',
    '0': '.000..',
    '.': '..00.0',
    ',': '..0...',
    '?': '..0.00',
    '!': '..000.',
    ':': '..00..',
    ';': '..0.0.',
    '-': '....00',
    '/': '.0..0.',
    '<': '.00..0',
    '>': '0..00.',
    '(': '0.0..0',
    ')': '.0.00.',
    ' ': '......',
};

const capitalFollows = '.....0';
const decimalFollows = '.0...0'; 
const numberFollows = '.0.000';  



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
console.log(translateEngToBraille('Abc 123 xYz'));



const brailleToEng = {
    '0.....': 'a',
    '0.0...': 'b',
    '00....': 'c',
    '00.0..': 'd',
    '0..0..': 'e',
    '000...': 'f',
    '0000..': 'g',
    '0.00..': 'h',
    '.00...': 'i',
    '.000..': 'j',
    '0...0.': 'k',
    '0.0.0.': 'l',
    '00..0.': 'm',
    '00.00.': 'n',
    '0..00.': 'o',
    '000.0.': 'p',
    '00000.': 'q',
    '0.000.': 'r',
    '.00.0.': 's',
    '.0000.': 't',
    '0...00': 'u',
    '0.0.00': 'v',
    '.000.0': 'w',
    '00..00': 'x',
    '00.000': 'y',
    '0..000': 'z',
    '..00.0': '.',
    '..0...': ',',
    '..0.00': '?',
    '..000.': '!',
    '..00..': ':',
    '..0.0.': ';',
    '....00': '-',
    '.0..0.': '/',
    '.00..0': '<',
    '0.0..0': '(',
    '.0.00.': ')',
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


console.log(translateBrailleToEng('.....00.....0.0...00...........0.0000.....0.0...00..........00..00.....000.0000..000')); 



