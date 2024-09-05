"""
This module contains the Python implementation of the Braille-English translator.

The translator console application can be used by running this file or externally through translator.main()
"""

# imports
import sys

# translation constants
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

# a dictionary of braille symbols
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# a dictionary of number-letter symbol relationships
BRAILLE_NUMBER_EQUIVALENTS = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

# derived constants
ENGLISH_ALPHABET = {}

i = 1
for english_letter, braille_letter in BRAILLE_ALPHABET:
    if i is not None:
        ENGLISH_ALPHABET[braille_letter] = (english_letter, i)
        i = (i + 1) % 10

        if i == 1:
            i = None
    else:
        ENGLISH_ALPHABET[braille_letter] = english_letter


def translate_braille_to_english(braille: str) -> str:
    pass


def translate_english_to_braille(text: str) -> str:
    pass


def _get_braille(char: str) -> str:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
