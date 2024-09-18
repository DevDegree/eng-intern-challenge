const brailleMap = {
    // Lowercase letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    // Capitalization indicator
    '^': '.....O',

    // Numbers
    '#': '.O.OOO', // Number sign
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',

    // Special characters
    ' ': '......',
    ',': 'O.....',
    '.': 'O..OOO',
    '!': 'O.OO.O',
    '?': 'O.O.OO',
    '-': '......O',
};

// Creating a reverse map for Braille to English
const reverseBrailleMap = {};
for (const key in brailleMap) {
    reverseBrailleMap[brailleMap[key]] = key;
}

// Function to translate text to Braille
function translateToBraille(text) {
    let brailleOutput = '';
    let isNumber = false;

    for (let char of text) {
        if (char === ' ') {
            brailleOutput += brailleMap[' '];
            isNumber = false;
        } else if (!isNaN(char) && char !== ' ') {
            if (!isNumber) {
                brailleOutput += brailleMap['#'];
                isNumber = true;
            }
            brailleOutput += brailleMap[char];
        } else {
            isNumber = false;
            if (char === char.toUpperCase() && char.toLowerCase() in brailleMap) {
                brailleOutput += brailleMap['^'] + brailleMap[char.toLowerCase()];
            } else if (char.toLowerCase() in brailleMap) {
                brailleOutput += brailleMap[char.toLowerCase()];
            } else {
                brailleOutput += '[?] ';
            }
        }
    }

    return brailleOutput.trim();
}



// Function to translate Braille to English
function translateFromBraille(brailleText) {
    let englishOutput = '';
    const brailleChars = brailleText.match(/.{1,6}/g);
    let isCapital = false;
    let isNumber = false;

    for (let brailleChar of brailleChars) {
        if (brailleChar === brailleMap['^']) {
            isCapital = true;
        } else if (brailleChar === brailleMap['#']) {
            isNumber = true;
        } else if (brailleChar === '......') {
            englishOutput += ' ';
        } else if (brailleChar in reverseBrailleMap) {
            let translatedChar = reverseBrailleMap[brailleChar];

            if (isNumber) {
                englishOutput += translatedChar;
                isNumber = false; 
            } else {
                if (isCapital) {
                    translatedChar = translatedChar.toUpperCase();
                    isCapital = false;
                }
                englishOutput += translatedChar;
            }
        } else {
            englishOutput += '[?]';
        }
    }

    return englishOutput;
}




// Capture the text or Braille input passed in the terminal
const inputText = process.argv.slice(2).join(' ');

// Detect if it's Braille or English based on input
if (inputText && inputText.includes('O') || inputText.includes('.')) {
    const translatedText = translateFromBraille(inputText);
    console.log(translatedText);
} else if (inputText) {
    const translatedText = translateToBraille(inputText);
    console.log(translatedText);
} else {
    console.log("Type text to be translated");
}
