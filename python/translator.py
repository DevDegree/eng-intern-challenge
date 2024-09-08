"""
This module contains the Python implementation of the Braille-English translator.

The translator console application can be used by running this file or externally through translator.main()
"""

# imports
import sys

# translation constants
BRAILLE_CHARACTER_LENGTH = 6
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

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


def translate_braille_to_english(braille: str) -> str:
    _setup_braille_to_english_translator()
    number_or_letter_selector = 0
    capital_follows_flag = False
    text = []

    for i in range(0, len(braille), BRAILLE_CHARACTER_LENGTH):
        letter = braille[i: i + BRAILLE_CHARACTER_LENGTH]

        if letter == NUMBER_FOLLOWS:
            number_or_letter_selector = 1

        elif letter == SPACE:
            text.append(' ')
            number_or_letter_selector = 0

        elif letter == CAPITAL_FOLLOWS:
            capital_follows_flag = True

        else:
            english_letter = ENGLISH_ALPHABET[letter][number_or_letter_selector]
            text.append(english_letter.upper() if capital_follows_flag else english_letter)
            capital_follows_flag = False

    return ''.join(text)


def translate_english_to_braille(text: str) -> str:
    return SPACE.join(map(_get_braille_word, text.split()))


def _get_braille_word(word: str) -> str:
    braille = []

    if numeric := word.isnumeric():
        braille.append(NUMBER_FOLLOWS)

    for char in word:
        if numeric:
            char = BRAILLE_NUMBER_EQUIVALENTS[char]
        elif char.isupper():
            braille.append(CAPITAL_FOLLOWS)
            char = char.lower()

        braille.append(BRAILLE_ALPHABET[char])

    return ''.join(braille)


def _setup_braille_to_english_translator() -> None:
    if not ENGLISH_ALPHABET:
        _init_braille_to_english_constants()


def _init_braille_to_english_constants() -> None:
    i = 1
    for english_letter, braille_letter in BRAILLE_ALPHABET.items():
        if i is not None:
            ENGLISH_ALPHABET[braille_letter] = (english_letter, str(i))
            i = (i + 1) % 10

            if i == 1:
                i = None
        else:
            ENGLISH_ALPHABET[braille_letter] = english_letter


def main():
    pass


if __name__ == '__main__':
    main()
