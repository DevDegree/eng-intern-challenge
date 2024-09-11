
import sys

# --- Mappings ---
CHAR_TO_BRAILLE = {
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
}

DIGIT_TO_BRAILLE = {
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

BRAILLE_TO_TEXT = {v: k for k, v in CHAR_TO_BRAILLE.items()}
BRAILLE_TO_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}

UPPERCASE_SIGN = ".....O"
NUMERAL_SIGN = ".O.OOO"
SPACE = "......"

# --- Utilities ---


def is_plaintext(input_str: str) -> bool:
    """
    Determines if the input string is plain text or Braille. 
    It checks if the input contains periods, which are indicative of Braille dot patterns. 
    Returns True for plain text and False for Braille.

    Examples:
    >>> is_plaintext("hello")
    True
    >>> is_plaintext("O.....")
    False
    """

    return "." not in input_str


def text_to_braille(input_str: str) -> str:
    """
    Converts a given plain text string into Braille, including handling uppercase letters and numbers. 
    Uppercase letters are prefixed with a special Braille indicator, and numbers switch to a numeric mode. 
    Spaces are maintained as well, ensuring correct Braille translation.

    Examples:
    >>> text_to_braille("Hello 1")
    '.....O.OO....O.OOOO..... .O.OOOO.....'
    >>> text_to_braille("abc")
    'O.....O.O...OO....'
    """

    braille_rep = ""
    number_mode = False

    for character in input_str:
        if character.isalpha():
            if character.isupper():
                braille_rep += UPPERCASE_SIGN
            braille_rep += CHAR_TO_BRAILLE[character.lower()]
        elif character.isdigit():
            if not number_mode:
                number_mode = True
                braille_rep += NUMERAL_SIGN
            braille_rep += DIGIT_TO_BRAILLE[character]
        elif character == " ":
            braille_rep += SPACE
            number_mode = False
    return braille_rep


def braille_to_text(input_str: str) -> str:
    """
    Translates a Braille string back to plain text, supporting letters, numbers, and capitalization. 
    It processes 6-character segments and adjusts for numeric and capitalization modes based on Braille indicators. 
    The function restores spaces and ensures that uppercase letters are correctly converted.

    Examples:
    >>> braille_to_text('.....O.OO....O.OOOO..... .O.OOOO.....')
    'Hello 1'
    >>> braille_to_text('O.....O.O...OO....')
    'abc'
    """

    segments = [input_str[i:i+6] for i in range(0, len(input_str), 6)]
    plain_text = ""
    uppercase_flag = False
    number_flag = False

    for segment in segments:
        if segment == UPPERCASE_SIGN:
            uppercase_flag = True
        elif segment == NUMERAL_SIGN:
            number_flag = True
        elif segment == SPACE:
            plain_text += " "
            number_flag = False
        elif number_flag:
            plain_text += BRAILLE_TO_DIGIT[segment]
        elif uppercase_flag:
            plain_text += BRAILLE_TO_TEXT[segment].upper()
            uppercase_flag = False
        else:
            plain_text += BRAILLE_TO_TEXT[segment]

    return plain_text


def run():
    assert len(sys.argv) >= 2
    inputs = sys.argv[1:]
    input_str = ' '.join(inputs)

    if is_plaintext(input_str):
        print(text_to_braille(input_str))
    else:
        print(braille_to_text(input_str))


if __name__ == "__main__":
    run()
