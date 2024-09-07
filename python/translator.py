import sys
from enum import Enum

# Define symbols for special Braille cases
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"


class TranslationMode(Enum):
    BRAILLE_TO_ENGLISH = 0
    ENGLISH_TO_BRAILLE = 1


class Dictionaries:
    # Define Braille alphabet for English translation
    braille_to_letter = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
    }

    braille_to_number = {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
    }

    # Reverse mappings for English to Braille translations
    letter_to_braille = {v: k for k, v in braille_to_letter.items()}
    number_to_braille = {v: k for k, v in braille_to_number.items()}


def determine_translation_mode(string_input: str) -> TranslationMode:
    """
    Determines the translation mode based on the characters in the input string.
    If the string contains only 'O', '.', or ' ', the translation mode is 'braille-to-english', otherwise it is 'english-to-braille'.

    Args:
        string_input (str): Input string to determine the translation mode.

    Returns:
        str: 'braille-to-english' if string only contains Braille characters, otherwise 'english-to-braille'
    """

    is_braille = all(c in ["O", ".", " "] for c in string_input)
    return (
        TranslationMode.BRAILLE_TO_ENGLISH
        if is_braille
        else TranslationMode.ENGLISH_TO_BRAILLE
    )


def braille_to_english(braille_string: str) -> str:
    """
    Translates Braille text into English text.

    Args:
        braille_string (str): Braille text to be translated into English.

    Returns:
        str: English translation of the given Braille text.
    """

    translated_string = []
    i = 0
    is_number_mode = False  # Flag to indicate next char is number
    is_capital = False  # Flag to indicate next char is capital

    # Loop over input Braille string in groups of 6 chars
    while i < len(braille_string):
        current_char = braille_string[i : i + 6]

        # Handle space
        if current_char == SPACE:
            translated_string.append(" ")
            is_number_mode = False
        # Handle capital letter
        elif current_char == CAPITAL_FOLLOWS:
            is_capital = True
            is_number_mode = False
        # Handle number
        elif current_char == NUMBER_FOLLOWS:
            is_number_mode = True
        # Handle regular Braille translation
        else:
            if is_number_mode:
                translated_string.append(Dictionaries.braille_to_number[current_char])
            elif is_capital:
                translated_string.append(
                    Dictionaries.braille_to_letter[current_char].upper()
                )
                is_capital = False
            else:
                translated_string.append(Dictionaries.braille_to_letter[current_char])

        i += 6  # Read next char

    return "".join(translated_string)


def english_to_braille(english_string: str) -> str:
    """
    Translates Englis text into Braille text.

    Args:
        english_string (str): English text to be translated into Braille.

    Returns:
        str: Braille translation of the given English text.
    """

    translated_string = []
    is_number_mode = False  # Flag to indicate when to add NUMBER_FOLLOWS symbol

    # Loop over input English string by character
    for char in english_string:
        # Handle space
        if char == " ":
            translated_string.append(SPACE)
            is_number_mode = False
        # Handle number
        elif char.isdigit():
            if not is_number_mode:
                translated_string.append(NUMBER_FOLLOWS)
                is_number_mode = True
            translated_string.append(Dictionaries.number_to_braille[char])
        # Handle letter
        else:
            # Handle capitalization
            if char.isupper():
                translated_string.append(CAPITAL_FOLLOWS)
                char = char.lower()  # Convert to lowercase for Braille lookup
                is_number_mode = False
            translated_string.append(Dictionaries.letter_to_braille[char])

    return "".join(translated_string)


if __name__ == "__main__":
    # Get command line args as one string
    string_input = sys.argv[1:]
    combined_imput = " ".join(string_input)
    translation_mode = determine_translation_mode(combined_imput)

    # Translate input based on detected mode
    if translation_mode == TranslationMode.BRAILLE_TO_ENGLISH:
        result = braille_to_english(combined_imput)
    else:
        result = english_to_braille(combined_imput)

    print(result)
