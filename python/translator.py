import sys

"""
    English -> Braille translator function
"""


def translate_to_braille(string):
    english_to_braille = {
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
        "capitalize": ".....O",
        "num start": ".O.OOO",
        " ": "......",
    }

    num_to_braille = {
        "0": ".OOO..",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
    }

    # initialize states
    capitalize, is_number = False, False
    braille_string = ""

    """
        Turn states for capitalization and is_number on and off
        based on the read character and continuously append the needed
        braille equivalent based on state
    """
    for char in string:
        if char.isupper():
            braille_string += english_to_braille["capitalize"]
            capitalize = True
        elif char.isnumeric():
            if not is_number:
                braille_string += english_to_braille["num start"]
                is_number = True
        elif char == " ":
            if is_number:
                is_number = False

        if is_number:
            braille_string += num_to_braille[char]
        elif capitalize:
            braille_string += english_to_braille[char.lower()]
            capitalize = False
        else:
            braille_string += english_to_braille[char]

    return braille_string


"""
    Braille -> English translator
"""


def translate_to_english(string: str) -> str:
    braille_to_english = {
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
        ".....O": "capitalize",
        ".O.OOO": "num start",
        "......": " ",
    }

    braille_to_num = {
        ".OOO..": "0",
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
    }

    # split the initial string into braille characters each of which are of length 6
    len_of_six = [string[i : i + 6] for i in range(0, len(string), 6)]

    # initialize states
    capitalize, is_number = False, False
    english_string = ""

    # Change state based on the character being read and mutate the output based on this
    for char in len_of_six:
        if braille_to_english[char] == " ":
            is_number = False
        if braille_to_english[char] == "capitalize":
            capitalize = True
        elif braille_to_english[char] == "num start" and not is_number:
            is_number = True
        else:
            if capitalize:
                english_string += braille_to_english[char].capitalize()
                capitalize = False
            elif is_number:
                english_string += braille_to_num[char]
            else:
                english_string += braille_to_english[char]

    return english_string


def is_english(string: str) -> bool:
    str_len = len(string)
    """
        Given the constraints if the given string contains the ' ' character
        or is not a string of a length divisible by 6 it is guaranteed to be
        an English sentence.

        If however there are no spaces we can see that this could be an English
        word. If it is a possible English word and it has a length that is a multiple
        of 6 but it only consists of 'O's and '.'s it must be braille

        NOTE: I did notice that one could simply check that if a string 
        contains '.' given the constraints of the input we could
        immediately decide it is in fact braille however I felt this didn't allow
        sentences ending with '.' to be translated if one were to add this functionality later
    """

    return (
        " " in string
        or str_len % 6 != 0
        or string.count("O") + string.count(".") != str_len
    )


def main():
    string = " ".join(sys.argv[1:])
    if is_english(string):
        print(translate_to_braille(string))
    else:
        print(translate_to_english(string))


if __name__ == "__main__":
    main()
