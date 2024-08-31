import sys

SPACE = 'space'
CAPITAL = 'capital'
NUMBER = 'number'

SPACE_CHAR = ' '

text_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    'capital': '.....O',
    'number': '.O.OOO',
    'space': '......',
}
nums_to_braille = {
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
braille_to_text = {v: k for k, v in text_to_braille.items()}
braille_to_numbers = {v: k for k, v in nums_to_braille.items()}


def check_braille_valid(user_input):
    """
    Checks if the given Braille string is valid.

    A valid Braille string must:
    - Have a length that is a multiple of 6
    - Contain only the characters 'O' and '.'

    Args:
    - user_input (str): The Braille string to be validated.

    Returns:
    - bool: True if the Braille string is valid, False otherwise.
    """
    if len(user_input) % 6 == 0 and all(char in "O." for char in user_input):
        return True
    return False


def english_to_braille(english_string):
    """
    Converts an English string into its Braille representation.

    The function handles:
    - Conversion of alphabetic characters to Braille.
    - Conversion of numeric characters to Braille, with proper handling of the number indicator.
    - Conversion of spaces to Braille.

    Args:
    - english_string (str): The English text to be converted to Braille.

    Returns:
    - str: The Braille representation of the input English string.
    """
    res = ""
    is_num = False
    for char in english_string:
        if char.isalpha():
            if char.isupper():
                res += text_to_braille[CAPITAL]
            res += text_to_braille[char.lower()]
        elif char.isdigit():
            if not is_num:
                res += text_to_braille[NUMBER]
                is_num = True
            res += nums_to_braille[char]
        elif char == SPACE_CHAR:
            is_num = False
            res += text_to_braille[SPACE]
        else:
            res += text_to_braille[char]

    return res


def braille_to_english(braille_string):
    """
    Converts a Braille string into its English representation.

    The function handles:
    - Conversion of Braille characters to their corresponding English letters.
    - Handling of special Braille indicators for capital and numbers.
    - Proper handling of spaces.

    Args:
    - braille_string (str): The Braille text to be converted to English.

    Returns:
    - str: The English representation of the input Braille string.
    """
    res = ""
    is_capital = False
    is_number = False
    for i in range(0, len(braille_string), 6):
        braille_cell = braille_string[i:i + 6]
        strs = braille_to_text.get(braille_cell, "")
        if strs == CAPITAL:
            is_capital = True
            continue
        elif strs == NUMBER:
            is_number = True
            continue
        elif strs == SPACE:
            res += SPACE_CHAR
            is_number = False
            continue

        if is_number:
            num = braille_to_numbers.get(braille_cell, "")
            res += num
        elif is_capital:
            res += strs.upper()
            is_capital = False
        else:
            res += strs

    return res


def process_input(args):
    """
    Processes the command-line input and determines whether to convert
    a Braille string to English or an English string to Braille.

    Args:
    - args (list): List of command-line arguments

    Returns:
    - None: The function prints the result directly and exits the script if input is invalid.
    """

    if len(args) < 2:
        print("Python Script.py, invalid input")
        sys.exit(1)

    user_input = args[1:]

    if check_braille_valid(user_input[0]):

        print(braille_to_english(user_input[0]))
    else:
        english_string = " ".join(user_input)
        print(english_to_braille(english_string))


if __name__ == "__main__":
    process_input(sys.argv)
