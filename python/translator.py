import sys
from enum import Enum

CAPITAL_FOLLOWS =  ".....O"
NUMBER_FOLLOWS  =  ".O.OOO"
SPACE           =  "......"

class Mode(Enum):
    LETTER = 0
    CAPITAL = 1
    NUMBER = 2
    
def number_to_top_part_braille(n: int) -> str:
    if n % 10 == 1:
        return "O..."
    elif n % 10 == 2:
        return "O.O."
    elif n % 10 == 3:
        return "OO.."
    elif n % 10 == 4:
        return "OO.O"
    elif n % 10 == 5:
        return "O..O"
    elif n % 10 == 6:
        return "OOO."
    elif n % 10 == 7:
        return "OOOO"
    elif n % 10 == 8:
        return "O.OO"
    elif n % 10 == 9:
        return ".OO."
    else:
        return ".OOO"

def number_to_bottom_part_braille(n: int) -> str:
    if n // 10 == 0:
        return ".."
    elif n // 10 == 1:
        return "O."
    elif n // 10 == 2:
        return "OO"
    else:
        return ".O"

CHAR_NUM_MAP = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 0,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 10,
    "u": 21,
    "v": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "w": 30,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 0,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 10,
    "U": 21,
    "V": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "W": 30,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}

REV_ALPHA_MAP = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    0: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    10: "t",
    21: "u",
    22: "v",
    23: "x",
    24: "y",
    25: "z",
    30: "w"
}

def convert_english_char(c: str) -> str:
    number = CHAR_NUM_MAP[c]
    return number_to_top_part_braille(number) + number_to_bottom_part_braille(number)

def top_part_braille_to_number(s: str) -> int:
    if s == "O...":
        return 1
    elif s == "O.O.":
        return 2
    elif s == "OO..":
        return 3
    elif s == "OO.O":
        return 4
    elif s == "O..O":
        return 5
    elif s == "OOO.":
        return 6
    elif s == "OOOO":
        return 7
    elif s == "O.OO":
        return 8
    elif s == ".OO.":
        return 9
    else:
        return 0

def bottom_part_braille_to_number(s: str) -> int:
    if s == "..":
        return 0
    elif s == "O.":
        return 10
    elif s == "OO":
        return 20
    else:
        return 30

def convert_braille_char(char: str, mode: Mode) -> str:
    number = top_part_braille_to_number(char[:4]) + bottom_part_braille_to_number(char[4:])
    if mode == Mode.LETTER:
        return REV_ALPHA_MAP[number]
    elif mode == Mode.CAPITAL:
        return REV_ALPHA_MAP[number].upper()
    else:
        return str(number)

result_text = []
input_strings = sys.argv[1:]

if (
    len(input_strings) == 1
    and len(input_strings[0]) % 6 == 0
    and "." in input_strings[0]
):
    # Braille
    mode = Mode.LETTER
    braille_string = input_strings[0]
    for i in range(0, len(braille_string), 6):
        curr_braille_char = braille_string[i:i+6]
        if curr_braille_char == SPACE:
            result_text.append(" ")
            mode = Mode.LETTER
        elif curr_braille_char == CAPITAL_FOLLOWS:
            mode = Mode.CAPITAL
        elif curr_braille_char == NUMBER_FOLLOWS:
            mode = Mode.NUMBER
        else:
            result_text.append(convert_braille_char(curr_braille_char, mode))
            if mode == Mode.CAPITAL:
                mode = Mode.LETTER
    result = ''.join(result_text)
    print(result)
         
else:
    # English
    for string in input_strings:
        converted_chars = []
        number_mode = False
        for char in string:
            if char.isnumeric() and not number_mode:
                # add "number is next"
                number_mode = True
                converted_chars.append(NUMBER_FOLLOWS)
            elif char.isalpha() and char.isupper():
                # add "capital is next"
                converted_chars.append(CAPITAL_FOLLOWS)
            converted_chars.append(convert_english_char(char))
        result_text.append(''.join(converted_chars))
    result = SPACE.join(result_text)
    print(result)