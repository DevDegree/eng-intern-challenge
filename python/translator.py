'''Shopify Eng Intern Challenge Fall - Winter 2025

Author: Azaria Kelman

File Description:
A command-line application to translate from English to Braille and vice versa.
'''
import sys

INPUT_TEXT = sys.argv[1:]

ENGLISH_TO_BRAILLE = {
    # This dictionary maps English (+ numbers) characters to their correspondent
    # Braille characters
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
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
}


def translate_language(input_text: str) -> bool:
    """Returns 1 to translate to English, 0 to translate to Braille"""
    for char in input_text:
        if char not in ['.', 'O']:
            return 0
    return 1


def translate_text_to_braille() -> str:
    """Returns the translated text"""
    pass


def translate_text_to_english() -> str:
    """Returns the translated text"""
    # Call divide_string_into_sections
    # Use the dictionary to translate each section, and append to string
    pass


def divide_string_into_sections(input_text: str) -> list:
    """Returns a list of braille charachters"""
    sections = []
    for i in range(0, len(input_text), 6):
        section = input_text[i:i + 6]
        sections.append(section)
    return sections


if __name__ == '__main__':

    import python_ta
    python_ta.check_all(config={'allowed-import-modules': ["sys", "python_ta"]})

    if translate_language(INPUT_TEXT):
        print(translate_text_to_english())
    else:
        print(translate_text_to_braille())
