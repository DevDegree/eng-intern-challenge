const ENGLISH_TO_BRAILLE = {
    a: 'O.....',
    b: 'O.O...',
    c: 'OO....',
    d: 'OO.O..',
    e: 'O..O..',
    f: 'OOO...',
    g: 'OOOO..',
    h: 'O.OO..',
    i: '.OO...',
    j: '.OOO..',
    k: 'O...O.',
    l: 'O.O.O.',
    m: 'OO..O.',
    n: 'OO.OO.',
    o: 'O..OO.',
    p: 'OOO.O.',
    q: 'OOOOO.',
    r: 'O.OOO.',
    s: '.OO.O.',
    t: '.OOOO.',
    u: 'O...OO',
    v: 'O.O.OO',
    w: '.OOO.O',
    x: 'OO..OO',
    y: 'OO.OOO',
    z: 'O..OOO',
    1: 'O.....',
    2: 'O.O...',
    3: 'OO....',
    4: 'OO.O..',
    5: 'O..O..',
    6: 'OOO...',
    7: 'OOOO..',
    8: 'O.OO..',
    9: '.OO...',
    0: '.OOO..',
    // Punctuation and special symbols
    '.': '.O..OO',
    ',': '.O....',
    '?': '.O.O.O',
    '!': '.OOO.O',
    ':': '.OO...',
    ';': '.O.O..',
    '-': '..O...',
    '/': '..O.O.',
    '<': '..OO..',
    '>': '..OOO.',
    '(': 'O..O.O',
    ')': '.OO.OO',
    ' ': '......',
};

const BRAILLE_CAPITAL_FOLLOWS = '.....O';

const BRAILLE_NUMBER_FOLLOWS = '.O.OOO';

const BRAILLE_DECIMAL_FOLLOWS = '.O...O';

const BRAILLE_TO_ENGLISH = Object.fromEntries(Object.entries(ENGLISH_TO_BRAILLE).map(([k, v]) => [v, k]));

// Check if input is braille
const isBraille = (input) => /^[O\. ]+$/.test(input);

// Convert English to Braille
const englishToBraille = (input) => {
    let isNumber = false;
    return input
        .split('')
        .map((char) => {
            if (char >= 'A' && char <= 'Z') {
                return BRAILLE_CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.toLowerCase()];
            }
            if (char >= '0' && char <= '9') {
                if (!isNumber) {
                    isNumber = true;
                    return BRAILLE_NUMBER_FOLLOWS + ENGLISH_TO_BRAILLE[char];
                }
                return ENGLISH_TO_BRAILLE[char];
            } else {
                isNumber = false;
            }
            if (ENGLISH_TO_BRAILLE[char]) return ENGLISH_TO_BRAILLE[char];
            throw new Error(`Unsupported character: ${char}`);
        })
        .join('');
};

// Convert Braille to English
const brailleToEnglish = (input) => {
    const chunks = input.match(/.{6}/g) || [];
    let result = '',
        isCapital = false,
        isNumber = false;

    chunks.forEach((chunk) => {
        if (chunk === BRAILLE_CAPITAL_FOLLOWS) {
            isCapital = true;
        } else if (chunk === BRAILLE_NUMBER_FOLLOWS) {
            isNumber = true;
        } else {
            const letter = brailleToEnglish[chunk];
            if (letter) {
                if (isNumber) {
                    result += letter; // Numbers don't need capitalization
                    isNumber = false;
                } else if (isCapital) {
                    result += letter.toUpperCase();
                    isCapital = false;
                } else {
                    result += letter;
                }
            } else {
                throw new Error(`Unsupported Braille sequence: ${chunk}`);
            }
        }
    });

    return result;
};

// Automatically translate Braille to English or vice versa
const translate = (input) => (isBraille(input.trim()) ? brailleToEnglish(input.trim()) : englishToBraille(input.trim()));

// Get input from command-line arguments
const input = process.argv.slice(2).join(' ');
if (!input) process.exit(1);

try {
    // Output the translated result
    console.log(translate(input));
} catch (error) {
    console.error(error.message);
    process.exit(1);
}
