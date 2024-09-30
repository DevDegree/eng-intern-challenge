
// lookup table

const braille_lut = {
    'a': 'o.....',
    'b': 'o.o...',
    'c': 'oo....',
    'd': 'oo.o..',
    'e': 'o..o..',
    'f': 'ooo...',
    'g': 'oooo..',
    'h': 'o.oo..',
    'i': '.oo...',
    'j': '.ooo..',
    'k': 'o...o.',
    'l': 'o.o.o.',
    'm': 'oo..o.',
    'n': 'oo.oo.',
    'o': 'o..oo.',
    'p': 'ooo.o.',
    'q': 'ooooo.',
    'r': 'o.ooo.',
    's': '.oo.o.',
    't': '.oooo.',
    'u': 'o...oo',
    'v': 'o.o.oo',
    'w': '.ooo.o',
    'x': 'oo..oo',
    'y': 'oo.ooo',
    'z': 'o..ooo',
    '1': '0.....',
    '2': '0.0...',
    '3': '00....',
    '4': '00.0..',
    '5': '0..0..',
    '6': '000...',
    '7': '0000..',
    '8': '0.00..',
    '9': '.00...',
    '0': '.000..',
    // special commands
    'CAPITAL': '.....o',
    'DECIMAL': '.o...o',
    'NUMBER': '.o.ooo',
    '.': '..oo.o',
    ',': '..o...',
    '?': '..o.oo',
    '!': '..ooo.',
    ':': '..oo..',
    ';': '..o.o.',
    '-': '....oo',
    '/': '.o..o.',
    '<': '.oo..o',
    '>': 'o..oo.',
    '(': 'o.o..o',
    ')': '.o.oo.',
    ' ': '......',
};

// a couple helpers

// Fetch the braille value from lut with a fallback to empty str
const get_braille = (char) => braille_lut[char] || '';

// check if char is am ascii digit
function isDigit(char) {
    return char >= '0' && char <= '9'; // Checks if the character is within the ASCII range for digits
}

// get the args
const args = process.argv.slice(2);
// console.log('Arguments:', args);

let str_result = '';

for (arg of args) {
    // keep track of number runs
    let wasLastADigit = false;
    for(c of arg) {
        let lowerchar = c.toLowerCase();
        // console.log(lowerchar);

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
   
}
console.log(str_result);