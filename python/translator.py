import sys
from constants import *
from typing import Union


def is_braille(s: str) -> bool:
    """
    Checks whether a given string is braille (only consisting of 'O' and '.')

    Parameters:
        s: A string possibly containing braille characters
    """
    return all(char in {'O', '.'} for char in s)

def is_english(s: str) -> bool:
    """
    Checks whether a string consists of only English characters

    Parameters:
        s: A string possibly containing english text
    """
    s = s.lower()

    # Union both sets of valid characters and numbers as well as a blank space into a joint set for fast lookup
    valid_chars = set(ENGLISH_TO_BRAILLE.keys()) | set(NUMBERS_TO_BRAILLE.keys()) | set(' ')
    return all([char in valid_chars for char in s])

def convert_braille_to_english(braille_str: str) -> Union[str, None]:
    """
    Converts a given braille string into an english representation.

    Parameters:
        braille_str (str): A string containing braille characters

    Returns:
        A string containing an english representation of braille_str or None
        if the string is badly formatted.
    """
    res = ''
    capitalize = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i: i + 6]

        if braille_char == CAPITAL_FOLLOWS:
            capitalize = True
        elif braille_char == NUMBER_FOLLOWS:
            is_number = True
        elif braille_char == SPACE:
            res += ' '
            is_number = False

        elif braille_char in BRAILLE_TO_ENGLISH:
            if is_number:
                res += BRAILLE_TO_NUMBERS[braille_char]
            elif capitalize:
                res += BRAILLE_TO_ENGLISH[braille_char].upper()
                capitalize = False
            else:
                res += BRAILLE_TO_ENGLISH[braille_char]
        # Invalid character detected
        else:
            return 

    return res

def convert_english_to_braille(english_str: str) -> Union[str, None]:
    """
    Converts an english string into a braille representation.

    Parameters:
        english_str (str): A string containing english characters

    Returns:
        A string containing a braille representation of english_str or None if 
        the string is badly formatted.
    """
    res = ''
    is_number = False
    for char in english_str:
        if char.isdigit():
            if not is_number:
                res += NUMBER_FOLLOWS + NUMBERS_TO_BRAILLE[char]
                is_number = True
            else:
                res += NUMBERS_TO_BRAILLE[char]
        elif char == ' ':
            res += SPACE
            is_number = False
        else:
            # If no space is detected before we reach an alphabetic character, we have an error (according to our rules)
            if is_number:
                return
            elif char.isupper():
                # If we have an uppercase letter, add the control sequence along with the braille representation
                res += CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.lower()]
            else:
                res += ENGLISH_TO_BRAILLE[char]
    return res

def translate(input: str) -> Union[str, None] :
    """
    A wrapper for translating between braille and english.

    Returns the correctly formatted string depending on whether
    the input is in braille or english and None if the string is
    incorrectly formatted.
    """

    if is_braille(input) and len(input) % 6 == 0:
        return convert_braille_to_english(input)
    elif is_english(input):
        return convert_english_to_braille(input)
    return None

if __name__ == '__main__':
    num_args = len(sys.argv)
    # Ensure that at least one string is entered into the command line
    if num_args > 1:
        input_str = ' '.join(sys.argv[1:])

        res = translate(input_str)
        if not res:
            print("Incorrectly formatted string")
        print(res)
