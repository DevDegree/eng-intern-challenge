import argparse

ENGLISH_TO_BRAILLE_CONV = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
    "-": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.", " ": "......"
}

BRAILLE_TO_ENGLISH_CONV_NUM = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "......": " "
}

BRAILLE_TO_ENGLISH_CONV_NON_NUM = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", "O.O..O": "(",
    ".O.OO.": ")", "......": " "
}

BRAILLE_CHARACTERS = ".O"

BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMERIC = ".O.OOO"


def is_english(inputs) -> bool:
    if len(inputs) > 1:
        return True

    if len(inputs[0]) % 6 != 0:
        return True

    for input in inputs:
        for char in input:
            if char not in BRAILLE_CHARACTERS:
                return True

    return False


def english_to_braille(english_phrase) -> str:
    braille = ""
    numeric_flag = False

    for char in english_phrase:
        if char.isnumeric():
            if not numeric_flag:
                numeric_flag = True
                braille += BRAILLE_NUMERIC
        elif char != " ":
            if char.isupper():
                braille += BRAILLE_CAPITAL
        else:
            numeric_flag = False

        braille += ENGLISH_TO_BRAILLE_CONV[char.lower()]

    return braille


def braille_to_english(braille_phrase) -> str:
    english = ""
    capital_flag = False
    numeric_flag = False

    for i in range(0, len(braille_phrase), 6):
        braille_char = braille_phrase[i:i + 6]
        if braille_char == BRAILLE_NUMERIC:
            numeric_flag = True
        elif braille_char == BRAILLE_CAPITAL:
            capital_flag = True
        else:
            if numeric_flag:
                english_char = BRAILLE_TO_ENGLISH_CONV_NUM[braille_char]
            else:
                english_char = BRAILLE_TO_ENGLISH_CONV_NON_NUM[braille_char]

            if capital_flag:
                english_char = english_char.upper()
                capital_flag = False

            if english_char == " ":
                numeric_flag = False

            english += english_char

    return english


def main(inputs):
    if is_english(inputs):
        print(english_to_braille(" ".join(inputs)))
    else:
        print(braille_to_english("".join(inputs)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+")
    args = parser.parse_args()
    main(args.inputs)
