import sys

"""
Purpose:
- This program translates English text to Braille and vice versa.

USAGE
python translator.py <english> <text> <here>
python translator.py <braille text here>
"""

# ASSUMPTIONS
# - The > character will always be followed by a space, to ensure that it is used to close the < character. Additionally, it is assumed that within <>, there will be no spaces.
# - No alphabetic characters will be used following a number, due to the possible overlap. However, punctuation can be used.

# CONSTANTS
SPACE = "......"
CAPITAL = ".....O"
DECIMAL = ".O...O"
NUMBER = ".O.OOO"

CHAR_TO_BRAILLE = {
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

    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": SPACE,
}

# create a reverse mapping of CHAR_TO_BRAILLE
BRAILE_ITEMS = list(CHAR_TO_BRAILLE.items())
BRAILE_TO_ALPHA = {value: key for key, value in BRAILE_ITEMS[0:26]}
BRAILE_TO_NUMBER = {value: key for key, value in BRAILE_ITEMS[26:36]}
BRAILE_TO_PUNCTUATION = {value: key for key, value in BRAILE_ITEMS[36:]}

# add decimal point
BRAILE_TO_NUMBER[DECIMAL] = "."

def is_braille(string: str) -> bool:
    """
    Determines if `string` is in Braille or not. 
    
    A string is considered to be in Braille if it is:
    - Divisible by 6
    - Contains only "." and "0" characters

    :param string: The string to check.
    :return: True if `string` is in Braille, False otherwise.
    """
    
    is_divisible_by_6 = len(string) % 6 == 0
    is_braille_chars = all(char in "O." for char in string)

    return is_divisible_by_6 and is_braille_chars

def use_greater_than(string: str, result:str, i: int) -> bool:
    """
    Determines if the character is O or >, based on the context.
    - If < is found before > and there is a space after >, then it is a bracket. The space is needed to ensure that it is used to close the < and is not interfering with an O.

    :param string: The string to check.
    :param result: The current result string.
    :param i: The current index of the string (multiple of 6).

    :return: True if the character is >, False otherwise.
    """

    # check if there exists a < before the current index.
    open_index = result.rfind("<")
    has_open_bracket = open_index != -1 and open_index > result.rfind(">")

    # check if there is a space after the current index or is end of string.
    has_space = i + 6 == len(string) or string[i + 6: i + 12] == SPACE

    return has_open_bracket and has_space

def translate_to_braille(string: str) -> str:
    """
    Translates `string` to Braille.

    :param string: The string to translate.
    :return: The Braille translation of `string`.
    """
    
    is_number = False

    result = ""

    for char in string:
        if char == " ":
            result += SPACE
            is_number = False
        elif char.isupper():
            result += CAPITAL
            char = char.lower()
            result += CHAR_TO_BRAILLE[char]
        elif char.isdigit() and not is_number:
            result += NUMBER
            result += CHAR_TO_BRAILLE[char]

            is_number = True
        elif is_number:
            # handle `.` in numbers, as it uses DECIMAL_FOLLOWS instead.
            if char == ".":
                result += DECIMAL
            else:
                result += CHAR_TO_BRAILLE[char]
        else:
            result += CHAR_TO_BRAILLE[char]

    return result

def translate_to_english(string: str) -> str:
    """
    Translates `string` from Braille to English.

    :param string: The string to translate.
    :return: The English translation of `string`.
    """
    is_number = False
    is_capital = False

    result = ""

    # iterate over the string in chunks of 6 (due to Braille encoding size)
    for i in range(0, len(string), 6):
        braille_char = string[i:i+6]

        # handle special cases, dont do anything because we want to skip them.
        if braille_char == SPACE:
            is_number = False
            result += " "
        elif braille_char == CAPITAL:
            is_capital = True
        elif braille_char == NUMBER:
            is_number = True
        else:
            if is_capital:
                result += BRAILE_TO_ALPHA[braille_char].upper()
                is_capital = False
            elif is_number:
                punctuation = BRAILE_TO_PUNCTUATION.get(braille_char)

                # handle punctuation (except `.` as it is handeled seperately) first, as it is a smaller set. 
                if punctuation and punctuation != ".":
                    result += punctuation
                else:
                    result += BRAILE_TO_NUMBER[braille_char]
            else:
                # If the character is a punctuation first, as it is a smaller set, anything eles should be a alphabet.
                punctuation = BRAILE_TO_PUNCTUATION.get(braille_char)

                if punctuation and punctuation == ">" and use_greater_than(string, result, i):
                    # verify that there was a previous character (<) opens the bracket OR used with a number for comparison.
                    result += punctuation
                elif punctuation and punctuation != ">" and braille_char in BRAILE_TO_PUNCTUATION:
                    result += punctuation
                else:
                    result += BRAILE_TO_ALPHA[braille_char]

    return result

def translate(string: str) -> str:
    """
    Determines if `string` is in Braille or not and translates it accordingly.

    :param string: The string to translate.
    :return: The translation of `string`.
    """
    
    if is_braille(string):
        return translate_to_english(string)
    else:
        return translate_to_braille(string)

if __name__ == "__main__":
    string = " ".join(sys.argv[1:])
    print(translate(string))