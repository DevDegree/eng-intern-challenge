import sys

CAPITAL_LETTER = "capital"
DIGIT = "digit"
SPACE = " "

ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", 
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}
DIGITS_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
}
SPECIAL_CHARS = {
    CAPITAL_LETTER: ".....O", DIGIT: ".O.OOO", SPACE: "......",
}

BRAILLE_TO_DIGITS = {v: k for k, v in DIGITS_TO_BRAILLE.items()}
BRAILLE_TO_ENG = {v: k for k, v in ENG_TO_BRAILLE.items()}
REVERSE_SPECIAL_CHARS = {v: k for k, v in SPECIAL_CHARS.items()}


def main():
    return 0

if __name__ == "__main__":
    main()