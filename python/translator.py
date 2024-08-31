import sys
from typing import List

BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " "
}

BRAILLE_TO_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7",
    "O.OO..": "8", ".OO...": "9", ".000..": "0"
}

ENGLISH_TO_BRAILLE = dict(zip(BRAILLE_TO_ENGLISH.values(), BRAILLE_TO_ENGLISH.keys()))
NUMBERS_TO_BRAILLE = dict(zip(BRAILLE_TO_NUMBERS.values(), BRAILLE_TO_NUMBERS.keys()))
BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMBER = ".O.OOO"
BRAILLE_SPACE = "......"


def translate_input(words: List[str]) -> str:
    """
    Checks the given arguments for braille or english and calls the respective function to translate the argument. It
    then returns the translated string
    """
    line = " ".join(words)
    if line == "":
        return ""

    if line.count(".") + line.count("O") == len(line):
        result = translate_braille_to_english(line)
    else:
        result = translate_english_to_braille(line)
    return result


def translate_braille_to_english(line: str) -> str:
    """
    Translates the given braille string to a english string using the global dictionaries defined at start of file
    """

    # Separates the braille string to a list of braille characters
    chars = []
    for i in range(0, len(line), 6):
        chars.append(line[i:i + 6])

    result = []
    i = 0
    number_switch = False
    while i < len(chars):
        if chars[i] == BRAILLE_CAPITAL:
            i += 1
            result.append(BRAILLE_TO_ENGLISH[chars[i]].upper())
        elif chars[i] == BRAILLE_NUMBER:
            i += 1
            result.append(BRAILLE_TO_NUMBERS[chars[i]])
            number_switch = True
        # Write numbers until space
        elif chars[i] == BRAILLE_SPACE:
            number_switch = False
            result.append(BRAILLE_TO_ENGLISH[chars[i]])
        elif number_switch:
            result.append(BRAILLE_TO_NUMBERS[chars[i]])
        else:
            result.append(BRAILLE_TO_ENGLISH[chars[i]])
        i += 1
    result = "".join(result)
    return result


def translate_english_to_braille(line: str) -> str:
    """
    Translates the given string to a braille string using the global dictionaries defined at start of file
    """
    result = []
    number_switch = False
    for char in line:
        if char.isupper():
            result.append(BRAILLE_CAPITAL)
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char.isdigit():
            # Only add 'number follows' once
            if not number_switch:
                result.append(BRAILLE_NUMBER)
                number_switch = True
            result.append(NUMBERS_TO_BRAILLE[char])
        elif char == " ":
            number_switch = False
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            result.append(ENGLISH_TO_BRAILLE[char])
    result = "".join(result)
    return result


def main():
    """
    Program entry point
    """
    arguments = sys.argv[1:]
    result = translate_input(arguments)
    print(result)


if __name__ == "__main__":
    main()
