import sys

braille = {
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
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO',
    '.': '..OO.O',
    ',': '..O.OO',
    '!': '..OOO.',
    ':': '..O.O.',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

# Defining some functions!
def check_braille(string):
    '''Check if given string is a braille text'''
    symbols = {'.', 'O'}
    if len(string) % 6 != 0:
        return False
    for char in string:
        if char not in symbols:
            return False
    return True

# for value in braille.values():
#     assert check_braille(value)

# Skipping file name
text = sys.argv[1:]

# Passed argument is English, to be translated into braille
if len(text) > 1 or check_braille(value) is False:
    for char in text.join(' '):
        if char.isupper():
            sys.stdout.write(braille[capital_follows])
            sys.stdout.write(braille[char])
            sys.stdout.flush()
        else:
            sys.stdout.write(braille[char])

# Passed argument is a braille text, to be translated into English
else:
    print('test')
