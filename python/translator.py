"""
NOTE:
    In the given image provided of the braille grid both charachters 'o' and '>' have the exact same diagram.
    As there is no offical and consistent standard for this, I remapped charachter '>' to 'OOOOOO'.
Assumptions made:
    For text -> braille:
        - Spaces do not distinguish between numbers and text (eventhough it is required in decoding)
        - This means my text -> braille can convert inputs like "Hello m8" -> ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.......OO..O..O.OOOO.OO.."
        - NOTE Still passes and works as expected for spaces between text and numbers!

    For braille -> text:
        - Wanted to make decoding similar so I can perform such conversion "......0(abbreviated)" -> "Th1s1s4dvanced" however stuck wth assumptions
          because decoding will get more complicated than it already is.
    
    Possible optimzations:
        - If we can assume input will be valid braille such that it cannot be mixed with english
        then we do not have to check the whole string. 


    Both take O(n) time, linear functions.
"""

import sys
from typing import List

BRAILLE_CAPITAL_SYMBOL = ".....O"
BRAILL_NUMBER_SYMBOL = ".O.OOO"
BRAILLE_DECIMAL_SYMBOL = ".O...O"

LETTER_TO_BRAILLE = {
    " ": "......",
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
    ";": "..O.O.",
    ":": "..OO..",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "OOOOOO",
    "(": "O.O..O",
    ")": ".O.OO.",
}

BRAILLE_TO_LETTER = {value: key for key, value in LETTER_TO_BRAILLE.items()}


def get_number_braille(num: int, is_first: bool) -> str:
    """Returns a braille charachter for given number by mapping 0-9 to a-j"""
    return is_first * BRAILL_NUMBER_SYMBOL + (
        LETTER_TO_BRAILLE["j"]
        if num == 0
        else LETTER_TO_BRAILLE[chr(ord("a") + int(num) - 1)]
    )


def get_char_braille(char: str) -> str:
    """Returns a braille charachter for given charachter"""
    return char.isupper() * BRAILLE_CAPITAL_SYMBOL + LETTER_TO_BRAILLE[char.lower()]


def convert_to_braille(text: str) -> str:
    """Converts a string of charachters to a string of braille charachters"""
    conversion = ""

    for i in range(len(text)):
        char, prev = text[i], text[i - 1]

        if char == ".":
            if prev.isdigit():
                conversion += BRAILLE_DECIMAL_SYMBOL

            elif not prev.isdigit() and i + 1 != len(text) and text[i + 1].isdigit():
                conversion += BRAILL_NUMBER_SYMBOL + BRAILLE_DECIMAL_SYMBOL

        conversion += (
            get_number_braille(int(char), not (prev.isdigit() or prev == ".") or i == 0)
            if char.isdigit()
            else get_char_braille(char)
        )

    return conversion


def get_braille_number(braille: str) -> str:
    """Converts braille charachter to integer"""
    return (
        "0"
        if braille == LETTER_TO_BRAILLE["j"]
        else str(ord(BRAILLE_TO_LETTER[braille]) - 97 + 1)
    )


def convert_to_text(braille: str) -> str:
    """Converts braille to text"""
    conversion = ""
    current_symbol = None
    i = 0

    while i < len(braille):
        charachter = braille[i : i + 6]

        if charachter == BRAILLE_DECIMAL_SYMBOL:
            conversion += "."
            i += 6

        elif charachter == LETTER_TO_BRAILLE[" "]:
            conversion += " "
            current_symbol = None

        elif current_symbol == BRAILL_NUMBER_SYMBOL:
            conversion += get_braille_number(charachter)

        elif letter := BRAILLE_TO_LETTER.get(charachter):
            if current_symbol == BRAILLE_CAPITAL_SYMBOL:
                conversion += letter.upper()
            else:
                conversion += letter

            current_symbol = None

        else:
            current_symbol = charachter

        i += 6

    return conversion


def is_braille(text: str) -> bool:
    """Checks if a string is braille based of assumptions"""
    return all(c in "O." for c in text) and len(text) % 6 == 0


def main(argv: List[str]):
    string = " ".join(argv[1:])

    if is_braille(string):
        print(convert_to_text(string))
        return

    print(convert_to_braille(string))


if __name__ == "__main__":
    main(sys.argv)
