import sys

# Dictionary (alphabet, numbers, special chars)
alphabet_dict = {
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

special_dict = {
    'number': '.O.OOO',
    'space' : '......',
    'capital' : '.....O'
}

numbers_dict = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

#
braille_to_alphabet = {v: k for k, v in alphabet_dict.items()}
braille_to_numbers = {v: k for k, v in numbers_dict.items()}

def is_braille(str):
    """
    Determines whether a given string represents Braille or English text.

    This function checks if the string contains only the characters '.' or 'O',
    and whether its length is a multiple of 6, a common characteristic of Braille
    encoded as a series of six-dot cells.

    :param str: The string to be checked.
    :return: True if the input is likely Braille, False otherwise.
    """
    # Early exit for empty strings or strings of lengths not multiple of 6
    if not str or len(str) % 6 != 0:
        return False

    # Check if all characters in the string are either '.' or 'O'
    return all(c in {'O', '.'} for c in str)


# Function to translate Braille to English



# Function to translate English to Braille