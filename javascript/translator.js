// 1. Define mappings for English to Braille and Braille to English
// 2. Implement a function to detect if input is Braille or English
// 3. Implement a function to translate English to Braille
// 4. Implement a function to translate Braille to English
// 5. Get the input string
// 6. Detect input type and call appropriate translation function
// 7. Output the translated string in terminal

const brailleMap = {
    'a': 'o.....',
    'b': 'o.o....',
    'c': 'oo.....',
    'd': 'oo.o...',
    'e': 'o..o...',
    'f': 'ooo....',
    'g': 'oooo...',
    'h': 'o.oo...',
    'i': '.oo....',
    'j': '.ooo...',
    'k': 'o...o..',
    'l': 'o.o.o..',
    'm': 'oo..o..',
    'n': 'oo.oo..',
    'o': 'o..oo..',
    'p': 'ooo.o..',
    'q': 'ooooo..',
    'r': 'o.ooo..',
    's': '.oo.o..',
    't': '.oooo..',
    'u': 'o...oo.',
    'v': 'o.o.oo.',
    'w': '.ooo.o.',
    'x': 'oo..oo.',
    'y': 'oo.ooo.',
    'z': 'o..ooo.',
    '1': 'o.....',
    '2': 'o.o....',
    '3': 'oo.....',
    '4': 'oo.o...',
    '5': 'o..o...',
    '6': 'ooo....',
    '7': 'oooo...',
    '8': 'o.oo...',
    '9': '.oo....',
    '0': '.ooo...',
    'capital': '.....o',
    'number': '.o.ooo',
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

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));