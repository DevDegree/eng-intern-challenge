"""
    Braille to English dictionary where braille strings are matched to arrays of letters/symbols/numbers.
    As per instructions this includes only a-z, 0-9, spaces, and symbols required to support their full implementation.
    Braille symbols may have several modes (standard, uppercase, numerical) which have been assigned
    to distinct indices within each array. Note as well that all braille keys must have 6 symbols consisting
    of only '.' and 'O'
"""
STANDARD_DEF = 0
UPPER = 1
NUM = 2
BR_SIZE = 6

b_to_e = {
    'O.....':['a', 'A', '1'], 'O.O...':['b', 'B', '2'], 'OO....':['c', 'C', '3'], 'OO.O..':['d', 'D','4'],
    'O..O..':['e', 'E', '5'], 'OOO...':['f', 'F', '6'], 'OOOO..':['g', 'G', '7'], 'O.OO..':['h', 'H', '8'],
    '.OO...':['i', 'I', '9'], '.OOO..':['j', 'J', '0'], 'O...O.':['k', 'K'], 'O.O.O.':['l', 'L'], 'OO..O.':['m', 'M'],
    'OO.OO.':['n', 'N'], 'O..OO.':['o', 'O'], 'OOO.O.':['p', 'P'], 'OOOOO.':['q', 'Q'], 'O.OOO.':['r', 'R'],
    '.OO.O.':['s', 'S'], '.OOOO.':['t', 'T'], 'O...OO':['u', 'U'], 'O.O.OO':['v', 'V'], '.OOO.O':['w', 'W'],
    'OO..OO':['x', 'X'], 'OO.OOO':['y', 'Y'], 'O..OOO':['z', 'Z'], '.....O':['CAP FOLLOWS'],
    '.O.OOO':['NUM FOLLOWS'], '......':[' ']
}
"""
    English to Braille dictionary matching letters (lower and upper case) and numbers to braille strings.
    Additionally, strings to capture capital letters, indicate numbers, and the space symbol are contained as well
"""
e_to_b = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..',
    'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.',
    'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
    'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    ' ': '......', 'CAP FOLLOWS': '.....O', 'NUM FOLLOWS': '.O.OOO'
}


