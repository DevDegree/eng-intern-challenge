import argparse

BRAILLE_DICT_FWD = {
    "A": "O.....",
    "1": "O.....",
    "B": "O.O...",
    "2": "O.O...",
    "C": "OO....",
    "3": "OO....",
    "D": "OO.O..",
    "4": "OO.O..",
    "E": "O..O..",
    "5": "O..O..",
    "F": "OOO...",
    "6": "OOO...",
    "G": "OOOO..",
    "7": "OOOO..",
    "H": "O.OO..",
    "8": "O.OO..",
    "I": ".OO...",
    "9": ".OO...",
    "J": ".OOO..",
    "0": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "CAP": ".....O",
    "NUM": ".O.OOO",
    "SPACE": "......",
}

BRAILLE_DICT_BWD = {
    "O.....": ["A", "1"],
    "O.O...": ["B", "2"],
    "OO....": ["C", "3"],
    "OO.O..": ["D", "4"],
    "O..O..": ["E", "5"],
    "OOO...": ["F", "6"],
    "OOOO..": ["G", "7"],
    "O.OO..": ["H", "8"],
    ".OO...": ["I", "9"],
    ".OOO..": ["J", "0"],
    "O...O.": ["K"],
    "O.O.O.": ["L"],
    "OO..O.": ["M"],
    "OO.OO.": ["N"],
    "O..OO.": ["O"],
    "OOO.O.": ["P"],
    "OOOOO.": ["Q"],
    "O.OOO.": ["R"],
    ".OO.O.": ["S"],
    ".OOOO.": ["T"],
    "O...OO": ["U"],
    "O.O.OO": ["V"],
    ".OOO.O": ["W"],
    "OO..OO": ["X"],
    "OO.OOO": ["Y"],
    "O..OOO": ["Z"],
    ".....O": ["CAP"],
    ".O.OOO": ["NUM"],
    "......": ["SPACE"],
}


def detect(input_str):
    # The logic should be: if the string has anything other than '.' and 'O' then it is English. Else, it is Braille.
    english_chars = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "

    for char in input_str:
        if char in english_chars:
            print("Bad Char: ", char)
            return False
    return True


def braille_to_english(input_str):
    pass


def english_to_braille(input_str):
    res = ""
    char_idx = 0
    while char_idx < len(input_str):
        # Check if it is a space character
        if input_str[char_idx] == " ":
            res += BRAILLE_DICT_FWD["SPACE"]
            char_idx += 1
        # Check if its letter or number
        elif input_str[char_idx].isalpha():
            # Check if the letter is capital or not
            if input_str[char_idx].isupper():
                # Put a 'capital follows' then the letter
                res += BRAILLE_DICT_FWD["CAP"]
                res += BRAILLE_DICT_FWD[input_str[char_idx]]
            else:
                res += BRAILLE_DICT_FWD[input_str[char_idx].upper()]
            char_idx += 1
        elif input_str[char_idx].isnumeric():
            res += BRAILLE_DICT_FWD["NUM"]
            while char_idx < len(input_str) and input_str[char_idx].isnumeric():
                res += BRAILLE_DICT_FWD[input_str[char_idx]]
                char_idx += 1
    return res


def main():
    parser = argparse.ArgumentParser(
        description="Detects and converts Braille to English and vice versa"
    )

    # Only one argument which is the string to be translated
    parser.add_argument("input_str", type=str, nargs="+", default="")

    args = parser.parse_args()

    input_str = " ".join(args.input_str)
    print("input_str: ", input_str)

    # Check if input is valid and is not empty
    if not input_str:
        return ""

    is_braille = detect(input_str)
    if is_braille:
        print("Its braille")
    else:
        print("Its english")

    output = ""
    # print(output)

    if is_braille:
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)

    print("Out:")
    print(output)


if __name__ == "__main__":
    main()
