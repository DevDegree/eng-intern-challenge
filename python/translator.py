'''Shopify Eng Intern Challenge Fall - Winter 2025

Author: Azaria Kelman
Contact: azaria.kelman@mail.utoronto.ca

File Description:
A command-line application to translate from English to Braille and vice versa.
This application supports numbers, letters and spaces.
'''
import sys
import argparse

ENGLISH_TO_BRAILLE = {
    # This dictionary maps English characters to their
    # corresponding Braille characters
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
    ' ': '......'  # Space
}

NUMBERS_TO_BRAILLE = {
    # This dictionary maps numbers to their
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
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}  # Reverses dictionary
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}  # Reverses dictionary

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'


def translate_language(input_text: str) -> bool:
    """Returns 1 to translate to English, 0 to translate to Braille"""
    for char in input_text:
        if char not in ['.', 'O']:
            return 0
    return 1


def translate_text_to_braille(input_text: str) -> str:
    """Returns the text translated from English to Braille"""
    new_string = ''
    for char in input_text:
        if char.isupper():
            new_string += CAPITAL_FOLLOWS
        elif char.isdigit():
            new_string += NUMBER_FOLLOWS
        else:
            new_string += ENGLISH_TO_BRAILLE[char.upper()]
    return new_string


def translate_text_to_english(input_text: str) -> str:
    """Returns the text translated from Braille to English"""
    # Call divide_string_into_sections
    # Use the dictionary to translate each section, and append to string
    sections = divide_string_into_sections(input_text)
    new_string = ''
    next_capital = False
    next_number = False

    for section in sections:
        if section == CAPITAL_FOLLOWS:
            next_capital = True
        elif section == NUMBER_FOLLOWS:
            next_number = True
        elif section in BRAILLE_TO_ENGLISH:
            if next_capital:
                new_string += BRAILLE_TO_ENGLISH[section].upper()
                next_capital = False
            elif next_number:
                new_string += BRAILLE_TO_NUMBERS[section]
                next_number = False
            else:
                new_string += BRAILLE_TO_ENGLISH[section].lower()
        else:
            raise ValueError('Invalid Braille character')  # Just in case

    return new_string


def divide_string_into_sections(input_text: str) -> list:
    """Returns a list of braille charachters"""
    sections = []
    for i in range(0, len(input_text), 6):
        section = input_text[i:i + 6]
        sections.append(section)
    return sections


def main() -> None:
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('input_text')
    INPUT_TEXT = parser.parse_args().input_text

    if translate_language(INPUT_TEXT):
        print(translate_text_to_english(INPUT_TEXT))
    else:
        print(translate_text_to_braille(INPUT_TEXT))


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'allowed-import-modules': ["sys", "python_ta", 'argparse']})
    main()
