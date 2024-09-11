import sys
from typing import List

TRANSLATION_TABLE = {
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
    " ": "......",
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
    "......": " "
}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

# Lambda expression used to apply an offset to the ascii code
# of a char to avoid duplicates in the translation table
# (Numbers 0-9 are mapped to the same braille strings as a-j)
NUMBER_OFFSET = lambda char: 58 if char in {'0', 'j'} else 48

def translate(args: List[str]) -> str:
    """
    Translates the given arguments to braille or english.

    This function takes a braille or english string and converts it to the appropriate
    language (english if it is in braille, braille if it is in english).

    Parameters:
    args (List[str]): A list of strings containing the arguments to translate.

    Returns:
    str: The arguments translated to braille or english.

    Examples:
    >>> translate(["Hello", "world"])
    .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
    >>> translate([".....O.OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO"])
    Shopify
    """
    res = ""

    if not len(args):
        return res
    
    if (
        len(args) == 1
        and len(args[0]) % 6 == 0
        and set(args[0]) <= {'.', 'O'}
    ):
        res = braille_to_english(args[0])
    else:
        res = english_to_braille(args)
    
    return res


def braille_to_english(arg: str) -> str:
    """
    Translates braille to english.

    This function takes a braille string as input and returns its translation in english.

    Parameters:
    arg (str): The braille string to translate.

    Returns:
    str: The english translation of the braille string.

    Examples:
    >>> braille_to_english(.....OO.....O.O...OO...........O.OOOO.....O.O...OO....)
    Abc 123
    >>> braille_to_english(.O.OOOOO.O..O.O...)
    42
    """
    ptr = 0
    res = ""
    is_cap, is_num = False, False

    while ptr < len(arg):
        char = str(arg[ptr:ptr+6])

        if char == CAPITAL_FOLLOWS:
            is_cap = True
        elif char == NUMBER_FOLLOWS:
            is_num = True
        else:
            translated_char = TRANSLATION_TABLE[char]

            if translated_char == " ":
                is_num = False

            if is_cap:
                translated_char = translated_char.upper()
                is_cap = False
            elif is_num:
                translated_char = chr(ord(translated_char)-NUMBER_OFFSET(translated_char))
            
            res += translated_char
        
        ptr += 6
    
    return res


def english_to_braille(args: List[str]) -> str:
    """
    Translates english to braille.

    This function takes an english text as a list of strings as input and returns its
    translation in braille.

    Parameters:
    arg (List[str]): The english text to translate, passed as a list of string arguments.

    Returns:
    str: The braille translation of the english text.

    Examples:
    >>> english_to_braille(Abc 123)
    .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
    >>> braille_to_english(42)
    .O.OOOOO.O..O.O...
    """
    ptr = 0
    res = ""
    arg = ' '.join(args)

    while ptr < len(arg):
        char = arg[ptr]

        if char.isupper():
            res += CAPITAL_FOLLOWS + TRANSLATION_TABLE[char.lower()]
        elif char.isdigit():
            res += NUMBER_FOLLOWS

            while ptr < len(arg) and arg[ptr] != " ":
                translated_char = TRANSLATION_TABLE[chr(ord(arg[ptr])+NUMBER_OFFSET(arg[ptr]))]
                res += translated_char
                ptr += 1
            
            if ptr < len(arg):
                ptr -= 1
        else:
            res += TRANSLATION_TABLE[char]

        ptr += 1
    
    return res

if __name__ == "__main__":
    print(translate(sys.argv[1:]))
