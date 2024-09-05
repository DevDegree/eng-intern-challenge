import sys
from textwrap import wrap

ENGLISH_TO_BRAILLE_MAP = {
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
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO",
}

BRAILLE_TO_ENGLISH_MAP = {val: key for key, val in ENGLISH_TO_BRAILLE_MAP.items()}

NUMERICS_MAP = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "O": ".OOO..",
}


def is_braille(input_string: str) -> bool:
    """Checks whether a string is written in Braille or English.

    Args:
        input_string (str): User string input from the command line.

    Returns:
        bool: True if Braille, else False.
    """
    BRAILLE_SYMBOLS = {"O", "."}
    return BRAILLE_SYMBOLS.issuperset(set(input_string))


def convert_to_english(braille_input: str) -> str:
    """Converts a chunked string of Braille characters into English. Checks for
    Capitalization and Numeric values, including whitespace between characters.

    Args:
        braille_input (str): Braille input string to be converted to English.

    Returns:
        str: Converted English String, includes whitespaces.
    """
    number_mode = False
    capitalize_next = False
    translated_chars = []
    braille_chunks = wrap(braille_input, width=6)

    for braille_char in braille_chunks:
        if braille_char == ENGLISH_TO_BRAILLE_MAP["capital follows"]:
            capitalize_next = True
        elif braille_char == ENGLISH_TO_BRAILLE_MAP["number follows"]:
            number_mode = True
        elif braille_char == ENGLISH_TO_BRAILLE_MAP[" "]:
            number_mode = False
            translated_chars.append(BRAILLE_TO_ENGLISH_MAP[braille_char])
        else:
            if number_mode and braille_char in NUMERICS_MAP.values():
                num_char = next(
                    key for key, value in NUMERICS_MAP.items() if value == braille_char
                )
                translated_chars.append(num_char)
            elif capitalize_next:
                translated_chars.append(BRAILLE_TO_ENGLISH_MAP[braille_char].upper())
                capitalize_next = False
            else:
                translated_chars.append(BRAILLE_TO_ENGLISH_MAP[braille_char])
    return "".join(translated_chars)


def convert_to_braille(english_input: str) -> str:
    """Converts English words to Braille respecting capitalization, numerics and whitespaces.

    Args:
        english_input (str): English text as string to convert to Braille.

    Returns:
        str: Converted Braille text as string.
    """
    translated_chars = []
    number_mode = False

    for english_char in english_input:
        if english_char.isupper():
            number_mode = False
            translated_chars.append(ENGLISH_TO_BRAILLE_MAP["capital follows"])
            translated_chars.append(ENGLISH_TO_BRAILLE_MAP[english_char.lower()])
        elif english_char.isdigit():
            if number_mode:
                translated_chars.append(NUMERICS_MAP[english_char])
            else:
                number_mode = True
                translated_chars.append(ENGLISH_TO_BRAILLE_MAP["number follows"])
                translated_chars.append(NUMERICS_MAP[english_char])
        else:
            number_mode = False
            translated_chars.append(ENGLISH_TO_BRAILLE_MAP[english_char])
    return "".join(translated_chars)


def convert_text_input(input: str) -> str:
    """Converts Command Line user input between Braille and English automatically.

    Args:
        input (str): User string input received from the command line.

    Returns:
        str: Converted user input in either Braille or English format.
    """
    if is_braille(input):
        return convert_to_english(input)
    return convert_to_braille(input)


def main():
    input = " ".join(sys.argv[1:])
    completed_translation = convert_text_input(input)
    sys.stdout.write(completed_translation)


if __name__ == "__main__":
    main()
