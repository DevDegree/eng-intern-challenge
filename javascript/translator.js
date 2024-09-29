// Braille Alphabet Mapping
const brailleAlphabets = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Reverse Mapping
const brailleToEnglish = Object.keys(brailleAlphabets).reduce((obj, key) => {
    obj[brailleAlphabets[key]] = key;
    return obj;
}, {});

// Function to Determine if String is Braille
function isBraille(str) {
    return /^[O.]+$/.test(str);
}

// Function to Translate Braille to English
function translateToEnglish(brailleText) {
    let english = '';
    let isCapital = false;

    for (let i = 0; i < brailleText.length; i += 6) {
        const brailleChar = brailleText.slice(i, i + 6);
        if (brailleChar === '.....O') { // Capital letter flag
            isCapital = true;
            continue;
        }

        const translatedChar = brailleToEnglish[brailleChar];
        if (translatedChar !== undefined) {
            english += isCapital ? translatedChar.toUpperCase() : translatedChar;
            isCapital = false; // Reset capital flag
        } 
    }
    return english;
}

// Function to Translate English to Braille
function translateToBraille(text) {
    let braille = '';
    
    for (const char of text) {
        if (/[A-Z]/.test(char)) {
            braille += '.....O' + brailleAlphabets[char.toLowerCase()]; // Capital letter
        } else if (brailleAlphabets[char]) {
            braille += brailleAlphabets[char];
        }
    }
    return braille;
}

// Main Function to Handle Translation
function brailleTranslator(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

// Get input from command line arguments
const input = process.argv.slice(2).join(' ');
console.log(brailleTranslator(input));
