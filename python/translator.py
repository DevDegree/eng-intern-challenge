'''
    Braille Translator:
    This command_line program takes a string and 
    determines if the string is either Braille or English
    and coverts it to the correct opposite
    Gavin Xu
    Aug 30, 2024
'''

import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    'capital_follows': '....O', 
    'decimal_follows': '.O...O', 
    'number_follows': '.O.OOO',

    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

BRAILLE_TO_ENGLISH = {val: key for key, val in ENGLISH_TO_BRAILLE.items()}

def determine_braille(text):
    '''
        Determine if the input text is braille or not
    '''
    braille_characters = ('.', 'O')
    if len(text) % 6:
        return False
    for c in text:
        if c not in braille_characters:
            return False
    return True




if __name__ == '__main__':
    text = 'hello world'
    text1 = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
    print(determine_braille(text))
    print(determine_braille(text1))