# Translator Script for Shopify Technical Challenge
# Submission by: Masoud Karimi

import sys

# Constants for special Braille symbols
BRAILLE_CAPITAL_PREFIX = ".....O"
BRAILLE_NUMBER_PREFIX = ".O.OOO"

# Mapping of English letters, punctuation, and space to Braille
english_to_braille_map = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..OOO.",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

# Mapping of English digits to Braille
english_to_braille_number_map = {
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

# Reverse mappings for Braille to English
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}
braille_to_english_number_map = {v: k for k, v in english_to_braille_number_map.items()}

def main():
    # Ensure the script has arguments
    if len(sys.argv) < 2:
        print("")
        quit()

    # Extract arguments and determine if input is Braille or English
    input_args = sys.argv[1:]
    is_braille = input_args[0][0] in ['O', '.']

    # Convert based on input type
    if is_braille:
        convert_braille_to_english(input_args)
    else:
        convert_english_to_braille(input_args)

def convert_braille_to_english(input_args):
    braille_text = input_args[0]
    # Split Braille string into individual character blocks
    braille_characters = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    capital_next = False
    number_mode = False
    output_text = ""

    # Process each Braille character
    for braille_char in braille_characters:
        if braille_char == BRAILLE_CAPITAL_PREFIX:
            capital_next = True
        elif braille_char == BRAILLE_NUMBER_PREFIX:
            number_mode = True
        elif capital_next:
            # Convert Braille to English, handling capitalization
            english_char = braille_to_english_map.get(braille_char, '?').upper()
            output_text += english_char
            capital_next = False
        elif braille_char == "......":
            # Handle spaces
            output_text += " "
            number_mode = False
        elif number_mode:
            # Convert Braille to English digit
            english_digit = braille_to_english_number_map.get(braille_char, '?')
            output_text += english_digit
        else:
            # Convert Braille to lowercase English character
            english_char = braille_to_english_map.get(braille_char, '?')
            output_text += english_char

    print(output_text)

def convert_english_to_braille(input_args):
    english_text = " ".join(input_args)
    number_mode = True
    output_braille = ""

    # Process each English character
    for char in english_text:
        if char.isupper():
            # Handle capitalization
            output_braille += BRAILLE_CAPITAL_PREFIX
            char = char.lower()
            braille_char = english_to_braille_map.get(char, '?')
            output_braille += braille_char
        elif char == " ":
            # Handle spaces
            number_mode = True
            braille_char = english_to_braille_map.get(char, '?')
            output_braille += braille_char
        elif char.isdigit():
            if number_mode:
                output_braille += BRAILLE_NUMBER_PREFIX
                number_mode = False
            braille_char = english_to_braille_number_map.get(char, '?')
            output_braille += braille_char
        else:
            # Convert lowercase English to Braille
            braille_char = english_to_braille_map.get(char, '?')
            output_braille += braille_char

    print(output_braille)

if __name__ == "__main__":
    main()
