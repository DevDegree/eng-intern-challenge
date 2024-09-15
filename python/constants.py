# constants.py
"""
This files contains constants used in the translator.py Class BrailleTranslator.

Constants:
    NUMBER_FOLLOWS (str): Indicator for numbers in Braille.
    CAPITAL_FOLLOWS (str): Indicator for capital letters in Braille.
    ALPHABETS_TO_BRAILLE (dict): Mapping of English alphabets to their Braille representation.
    NUMBERS_TO_BRAILLE (dict): Mapping of numbers to their Braille representation.
    BRAILLE_TO_ALPHABETS (dict): Reverse mapping of Braille to English alphabets.
    BRAILLE_TO_NUMBERS (dict): Reverse mapping of Braille to numbers.
"""

NUMBER_FOLLOWS = ".O.OOO"
CAPITAL_FOLLOWS = ".....O"

ALPHABETS_TO_BRAILLE = {
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

NUMBERS_TO_BRAILLE = {
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

BRAILLE_TO_ALPHABETS = {v: k for k, v in ALPHABETS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}
