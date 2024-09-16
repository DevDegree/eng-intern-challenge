# translator.py

import sys
from braille_dictionaries import (
    english_to_braille,
    braille_to_english,
    number_map,
    number_map_reversed,
)

def is_braille(input_string):
    """
    Check if the input string is Braille by verifying its characters.
    """
    return all(c in ('O', '.', ' ') for c in input_string)

def english_to_braille_translation(text):
    """
    Converts English text to Braille notation.
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
            # Map digit to corresponding Braille pattern
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
    result = []
    number_mode = False
    capital_mode = False

    # Remove spaces and split the text into Braille cells of 6 characters
    braille_text = braille_text.replace(' ', '')
    braille_cells = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    for braille_cell in braille_cells:
        if braille_cell == english_to_braille['capital']:
            capital_mode = True
            continue

        if braille_cell == english_to_braille['number']:
            number_mode = True
            continue

        if braille_cell == english_to_braille[' ']:
            result.append(' ')
            number_mode = False
            continue

        # Get the corresponding character
        char = braille_to_english.get(braille_cell, '')
        
        if number_mode:
            # Convert to digit
            digit = number_map_reversed.get(char, '')
            result.append(digit)
        else:
            if capital_mode:
                char = char.upper()
                capital_mode = False
            result.append(char)

    return ''.join(result)


def main():
    # Combine all command-line arguments into one string
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        # Input is Braille
        output = braille_to_english_translation(input_text)
    else:
        # Input is English
        output = english_to_braille_translation(input_text)

    print(output)

if __name__ == '__main__':
    main()
