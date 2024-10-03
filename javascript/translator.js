const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O.OO..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O.OOO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO..', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O.OO..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Braille number, alphabet, and capital letter indicators
const numberIndicator = ".O.OOO";  // Number mode indicator
const capitalIndicator = ".....O";  // Capital letter indicator

// Function to translate Braille to English
const brailleToEnglish = (braille) => {
    const brailleMap = {
        '.....O': 'a', 'O.....': 'b', 'O.O...': 'c', 'OO....': 'd', 'O.OO..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O.OOO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO..': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '......': ' ', 'O.....': '1', 'O.O...': '2',
        'OO....': '3', 'OO.O..': '4', 'O.OO..': '5', 'OOO...': '6', 'OOOO..': '7',
        'O.OO..': '8', '.OO...': '9'
    };
    
    let isNumber = false;
    let isCapital = false;
    let result = '';
    
    const brailleChars = braille.split(' ');
    
    for (let b of brailleChars) {
        if (b === numberIndicator) {
            isNumber = true;
            continue;
        }
        
        if (b === capitalIndicator) {
            isCapital = true;
            continue;
        }

        const char = brailleMap[b] || '?';
        
        // Capitalize the letter if we encountered a capital indicator
        if (isCapital) {
            result += char.toUpperCase();
            isCapital = false;
        } else {
            result += char;
        }
        
        // Reset number mode after letter
        if (isNumber && /^[a-zA-Z]$/.test(char)) {
            isNumber = false;  // Reset number mode if a letter is encountered
        }
    }
    
    return result;
};

// Function to translate English to Braille
const englishToBraille = (text) => {
    let braille = '';
    let isNumber = false;  // Track if we are in number mode
    
    for (let char of text) {
        if (/[A-Z]/.test(char)) {
            // Handle capital letters
            braille += capitalIndicator + brailleAlphabet[char.toLowerCase()];
            isNumber = false;  // Reset number mode after capital letters
        } else if (/[0-9]/.test(char)) {
            // Handle numbers
            if (!isNumber) {
                braille += numberIndicator;  // Add number indicator only once
                isNumber = true;
            }
            braille += brailleAlphabet[char];
        } else {
            // Handle regular letters and spaces
            if (isNumber && /[a-z]/.test(char)) {
                // Reset back to alphabet mode
                isNumber = false;
            }
            braille += brailleAlphabet[char] || '?';
        }
    }
    
    return braille;
};

// Input detection and translation
const input = process.argv.slice(2).join(' ');
const isBraille = input.split('').every(c => 'O.'.includes(c) || c === ' ');

const result = isBraille ? brailleToEnglish(input) : englishToBraille(input);
console.log(result);
