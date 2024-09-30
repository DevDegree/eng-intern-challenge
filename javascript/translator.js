
// Lookup Table Based Braille Translator
// Author: Connor "ConnorBP" Postma
// 2024-09-30

// Missing: decimals handling

const braille_lut = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    // special commands
    'CAPITAL': '.....O',
    'DECIMAL': '.O...O',
    'NUMBER': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
};

// Create a reverse lookup table of the brail
const english_lut = {};
const numbers_lut = {};
for (const [key, value] of Object.entries(braille_lut)) {
    if(isDigit(key)) {
        numbers_lut[value] = key;
    } else {
        english_lut[value] = key;
    }
}

// a couple helpers

// Fetch the braille value from lut with a fallback to empty str
const get_braille = (char) => braille_lut[char] || '';

// Fetch the eng char value from lut with a fallback to empty str
const get_char = (char) => english_lut[char] || '';

// check if char is am ascii digit
function isDigit(char) {
    return char >= '0' && char <= '9'; // Checks if the character is within the ASCII range for digits
}

// iterate all characters and check for non o or .
// to determine if it is a non braille string
function isBraille(input) {
    for (const char of input) {
        if (char!== ' ' && char !== 'O' && char !== '.') {
            return false; // Found an invalid character
        }
    }
    return true;
}

// console.log(process.argv);

// get the args
// and connect seperate args with spaces
// since that seems to be what the test case is expecting
const args = process.argv.slice(2).join(' ');

function convert_args_to_braille() {
    let str_result = '';

    // keep track of number runs
    let wasLastADigit = false;
    for(c of args) {
        let lowerchar = c.toLowerCase();

        if(isDigit(c) && !wasLastADigit) {
            wasLastADigit = true;
            str_result += braille_lut['NUMBER'];
        } else if(c === ' ') {
            // end the digit run
            // to allow another number cmd
            wasLastADigit = false;
        }

        // if lowerchar and char are diff
        // then char is uppercase
        if(lowerchar!==c) {
            str_result+=braille_lut['CAPITAL'];
        }

        str_result += get_braille(lowerchar)
    }
    return str_result;
}

function convert_args_to_english() {
    let str_result = '';

    // track command characters
    let nextIsNumber = false;
    let nextIsCapital = false;
    // iterate over the braille string in chunks
    for (let i = 0; i < args.length; i += 6) {
        const section = args.slice(i, i + 6);
        
        let c = get_char(section);

        // parse number command
        if(c==='NUMBER') {
            // console.log('number')
            nextIsNumber = true;
            continue;
        } 
        if(c === 'CAPITAL') {
            nextIsCapital = true;
            continue;
        }
        
        if(nextIsNumber) {
            let num = numbers_lut[section];
            if(num != undefined) {
                // append the num to our result
                // if it was a valid number result
                str_result += num;
                continue;
            } else {
                // any number not in range of numbers
                // will end the number token stream
                nextIsNumber = false;
            }
        }

        if(nextIsCapital) {
            c = c.toUpperCase();
            nextIsCapital = false;
        }

        str_result += c;
    }

    return str_result;
}

// check if the input is in english or braille
// does not handle trailing or prefixed space characters
// or other characters dirtying the input
let is_braille = isBraille(args);


let translated = is_braille ? convert_args_to_english() : convert_args_to_braille();

//output answer
process.stdout.write(translated);