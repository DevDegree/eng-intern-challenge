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
    'CAPITAL': '.....O',
    'DECIMAL': '.O...O',
    'NUMBER': '.O.OOO',
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

BRAILLE_ALPHABET_TO_NUMBERS = {
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

BRAILLE_TO_ALPHABET = {braille: alphabet for alphabet, braille in ALPHABET_TO_BRAILLE.items()}


def check_is_braille(text: List[str]) -> bool:
    chars_set = set()
    for word in text:
        for char in word:
            chars_set.add(char)
    if chars_set == {'O', '.'}:
        return True
    return False


def parse_braille(text: List[str]) -> None:
    translated = ""

    print(translated)


def parse_alphabet(text: List[str]) -> None:
    translated = ""

    print(translated)


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
