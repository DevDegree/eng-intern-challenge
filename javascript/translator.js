// Updated Braille mappings with symbols
const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
};

const brailleNumbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleSymbols = {
    '.': '..OO.O', ',': 'O.....', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': 'O.OO..', '-': '..O...', '/': '..O.O.', '>': '..O.O.', '<': '..O.O.',
    '(': '.OOO..', ')': '.OO.O.'
};

const specialSymbols = {
    'capital': '.....O',
    'number': '.O.OOO'
};

// Utility function to check if a string contains only valid English characters
function isValidEnglish(input) {
    const validChars = /^[a-zA-Z0-9.,?!:;\/><() \-]+$/;
    return validChars.test(input);
}


// Utility function to check if a string contains only valid Braille characters
function isValidBraille(input) {
    return /^[O.]+$/.test(input) && input.length % 6 === 0; 
}

// Translate from English to Braille
function englishToBraille(input) {
    let brailleOutput = '';
    let isNumber = false;

    for (let char of input) {
        if (char >= 'A' && char <= 'Z') {
            brailleOutput += specialSymbols['capital']; // Add capital follow symbol
            brailleOutput += brailleAlphabet[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            if (!isNumber) {
                brailleOutput += specialSymbols['number']; // Add number follow symbol
                isNumber = true;
            }
            brailleOutput += brailleNumbers[char];
        } else if (char in brailleSymbols) {
            if (isNumber) isNumber = false; 
            brailleOutput += brailleSymbols[char];
        } else {
            if (isNumber) isNumber = false; 
            brailleOutput += brailleAlphabet[char];
        }
    }
    return brailleOutput;
}

// Translate from Braille to English
function brailleToEnglish(input) {
    let englishOutput = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        let brailleChar = input.substring(i, i + 6);

        if (brailleChar === specialSymbols['capital']) {
            isCapital = true;
        }

        else if (brailleChar === specialSymbols['number']) {
            isNumber = true;
        }
        
        else if (brailleChar === '......') {
            englishOutput += ' ';
            isNumber = false; 
        }
        
        else {
            let letter = Object.keys(isNumber ? brailleNumbers : brailleAlphabet).find(key =>
                (isNumber ? brailleNumbers : brailleAlphabet)[key] === brailleChar
            );

            if (letter) {
                if (isCapital) {
                    letter = letter.toUpperCase();
                    isCapital = false;
                }
                englishOutput += letter;
            }

            if (!isNumber && letter) {
                isNumber = false;
            }
        }
    }

    return englishOutput;
}


// Main translation function with edge case checks
function translate(input) {
    if (input.trim() === '') {
        return "Error: Input is empty.";
    }

    if (/^[O\.]+$/.test(input)) {
        // Check if it's valid Braille
        if (!isValidBraille(input)) {
            return "Error: Invalid Braille input. Braille must contain only 'O' and '.' and be in multiples of 6.";
        }
        return brailleToEnglish(input);
    } else {
        // Check if it's valid English
        if (!isValidEnglish(input)) {
            return "Error: Invalid English input. Only letters, numbers, and common punctuation are allowed.";
        }
        return englishToBraille(input);
    }
}

// Command line arguments handling with edge case handling
const args = process.argv.slice(2);
if (args.length > 0) {
    const input = args.join(' ');
    console.log(translate(input));
} else {
    console.log("Error: Please provide input for translation.");
}
