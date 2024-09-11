import sys
from constants import *


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input>")
        sys.exit(1)

    input_str = sys.argv[1:len(sys.argv)]
    input_str = " ".join(input_str)

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))


def is_braille(s: str):
    for c in s:
        if c not in [".", "O"]:
            return False
    return True


def translate_to_english(s: str):
    if len(s) % 6 != 0:
        return "Invalid input: length of braille string should be a multiple of 6"

    # Split the string into sequences of 6 characters
    braille_cells = [s[i:i+6] for i in range(0, len(s), 6)]

    # Translate each sequence to a letter, checking for special sequences
    english = ""

    # Special state variables
    cap = False
    num = False

    for cell in braille_cells:
        if cell == CAPITAL:
            # Following cells are capitalized until next space
            cap = True

        elif cell == NUMBER:
            # Next cell is a number
            num = True

        elif cell == SPACE:
            # Next cell is a space
            english += " "
            cap = False
            num = False

        else:
            # Translate the cell to a letter
            english += get_char(cell, cap, num)
            cap = False

    return english


def get_char(cell: str, cap: bool, num: bool):
    if num:
        return BRAILLE_TO_NUMBER[cell]
    elif cap:
        return BRAILLE_TO_LETTER[cell].upper()
    else:
        return BRAILLE_TO_LETTER[cell]


def translate_to_braille(s: str):
    braille = ""

    # Special state variables
    num = False

    for c in s:
        if c.isnumeric() and not num:
            # First number in sequence
            num = True
            braille += NUMBER + NUMBER_TO_BRAILLE[c]

        elif num:
            # Number
            braille += NUMBER_TO_BRAILLE[c]

        elif c.isupper():
            # Capital letter
            braille += CAPITAL + LETTER_TO_BRAILLE[c.lower()]

        elif c == " ":
            # Space
            braille += SPACE
            num = False

        else:
            try:
                # Translate the character to braille
                braille += LETTER_TO_BRAILLE[c]
            except KeyError:
                # Character is not in the dictionary
                exit(f"Invalid input: character '{c}' is not supported")

    return braille


if __name__ == "__main__":
    main()
