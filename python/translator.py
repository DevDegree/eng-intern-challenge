"""A command-line application that can translate Braille to English and vice versa."""

import sys
from typing import List

ALPHABET_TO_BRAILLE = {
    ' ': '......',
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
    'CAPITAL_FOLLOWS': '.....O',
    'DECIMAL_FOLLOWS': '.O...O',
    'NUMBER_FOLLOWS': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

BRAILLE_TO_ALPHABET = {braille: alphabet for alphabet, braille in ALPHABET_TO_BRAILLE.items()}

ALPHABET_TO_NUMBERS = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0',
}

NUMBERS_TO_ALPHABET = {number: alphabet for alphabet, number in ALPHABET_TO_NUMBERS.items()}

def check_is_braille(text: List[str]) -> bool:
    chars_set = set()
    for word in text:
        for char in word:
            chars_set.add(char)
    if chars_set == {'O', '.'}:
        return True
    return False


def parse_braille(text: List[str]) -> None:
    translated = ''

    for element in text:
        translated += parse_single_braille(element)

    print(translated)


def parse_single_braille(text: str) -> str:
    translated = ''
    return translated


def parse_alphabet(text: List[str]) -> None:
    translated = ''

    for i, word in enumerate(text):
        translated += parse_single_alphabet_word(word=word)
        if i < len(text) - 1:
            translated += ALPHABET_TO_BRAILLE[' ']

    print(translated)


def parse_single_alphabet_word(word: str) -> str:
    translated = ''
    is_number = False

    for char in word:
        if char.isdigit() and not is_number:
            translated += ALPHABET_TO_BRAILLE['NUMBER_FOLLOWS']
            is_number = True
        if char.isdigit():
            alphabet = NUMBERS_TO_ALPHABET[char]
            translated += ALPHABET_TO_BRAILLE[alphabet]
        else:
            if char.isupper():
                translated += ALPHABET_TO_BRAILLE['CAPITAL_FOLLOWS']
                char = char.lower()
            translated += ALPHABET_TO_BRAILLE[char]

    return translated


def main():
    if len(sys.argv) < 2:
        print(f'Usage: python translator.py <braille|alphabet>')
        exit(1)

    text = sys.argv[1:]
    is_braille = check_is_braille(text=text)

    if is_braille:
        parse_braille(text=text)
    else:
        parse_alphabet(text=text)


if __name__ == '__main__':
    main()

