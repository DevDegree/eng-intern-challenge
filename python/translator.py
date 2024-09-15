
import sys
from  braille_dictionaries import (
    english_to_braille,
    braille_to_english,
    number_map,
    number_map_reversed,
)

def is_braille(input_string):
    return all(c in ('0', '.','')for c in input_string)

# Algorithm
#     The function checks each character in the input string.
#     if all characters are either 'O','.', or a space, it considers the input as Braille.

def english_to_braille_translation(text):
    """
    Converts English text to Braille
    """
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            # Add capital sign
            result.append(english_to_braille['capital'])
            char = char.lower()

            if char.isdigit():
                if not number_mode:
                    # Enter number mode
                    result.append(english_to_braille['number'])
                    number_mode = True
                # Map digit to corresponding Braille 
                letter_equivalent = number_map[char]
                result.append(english_to_braille[letter_equivalent])
            else:
                if number_mode:
                    # Exit number mode
                    number_mode = False
                # Append Braille pattern for the character
                braille_char = english_to_braille.get(char, '')
                result.append(braille_char)

    return ''.join(result)

def braille_to_english_translation(braille_text):
    """
    Converts Braille notation to English text.
    """
    result = []

