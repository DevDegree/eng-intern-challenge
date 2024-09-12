""""A Braile translator CLI app"""

import sys

"""
Dictionary to translate English to Braile.
A Braille symbol is a 6-char string reading from left to right, line by line, starting at the top left.
Image for ref at /braille.jpg

a `O` represents a raised dot and a `.` represent an unraised dot.
"""
english_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO',
    '.': '..OO.O', "'": '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..OO..', '-': '....OO', '/': '.O..O.', '<': '.O..O.', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

"""Dictionary to translate Braile to English."""
braille_to_english_dict = {
    # Same Braille symbol for both letter and digit (ex: 'a' and '1')
    'O.....': {'letter': 'a', 'number': '1'},
    'O.O...': {'letter': 'b', 'number': '2'},
    'OO....': {'letter': 'c', 'number': '3'},
    'OO.O..': {'letter': 'd', 'number': '4'},
    'O..O..': {'letter': 'e', 'number': '5'},
    'OOO...': {'letter': 'f', 'number': '6'},
    'OOOO..': {'letter': 'g', 'number': '7'},
    'O.OO..': {'letter': 'h', 'number': '8'},
    '.OO...': {'letter': 'i', 'number': '9'},
    '.OOO..': {'letter': 'j', 'number': '0'},

    # No number equivalent for these Braille symbols
    'O...O.': {'letter': 'k'},
    'O.O.O.': {'letter': 'l'},
    'OO..O.': {'letter': 'm'},
    'OO.OO.': {'letter': 'n'},
    'O..OO.': {'letter': 'o'},
    'OOO.O.': {'letter': 'p'},
    'OOOOO.': {'letter': 'q'},
    'O.OOO.': {'letter': 'r'},
    '.OO.O.': {'letter': 's'},
    '.OOOO.': {'letter': 't'},
    'O...OO': {'letter': 'u'},
    'O.O.OO': {'letter': 'v'},
    '.OOO.O': {'letter': 'w'},
    'OO..OO': {'letter': 'x'},
    'OO.OOO': {'letter': 'y'},
    'O..OOO': {'letter': 'z'},

    # Control symbols:
    'cap': '.....O',
    'num': '.O.OOO',
    'dec': '.O...O',

    # Punctuation:
    '.': '..OO.O',
    "'": '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..OO..',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}


def is_braille(input_string):
    """Check if the input string contains only 'O' and '.'."""
    return all(c in 'O.' for c in input_string)


def translate_to_braille(english_string):
    """Translate English to Braille"""
    result = []
    in_number_mode = False

    for char in english_string:
        # Handle uppercase letters
        if char.isupper():
            result.append(english_to_braille_dict['cap'])  # cap follows indicator
            result.append(english_to_braille_dict[char.lower()])

        # Handle digits (numbers)
        elif char.isdigit():
            if not in_number_mode:  # add num indicator before first number
                result.append(english_to_braille_dict['num'])  # num follows indicator
                in_number_mode = True
            result.append(english_to_braille_dict[char])

        # Handle decimal point (in numbers)
        elif char == '.':
            result.append(english_to_braille_dict['dec'])  # dec follows indicator
            result.append(english_to_braille_dict['.'])
            in_number_mode = True  # cont number mode

        # Handle spaces and reset number mode
        elif char == ' ':
            result.append(english_to_braille_dict[' '])
            in_number_mode = False  # Reset number mode after a space

        # Handle lowercase letters
        else:
            result.append(english_to_braille_dict[char])
            in_number_mode = False

    return ''.join(result)


def translate_to_english(braille_string):
    """Translate Braille to English."""
    result = []
    is_capital = False
    is_number = False

    # Process the string in chunks of 6 characters (Braille symbols are 6 dots long)
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        # Handle capital follows indicator
        if braille_char == english_to_braille_dict['cap']:
            is_capital = True
            continue

        # Handle number follows indicator
        elif braille_char == english_to_braille_dict['num']:
            is_number = True
            continue

        # Handle space
        elif braille_char == '......':
            result.append(' ')
            is_number = False  # Reset number mode after space
            continue

        # Get the letter or number based on the current mode
        if braille_char in braille_to_english_dict:
            if is_number:
                result.append(braille_to_english_dict[braille_char]['number'])
            else:
                letter = braille_to_english_dict[braille_char]['letter']
                if is_capital:
                    result.append(letter.upper())
                    is_capital = False  # Reset capital mode after one letter
                else:
                    result.append(letter)

    return ''.join(result)


def main():
    """
    Runs the Braille translator CLI app.

    Accepts a string and translates it between English and Braille based on the input format.
    If the input is in Braille, it translates to English; if in English, it translates to Braille.

    To run the application from the terminal:
    python3 translator.py <string>
    """
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    # Collect all arguments after the script name and join them as a single input string
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()

