// Braille and English mapping
const brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ',  // space
};

const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  // space
};

// Special symbols
const CAPITAL_BRAILLE = '.....O';
const NUMBER_BRAILLE = '.O.OOO';

// Helper function to detect if input is Braille or English
const isBraille = (input) => input[0] === 'O' || input[0] === '.';

// Braille to English converter
function brailleToEnglishConverter(brailleStr) {
    const words = brailleStr.split('......');  // Split into words using the Braille space (......)
    let result = '';
    
    for (let word of words) {
        if (!word) continue;  // Avoid processing empty strings between words
        const chars = word.match(/.{1,6}/g);  // Split every 6 characters (Braille cell)
        let capitalNext = false;
        let numberMode = false;
        
        for (let char of chars) {
            if (char === CAPITAL_BRAILLE) {
                capitalNext = true;
                continue;
            }
            if (char === NUMBER_BRAILLE) {
                numberMode = true;
                continue;
            }
            if (char in brailleToEnglish) {
                let letter = brailleToEnglish[char];
                
                if (capitalNext) {
                    letter = letter.toUpperCase();
                    capitalNext = false;
                }
                
                result += letter;
            }
        }
        result += ' ';  // Add space between words
    }
    return result.trim();
}

// English to Braille converter
function englishToBrailleConverter(englishStr) {
    let result = '';
    
    for (let char of englishStr) {
        if (char === ' ') {
            result += '......';  // Handle spaces
            continue;
        }

        if (char === char.toUpperCase()) {
            result += CAPITAL_BRAILLE;  // Add capital marker before uppercase letters
            char = char.toLowerCase();
        }
        
        if (char in englishToBraille) {
            result += englishToBraille[char];
        }
    }
    
    return result.trim();  // Remove any trailing spaces
}

// Main translation function to handle both directions
function translate(input) {
    if (isBraille(input)) {
        return brailleToEnglishConverter(input);
    } else {
        return englishToBrailleConverter(input);
    }
}

// Command-line input handling
if (require.main === module) {
    const input = process.argv.slice(2).join(' ');  // Take input from the command line
    console.log(translate(input));
}
