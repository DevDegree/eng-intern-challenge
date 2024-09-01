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
    """
    Detects if the given string is written in Braille or English.

    This function checks the input string to determine if it is written
    in English or Braille. If the string contains any character other
    than '.' and 'O', it is considered to be English. Otherwise, it is
    considered Braille.

    Args:
        input_str (str): The input string to be checked.

    Returns:
        bool: True if the input string is in Braille, False if it is in English.
    """
    # The logic should be: if the string has anything other than '.' and 'O' then it is English. Else, it is Braille.
    english_chars = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "

    for char in input_str:
        if char in english_chars:
            return False
    return True


def braille_to_english(input_str):
    """
    Converts a Braille string to its corresponding English text.

    This function takes a Braille-encoded string and converts it to
    the equivalent English text. It validates the Braille input
    for correctness based on its length and character content.

    Args:
        input_str (str): The Braille string to be converted to English.

    Returns:
        str: The translated English text or an error message if the Braille
             string is invalid.
    """
    res = ""
    # Check if Braille is valid
    if len(input_str) % 6 != 0:
        return "Invalid Braille string."
    char_idx = 0

    while char_idx < len(input_str):
        curr = input_str[char_idx : char_idx + 6]
        if curr not in BRAILLE_DICT_BWD:
            return "Invalid Braille string."
        mapped_arr = BRAILLE_DICT_BWD[curr]
        # Check if its a "special char"
        if mapped_arr[0] == "CAP":
            # Get next character and add it capitalized
            char_idx += 6
            curr = input_str[char_idx : char_idx + 6]
            mapped_arr = BRAILLE_DICT_BWD[curr]
            res += mapped_arr[0]
            char_idx += 6
        elif mapped_arr[0] == "NUM":
            char_idx += 6
            while char_idx < len(input_str):
                curr = input_str[char_idx : char_idx + 6]
                mapped_arr = BRAILLE_DICT_BWD[curr]
                if mapped_arr[0] == "SPACE":
                    break
                res += mapped_arr[1]
                char_idx += 6

        elif mapped_arr[0] == "SPACE":
            res += " "
            char_idx += 6
        else:
            res += mapped_arr[0].lower()
            char_idx += 6

    return res


def english_to_braille(input_str):
    """
    Converts an English string to its corresponding Braille representation.

    This function takes an English text string and converts it into
    Braille code. It handles alphabetic characters, numbers, and spaces,
    and uses special indicators for capital letters and numbers.

    Args:
        input_str (str): The English string to be converted to Braille.

    Returns:
        str: The Braille representation of the English input string.
    """
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
            # Add 'number follows' then iterate over all numbers and add them
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

    # Check if input is valid and is not empty
    if not input_str:
        return ""

    is_braille = detect(input_str)

    output = ""

    if is_braille:
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)

    print(output)


if __name__ == "__main__":
    main()
