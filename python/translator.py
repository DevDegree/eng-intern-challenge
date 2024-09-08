"""
This module contains the Python implementation of the Braille-English translator.

The translator console application can be used by running this file or externally through translator.main()
"""

# imports
import sys

# translation constants
BRAILLE_CHARACTER_LENGTH = 6
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

# a dictionary of braille symbols
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# a dictionary of number-letter symbol relationships
BRAILLE_NUMBER_EQUIVALENTS = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

# derived constants
ENGLISH_ALPHABET = {}
BRAILLE_NUMBERS = set()


def translate_braille_to_english(braille: str) -> str:
    """
    Translate a braille string to English characters.

    Precondition that braille arg is a valid braille string.

    :param braille: a string of braille characters represented as 6 character strings of Os and .s
    :return: the translated text as an English character string
    """

    _set_up_braille_to_english_translator()
    number_or_letter_selector = 0
    capital_follows_flag = False
    text = []

    for i in range(0, len(braille), BRAILLE_CHARACTER_LENGTH):
        letter = braille[i: i + BRAILLE_CHARACTER_LENGTH]

        if letter == NUMBER_FOLLOWS:
            number_or_letter_selector = 1

        elif letter == SPACE:
            text.append(' ')
            number_or_letter_selector = 0

        elif letter == CAPITAL_FOLLOWS:
            capital_follows_flag = True

        else:
            english_letter = ENGLISH_ALPHABET[letter][number_or_letter_selector]
            text.append(english_letter.upper() if capital_follows_flag else english_letter)
            capital_follows_flag = False

    return ''.join(text)


def translate_english_to_braille(text: str) -> str:
    """
    Translate a text string to braille characters.

    :param text: a string of English characters
    :return: the translated text as a braille string
    """

    braille = []
    number = [NUMBER_FOLLOWS]

    for char in text:
        if char.isnumeric():
            number.append(BRAILLE_ALPHABET[BRAILLE_NUMBER_EQUIVALENTS[char]])

        else:
            if len(number) > 1:
                braille += number
                number = [number[0]]  # reset number to its original state

            if char == ' ':
                braille.append(SPACE)

            else:
                if char.isupper():
                    braille.append(CAPITAL_FOLLOWS)
                    char = char.lower()

                braille.append(BRAILLE_ALPHABET[char])

    if len(number) > 1:
        braille += number  # account for trailing numbers at the end of the string

    return ''.join(braille)


def _set_up_braille_to_english_translator() -> None:
    """
    Set up all derived constants required to translate braille to english.

    Lazy initialisation to only allocate memory if the functionality is required.
    """

    if not ENGLISH_ALPHABET:
        _init_braille_to_english_constants()


def _init_braille_to_english_constants() -> None:
    """
    Initialise ENGLISH_ALPHABET derived constant.
    """

    i = 1
    for english_letter, braille_letter in BRAILLE_ALPHABET.items():
        if i is not None:
            ENGLISH_ALPHABET[braille_letter] = (english_letter, str(i))
            i = (i + 1) % 10

            if i == 1:
                i = None
        else:
            ENGLISH_ALPHABET[braille_letter] = english_letter


def _set_up_braille_verification_constants() -> None:
    """
    Set up all derived constants required to verify a potential braille string.
    """

    if not BRAILLE_NUMBERS:
        for letter in BRAILLE_NUMBER_EQUIVALENTS.values():
            BRAILLE_NUMBERS.add(BRAILLE_ALPHABET[letter])


def _verify_braille_text(text: str) -> bool:
    """
    Check if a string is a valid braille string.

    :return: True if the string is braille, False otherwise
    """

    if len(text) % 6 != 0:
        return False

    _set_up_braille_verification_constants()
    number_follows_flag = False
    braille_symbols = set(BRAILLE_ALPHABET.values()).union({NUMBER_FOLLOWS, CAPITAL_FOLLOWS, SPACE})

    for i in range(0, len(text), BRAILLE_CHARACTER_LENGTH):
        letter = text[i: i + BRAILLE_CHARACTER_LENGTH]

        if letter not in braille_symbols:
            return False

        if letter == SPACE:
            number_follows_flag = False

        else:
            if number_follows_flag and letter not in BRAILLE_NUMBERS:
                # if the character between a "number follows" and space is not a number
                return False

            number_follows_flag = number_follows_flag or (letter == NUMBER_FOLLOWS)

    return True


def main() -> str:
    """
    Run the main translator application.

    The console application takes as input 1 or more space separated strings
    and prints the translation to standard output.

    :return: the translated string
    """

    if len(sys.argv) > 1:
        # only process if arguments are supplied to the program
        arg_string = ' '.join(sys.argv[1:])

        if _verify_braille_text(arg_string):
            translated_text = translate_braille_to_english(arg_string)

        else:
            # assume if the argument string is not braille then translate it from english
            translated_text = translate_english_to_braille(arg_string)

        print(translated_text, end='')
        return translated_text


if __name__ == '__main__':
    main()
