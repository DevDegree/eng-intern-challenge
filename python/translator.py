"""Assumptions:
1. The inputted english or braille will be in the form of grammatically correct english sentences. Meaning that words with combinations of letters and numbers won't be used. If there is a word like ABC123abc in braille, the translation into english will be ABC123123 since there is no braille escape pattern for number ended.
2. Since 'o' and '>' share the same braille pattern. I will be assuming that the sign is '>' only if it is surrounded by spaces. such as '50 > 70', otherwise it will assume the character to be o. Edge cases that will fail for this is if there is a word like <test>, it will be translated into <testo
3. Decimals can possibly not have a leading number and take either the form of .5 or 0.5
4. If the string is not valid for translation (insufficient cmd line arguments, non-english characters, braille length that isn't divisible by 6), the reason will be printed to the cmd line
"""

import sys
from typing import List

ENG_TO_BRAILLE = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "capital_next": ".....O",
    "decimal_next": ".O...O",
    "number_next": ".O.OOO",
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENG_TO_BRAILLE.items()}

BRAILLE_NUMBER_TO_LETTER_MAP = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j",
}

BRAILLE_LETTER_TO_NUMBER_MAP = {v: k for k, v in BRAILLE_NUMBER_TO_LETTER_MAP.items()}

ALLOWED_ENGLISH_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,?!:;-/<>() "
)

def english_to_braille(english_str: str) -> str:
    """
    Converts an english string into a braille string
      Parameters:
        english_str (str): A string containing english characters
      Returns:
        braille_str (str): The translated braille string
    """
    braille_str = ""
    is_number_next = False

    for i, char in enumerate(english_str):
        if char.isdigit():
            # if this is the start of a number
            if not is_number_next:
                braille_str += ENG_TO_BRAILLE["number_next"]
                is_number_next = True

            # get the corresponding letter for the digit
            char_num_map = BRAILLE_NUMBER_TO_LETTER_MAP[char]
            braille_str += ENG_TO_BRAILLE[char_num_map]
        elif char == ".":
            # will be assuming that decimals don't have to have a leading number
            # eg. decimal can be both .5 or 0.5

            # decimal point if theres a number up next
            if i < len(english_str) - 1 and english_str[i + 1].isdigit():
                is_number_next = True
                braille_str += ENG_TO_BRAILLE["decimal_next"]
            # regular period
            else:
                is_number_next = False
                braille_str += ENG_TO_BRAILLE["."]
        else:
            if is_number_next:
                is_number_next = False

            # add the uppercase braille if char is uppercase
            if char.isupper():
                braille_str += ENG_TO_BRAILLE["capital_next"]
                char = char.lower()

            braille_str += ENG_TO_BRAILLE.get(char)

    return braille_str


def braille_to_english(braille_str: str) -> str:
    """
    Converts a braille string into an english string
      Parameters:
        braille_str (str): A string containing only 'O' and '.' characters
      Returns:
        english_str (str): The translated english string
    """
    english_str = ""
    is_number_next = False
    is_capital_next = False
    braille_chunks = get_braille_chunks(braille_str)
    for i, chunk in enumerate(braille_chunks):
        # handle the next char cases
        if chunk == ENG_TO_BRAILLE["capital_next"]:
            is_capital_next = True
            continue
        elif chunk == ENG_TO_BRAILLE["number_next"]:
            is_number_next = True
            continue
        elif chunk == ENG_TO_BRAILLE["decimal_next"]:
            continue
        elif chunk == ENG_TO_BRAILLE["o"]:
            # logic for the edge case of o and > having the same braille pattern. See assumptions for more details.
            if is_capital_next:
                english_str += "O"
            elif (
                i - 1 > 0
                and i + 1 < len(braille_chunks) - 1
                and braille_chunks[i - 1] == ENG_TO_BRAILLE[" "]
                and braille_chunks[i + 1] == ENG_TO_BRAILLE[" "]
            ):
                english_str += ">"
            else:
                english_str += "o"
        else:
            char = BRAILLE_TO_ENGLISH.get(chunk)
            if is_number_next and char in BRAILLE_LETTER_TO_NUMBER_MAP.keys():
                char = BRAILLE_LETTER_TO_NUMBER_MAP[char]
            elif is_number_next and not char.isdigit():
                is_number_next = False
            elif is_capital_next:
                char = char.upper()
                is_capital_next = False

            english_str += char

    return english_str


def is_braille(s: str) -> bool:
    """
    Returns a boolean corresponding to whether the input string braille
      Parameters:
        s (str): A string of characters
      Returns:
        (bool): True if the sum of 'O's and '.'s is the same as the input string length else False
    """
    period_count = s.count(".")
    letter_O_count = s.count("O")
    return period_count + letter_O_count == len(s)


def is_valid_english(s: str) -> bool:
    for char in s:
        if char not in ALLOWED_ENGLISH_CHARS:
            return False
    return True


def get_braille_chunks(b: str) -> List[str]:
    """
    Return the 6 character chunks corresponding to an english character
      Parameters:
        b (str): a string that is assumed to be in braille
      Returns:
        chunks_array (List[str]): A list of 6 character strings
    """
    chunks_array = []
    for i in range(0, len(b), 6):
        chunk = b[i : i + 6]
        chunks_array.append(chunk)
    return chunks_array


def translator() -> None:
    """
    Main function that runs checks on the input string, translates it and prints it
      Args:
        args List[str]: Args from cmd line, index 0 is the script name and the rest are input words to be translated
      Returns:
        None: prints the translated string to cmd line
    """
    if len(sys.argv) <= 1:
        print("Insufficient cmd line arguments. Please provide a word to be translated when running the script")
        sys.exit(1)

    args_string = " ".join(sys.argv[1:])

    translate_to_braille = is_braille(args_string)

    translated_string = ""
    if translate_to_braille:
        # if the braille is not divisible by 6 then it is not valid
        if len(args_string) % 6 != 0:
            print("Invalid braille string - string is not divisible by 6")
            sys.exit(1)
        translated_string = braille_to_english(args_string)
    else:
        # check if the input string has non-english characters
        if not is_valid_english(args_string):
            print("The input has non-english characters")
            sys.exit(1)

        translated_string = english_to_braille(args_string)

    print(translated_string)

if __name__ == "__main__":
    translator()
