import sys

from enum import Enum

from mapper.braille_to_english_mapper import *
from mapper.english_to_braille_mapper import *


class SpecialConstant(Enum):
    NUM_FOLLOW = "NUM_FOLLOW"
    CAPITAL_FOLLOW = "CAPITAL_FOLLOW"
    WHITESPACE = " "


def is_braille(input_word):
    """Check if the input string is a valid Braille representation.

    Args:
    input_word (str): The string to check.

    Returns:
    bool: True if all characters are Braille dots or spaces, False otherwise.
    """
    return all(char in "O." for char in input_word)


def translate_english_to_braille(input_word):
    """Translate an English phrase into Braille.

    Args:
    input_word (str): The English phrase to translate.

    Returns:
    str: The Braille representation of the input phrase.
    """

    braille_output = ""
    numeric_flag = False
    for letter in input_word:
        # Check if the letter is numeric
        if letter.isnumeric() and letter in NUMBERS_TO_BRAILLE_MAPPING:
            if not numeric_flag:
                numeric_flag = True
                braille_output += ENGLISH_TO_BRAILLE_MAPPING.get(SpecialConstant.NUM_FOLLOW.value)
            braille_output += NUMBERS_TO_BRAILLE_MAPPING.get(letter)

        elif letter.isspace():
            if numeric_flag:
                numeric_flag = False
            braille_output += ENGLISH_TO_BRAILLE_MAPPING.get(letter)

        elif letter.lower() in ENGLISH_TO_BRAILLE_MAPPING:
            if letter.isupper():
                braille_output += ENGLISH_TO_BRAILLE_MAPPING.get(SpecialConstant.CAPITAL_FOLLOW.value)
            braille_output += ENGLISH_TO_BRAILLE_MAPPING.get(letter.lower())

    return braille_output


def translate_braille_to_english(input_word):
    """Translate a Braille representation into English.

    Args:
    input_word (str): The Braille input to translate.

    Returns:
    str: The English representation of the Braille input.
    """

    english_output = ""
    capital_flag = False
    numeric_flag = False
    str_length = len(input_word)

    for index in range(0, str_length, 6):
        braille_sequence = input_word[index:index + 6]

        if BRAILLE_TO_ENGLISH_MAPPING.get(braille_sequence) == SpecialConstant.CAPITAL_FOLLOW.value:
            capital_flag = True

        elif BRAILLE_TO_ENGLISH_MAPPING.get(braille_sequence) == SpecialConstant.NUM_FOLLOW.value:
            numeric_flag = True

        elif BRAILLE_TO_ENGLISH_MAPPING.get(braille_sequence) == SpecialConstant.WHITESPACE.value:
            numeric_flag = False
            english_output += BRAILLE_TO_ENGLISH_MAPPING.get(braille_sequence)

        else:
            if numeric_flag:
                english_output += BRAILLE_TO_NUMBERS_MAPPING.get(braille_sequence)
            else:
                eng_char = BRAILLE_TO_ENGLISH_MAPPING.get(braille_sequence)
                if capital_flag:
                    english_output += eng_char.upper()
                    capital_flag = False
                else:
                    english_output += eng_char

    return english_output


def translate_input(words):
    """Determine if the input is Braille or English and perform the translation.

    Args:
    words (list[str]): The list of words or Braille sequences to translate.
    """
    input_str = ' '.join(words)
    if is_braille(input_str):
        if len(input_str) % 6 != 0:
            print("Please enter valid braille input")
            return
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))


def main():
    """
    Main function to handle command-line
    input and initiate translation.
    """

    # Check if user has provided any Phrase to translate
    if len(sys.argv) > 1:
        translate_input(sys.argv[1:])
    else:
        print("Enter a Phrase to be translated")


if __name__ == "__main__":
    main()
