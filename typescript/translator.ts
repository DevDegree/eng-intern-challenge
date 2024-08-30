type BrailleMap = { [key: string]: string };

// Constants for Braille translation
const BRAILLE_CAPITAL = '.....O';
const BRAILLE_NUMBER = '.O.OOO';
const BRAILLE_SPACE = '......';

// Braille alphabet and punctuation map
const BRAILLE_MAP: BrailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOO.O', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.O', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.OO', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    ' ': BRAILLE_SPACE, '.': '.O.OOO', ',': '.O....', '?': '.OO.OO', '!': '.OOO.O', 
    ':': 'OO.O..', ';': 'O.O...', '-': 'O.....', '/': 'O..O.O', '<': 'O...OO', 
    '>': 'O.OO.O', '(': 'OO..OO', ')': 'OO..OO'
};

// Numbers map (1-9 and 0, corresponding to a-j in Braille when preceded by number symbol)
const NUMBER_MAP: BrailleMap = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Reverse lookup for English translation
const REVERSE_BRAILLE_MAP: BrailleMap = Object.fromEntries(Object.entries(BRAILLE_MAP).map(([k, v]) => [v, k]));
const REVERSE_NUMBER_MAP: BrailleMap = Object.fromEntries(Object.entries(NUMBER_MAP).map(([k, v]) => [v, k]));

/**
 * Translates an English text to Braille.
 * Handles capitalization and numbers by adding appropriate prefix symbols.
 */
function translateEnglishToBraille(text: string): string {
    let result: string[] = [];
    let numberMode = false;

    for (let char of text) {
        if (char === ' ') {
            result.push(BRAILLE_SPACE);
            numberMode = false;  // Reset number mode on space
            continue;
        }

        if (char.toUpperCase() === char && char.match(/[A-Z]/i)) {
            result.push(BRAILLE_CAPITAL);
            char = char.toLowerCase();
        }

        if (char.match(/\d/)) {
            if (!numberMode) {  // Only add number prefix if not already in number mode
                result.push(BRAILLE_NUMBER);
                numberMode = true;
            }
            result.push(NUMBER_MAP[char]);
        } else {
            result.push(BRAILLE_MAP[char] || BRAILLE_SPACE);
            numberMode = false;  // Exit number mode on non-digit
        }
    }

    return result.join('');
}

/**
 * Translates a Braille string to English text.
 * Handles number mode and capitalization appropriately.
 */
function translateBrailleToEnglish(brailleText: string): string {
    let result: string[] = [];
    let i = 0;
    let numberMode = false;

    while (i < brailleText.length) {
        const symbol = brailleText.slice(i, i + 6);

        if (symbol === BRAILLE_CAPITAL) {
            const nextSymbol = brailleText.slice(i + 6, i + 12);
            result.push((REVERSE_BRAILLE_MAP[nextSymbol] || '').toUpperCase());
            i += 12;
        } else if (symbol === BRAILLE_NUMBER) {
            numberMode = true;
            i += 6;
        } else if (symbol === BRAILLE_SPACE) {
            result.push(' ');
            i += 6;
        } else {
            if (numberMode) {
                result.push(REVERSE_NUMBER_MAP[symbol] || '');
            } else {
                result.push(REVERSE_BRAILLE_MAP[symbol] || '');
            }
            i += 6;
            numberMode = false;
        }
    }

    return result.join('');
}

/**
 * Detects whether the input text is Braille or English based on its content.
 */
function detectInputType(inputText: string): boolean {
    return /^[O. ]+$/.test(inputText);
}

/**
 * Main function to handle input and call the appropriate translation function.
 */
function main(): void {
    const inputText = process.argv.slice(2).join(' ');

    if (detectInputType(inputText)) {
        // Braille to English translation
        console.log(translateBrailleToEnglish(inputText));
    } else {
        // English to Braille translation
        console.log(translateEnglishToBraille(inputText));
    }
}

main();
