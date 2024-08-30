ALPHABET = {
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

PUNCTUATION = {
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
}

NUMBERS = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

BRAILLE_ALPHABET = dict((reversed(item) for item in ALPHABET.items()))
BRAILLE_NUMBERS = dict((reversed(item) for item in NUMBERS.items()))
BRAILLE_PUNCTUATION = dict((reversed(item) for item in PUNCTUATION.items()))

UPPERCASE = '.....O'
DECIMAL = '.O...O'
NUMBER = '.O.OOO'

BRAILLE = {'O', '.'}

'''
Converts a given braille string to english
'''
def braille_to_english(text: str) -> str:
    res = ''
    number = False
    upper = False

    for i in range(0, len(text), 6):
        braille = text[i: i+6]

        if braille == NUMBER:
            number = True
        elif braille == UPPERCASE:
            upper = True
        elif number:
            if braille == PUNCTUATION[' ']:
                number = False
                res += ' '
            elif braille == DECIMAL:
                continue
            elif braille == PUNCTUATION['.']:
                res += '.'
            else:
                res += BRAILLE_NUMBERS[braille]
        elif braille in BRAILLE_ALPHABET:
            res += BRAILLE_ALPHABET[braille].upper() if upper else BRAILLE_ALPHABET[braille]
            upper = False
        elif braille in BRAILLE_PUNCTUATION:
            res += BRAILLE_PUNCTUATION[braille]

    return res

'''
Converts a given english string to braille
'''
def english_to_braille(text: str) -> str:
    res = ''
    number = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                res += UPPERCASE
            res += ALPHABET[char.lower()]
        elif char in NUMBERS:
            if not number:
                number = True
                res += NUMBER

            res += NUMBERS[char]
        elif char in PUNCTUATION:
            if char == ' ' and number:
                number = False
            if char == '.' and number:
                res += DECIMAL

            res += PUNCTUATION[char]

    return res

if __name__ == '__main__':
    import sys
    args = sys.argv
    args.pop(0)

    text = ' '.join(args)
    chars = set(text)

    res = braille_to_english(text) if chars == BRAILLE else english_to_braille(text)

    print(res)