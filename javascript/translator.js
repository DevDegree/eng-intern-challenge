// Braille to English and English to Braille mappings
const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O',  // Special symbol for capitalizing
    'number': '.O.OOO',  // Special symbol for numbers
    ' ': '......',      // Space symbol
    'decimal': '.0...0', // Braille symbol for decimal point
    
    // Special Characters
     ',': '..O...',   // Comma
     ';': '..O.O.',   // Semicolon
     ':': '..OO..',   // Colon
    '.': '..OO.O',   // Period
     '!': '..OOO.',   // Exclamation mark
     '?': '..O.OO',   // Question mark
     '-': '.....OO',  // Hyphen
    '(': 'O.O..O',   // Open parenthesis
    ')': '.O.OO.',   // Close parenthesis (same as open)
     '/': '.O..O.',   // Forward slash
     '>': 'OOOOOO',
     '<': '.OO..O', //
};

const numberMap = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleToEnglishMap = Object.keys(brailleMap).reduce((obj, key) => {
    obj[brailleMap[key]] = key;
    return obj;
}, {});

// Inverse Braille map for decoding
const brailleToNumberMap = Object.keys(numberMap).reduce((obj, key) => {
    obj[numberMap[key]] = key;
    return obj;
}, {});
// Function to translate English to Braille
function englishToBraille(text) {
    let result = '';
    let inNumberMode = false; // Track number mode
    
    for (let i = 0; i < text.length; i++) {
        let char = text[i];

        // Handle capital letters
        if (char >= 'A' && char <= 'Z') {
            result += brailleMap['capital'];  // Capital symbol
            char = char.toLowerCase();
        }

        // Handle numbers
        if (char >= '0' && char <= '9') {
            if (!inNumberMode) {
                result += brailleMap['number'];  // Start number mode
                inNumberMode = true;
            }
            result += numberMap[char];
            // inNumberMode = false;

            continue;
        }
        
        // Handle decimal point within numbers
        if (char === '.') {
            if(inNumberMode) {
                result += brailleMap['decimal'];  // Add Braille decimal symbol
            } 
            result += brailleMap['.'];
            continue;
        }
        
        // Exit number mode after a space
        if (char === ' ') {
            inNumberMode = false;
        }

        // Translate the letter or space
        result += brailleMap[char] || brailleMap[' '];
    }
    return result;
}

// Function to translate Braille to English
function brailleToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.slice(i, i + 6);

        if (brailleChar === brailleMap['capital']) {
            isCapital = true;
            continue;
        }

        if (brailleChar === brailleMap['number']) {
            isNumber = true;
            continue;
        }

        // Handle decimal point
        if (brailleChar === brailleMap['decimal']) {
            result += '.';
            continue;
        }

        const char = brailleToEnglishMap[brailleChar];
        
        if (isNumber && brailleToNumberMap[brailleChar]) {
            result += brailleToNumberMap[brailleChar].toString();
            isNumber = false;  // Reset after one number
        } else if (isCapital) {
            result += char.toUpperCase();
            isCapital = false;
        } else {
            result += char;
        }
    }
    return result;
}

// Example usage
const inputArgs = process.argv.slice(2).join(' ');
if(inputArgs[0] === '.' || inputArgs[0] === 'O') {
    let englishBack = brailleToEnglish(inputArgs);
    console.log(englishBack);
} else {
    let brailleTranslation = englishToBraille(inputArgs);
    console.log(brailleTranslation);
}

