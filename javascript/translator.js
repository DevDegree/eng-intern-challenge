// Braille object
const brailleLetters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.',
    'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO',
    'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    '^': '.....O',
};

const brailleNumbers = {
    '#': '.O.OOO', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
};

const brailleSpecial = {
    ' ': '......', ',': 'O.....', '.': 'O..OOO', '!': 'O.OO.O', '?': 'O.O.OO', '-': '......O',
};

// Reverse map to translate from Braille to English
const reverseBrailleLetters = Object.fromEntries(Object.entries(brailleLetters).map(([k, v]) => [v, k]));
const reverseBrailleNumbers = Object.fromEntries(Object.entries(brailleNumbers).map(([k, v]) => [v, k]));
const reverseBrailleSpecial = Object.fromEntries(Object.entries(brailleSpecial).map(([k, v]) => [v, k]));

// Function to translate Braille to English
function translateFromBraille(text) {
    let englishOutput = '';
    let isCapital = false;
    let isNumber = false;

    // Split input text into of 6 characters group
    const brailleChars = text.match(/.{1,6}/g);

    for (let brailleChar of brailleChars) {
        if (brailleChar === '......') {
            // Handle space
            englishOutput += ' ';
            // Reset number variable
            isNumber = false;
        } else if (brailleChar === '.O.OOO') { 
            // Number indicator
            isNumber = true;
        } else if (brailleChar === '.....O') { 
            // Capitalize indicator
            isCapital = true;
        } else if (isNumber && brailleChar in reverseBrailleNumbers) {
            // Translate Braille numbers
            englishOutput += reverseBrailleNumbers[brailleChar];
        } else if (brailleChar in reverseBrailleLetters) {
            // Translate Braille letters
            let translatedChar = reverseBrailleLetters[brailleChar];

            if (isCapital) {
                translatedChar = translatedChar.toUpperCase();
                // Only capitalize the next letter
                isCapital = false; 
            }

            englishOutput += translatedChar;
            // Reset number variable
            isNumber = false;  
        } else if (brailleChar in reverseBrailleSpecial) {
            // Translate special characters
            englishOutput += reverseBrailleSpecial[brailleChar];
            // Reset number variable
            isNumber = false;  
        } else {
            // If error, unknow characters
            englishOutput += '[?]';  
        }
    }

    return englishOutput.trim();
}

// Function to translate English to Braille
function translateToBraille(text) {
    let brailleOutput = '';
    let isNumber = false;

    for (let char of text) {
        if (/[A-Z]/.test(char)) {
            // Add capitalize sign
            brailleOutput += brailleLetters['^'];
            brailleOutput += brailleLetters[char.toLowerCase()];
            // Reset number variable
            isNumber = false; 
        } else if (/[a-z]/.test(char)) {
            brailleOutput += brailleLetters[char];
            // Reset number variable
            isNumber = false;
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                // Add number sign only once (before first number)
                brailleOutput += brailleNumbers['#'];
                isNumber = true;
            }
            brailleOutput += brailleNumbers[char];
        } else if (char in brailleSpecial) {
            brailleOutput += brailleSpecial[char];
            // Reset number variable
            isNumber = false;
        } else {
            // If error, unknow characters
            brailleOutput += '[?]';
            // Reset number variable
            isNumber = false;
        }
    }
    return brailleOutput;
}


// Capture the text or Braille in terminal
const inputText = process.argv.slice(2).join(' ');

// Detect if it's Braille or Englisht
if (inputText && (inputText.includes('O') || inputText.includes('.'))) {
    const translatedText = translateFromBraille(inputText);
    console.log(translatedText);
} else if (inputText) {
    const translatedText = translateToBraille(inputText);
    console.log(translatedText);
} else {
    console.log("Type text to be translated");
}
