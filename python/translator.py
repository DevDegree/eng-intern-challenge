import sys

char_to_braille = {
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
    "cap_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
}


def identify_lang(input_str: str) -> bool:
    """Determines whether the input string is written in English or Braille format.

    Args:
        input_str (str): The input string provided (either English or Braille).

    Returns:
        bool: True if the input is identified as English, False if Braille.
    """

    return False


def convert_english_to_braille(input_str: str) -> str:
    """Converts the given English input string into its Braille representation.

    Args:
        input_str (str): A string of English text (lowercase/uppercase).

    Returns:
        str: The corresponding Braille translation in string format.
    """

    return ""


def convert_braille_to_english(input_str: str) -> str:
    """Converts a Braille string into its English equivalent.

    Args:
        input_str (str): A string in Braille format (dots as O and periods).

    Returns:
        str: The corresponding English translation of the Braille input.
    """

    return ""


def convert(input_str: str) -> str:
    """Main function that decides which conversion to apply (English to Braille or Braille to English).

    Args:
        input_str (str): The input string (English or Braille) to be converted.

    Returns:
        str: The converted string in either Braille or English.
    """

    if identify_lang(input_str):
        return convert_english_to_braille(input_str)

    return convert_braille_to_english(input_str)


if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])

    print(convert(input_str))
