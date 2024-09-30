#!/usr/bin/env python3

import sys

BRAILLE_DICT = {
    'O.....': ['A', '1'], 'O.O...': ['B', '2'], 'OO....': ['C', '3'], 'OO.O..': ['D', '4'],
    'O..O..': ['E', '5'], 'OOO...': ['F', '6'], 'OOOO..': ['G', '7'], 'O.OO..': ['H', '8'],
    '.OO...': ['I', '9'], '.OOO..': ['J', '0'], 'O...O.': ['K'], 'O.O.O.': ['L'], 'OO..O.': ['M'],
    'OO.OO.': ['N'], 'O..OO.': ['O', '>'], 'OOO.O.': ['P'], 'OOOOO.': ['Q'], 'O.OOO.': ['R'],
    '.OO.O.': ['S'], '.OOOO.': ['T'], 'O...OO': ['U'], 'O.O.OO': ['V'], '.OOO.O': ['W'],
    'OO..OO': ['X'], 'OO.OOO': ['Y'], 'O..OOO': ['Z'], '......': [' '], '.....O': ['capital_follows'],
    '.O.OOO': ['number_follows'], '.O...O': ['decimal_point'],
    # Symbols
    '..OO.O': ['.'], '..O...': [','], '..O.OO': ['?'], '..OOO.': ['!'], '..OO..': [':'],
    '..O.O.': [';'], '....OO': ['-'], '.O..O.': ['/'], '.OO..O': ['<'], 'O.O..O': ['('],
    '.O.OO.': [')']
}

ENG_TO_BRAILLE = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......', 'capital_follows': '.....O',
    'number_follows': '.O.OOO',
    'decimal_point': '.O...O',
    # Numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    # Symbols
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}


def braille_to_eng(braille):
    result = ""
    is_capital = False
    is_number = False
    i = 0
    while i < len(braille):
        char = braille[i:i + 6]
        if char == '.....O':  # Capital indicator
            is_capital = True
        elif char == '.O.OOO':  # Number indicator
            is_number = True
        elif char in BRAILLE_DICT:
            options = BRAILLE_DICT[char]
            if 'capital_follows' in options or 'number_follows' in options or 'decimal_point' in options:
                pass
            elif is_capital:
                result += options[0].upper()
                is_capital = False
                is_number = False
            elif is_number and len(options) > 1:
                result += options[1]  # Use the number if in number mode and number exists
            else:
                result += options[0].lower()
                is_number = False

            if char == '......':
                is_number = False
        i += 6
    return result


def eng_to_braille(text):
    result = ""
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                result += ENG_TO_BRAILLE['number_follows']
                is_number = True
            result += ENG_TO_BRAILLE[char]
        elif char.isalpha():
            if is_number:
                is_number = False
            if char.isupper():
                result += ENG_TO_BRAILLE['capital_follows']
            result += ENG_TO_BRAILLE.get(char.upper(), '')
        else:
            is_number = False
            result += ENG_TO_BRAILLE.get(char, '')
    return result

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_eng(input_string)
    else:
        return eng_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string), end='')
    else:
        print("Please provide a string to translate.")