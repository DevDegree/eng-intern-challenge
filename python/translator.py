
# . -> dot, O -> raised dot

import sys

# braille -> letters
letter_braille_map = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}

# can be done with list comprehension, but kept for clarity
# number -> braille
number_braille_map = {
    '1' : letter_braille_map['a'],
    '2' : letter_braille_map['b'],
    '3' : letter_braille_map['c'],
    '4' : letter_braille_map['d'],
    '5' : letter_braille_map['e'],
    '6' : letter_braille_map['f'],
    '7' : letter_braille_map['g'],
    '8' : letter_braille_map['h'],
    '9' : letter_braille_map['i'],
    '0' : letter_braille_map['j']
}

# 0 -> capital follows, 1 -> number input until space
modifier_map = {
    '.....O' : 0,
    '.O.OOO' : 1 
}

# braille -> letter
braille_letter_map = { b : l for l, b in letter_braille_map.items()}

# braille -> number
braille_number_map = { b : n for n, b in number_braille_map.items()}

'''
checks if a given input string is in braille or not.
assuming all input is correct and something like "OOOOOO" is not given as input

TODO: check for multiple of 6, validate each chunk of 6 to see if it exists in braille library
'''
def is_braille(str):
    for c in str:
        if not (c in ['.', 'O']):
            return False
    return True

input_str = ' '.join(sys.argv[1:])

print(is_braille(input_str))