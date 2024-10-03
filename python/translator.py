"""This script is a create a terminal / command-line application 
that can translate Braille to English and vice versa."""

import sys


BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_DECIMAL_POINT = ".O...O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"

english_to_braille = {
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
    "?": "..OOO.",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    " ": "......",
}

braille_to_english = {}
for key, value in english_to_braille.items():
    braille_to_english[value] = key

braille_to_english[BRAILLE_DECIMAL_POINT] = "."


number_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

braille_to_number = {v: k for k, v in number_to_braille.items()}


def convert_to_braille(text):
    """Converts English to Braille"""

    is_first_number = True
    number_follows = False

    result = []
    for char in text:
        # Check to see if char is valid
        if char.lower() not in english_to_braille and char not in number_to_braille:
            print(
                "Invalid Input: Allowed characters are a-z, A-Z, 0-9, ',', "
                + "'<', '.', '>', '/', '?', ';', ':', '!', '-', '(', ')', or ' '"
            )
            return

        # Check if char is capital. If it is, add the special BRAILLE_CAPITAL_FOLLOWS and the char to result
        if char.isupper() and not number_follows:
            result.append(BRAILLE_CAPITAL_FOLLOWS)
            result.append(english_to_braille[char.lower()])

        # If we see a space that means number_follows should be False
        elif char == " ":
            is_first_number = True
            result.append(english_to_braille[char])
            number_follows = False
        elif char.isdigit():
            if is_first_number:
                result.append(BRAILLE_NUMBER_FOLLOWS)

                is_first_number = False

            result.append(number_to_braille[char])
            number_follows = True

        # Adds special BRAILLE_DECIMAL_POINT if a period appears while in a number
        elif char == "." and number_follows:
            # Prepend the decimal point with `.O...O` if inside a number
            result.append(BRAILLE_DECIMAL_POINT)
        else:
            result.append(english_to_braille[char])
            number_follows = False

    print("".join(result))


def convert_to_english(braille_string):
    """Converts Braille to English"""

    if 0 != (len(braille_string) % 6):
        print("Invalid Input: All braille characters must be 6 in length")
        return

    seperated_braille_array = []
    for i in range(0, len(braille_string), 6):
        seperated_braille_array.append(braille_string[i : i + 6])

    capital_follows = False
    number_follows = False

    result = []
    for char in seperated_braille_array:
        # Check to see if the char exists
        if (
            char not in braille_to_number
            and char not in braille_to_english
            and char != BRAILLE_CAPITAL_FOLLOWS
            and char != BRAILLE_NUMBER_FOLLOWS
            and char != BRAILLE_DECIMAL_POINT
        ):
            print("One or more braille characters are invalid")
            return

        if char == BRAILLE_CAPITAL_FOLLOWS:
            capital_follows = True
        elif char == BRAILLE_NUMBER_FOLLOWS:
            number_follows = True
        elif capital_follows:
            english_character = braille_to_english[char]
            result.append(english_character.upper())
            capital_follows = False
        elif char == "......":
            english_character = braille_to_english[char]
            result.append(english_character)
        elif number_follows and char in braille_to_number:
            english_number = braille_to_number[char]
            result.append(english_number)
        else:
            english_character = braille_to_english[char]
            result.append(english_character)

    print("".join(result))


def main():
    if 2 > len(sys.argv):
        print("Arguments passed were invalid")
        return

    input_str = " ".join(sys.argv[1:])

    # Improved detection for Braille vs English input
    if all(c in ["O", "."] for c in input_str):  # Braille only contains 'O' and '.'
        convert_to_english(input_str)
    else:
        convert_to_braille(input_str)


if __name__ == "__main__":
    main()
