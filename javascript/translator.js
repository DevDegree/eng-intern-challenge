// Braille translation dictionaries
const engToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 
    'capital': '..O...', 'number': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleToLetter = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', 
    '..O...': 'capital', '.O.OOO': 'number'
};

const brailleToDigit = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
};

// Detect whether input is Braille (contains only "O" and "." characters)
function isBraille(input) {
    return /^[O.\s]+$/.test(input.trim());  // Include whitespace in the regex
}

// Eng to Braille translation
function engToBrailleTranslator(input) {
    let brailleSymbols = [];
    let numberMode = false;

    for (let char of input) {
        // Handle capital letters
        if (/[A-Z]/.test(char)) {
            brailleSymbols.push(engToBraille['capital']);  
            char = char.toLowerCase();
        }

        // Handle numbers
        if (/[0-9]/.test(char)) {
            if (!numberMode) {
                brailleSymbols.push(engToBraille['number']);  
                numberMode = true;
            }
            brailleSymbols.push(engToBraille[char]); 
        } else {
            numberMode = false; // Reset number mode for non-numeric
            brailleSymbols.push(engToBraille[char] || '');  // Append Braille letter or space
        }
    }

    return brailleSymbols.join(' ');
}

// Braille to Eng translation
function brailleToengTranslator(input) {
    let eng = '';
    let capitalMode = false;
    let numberMode = false;
    
    const brailleSymbols = input.trim().split(/\s+/);

    if (!brailleSymbols) {
        console.error("Invalid Braille input.");
        return;
    }

    for (let symbol of brailleSymbols) {
        // Handle capital and number symbols
        if (symbol === '..O...') {
            capitalMode = true;
            continue;
        }

        if (symbol === '.O.OOO') {
            numberMode = true;
            continue;
        }

        let char;
        if (numberMode) {
            if (symbol in brailleToDigit) {
                char = brailleToDigit[symbol];
            } else {
                // Symbol is not a digit, reset numberMode and process symbol as letter
                numberMode = false;
                char = brailleToLetter[symbol];
            }
        } else {
            char = brailleToLetter[symbol];
        }

        if (!char) {
            console.error(`Unrecognized Braille symbol: ${symbol}`);
            continue; 
        }

        if (capitalMode) {
            char = char.toUpperCase();
            capitalMode = false;  // Reset capital mode after applying it
        }

        eng += char;
    }

    return eng;
}

// Main function to determine if input is Eng or Braille and translate accordingly
function translate(input) {
    if (isBraille(input)) {
        console.log(brailleToengTranslator(input));
    } else {
        console.log(engToBrailleTranslator(input));
    }
}

// Capture command-line arguments and translate
const input = process.argv.slice(2).join(' ');
translate(input);
