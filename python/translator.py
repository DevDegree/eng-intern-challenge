'''Shopify Eng Intern Challenge Fall - Winter 2025

Author: Azaria Kelman

File Description:
A command-line application to translate from English to Braille and vice versa.
'''
import sys

INPUT_TEXT = sys.argv[1:].join('')

ENGLISH_TO_BRAILLE = {
    # This dictionary maps English (+ numbers, commands) characters to their
    # corresponding Braille characters
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
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
}

CAPITAL_FOLLOWS = '.....O'  # Move to dict?
NUMBER_FOLLOWS = '.0.000'
# DECIMAL_FOLLOWS = '.0...0'
SPACE = '......'


def translate_language(input_text: str) -> bool:
    """Returns 1 to translate to English, 0 to translate to Braille"""
    for char in input_text:
        if char not in ['.', 'O']:
            return 0
    return 1


def translate_text_to_braille(input_text: str) -> str:
    """Returns the translated text"""
    new_string = ''
    for char in input_text:
        new_string += ENGLISH_TO_BRAILLE[char.upper()]


def translate_text_to_english(input_text: str) -> str:
    """Returns the translated text"""
    # Call divide_string_into_sections
    # Use the dictionary to translate each section, and append to string
    sections = divide_string_into_sections(input_text)
    new_string = ''
    for section in sections:
        for key, value in ENGLISH_TO_BRAILLE.items():
            if section == value:
                new_string += key


def divide_string_into_sections(input_text: str) -> list:
    """Returns a list of braille charachters"""
    sections = []
    for i in range(0, len(input_text), 6):
        section = input_text[i:i + 6]
        sections.append(section)
    return sections


if __name__ == '__main__':

    # import python_ta
    # python_ta.check_all(config={'allowed-import-modules': ["sys", "python_ta"]})

    if translate_language(INPUT_TEXT):
        print(translate_text_to_english(INPUT_TEXT))
    else:
        print(translate_text_to_braille(INPUT_TEXT))
