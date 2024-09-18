import sys

ENGLISH_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
ENGLISH_NUMBERS = set('0123456789')
ENGLISH_CHARACTERS = ENGLISH_LETTERS.union(ENGLISH_NUMBERS)

BRAILLE_CHARACTERS = set('O.')

CAPITAL_FOLLOWS = 'CAPITAL_FOLLOWS'
DECIMAL_FOLLOWS = 'DECIMAL_FOLLOWS'
NUMBER_FOLLLOWS = 'NUMBER_FOLLLOWS'
SPACE = 'SPACE'

BRAILLE_ALPHABET_SYMBOLS = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    CAPITAL_FOLLOWS: '.....O',
    DECIMAL_FOLLOWS: '.O...O',
    NUMBER_FOLLLOWS: '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OO.O',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    SPACE: '......',
}

BRAILLE_NUMBERS_SYMBOLS = {
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
}

def is_english(text):
    for word in text:
        if not set(word.lower()).issubset(ENGLISH_CHARACTERS):
            return False
    return True

def is_braille(text):
    if len(text) != 1:
        return False
    if not set(text[0]).issubset(BRAILLE_CHARACTERS):
        return False
    return True

def translate_to_braille(english_text):
    does_number_follows = False

    output = ''
    for char in ' '.join(english_text):
        if char not in ENGLISH_LETTERS and char.lower() in ENGLISH_LETTERS:
            output += BRAILLE_ALPHABET_SYMBOLS[CAPITAL_FOLLOWS]
            output += BRAILLE_ALPHABET_SYMBOLS[char]
        elif char in ENGLISH_NUMBERS:
            if not does_number_follows:
                does_number_follows = True
                output += BRAILLE_ALPHABET_SYMBOLS[NUMBER_FOLLLOWS]
            output += BRAILLE_NUMBERS_SYMBOLS[char]
        elif char == ' ':
            does_number_follows = False
            output += BRAILLE_ALPHABET_SYMBOLS[SPACE]
        else:
            output += BRAILLE_ALPHABET_SYMBOLS[char.upper()]

    return output

def translate_to_english(text):
    # TODO: Implement translate to English
    pass

def translate(text):
    if is_english(text):
        return translate_to_braille(text)
    elif is_braille(text):
        return translate_to_english(text)

if __name__ == "__main__":
    argvs = sys.argv
    text = argvs[1:]

    print(text)
    print(translate(text))