# Dictionary to translate from Braille to English
braille_to_english = {
    # Letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",

    # Numbers (Braille digits correspond to letters a-j)
    ".O.....": "1", ".O.O...": "2", "..OO...": "3", "..OO.O.": "4", ".O.O.O.": "5", "..OOOO": "6",
    "..OOO.": "7", ".O.O..": "8", ".OOO.O": "9", ".OOO..": "0",

    # Modifiers
    ".....O": "capital follows",  # Capital letters modifier
    ".O.O.O": "number follows",   # Number modifier
    "......": " ",                # Space

    # Punctuation
    "..O...": ".",   # Period
    "..OO..": ",",   # Comma
    "..OO.O": ";",   # Semicolon
    "..O.O.": ":",   # Colon
    ".O..O.": "!",   # Exclamation mark
    ".O.OO.": "?",   # Question mark
    ".O...O": "-",   # Hyphen or dash
    ".O....": "'",   # Apostrophe
    ".OO...": "/",   # Forward slash
    "O.OOOO": "(",   # Opening parenthesis
    ".OOOOO": ")",   # Closing parenthesis
    "O..O..": "<",   # Less than
    "O..O.O": ">",   # Greater than
}


# Dictionary to translate from English to Braille
english_to_braille = {
    # Lowercase letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",

    # Uppercase letters (needs capital modifier first)
    "A": ".....O" + "O.....", "B": ".....O" + "O.O...", "C": ".....O" + "OO....", "D": ".....O" + "OO.O..",
    "E": ".....O" + "O..O..", "F": ".....O" + "OOO...", "G": ".....O" + "OOOO..", "H": ".....O" + "O.OO..",
    "I": ".....O" + ".OO...", "J": ".....O" + ".OOO..", "K": ".....O" + "O...O.", "L": ".....O" + "O.O.O.",
    "M": ".....O" + "OO..O.", "N": ".....O" + "OO.OO.", "O": ".....O" + "O..OO.", "P": ".....O" + "OOO.O.",
    "Q": ".....O" + "OOOOO.", "R": ".....O" + "O.OOO.", "S": ".....O" + ".OO.O.", "T": ".....O" + ".OOOO.",
    "U": ".....O" + "O...OO", "V": ".....O" + "O.O.OO", "W": ".....O" + ".OOO.O", "X": ".....O" + "OO..OO",
    "Y": ".....O" + "OO.OOO", "Z": ".....O" + "O..OOO",

    # Numbers (prefixed by number modifier)
    "1": ".O.....", "2": ".O.O...", "3": "..OO...", "4": "..OO.O.", "5": ".O.O.O.", "6": "..OOOO",
    "7": "..OOO.", "8": ".O.O..", "9": ".OOO.O", "0": ".OOO..",

    # Space
    " ": "......",

    # Punctuation
    ".": "..O...",   # Period
    ",": "..OO..",   # Comma
    ";": "..OO.O",   # Semicolon
    ":": "..O.O.",   # Colon
    "!": ".O..O.",   # Exclamation mark
    "?": ".O.OO.",   # Question mark
    "-": ".O...O",   # Hyphen or dash
    "'": ".O....",   # Apostrophe
    "/": ".OO...",   # Forward slash
    "(": "O.OOOO",   # Opening parenthesis
    ")": ".OOOOO",   # Closing parenthesis
    "<": "O..O..",   # Less than
    ">": "O..O.O",   # Greater than
}



def is_braille(input_string):
    """Determines if the input string is Braille (composed only of 'O' and '.')"""
    return all(char in "O." for char in input_string)


def translate_braille_to_english(braille_string):
    """Translates a Braille string to English"""
    translated = []
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille_string):
        braille_char = braille_string[i:i + 6]
        i += 6

        if braille_char == ".....O":  # Capital letter indicator
            is_capital = True
            continue
        elif braille_char == ".O.O.O":  # Number indicator
            is_number = True
            continue

        english_char = braille_to_english.get(braille_char, '')

#        print(f"braille_to_english *: {english_char+braille_char}")

        if is_number:
            if english_char.isalpha():
                # Convert letters to numbers
                number_mapping = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6",
                                  "g": "7", "h": "8", "i": "9", "j": "0"}
                english_char = number_mapping.get(english_char, english_char)
            is_number = False
        elif is_capital:
            english_char = english_char.upper()
            is_capital = False

        translated.append(english_char)

 #       print(f"braille_to_english #: {english_char + braille_char}")

    return ''.join(translated)


def translate_english_to_braille(english_string):
    """Translates an English string to Braille"""
    translated = []
    for char in english_string:
        if char.isdigit():
            translated.append(".O.O.O")  # Number indicator
            number_mapping = {"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
                              "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
                              "9": ".OO...", "0": ".OOO.."}
            translated.append(number_mapping[char])
        elif char.isupper():
            translated.append(".....O")  # Capital letter indicator
            translated.append(english_to_braille[char.lower()])
        else:
            translated.append(english_to_braille[char])

#       print(f"english_to_braille: {char}")
    return ''.join(translated)


# Main logic for running from the command line
import sys

if __name__ == "__main__":
    input_strings = sys.argv[1:]  # This captures all arguments after the script name
    for input_string in input_strings:
        if is_braille(input_string):
#            print(f"braille_to_english #: {input_string}")
            print(translate_braille_to_english(input_string), end="")
        else:
#            print(f"translate_english_to_braille #: {input_string}")
            print(translate_english_to_braille(input_string), end="")