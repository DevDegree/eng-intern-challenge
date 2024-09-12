import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital follows', '.O.OOO': 'number follows'
}

# Reverse mapping from English to Braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Mapping from numbers to Braille
NUMBERS = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
           '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

# Special Braille characters
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'


def braille_to_english(braille):
    """
    Converts a string of Braille characters to English text.

    Args:
        braille (str): The input string containing Braille characters.

    Returns:
        str: The converted English text.
    """
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == CAPITAL_FOLLOWS:
            capitalize_next = True
        elif char == NUMBER_FOLLOWS:
            number_mode = True
        elif char in BRAILLE_TO_ENGLISH:
            if number_mode:
                if char == SPACE:
                    result.append(' ')
                    number_mode = False
                else:
                    result.append(convert_braille_number(char))
            else:
                result.append(convert_braille_letter(char, capitalize_next))
                capitalize_next = False
        i += 6

    return ''.join(result)


def convert_braille_number(char):
    """
    Converts a Braille character to its corresponding number.

    Args:
        char (str): The Braille character.

    Returns:
        str: The corresponding number.
    """
    for num, letter in NUMBERS.items():
        if BRAILLE_TO_ENGLISH[char] == letter:
            return num
    return ''


def convert_braille_letter(char, capitalize_next):
    """
    Converts a Braille character to its corresponding letter, with optional capitalization.

    Args:
        char (str): The Braille character.
        capitalize_next (bool): Whether to capitalize the letter.

    Returns:
        str: The corresponding letter.
    """
    letter = BRAILLE_TO_ENGLISH[char]
    if capitalize_next and letter != ' ':
        return letter.upper()
    return letter


def english_to_braille(text):
    """
    Translates English text to Braille.

    Args:
        text (str): The English text to be translated.

    Returns:
        str: The Braille translation of the English text.
    """
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_FOLLOWS)
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[NUMBERS[char]])
        else:
            if number_mode and char != ' ':
                number_mode = False
            if char.isupper():
                result.append(CAPITAL_FOLLOWS)
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            if char == ' ':
                number_mode = False

    return ''.join(result)


def translate(input_string):
    """
    Translates the given input string from English to Braille or from Braille to English.

    Args:
        input_string (str): The string to be translated.

    Returns:
        str: The translated string.
    """
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string))
