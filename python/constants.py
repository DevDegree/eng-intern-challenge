from typing import Dict, FrozenSet

# Language constants
ENGLISH : str = "english"
BRAILLE : str = "braille"
CAPITAL : str = "capital"
NUMBER  : str = "number"

# Braille language constants
CAPITAL_FOLLOWS : str = ".....O"
NUMBER_FOLLOWS  : str = ".O.OOO"

# Error messages
INVALID_INPUT_MSG    : str = "Invalid input.\nOnly alphanumeric characters and spaces are allowed for english.\nOnly supported sequences of '.' and 'O' are allowed for braille. Refer to the project README for a description of supported braille characters."
INVALID_CHAR_SEQ_MSG : str = "Invalid character sequence.\nNumerical characters must be followed by a space or another numerical character.\nCapital characters must be followed by an alphabetical character.\nBraille sequences cannot end with a capital or number modifier."

# Character sets
PERMITTED_NON_ALPHANUMERIC_CHARS : FrozenSet[str] = frozenset([" "])
PERMITTED_MODIFIERS              : FrozenSet[str] = frozenset([CAPITAL, NUMBER])
NUMBER_TERMINATING_CHARS         : FrozenSet[str] = frozenset([" "])

# Translation dictionaries
ENGLISH_TO_BRAILLE : Dict[str, str] = {
    " " : "......", "a" : "O.....", "b" : "O.O...", 
    "c" : "OO....", "d" : "OO.O..", "e" : "O..O..",
    "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..",
    "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.",
    "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.",
    "o" : "O..OO.", "p" : "OOO.O.", "q" : "OOOOO.",
    "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O",
    "x" : "OO..OO", "y" : "OO.OOO", "z" : "O..OOO",
    CAPITAL : CAPITAL_FOLLOWS, 
    NUMBER  : NUMBER_FOLLOWS
}
BRAILLE_TO_ENGLISH : Dict[str, str] = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}

# Braille number to letter mapping
NUMBERS_TO_LETTERS : Dict[str, str] = {
    "1" : "a", "2" : "b", "3" : "c", "4" : "d", "5" : "e",
    "6" : "f", "7" : "g", "8" : "h", "9" : "i", "0" : "j"
}
LETTERS_TO_NUMBERS : Dict[str, str] = {value: key for key, value in NUMBERS_TO_LETTERS.items()}