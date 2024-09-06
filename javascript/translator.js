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


const brailleToEng = Object.fromEntries(
    Object.entries(engToBraille).map(([key, value]) => [value, key])
);


brailleToEng[capitalFollows] = 'CAPITAL';
brailleToEng[decimalFollows] = 'DECIMAL';
brailleToEng[numberFollows] = 'NUMBER';

console.log('brailleToEng:', brailleToEng);

function translateBrailleToEng(input) {
    let output = '';
    let mode = 'normal'; 
    let currentPattern = '';

    for (let i = 0; i < input.length; i++) {
        currentPattern += input[i];

        if (currentPattern.length === 6) {
            if (currentPattern === numberFollows) {
                mode = 'number';
            } else if (currentPattern === decimalFollows) {
                mode = 'decimal';
            } else if (currentPattern === capitalFollows) {
                mode = 'capital';
            } else {
                let char = brailleToEng[currentPattern];
                if (char === undefined) {
                    console.warn(`Braille pattern '${currentPattern}' not found in brailleToEng.`);
                } else {
                    if (char === 'CAPITAL') {
                        mode = 'capital';
                    } else if (char === 'NUMBER') {
                        mode = 'number';
                    } else if (char === 'DECIMAL') {
                        mode = 'decimal';
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
                }
                currentPattern = ''; 
            }
        }
    }

    return output;
}


// console.log(translateBrailleToEng('.O.OOOOO.O..O.O...'));
