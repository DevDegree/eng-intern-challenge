BRAILLE_TYPE = "braille"
ENGLISH_TYPE = "english"
UNKNOWN_TYPE = "unknown"
INVALID_BRAILLE_STRING = "Invalid braille string."
BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"

BRAILLE_TO_ENGLISH_DICT = {
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
}

BRAILLE_TO_SPECIAL_DICT = {
    "O.....": ".",
    "O.O...": ",",
    "O..OOO": "?",
    "OO....": "!",
    "OO.O..": ":",
    "O..O..": ";",
    "OO.OOO": "-",
    "OOOO..": "/",
    "O.OO.O": "<",
    "O.OOO.": ">",
    ".OOO..": "(",
    ".OO.O.": ")",
    "......": " ", 
}

BRAILLE_TO_NUMBER_DICT = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

ENGLISH_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.?!:;/-<>()"