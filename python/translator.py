# Author: Christopher Rossi
# Date: 9/10/2024
# Program Descrption: Translates Braille to English, vise-versa

import sys

# Dictionary mapping for Braille letters
braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
    'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
    's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO", 'z': "O..OOO", ' ': "......"
}

# Digits in Braille
braille_numbers = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...",
    '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

# Reverse lookup dictionaries for Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

# Special Braille codes
capital_indicator = ".....O"
number_indicator = ".O.OOO"

def braille_to_string(braille_string):
    converted = ""
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]

        # Detect the capital indicator
        if braille_char == capital_indicator:
            capitalize_next = True
            i += 6
            continue

        # Detect the number mode
        if braille_char == number_indicator:
            number_mode = True
            i += 6
            continue

        # Handle space
        if braille_char == "......":
            converted += " "
            i += 6
            number_mode = False  # Number mode ends after space
            continue

        # Handle letters and numbers
        if number_mode:
            converted += reverse_braille_numbers.get(braille_char, "?")
        else:
            letter = reverse_braille_dict.get(braille_char, "?")
            if capitalize_next:
                converted += letter.upper()
                capitalize_next = False
            else:
                converted += letter

        i += 6
    return converted

def string_to_braille(word):
    converted = ""
    number_mode = False

    for letter in word:
        # Handle capitalization
        if letter.isupper():
            converted += capital_indicator
            letter = letter.lower()

        # Handle numbers
        if letter.isdigit():
            if not number_mode:
                converted += number_indicator  # Only prepend number mode indicator once
                number_mode = True
            converted += braille_numbers[letter]
        else:
            number_mode = False  # Reset number mode on any non-number
            converted += braille_dict.get(letter.lower(), "......")  # Handle letters and spaces

    return converted

def decide_english_braille(input_string):
    # Determine if input is Braille or English
    if all(c in "O." for c in input_string):  # If it consists of 'O' and '.'
        return braille_to_string(input_string)
    else:
        return string_to_braille(input_string)

# Command line input
if len(sys.argv) > 1:
    input_string = sys.argv[1]

    # Determine if the input is Braille or English, and print the formatted result
    output_string = decide_english_braille(input_string)

    # Display output in the desired format
    print(output_string)
  
