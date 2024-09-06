// Braille and English mapping
const brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', // space
};

const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', // space
};

// Special symbols
const capitalBraille = '.....O';
const numberBraille = '.O.OOO';

const isBraille = (input) => input[0] === 'O' || input[0] === '.';

// Braille to English
function brailleToEnglishConverter(brailleStr) {
    const words = brailleStr.split('......');
    let result = '';
    
    for (let word of words) {
        let chars = word.match(/.{1,6}/g); // Split by every 6 characters (Braille)
        let capitalNext = false;
        let numberMode = false;
        
        for (let char of chars) {
            if (char === capitalBraille) {
                capitalNext = true;
                continue;
            }
            if (char === numberBraille) {
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
        result += ' '; // Add space between words
    }
    return result.trim();
}

// English to Braille
function englishToBrailleConverter(englishStr) {
    let result = '';
    
    for (let char of englishStr) {
        if (char === char.toUpperCase() && char !== ' ') {
            result += capitalBraille; // Add capital marker
            char = char.toLowerCase();
        }
        
        if (char in englishToBraille) {
            result += englishToBraille[char];
        }
    }
    
    return result;
}

// Main function to handle both directions
function translate(input) {
    if (isBraille(input)) {
        return brailleToEnglishConverter(input);
    } else {
        return englishToBrailleConverter(input);
    }
}

// Example usage:
const input = process.argv.slice(2).join(' '); // Take input from command line
console.log(translate(input));