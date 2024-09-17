# Jinda Zhang SU24 Shopify Intern Challenge

import sys

# Define mappings for Braille to English characters
braille_to_text_char = {
    "......": " ", "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", 
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", 
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", 
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", 
    ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z"
}

# Define mappings for Braille to English numbers
braille_to_text_num = {
    ".OOOO.": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", 
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".....O": "capital follows", ".O.OOO": "number follows"
}

# Define mappings for English to Braille characters
text_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "0": ".OOOO.", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    " ": "......"
}

# Braille symbols for special prefixes
num_prefix = ".O.OOO"
cap_prefix = ".....O"


def is_text(input_string):
    """Determines if the input is in English format."""
    return all(ch.isalpha() or ch.isdigit() or ch.isspace() for ch in input_string)


def is_braille(input_string):
    """Determines if the input is in Braille format."""
    return all(ch in 'O.' for ch in input_string.replace(' ', '')) and len(input_string.replace(' ', '')) % 6 == 0


def text_to_braille_conversion(input_string):
    """Converts English text to Braille."""
    braille_output = []
    num_mode = False

    for ch in input_string:
        if ch.isdigit():
            if not num_mode:
                braille_output.append(num_prefix)
                num_mode = True
            braille_output.append(text_to_braille[ch])
        elif ch.isalpha():
            if ch.isupper():
                braille_output.append(cap_prefix)
                ch = ch.lower()
            braille_output.append(text_to_braille[ch])
            num_mode = False  # Reset number mode after letter
        elif ch == ' ':
            braille_output.append(text_to_braille[' '])
            num_mode = False  # Reset number mode on space

    return ''.join(braille_output)


def braille_to_text_conversion(input_string):
    """Converts Braille representation back to English text."""
    text_output = []
    current_index = 0
    num_mode = False

    # Break the input into 6-character Braille blocks
    braille_blocks = [input_string[i:i+6] for i in range(0, len(input_string), 6)]

    while current_index < len(braille_blocks):
        current_block = braille_blocks[current_index]

        if current_block == cap_prefix:
            # Handle capital letters
            num_mode = False  # Exit number mode when encountering a capital letter
            current_index += 1
            if current_index < len(braille_blocks):
                current_block = braille_blocks[current_index]
                text_output.append(braille_to_text_char[current_block].upper())
        elif current_block == num_prefix:
            # Enter number mode
            num_mode = True
        elif num_mode:
            # In number mode, interpret Braille as numbers
            if current_block == "......":
                num_mode = False  # Exit number mode on a space
            else:
                text_output.append(braille_to_text_num[current_block])
        else:
            # Regular letter interpretation
            text_output.append(braille_to_text_char[current_block])

        current_index += 1

    return ''.join(text_output)


def main():
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_text_conversion(input_string))
    elif is_text(input_string):
        print(text_to_braille_conversion(input_string))
    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()