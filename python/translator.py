# Braille Translator (Python) - Shopify Engineering Challenge
# Author: Krish Chopra
# Date: September 9, 2024


import sys


############################## DATA/SYMBOLS ###################################


# dictionary that maps English letters to Braille sequences
braille_dictionary = {
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
    ".": "..OO.O",
}

# ASCII value of 'a' minus 1, used to map numbers to their corresponding letters
ASCII_OFFSET = ord("a") - 1

# dictionary that maps numbers to Braille sequences
number_dictionary = {
    str(i): braille_dictionary[chr(ASCII_OFFSET + i)] for i in range(1, 10)
}
number_dictionary["0"] = braille_dictionary["j"]

# dictionaries that map Braille sequences to English letters and numbers
braille_to_english_dict = {v: k for k, v in braille_dictionary.items()}
braille_to_number_dict = {v: k for k, v in number_dictionary.items()}

# special symbols
capital_follows = ".....O"
number_follows = ".O.OOO"


################################ FUNCTIONS ####################################


def is_braille(text):
    return set(text).issubset(".O") and len(text) % 6 == 0


def english_to_braille(text):
    result = []
    is_number = False

    for char in text:
        # handle capitalization
        if char.isupper():
            result.append(capital_follows)
            char = char.lower()

        # handle numbers
        if char.isdigit():
            if not is_number:
                result.append(number_follows)
                is_number = True
            result.append(number_dictionary.get(char, "......"))
        else:
            is_number = False
            result.append(braille_dictionary.get(char, "......"))

    return "".join(result)


def braille_to_english(text):
    result = []
    # split the Braille text into 6 character sequences
    braille_sequences = [text[i : i + 6] for i in range(0, len(text), 6)]
    is_capital = False
    is_number = False

    for sequence in braille_sequences:
        if sequence == capital_follows:
            is_capital = True
        elif sequence == number_follows:
            is_number = True
        elif is_number:
            char = braille_to_number_dict.get(sequence, " ")
            if char == " ":
                is_number = False
                char = braille_to_english_dict.get(sequence, " ")
            result.append(char)
        elif is_capital:
            char = braille_to_english_dict.get(sequence, " ").upper()
            result.append(char)
            is_capital = False
        else:
            char = braille_to_english_dict.get(sequence, " ")
            result.append(char)
    return "".join(result)


def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)


############################# PROGRAM EXECUTION ###############################


if __name__ == "__main__":
    # check if a string was provided as a command-line argument
    if len(sys.argv) < 2:
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])

    # translate and print the result!
    print(translate(input_text))


################################### END #######################################


""" Thanks for reviewing my submission, Shopify! Looking forward to sharing more
about myself with you during the interview process :) """
