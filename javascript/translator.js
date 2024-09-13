// Braille Translator in JavaScript

// Braille alphabet as O (raised) and . (not raised)
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', // Space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Reverse lookup for converting Braille to English
const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([letter, braille]) => [braille, letter])
);

// Convert English to Braille
function englishToBraille(text) {
    return text.split('').map(char => {
        const lowerChar = char.toLowerCase();
        if (lowerChar === char) {
            return brailleMap[lowerChar] || '';
        } else {
            return '.....O' + brailleMap[lowerChar]; // Capital letter in Braille
        }
    }).join('');
}

// Convert Braille to English
function brailleToEnglish(brailleText) {
    let result = '';
    for (let i = 0; i < brailleText.length; i += 6) {
        let brailleChar = brailleText.slice(i, i + 6);
        if (brailleChar === '.....O') {
            // Capitalization follows this marker
            let nextChar = brailleText.slice(i + 6, i + 12);
            result += reverseBrailleMap[nextChar]?.toUpperCase() || '';
            i += 6;
        } else {
            result += reverseBrailleMap[brailleChar] || '';
        }
    }
    return result;
}

// Detect whether the input is Braille or English
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Main function to handle the translation
function translate(input) {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

// Reading input from command line arguments
const input = process.argv[2]; // Get the input string from command-line
if (input) {
    console.log(translate(input)); // Output the translation result
} else {
    console.log("Please provide an input string to translate.");
}
