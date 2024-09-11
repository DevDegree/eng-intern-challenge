# Author: Clara Zhang
# Email: clara.z.dev@gmail.com


# Braille to English dictionary mapping
b2e = {
    # symbols
    '......': ' ',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',

    # letters
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',

    # decimal point
    '.O...O': ''
}


def isBrailleNumber(value):
    """Check if the Braille pattern represents the number indicator."""
    return value == '.O.OOO'


def isBrailleCapital(value):
    """Check if the Braille pattern represents the capital letter indicator."""
    return value == '.....O'


# Invert the Braille to English mapping to get an English to Braille dictionary
e2b = {v: k for k, v in b2e.items()}

# Add numeric Braille mappings (1-10 mapped to letters 'a'-'j')
for k in 'abcdefghij':
    e2b[str(ord(k) - ord('a') + 1)] = e2b[k]


brailleNumber = '.O.OOO'
brailleCapital = '.....O'