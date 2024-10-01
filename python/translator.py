import sys

# Define mappings
alphabet_to_braille = {
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

number_to_braille = {
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

braille_to_alphabet = {v: k for k, v in alphabet_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

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



def braille_to_english(str):
    """
    Convert a Braille string to English text.

    :param str: A string representing the Braille input, where each character is represented by a 6-digit Braille code.
    :return: A string containing the translated English text.
    """

    length = len(str)
    english_out = ""
    is_number = False
    for i in range(0, len(str), 6):
        braille_char = str[i:i + 6]
        if braille_char == str['space']:
            english_out += ' '
            is_number = False
        elif braille_char == str['capital']:
            i += 6
            braille_char = str[i:i + 6]
            english_out += braille_to_alphabet.get(braille_char, '?').upper()
        elif braille_char == special_dict['number']:
            is_number = True
        else:
            if is_number:
                english_out += braille_to_number.get(braille_char, '?')
            else:
                english_out += braille_to_alphabet.get(braille_char, '?')
    return english_out



def english_to_braille(str):
    """
    Convert a Braille string to English text.

    :param str: A string representing the Braille input, where each character is represented by a 6-digit Braille code.
    :return: A string containing the translated English text.
    """


def main():
    # Raise error if lenght of input less than 2
    if len(sys.argv) < 2:
        print('Error: Not sufficient argument to translate')
        sys.exit(1)

    input_str = sys.argv[1]

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


if __name__ == "__main__":
    main()

