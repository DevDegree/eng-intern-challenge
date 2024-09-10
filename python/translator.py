"""
Author: Rithik Kalra
Contact: rkalra24@uwo.ca
Date Updated: 9/10/2024

Shopify Coding Assesment
"""

import re
import sys

# Define code maps for encoding english to braille and decoding braille to english
BRAILLE_TEXT_ENCODER = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

BRAILLE_NUM_ENCODER = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...'
}

BRAILLE_TEXT_DECODER = {val: key for key, val in BRAILLE_TEXT_ENCODER.items()}
BRAILLE_NUM_DECODER = {val: key for key, val in BRAILLE_NUM_ENCODER.items()}

CAPITAL_MODE = '.....O'
NUMBER_MODE = '.O.OOO'
SPACE = '......'


def is_braille(input_string: str) -> bool:
    """
    Determines whether a string is braille
    Args:
        input_string: String to be tested

    Returns: Boolean result

    """
    # Check the following condition: Braille text is a multiple of 6
    if not len(input_string) % 6 == 0:
        return False

    # Check the following condition: Braille text only consists of 'O' and '.' is met
    pattern = r'^[O.]+$'
    if not re.match(pattern, input_string):
        return False

    return True


def encode(input_string: str) -> str:
    """
    Encodes an english string into braille and returns the result
    Args:
        input_string: English string

    Returns: Braille string

    """
    # flags
    is_number = False

    encoded_string = []

    # Iterate over all characters in a string
    for char in input_string:

        if re.match(r'^\d+$', char) and not is_number:
            # set number flag
            is_number = True
            encoded_string.append(NUMBER_MODE)
            encoded_string.append(BRAILLE_NUM_ENCODER[char])
        elif char == ' ':
            # clear number flag
            is_number = False
            encoded_string.append(SPACE)
        else:
            # encode characters based on unique conditions
            if is_number:
                # encode a number to braille
                encoded_string.append(BRAILLE_NUM_ENCODER[char])
            elif char.isupper():
                # encode a capital letter to braille
                encoded_string.append(CAPITAL_MODE)
                encoded_string.append(BRAILLE_TEXT_ENCODER[char.lower()])
            else:
                # encode a default letter to braille
                encoded_string.append(BRAILLE_TEXT_ENCODER[char])

    return ''.join(encoded_string)


def decode(input_string: str) -> str:
    """
    Decodes a braille string to an english string and returns the result
    Args:
        input_string: Braille string

    Returns: English string

    """
    # flags
    is_capital = False
    is_number = False

    decoded_string = []

    # Iterate over segments of braille code with each segment consisting of 6 braille characters
    for i in range(0, len(input_string), 6):

        braille_char = input_string[i:i+6]

        if braille_char == CAPITAL_MODE:
            # set capital flag
            is_capital = True
        elif braille_char == NUMBER_MODE:
            # set number flag
            is_number = True
        elif braille_char == SPACE:
            # clear number flag
            is_number = False
            decoded_string.append(' ')
        else:
            # decode character based on unique conditions
            if is_number:
                # decode a number to english
                decoded_string.append(BRAILLE_NUM_DECODER[braille_char])
            elif is_capital:
                # decode a capital letter to english
                is_capital = False
                char = BRAILLE_TEXT_DECODER[braille_char]
                char.upper()
                decoded_string.append(char)
            else:
                # decode a default character to english
                decoded_string.append(BRAILLE_TEXT_DECODER[braille_char])

    return ''.join(decoded_string)


if __name__ == '__main__':
    # Retrieve arguments from command line and convert it to a single string
    arg_list = sys.argv[1:]
    input_str = ' '.join(arg_list)

    # Determine whether to encode or decode based on the type of string passed
    if is_braille(input_str):
        output_str = decode(input_str)
    else:
        output_str = encode(input_str)

    print(output_str)
