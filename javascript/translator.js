// Braille mappings: English to Braille
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO'
};


const numMap = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
};


const brailleToText = {};
const numToText = {};

Object.keys(brailleMap).forEach(key => {
    brailleToText[brailleMap[key]] = key;
});
Object.keys(numMap).forEach(num => {
    numToText[numMap[num]] = num;
});

// Convert English text to Braille
const textToBraille = (input) => {
    let result = "";
    let numMode = false;

    for (const char of input) {
        let brailleChar = "";

    
        if (char === ' ') {
            result += brailleMap[' '];
            numMode = false;
            continue;
        }


        if (!isNaN(char)) {
            if (!numMode) {
                result += brailleMap['num'];
                numMode = true;
            }
            brailleChar = brailleMap[numMap[char]];
        } else {
           
            if (char === char.toUpperCase()) {
                result += brailleMap['cap'];
                brailleChar = brailleMap[char.toLowerCase()];
            } else {
                brailleChar = brailleMap[char];
            }
            numMode = false; 
        }

        result += brailleChar;
    }

    return result;
};

// Convert Braille text to English
const brailleToTextConvert = (input) => {
    let result = "";
    let capMode = false;
    let numMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleSegment = input.slice(i, i + 6);

        
        if (brailleSegment === brailleMap['cap']) {
            capMode = true;
            continue;
        }
        if (brailleSegment === brailleMap['num']) {
            numMode = true;
            continue;
        }

        
        if (brailleSegment === brailleMap[' ']) {
            result += ' ';
            continue;
        }

    
        let char = brailleToText[brailleSegment];
        if (numMode) {
            char = numToText[char] || '?'; 
            numMode = false;
        } else if (capMode) {
            char = char.toUpperCase();
            capMode = false;
        }

        result += char;
    }

    return result;
};

// Detect if input is Braille
const isBraille = (input) => /^[O.]+$/.test(input);

// Main translation function
const translate = (input) => isBraille(input) ? brailleToTextConvert(input) : textToBraille(input);

// Get input from command-line arguments
const userInput = process.argv.slice(2).join(' ');
const translation = translate(userInput);
console.log(translation);
