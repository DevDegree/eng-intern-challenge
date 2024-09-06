"""
Braille Translator Constants

"""


# constants for the constants
CAPITAL_FOLLOWS = "CAPITAL_FOLLOWS"
NUMBER_FOLLOWS = "NUMBER_FOLLOWS"
SPACE = " "




# ------------------------ English to Braille ------------------------
ENGLISH_TO_BRAILLE = {
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
    
    # TODO: Symbols included (present in alphabet, unspecified in requirements) => handle gracefully
    # ".": "..OO.O",
    # ",": "..O...",
    # "?": "..O.OO",
    # "!": "..OOO.",
    # ":": "..OO..",
    # ";": "..O.O.",
    # "-": "....OO",
    # "/": ".O..O.",
    # "<": ".OO..O",
    # ">": "O..OO.",
    # "(": "O.O..O",
    # ")": ".O.OO.",
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

SPECIAL_TO_BRAILLE = { 
    CAPITAL_FOLLOWS: ".....O",
    NUMBER_FOLLOWS: ".O.OOO",
    SPACE: "......",
}




# ------------------------ Braille to English ------------------------
BRAILLE_TO_ENGLISH = { braille: english for english, braille in ENGLISH_TO_BRAILLE.items() }
BRAILLE_TO_NUMBER = { braille: number for number, braille in NUMBER_TO_BRAILLE.items() }
BRAILLE_TO_SPECIAL = { braille: special for special, braille in SPECIAL_TO_BRAILLE.items() }
