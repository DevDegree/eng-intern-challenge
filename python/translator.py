braille_dict = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Indicators
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',

    # Special characters
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'

}

def is_braille (text):
    """
        Checks if the input string is a Braille representation.
        Args:
            text (str): The string to check.
        Returns:
            bool: True if the input string consists only of 'O' and '.'
    """
    return all(char in ['O', '.'] for char in text)

def is_english(text):
    """
        Checks if the input string is an English text.
        Args:
            text (str): The string to check.
        Returns:
            bool: True if the input string contains any alphanumeric characters or spaces
        """
    return any(char.isalnum() or char.isspace() for char in text)


def translate_to_braille(english_text):
    """
    Translates English text or numbers to Braille, handling numbers, capitalization, and decimals.

    Args:
        english_text (str): The English text or numbers to translate.
    Returns:
        str: The corresponding Braille translation.
    """
    braille_translation = []
    is_number = False
    i = 0

    while i < len(english_text):
        char = english_text[i]

        if char.isdigit():
            if i + 1 < len(english_text) and english_text[i + 1] == '.':
                # If the second character is a '.' then it is considered as a decimal
                braille_translation.append(braille_dict['decimal'])
                # Add the rest of the characters
                while i < len(english_text) and english_text[i].isdigit():
                    braille_translation.append(braille_dict[english_text[i]])
                    i += 1
                i += 1  # Skip the decimal point
                continue
            else:
                if not is_number:
                    braille_translation.append(braille_dict['number'])
                    is_number = True
                braille_translation.append(braille_dict[char])

        elif char.isalpha():

            if char.isupper():
                braille_translation.append(braille_dict['capital'])
                braille_translation.append(braille_dict[char.lower()])
            else:
                braille_translation.append(braille_dict[char])
            is_number = False

        elif char in braille_dict:

            braille_translation.append(braille_dict[char])
            is_number = False

        i += 1

    return ''.join(braille_translation)


