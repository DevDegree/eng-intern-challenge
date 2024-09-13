ENGLISH_TO_BRAILLE_ALPHABET = {
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
    'z': 'O..OOO'
}

CAPITAL_FOLLOWS = 'CAPITAL_FOLLOWS'
NUMBER_FOLLOWS = 'NUMBER_FOLLOWS'

ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS = {
    'CAPITAL_FOLLOWS': '.....O', 
    'NUMBER_FOLLOWS': '.O.OOO',

    '.': '..OO.O', 
    "'": '..O...', 
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
    ' ': '......'
}

ENGLISH_TO_BRAILLE_DIGITS = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..',
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..'
}

BRAILLE_TO_ENGLISH_DIGITS = { v: k for k, v in ENGLISH_TO_BRAILLE_DIGITS.items() } 
BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS = { v: k for k, v in ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS.items() } 
BRAILLE_TO_ENGLISH_ALPHABET = { v: k for k, v in ENGLISH_TO_BRAILLE_ALPHABET.items() } 

# The below constants are used to create a set of valid characters that can be used in an English string
ENGLISH_ALPHABET_LOWERCASE_KEYS_SET = set(ENGLISH_TO_BRAILLE_ALPHABET.keys())
ENGLISH_ALPHABET_UPPERCASE_KEYS_SET = {letter.upper() for letter in ENGLISH_ALPHABET_LOWERCASE_KEYS_SET}
ENGLISH_DIGITS_KEYS_SET = set(ENGLISH_TO_BRAILLE_DIGITS.keys())
ENGLISH_SPECIAL_CHARACTERS_KEYS_SET = set(ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS.keys())

VALID_CHARACTER_SET = ( ENGLISH_ALPHABET_LOWERCASE_KEYS_SET | 
                        ENGLISH_ALPHABET_UPPERCASE_KEYS_SET | 
                        ENGLISH_SPECIAL_CHARACTERS_KEYS_SET | 
                        ENGLISH_DIGITS_KEYS_SET )

BRAILLE_CHARACTER_LENGTH = 6