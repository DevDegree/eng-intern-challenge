import sys
from typing import List

CAPITAL = "capital follows"
DECIMAL_FOLLOWS = "decimal follows"
NUMBER_FOLLOWS = "number follows"

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", }

symbols_to_english = {
    "......": " ", ".....O": CAPITAL, ".O...O": DECIMAL_FOLLOWS, ".O.OOO": NUMBER_FOLLOWS,
}

braille_to_digits = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

english_to_braille = {v: k for k, v in braille_to_english.items()}
symbols_to_braille = {v: k for k, v in symbols_to_english.items()}
digit_to_braille = {v: k for k, v in braille_to_digits.items()}


def check_braille(input_string: str) -> bool:
    is_braille = True
    for char in input_string:
        if char == "." or char == "O":
            continue
        else:
            is_braille = False
            break

    return is_braille


def translate_braille(input_string: str) -> str:
    # chunk the string into 6 characters
    chunks = [input_string[i : i + 6] for i in range(0, len(input_string), 6)]

    is_number_follows = False
    is_capital = False

    result = ""
    for chunk in chunks:
        if symbols_to_english.get(chunk) == NUMBER_FOLLOWS:
            is_number_follows = True
            continue

        if symbols_to_english.get(chunk) == CAPITAL:
            is_capital = True
            continue

        if is_number_follows:
            if braille_to_english.get(chunk) == " ":
                is_number_follows = False
                result += " "
                continue
            else:
                result += braille_to_digits.get(chunk)
                continue

        if is_capital:
            result += braille_to_english.get(chunk).upper()
            is_capital = False
            continue

        if braille_to_english.get(chunk):
            result += braille_to_english.get(chunk)
        elif symbols_to_english.get(chunk):
            result += symbols_to_english.get(chunk)
        else:
            result += braille_to_digits.get(chunk)

    return result


def translate_english(splitted: List[str]) -> str:
    result = ""
    is_number_follows = False

    for i, word in enumerate(splitted):
        for char in word:
            if char.isupper():
                result += symbols_to_braille.get(CAPITAL)
                result += english_to_braille.get(char.lower())
                continue
            elif char.isdigit():
                if not is_number_follows:
                    result += symbols_to_braille.get(NUMBER_FOLLOWS)
                    is_number_follows = True
                result += digit_to_braille.get(char)
                continue
            else:
                if english_to_braille.get(char):
                    result += english_to_braille[char]
                elif symbols_to_braille.get(char):
                    result += symbols_to_braille[char]
                else:
                    result += digit_to_braille.get(char)

                is_number_follows = False
                continue

        if i != len(splitted) - 1:
            result += symbols_to_braille[" "]

    return result


def main():
    input_string = sys.argv[1:]

    # check whether string is completely braille or string
    is_braille = len(input_string) == 1 and check_braille(input_string[0])

    if is_braille:
        translation = translate_braille(input_string[0])
        print(translation)
        # return translation
    else:
        translation = translate_english(input_string)
        print(translation)
        # return translation


if __name__ == "__main__":
    main()
