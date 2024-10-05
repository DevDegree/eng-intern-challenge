'''Shopify Eng Intern Challenge Fall - Winter 2025

Author: Azaria Kelman
Contact: azaria.kelman@mail.utoronto.ca

File Description:
A command-line application to translate from English to Braille and vice versa.
This application supports numbers, letters and spaces.
'''
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

# Reverses dictionaries
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

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
    next_number = False  # Flag to check if next character is a number

    for char in input_text:
        if char.isupper():
            new_string += CAPITAL_FOLLOWS
            new_string += ENGLISH_TO_BRAILLE[char]
            next_number = False
        elif char.isdigit():
            if not next_number:  # If not already in number mode
                new_string += NUMBER_FOLLOWS
            new_string += NUMBERS_TO_BRAILLE[char]
            next_number = True
        elif char.islower():
            new_string += ENGLISH_TO_BRAILLE[char.upper()]
            next_number = False
        elif char == ' ':
            new_string += ENGLISH_TO_BRAILLE[char]
            next_number = False
        else:
            raise ValueError('Invalid English character')  # Just in case
    return new_string


def translate_text_to_english(input_text: str) -> str:
    """Returns the text translated from Braille to English"""
    # Call divide_string_into_sections
    # Use the dictionary to translate each section, and append to string
    sections = divide_string_into_sections(input_text)
    new_string = ''
    next_capital = False  # Flag to check if next char is capital
    next_number = False

    for section in sections:
        if section == CAPITAL_FOLLOWS:
            next_capital = True  # Update flags
        elif section == NUMBER_FOLLOWS:
            next_number = True
        elif section in BRAILLE_TO_ENGLISH or section in BRAILLE_TO_NUMBERS:
            if next_capital:
                new_string += BRAILLE_TO_ENGLISH[section].upper()
                next_capital = False
            elif next_number:
                new_string += BRAILLE_TO_NUMBERS[section]
            else:
                if BRAILLE_TO_ENGLISH[section] == ' ':  # If section is space
                    next_number = False
                new_string += BRAILLE_TO_ENGLISH[section].lower()
        else:
            raise ValueError('Invalid Braille character')  # Just in case

    return new_string


def divide_string_into_sections(input_text: str) -> list:
    """Returns a list of 6 char long braille tokens"""
    sections = []
    for i in range(0, len(input_text), 6):
        section = input_text[i:i + 6]
        sections.append(section)
    return sections


def main() -> None:
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Translate English to Braille and vice versa')
    parser.add_argument('input_text', nargs='+',
                        help='Text to translate', type=str)
    input_text = parser.parse_args().input_text  # Retreives input text

    input_text = ' '.join(input_text)

    if translate_language(input_text):  # Translation
        print(translate_text_to_english(input_text))
    else:
        print(translate_text_to_braille(input_text))


if __name__ == '__main__':
    main()
