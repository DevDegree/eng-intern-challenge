import sys

# Braille dictionary (alphabet -> braille)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',  # Capitalization leadd
    'num': '.O.OOO',  # New number lead
}

# Reverse mapping of Braille to English
english_dict = {b: e for e, b in braille_dict.items()}

number_braille_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OOO...': '4', 'O..O..': '5',
    'OO.O..': '6', 'OOO.O.': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

num_to_braille = {b: e for e, b in number_braille_dict.items()}


def is_braille(input_string : str) -> bool:
    # Check if the input is in Braille or not
    for char in input_string:
        if char != 'O' and char != '.' and char != ' ':
            return False
    return True


def translate(input_string : str) -> str:
    # TODO: Implement this function
    return ""


if __name__ == 'main':
    input_string = sys.argv[1]
    print(translate(input_string))