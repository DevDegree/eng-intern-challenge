# Python version 3.8
import sys

# Braille encoding for English letters and numbers
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

inverse_braille_alphabet = {
    v: k for k, v in braille_alphabet.items()
}

def is_braille(input_str: str):
    return all(char in 'O.' for char in input_str)

def translate_to_braille(input_str: str):
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit() and not number_mode:
            result.append(braille_alphabet['num'])
            number_mode = True
        elif char.isalpha() and char.isupper():
            result.append(braille_alphabet['cap'])
            char = char.lower()
        elif char == ' ':
            number_mode = False
        result.append(braille_alphabet.get(char, ''))
    return ''.join(result)
