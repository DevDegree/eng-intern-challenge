
#CONSTANTS
BRAILLLE_SET = {"O", "."}
ALPHANUMERICALS_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
        "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
        "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
        "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
        "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
        "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......", "capital": ".....O",
        "decimal": ".O...O", "number": ".O.OOO"
    }

BRAILLE_TO_ALPHANUMERICALS = {value: key for key, value in ALPHANUMERICALS_TO_BRAILLE.items()}

# Checks is the input string is alphanumerical or baille
def is_baille(sequence_chars):
    if len(sequence_chars) % 6 == 0 and set(sequence_chars) - BRAILLLE_SET == set({}):
        return True
    return False
