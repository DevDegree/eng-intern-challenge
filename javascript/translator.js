// Braille mappings based on the standard representation
const ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
};

// Reverse mapping Braille to English
const BRAILLE_TO_ENGLISH = Object.entries(ENGLISH_TO_BRAILLE).reduce((acc, [letter, braille]) => {
    acc[braille] = letter;
    return acc;
}, {});

// Add the capital letter and number symbols to the mapping
const CAPITAL_SYMBOL = '.....O'; // Capital letter indicator
const NUMBER_SYMBOL = '.O.O..'; // Number indicator

// Function to detect if input is Braille or English
function isBraille(input) {
    return input.includes('O') || input.includes('.');
}

// Function to translate English to Braille
function englishToBraille(input) {
    let braille = '';
    for (let char of input) {
        if (char >= 'A' && char <= 'Z') {
            braille += CAPITAL_SYMBOL + ENGLISH_TO_BRAILLE[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            braille += NUMBER_SYMBOL + ENGLISH_TO_BRAILLE[char];
        } else {
            braille += ENGLISH_TO_BRAILLE[char] || '......'; // Handle spaces and undefined characters
        }
    }
    return braille;
}

// Function to translate Braille to English
function brailleToEnglish(input) {
    let english = '';
    let isCapital = false;
    let isNumber = false;

    // Split input by chunks of 6 (representing Braille characters)
    for (let i = 0; i < input.length; i += 6) {
        let brailleChar = input.substring(i, i + 6);
        
        // Debugging: Output the current Braille character being processed
        console.log(`Processing Braille: ${brailleChar}`);
        
        if (brailleChar === CAPITAL_SYMBOL) {
            isCapital = true;
            continue;
        }
        if (brailleChar === NUMBER_SYMBOL) {
            isNumber = true;
            continue;
        }
        
        // Check if brailleChar exists in BRAILLE_TO_ENGLISH
        let letter = BRAILLE_TO_ENGLISH[brailleChar] || '?'; // Use '?' for unknown Braille sequences

        // Debugging: Output the letter determined for the current Braille character
        console.log(`Mapped to English letter: ${letter}`);
        
        if (isNumber) {
            letter = BRAILLE_TO_ENGLISH[brailleChar] || '?';
            isNumber = false; // Reset after number is handled
        }
        
        if (isCapital) {
            letter = letter.toUpperCase();
            isCapital = false; // Reset after capital letter is handled
        }
        
        english += letter;
    }
    return english;
}

// Main translation function
function translate(input) {
    return isBraille(input) ? brailleToEnglish(input) : englishToBraille(input);
}

// Capture input from command line
const input = process.argv[2]; // The string passed in from the command line
if (input) {
    const output = translate(input);
    console.log(output);
} else {
    console.log('Please provide a string to translate.');
}