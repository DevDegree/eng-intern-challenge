# Braille dictionary
# 17/09/2024
# Ashton Sicard

import sys

def braille_to_text(input_string):
    dictionary = {
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
        "..OO.O": ".",
        "..O...": ",",
        "...OOO": "?",
        "..OOO.": "!",
        "..OO..": ":",
        "..O.O.": ";",
        "....OO": "-",
        ".O..O.": "/",
        ".OO..O": "<",
        # "O..OO.": ">", omitted due to "collision" with o
        "O.O..O": "(",
        ".O.OO.": ")",
        "......": " "
    }

    number_flag = False
    capital_flag = False
    decimal_flag = False

    result_string = ""

    for i in range(0, len(input_string), 6):
        curr_char = input_string[i:i+6]

        # Check for capital follows...
        if curr_char == ".....O":
            capital_flag = True
            continue

        # decimal follows...
        elif curr_char == ".O...O":
            decimal_flag = True
            continue

        # and number follows.
        elif curr_char == ".O.OOO":
            number_flag = True
            continue
        
        # Check flags
        if capital_flag:
            # Using ASCII values to save space, although it may be slower
            result_string += chr(ord(dictionary[curr_char]) - 32)
            capital_flag = False

        elif decimal_flag:
            result_string += "."
            decimal_flag = False

        elif number_flag:
            # check if the number has ended
            if curr_char == "......":
                number_flag = False
                result_string += " "

            # j should be translated to 0
            elif curr_char == ".OOO..":
                result_string += chr(ord(dictionary[curr_char]) - 58)
            
            # otherwise, just reduce ASCII by 48 to get the number
            else:
                result_string += chr(ord(dictionary[curr_char]) - 48)
        
        # The > character is tricky because it shares a braille code with o.
        # My assumption is that > is only ever used to compare two numbers,
        # separated from > by one space, ie. 123 > 45. 
        # We check this condition after the capital flag, as > cannot be
        # capitalized, unlike o. The below conditional represents this.
        elif curr_char == "O..OO." and\
            len(result_string) >= 2 and result_string[-2].isdigit() and\
            len(input_string) - i >= 18 and input_string[i + 12:i + 18] == ".O.OOO":
            result_string += ">"

        # If no flags or >, just add the character.
        else:
            result_string += dictionary[curr_char]

    return result_string

def text_to_braille(input_string):
    dictionary = {
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
        "o": "O..OO.", # in this case, there is no "collision" between o and >
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
        ".": "..OO.O",
        ",": "..O...",
        "?": "...OOO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        ">": "O..OO.", # no collision (must be escaped "/>" in CLI)
        "(": "O.O..O",
        ")": ".O.OO.",
        " ": "......",
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
    }

    result_string = ""

    number_flag = False

    for i, character in enumerate(input_string):
        if 65 <= ord(character) <= 90:
            result_string += ".....O" + dictionary[character.lower()]
        
        # if we were previously in the middle of a number
        elif number_flag:

            # under this condition, do not remove number flag (number has not ended)
            if character == "." and i < len(input_string) - 1 and\
                input_string[i + 1].isdigit():
                continue

            # remove number flag
            elif not character.isdigit():
                number_flag = False

            result_string += dictionary[character]
        
        # if we are at the beginning of a number
        elif character.isdigit():
            number_flag = True
            result_string += ".O.OOO" + dictionary[character]

        else:
            result_string += dictionary[character]

    return result_string

def main(*args):
    input_string = " ".join(*args)

    # Braille letters are 6 characters long, len % 6 must == 0
    # Characters must also be O or .
    if len(input_string) % 6 == 0 and\
        set(input_string) == set(["O", "."]):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main(sys.argv[1:])
