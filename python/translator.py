import sys

# A python program/script that translates english to braille and vice versa.
# (Values to be translated should be passed in as a runtime argument).
# Made for Shopify's 2025 Summer Software Engineer Intern challenge.
# By: Athanasios Topaltsis

# Runtime arguments
args = sys.argv

# Dictionary of english letters mapped to their braille equivalent.
alphabet = {
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
    "z": "O..OOO"
}

# Dictionary of numbers mapped to their braille equivalent.
numbers = {
    "1": "O.....",  # Same as 'a'
    "2": "O.O...",  # Same as 'b'
    "3": "OO....",  # Same as 'c'
    "4": "OO.O..",  # Same as 'd'
    "5": "O..O..",  # Same as 'e'
    "6": "OOO...",  # Same as 'f'
    "7": "OOOO..",  # Same as 'g'
    "8": "O.OO..",  # Same as 'h'
    "9": ".OO...",  # Same as 'i'
    "0": ".OOO.."   # Same as 'j'
}

# Dictionary of symbols mapped to their braille equivalent.
symbols = {
    ".": ".O.OOO",
    ",": ".O....",
    "?": ".O..OO",
    "!": ".O.OO.",
    ":": ".OO...",
    ";": ".OO...",
    "-": "..O..O",
    "/": "..O.O.",
    "<": "..O..O",
    ">": "..OO..",
    "(": ".OO.O.",
    ")": ".OOO.O"
}

# Other braille variables
braille_space = "......"
braille_capital_prefix = ".....O"
braille_decimal_prefix = ".O...O"
braille_number_prefix = ".O.OOO"
