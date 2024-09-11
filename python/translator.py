import sys


def is_bratile(text: str) -> bool:
    return all(char in "O." for char in text)


def bratile_to_english(bratile_text: str) -> str:
    result = ""
    bratile_to_english_lookup = {
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
        "......": " ",
    }
    bratile_to_number_lookup = {
        ".OOO..": "0",
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
    }

    capital = False
    numeric = False
    for i in range(0, len(bratile_text), 6):
        translated_char = ""
        chunk = bratile_text[i : i + 6]
        if chunk == ".....O":
            capital = True
            continue
        elif chunk == ".O.OOO":
            numeric = True
            continue
        elif numeric and chunk == "......":
            numeric = False

        if capital:
            translated_char = bratile_to_english_lookup[chunk].upper()
            capital = False
        elif numeric:
            translated_char = bratile_to_number_lookup[chunk]
        else:
            translated_char = bratile_to_english_lookup[chunk]
        result += translated_char
    return result


def english_to_bratile(english_text: str) -> str:
    english_to_bratile_lookup = {
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
        " ": "......",
    }
    number_to_bratile_lookup = {
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
    result = ""
    started_numeric = False
    for c in english_text:
        if c in number_to_bratile_lookup:
            if not started_numeric:
                result += ".O.OOO"
                started_numeric = True
            result += number_to_bratile_lookup[c]
        else:
            started_numeric = False
            if c.isupper():
                result += ".....O"
            result += english_to_bratile_lookup[c.lower()]
    return result


if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])
    translated_str = ""

    if is_bratile(input_str):
        translated_str = bratile_to_english(input_str)
    else:
        translated_str = english_to_bratile(input_str)
    print(translated_str)
