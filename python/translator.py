"""Code to translate English letters and numbers to Braille and vice versa"""

import sys

# Setting up constants
ENG_TO_BRAILLE = {
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

BRAILLE_TO_ENG = {v: k for k, v in ENG_TO_BRAILLE.items()}

NUMS_TO_BRAILLE = {
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

BRAILLE_TO_NUMS = {v: k for k, v in NUMS_TO_BRAILLE.items()}

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'


def is_braille(text):
    """Checks if input text is braille or english"""
    return all(char in "O." for char in text) and len(text) % 6 == 0


def translate_to_english(input_text):
    """Function to translate braille to english"""

    characters = []
    for i in range(0, len(input_text), 6):
        characters.append(input_text[i:i+6])

    output_text = ''
    is_capital = False
    is_number = False

    for char in characters:
        if char == SPACE:
            output_text = output_text + " "
            is_number = False
        elif char == CAPITAL_FOLLOWS:
            is_capital = True
        elif is_capital:
            output_text = output_text + BRAILLE_TO_ENG.get(char).upper()
            is_capital = False
        elif char == NUMBER_FOLLOWS:
            is_number = True
        elif is_number:
            output_text = output_text + BRAILLE_TO_NUMS.get(char)
        else:
            output_text = output_text + BRAILLE_TO_ENG.get(char)

    return output_text


def translate_to_braille(input_text):
    """Function to translate english to braille"""

    output_text = ''
    is_number = False

    for char in input_text:
        if char == " ":
            output_text = output_text + SPACE
            is_number = False
        elif char.isupper():
            output_text = output_text + CAPITAL_FOLLOWS + \
                ENG_TO_BRAILLE.get(char.lower())
        elif char.isdigit():
            if is_number:
                output_text = output_text + NUMS_TO_BRAILLE.get(char)
            else:
                is_number = True
                output_text = output_text + NUMBER_FOLLOWS + \
                    NUMS_TO_BRAILLE.get(char)
        else:
            output_text = output_text + ENG_TO_BRAILLE.get(char)

    return output_text


def main():
    """Main function that translates braille to english and vice versa"""

    if len(sys.argv) < 2:
        print("Not enough arguments\nUsage: python3 translator.py <input text here>")

    text = " ".join(sys.argv[1:])

    if is_braille(text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))


if __name__ == '__main__':
    main()
