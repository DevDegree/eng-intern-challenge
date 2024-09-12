BRAILLE = {
    # letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',

    # nums
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # special chars
    'caps': '.....O', 'num': '.O.OOO', ' ': '......', '.': '..O.OO', ',': '..O...',
    '?': '..OO.O', '!': '..OOO.', ':': '..OO..', ';': 'O.OO..', '-': '....O.',
    '/': '.O..O.', '<': '.O..OO', '>': 'OO..O.', '(': '.O.OO.', ')': '.O.OOO'
}

char_dict = {value: key for key, value in BRAILLE.items() if key.isalpha()}
num_dict = {value: key for key, value in BRAILLE.items() if key.isdigit()}
special_char_dict = {value: key for key, value in BRAILLE.items() if not key.isalpha() and not key.isdigit()}
