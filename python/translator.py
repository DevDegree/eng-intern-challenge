# --------------- IMPORT STATEMENTS --------------- #
import sys

# --------------- DICTIONARY --------------- #
DICT = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..', 
    'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 
    'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO', 
    'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO',  '.': '..OO.O', ',': '..0...',
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

ACTIONS = {
    'capital_follows': '.....O', 'number_follows': '.O.OOO'
}


# --------------- FUNCTIONS --------------- #
def is_braille(string):
    """
    Parameters:
    string (str): String to be checked.

    Returns:
    True if string is braille (only contains '.' or 'O')
    False if string is text
    """
    for i in string:
        if i not in ('.', 'O'):
            return False
    return True


def convert_to_braille(text):
    """
    Parameters: text (str): text to be converted to braille.

    Returns: braille string
    """
    output = ""
    for i in range(0, len(text)):
        char = text[i]

        # Add 'capital follows' symbol if character is uppercase
        if char.isupper():
            output += ACTIONS['capital_follows']
            output += add_symbol(char)

        # Add 'number follows' if character is number
        # Assumes all following characters are numbers until next space symbol
        elif char.isnumeric():
            if i <= 0:
                output += ACTIONS['number_follows']
                output += add_symbol(char)
            else:
                prev_char = text[i - 1]
                if prev_char.isnumeric():
                    output += add_symbol(char)
                else:
                    output += ACTIONS['number_follows']
                    output += add_symbol(char)
        else:
            output += add_symbol(char)

    print(output)


def add_symbol(char):
    """
    Parameters: char (char): Character to be added to output string.

    Returns: 6-character braille symbol for character
    """
    if char.islower():
        return DICT[char.upper()]
    elif char.isnumeric():
        return NUMBERS[char]
    else:
        return DICT[char]


def convert_to_text(braille):
    """
    Parameters: braille (str): braille to be converted to text.

    Returns: Text string
    """
    output = ""
    # Convert braille string to list of braille symbols (6 characters each)
    output_list = [braille[char: char + 6] for char in range(0, len(braille), 6)]
    action_list = [symbol for a, symbol in ACTIONS.items()]

    for i in range(0, len(output_list)):
        item = output_list[i]

        # Replace symbols for actions with action names
        if item in action_list:
            action = list(ACTIONS.keys())[list(ACTIONS.values()).index(item)]
            output_list[i] = action
        else:
            item = output_list[i]
            prev_item = output_list[i - 1]
            # Check if previous symbol was 'capital_follows'
            if prev_item == 'capital_follows':
                output += get_char(item, DICT)

            # Check if previous symbol was 'number_follows'
            # Replace current value in list with 'number_follows' so next character pulls from number list
            elif prev_item == 'number_follows':
                if item == '......':
                    output += get_char(item, DICT)
                else:
                    output += get_char(item, NUMBERS)
                    output_list[i] = 'number_follows'

            else:
                output += get_char(item, DICT).lower()
    print(output)


def get_char(symbol, dictionary):
    """
    Parameters:
    symbol (str): Braille symbol to be converted to character
    dictionary (str): Name of dictionary to search for symbol

    Returns: character
    """
    i = list(dictionary.values()).index(symbol)
    char = list(dictionary.keys())[i]
    return char


# --------------- PROGRAM --------------- #
input_string = " ".join(sys.argv[1:])

# Braille to text conversion
if is_braille(input_string):
    convert_to_text(input_string)

# Text to braille conversion
else:
    convert_to_braille(input_string)
