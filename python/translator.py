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
    'NUMBER_FOLLOWS': '.O.OOO',
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
    """
    Checks whether the input text is braille or not.

    Args:
        text: A list of input arguments.

    Returns:
        Whether the input text is braille or not.
    """
    chars_set = set()
    for word in text:
        for char in word:
            chars_set.add(char)
    if chars_set == {'O', '.'}:
        return True
    return False


def parse_braille(text: List[str]) -> None:
    """
    Prints the braille input text translated as alphabet characters.

    Args:
        text: A list of braille input arguments.
    """
    translated = ''

    for element in text:
        translated += parse_single_braille(element)

    print(translated)


def parse_single_braille(text: str) -> str:
    """
    Translates a single braille input text.

    Args:
        text: A string containing braille characters.

    Returns:
        Alphabet-translated text.
    """
    translated = ''
    capital_follows = False
    number_follows = False

    for char_start in range(0, len(text), 6):
        char_end = char_start + 6
        braille_char = text[char_start:char_end]
        alphabet = BRAILLE_TO_ALPHABET[braille_char]
        if alphabet == 'CAPITAL_FOLLOWS':
            capital_follows = True
            continue
        if alphabet == 'NUMBER_FOLLOWS':
            number_follows = True
            continue
        if alphabet == ' ':
            number_follows = False
        if capital_follows:
            alphabet = alphabet.upper()
            capital_follows = False
        if number_follows:
            number = ALPHABET_TO_NUMBERS[alphabet]
            alphabet = number
        translated += alphabet

    return translated


def parse_alphabet(text: List[str]) -> None:
    """
    Prints the alphabet input text translated as braille characters.

    Args:
        text: A list of alphabet input arguments.
    """
    translated = ''

    for i, word in enumerate(text):
        translated += parse_single_alphabet_word(word=word)
        if i < len(text) - 1:
            translated += ALPHABET_TO_BRAILLE[' ']

    print(translated)


def parse_single_alphabet_word(word: str) -> str:
    """
    Translates a single alphabet input word.

    Args:
        word: A string containing alphabet characters.

    Returns:
        Braille-translated word.
    """
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
