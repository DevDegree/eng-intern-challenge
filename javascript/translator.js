const { exec } = require('child_process');

//Braille Mapping
const englishToBraille = {
    'a':'O.....',
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
    'cf': '.....O',
    'df': '.O...O',
    'nf': '.O.OOO',
};

//English Mapping
const brailleToEnglish = {
    'O.....': ['a', '1'],
    'O.O...': ['b', '2'],
    'OO....': ['c', '3'],
    'OO.O..': ['d', '4'],
    'O..O..': ['e', '5'],
    'OOO...': ['f', '6'],
    'OOOO..': ['g', '7'],
    'O.OO..': ['h', '8'],
    '.OO...': ['i', '9'],
    '.OOO..': ['j', '0'],
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
    '.....O': 'cf',
    '.O...O': 'df',
    '.O.OOO': 'nf',
};


// Check if argument is written in English or Braille
function isEnglish(argument){
    //check if argument contains characters besides O's and .
    return /[a-zA-Z0-9 ]/.test(argument);
}

function isBraille(argument){
    //check if argument is only composed of o's and .
    return /^[O. ]*$/.test(argument) && (argument.length % 6 === 0);
}


// Translation functions
//recognizes capitals but still need to work on recognizing spaces (ex. Hello World) only translates the Hello part
function translateEnglishToBraille(englishInput) {
    let brailleOutput = '';
    let char = englishInput.split("");
    for(let i = 0; i < char.length; i++) {
        //check if capital and alphabetical value
        if(char[i] >= 'A' && char[i] <= 'Z'){
            brailleOutput += englishToBraille['cf'] + englishToBraille[char[i].toLowerCase()];
        }
        //check if number
        else if (char[i] >= '0' && char[i] <= '9') {
            if (i === 0 || !(englishInput[i - 1] >= '0' && englishInput[i - 1] <= '9')) {
                brailleOutput += englishToBraille['nf'] + englishToBraille[char[i]];
            } else {
                brailleOutput += englishToBraille[char[i]];
            }
        }
        //check if character is a space
         else if(char[i] === ' '){
             // Add the space representation
            brailleOutput += englishToBraille[' '];
        }
         else {
            brailleOutput += englishToBraille[char[i]] || '?';
        }
    }
    return brailleOutput;
}


function translateBrailleToEnglish(brailleInput) {
    let englishOutput = '';
    // Split input into chunks of length 6
    let brailleChars = brailleInput.match(/.{1,6}/g) || [];

    let isNumberMode = false;
    let isCapitalMode = false;

    for (let i = 0; i < brailleChars.length; i++) {
        let brailleChar = brailleChars[i];

        if (brailleChar === '.....O') {
            // Capital mode flag
            isCapitalMode = true;
            continue; // Skip the capital flag character
        } else if (brailleChar === '.O.OOO') {
            // Number mode flag
            isNumberMode = true;
            continue; // Skip the number flag character
        } else if (brailleChar === '......') {
            // Space character
            englishOutput += ' ';
            isNumberMode = false; // Reset number mode
            isCapitalMode = false; // Reset capital mode
        } else {
            // Handle regular characters and special cases
            let englishCharArray = brailleToEnglish[brailleChar];
            if (Array.isArray(englishCharArray)) {
                if (isNumberMode) {
                    // Translate number
                    englishOutput += englishCharArray[1];
                    isNumberMode = false; // Reset number mode after use
                } else {
                    // Translate letter
                    if(isCapitalMode){
                        englishOutput += englishCharArray[0].toUpperCase();
                    }
                    else{
                        englishOutput += englishCharArray[0];
                    }

                }
            } else if (englishCharArray) {
                if (isCapitalMode) {
                    // Translate letter with capital mode
                    englishOutput += englishCharArray.toUpperCase();
                    isCapitalMode = false; // Reset capital mode after use
                } else {
                    // Translate regular letter
                    englishOutput += englishCharArray;
                }
            } else {
                // Handle undefined characters
                englishOutput += '?';
            }
            isCapitalMode = false;
        }
    }
    return englishOutput;
}




// Read command line arguments
const args = process.argv.slice(2); // Slice gets rid of node and file name
const argument = args.join(' '); // Join arguments into single string, keeping spaces
let translatedOutput = '';

if(isBraille(argument)){
    translatedOutput = translateBrailleToEnglish(argument);
} else if(isEnglish(argument)){
    translatedOutput = translateEnglishToBraille(argument);
} else {
    translatedOutput = 'Invalid input';
}

console.log(translatedOutput);
