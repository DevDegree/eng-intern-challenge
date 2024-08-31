BRAILLE_MAPPING = {
    'a': 'O.....', 'b': 'OO....', 'c': 'O..O..', 
    'd': 'O..OO.', 'e': 'O...O.', 'f': 'OO.O..', 
    'g': 'OO.OO.', 'h': 'OO..O.', 'i': '.O.O..', 
    'j': '.O.OO.', 'k': 'O.O...', 'l': 'OOO...', 
    'm': 'O.OO..', 'n': 'O.OOO.', 'o': 'O.O.O.', 
    'p': 'OOOO..', 'q': 'OOOOO.', 'r': 'OOO.O.', 
    's': '.OOO..', 't': '.OOOO.', 'u': 'O.O..O', 
    'v': 'OOO..O', 'w': '.O.OOO', 'x': 'O.OO.O', 
    'y': 'O.OOOO', 'z': 'O.O.OO',

    '1': 'O.....', '2': 'OO....', '3': 'O..O..', 
    '4': 'O..OO.', '5': 'O...O.', '6': 'OO.O..', 
    '7': 'OO.OO.', '8': 'OO..O.', '9': '.O.O..', 
    '0': '.O.OO.',

    'CAPITAL': '.....O',
    'NUMBER': '..OOOO',
    'SPACE': '......'
}

REVERSE_MAPPING = {v: k for k, v in BRAILLE_MAPPING.items()}