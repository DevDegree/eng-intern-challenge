from src.constants.braille_constants import BrailleConstant
from src.constants.english_constants import EnglishConstant

ENGLISH_TO_BRAILLE = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OO.O.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O.O.O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    EnglishConstant.SPACE: BrailleConstant.SPACE,
}

NUMBER_TO_BRAILLE = {
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

FOLLOWS_TO_BRAILLE = {
    EnglishConstant.CAPITAL_FOLLOWS.value: BrailleConstant.CAPITAL_FOLLOWS.value,
    EnglishConstant.NUMBER_FOLLOWS.value: BrailleConstant.NUMBER_FOLLOWS.value
}

BRAILLE_TO_ENGLISH = dict((value, key) for key, value in ENGLISH_TO_BRAILLE.items())
BRAILLE_TO_NUMBER = dict((value, key) for key, value in NUMBER_TO_BRAILLE.items()) 
BRAILLE_TO_FOLLOWS = dict((value, key) for key, value in FOLLOWS_TO_BRAILLE.items()) 