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
    """
    Converts Braille notation to English text.
    """
    result = []
    i = 0
    number_mode = False
    capital_mode = False

    # Remove spaces to process Braille cells correctly
    braille_text = braille_text.replace(' ', '')

    while i < len(braille_text):
        # Extract one Braille cell (6 dots)
        braille_cell = braille_text[i:i+6]

        if braille_cell == english_to_braille['capital']:
            # Set capital mode for next character
            capital_mode = True
        elif braille_cell == english_to_braille['number']:
            # Enter number mode
            number_mode = True
        else:
            if braille_cell == english_to_braille[' ']:
                # Handle space
                result.append(' ')
                number_mode = False  # Reset number mode at space
            else:
                if number_mode:
                    # Map Braille pattern to digit
                    letter = braille_to_english.get(braille_cell, '')
                    digit = number_map_reversed.get(letter, '')
                    result.append(digit)
                else:
                    # Map Braille pattern to letter
                    char = braille_to_english.get(braille_cell, '')
                    if capital_mode:
                        char = char.upper()
                        capital_mode = False
                    result.append(char)
        i += 6  # Move to the next Braille cell

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
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
