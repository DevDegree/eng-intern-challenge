import sys
# Braille Translation Module

# This module provides functionality to convert between English text and Braille representation.

# Mapping of lowercase English letters to their Braille equivalents
ENGLISH_TO_BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

# Mapping of digits to their Braille equivalents
ENGLISH_TO_BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Mapping of symbols to their Braille equivalents
ENGLISH_TO_BRAILLE_SYMBOLS = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# Mapping of flags to their Braille equivalents
BRAILLE_FLAGS = {
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

# Inverted mappings for Braille to English conversion
BRAILLE_TO_ENGLISH_LETTERS = {v: k for k, v in ENGLISH_TO_BRAILLE_LETTERS.items()}
BRAILLE_TO_ENGLISH_NUMBERS = {v: k for k, v in ENGLISH_TO_BRAILLE_NUMBERS.items()}
BRAILLE_TO_ENGLISH_SYMBOLS = {v: k for k, v in ENGLISH_TO_BRAILLE_SYMBOLS.items()}
BRAILLE_TO_ENGLISH_FLAGS = {v: k for k, v in BRAILLE_FLAGS.items()}

def validate_braille_input(braille_text):
    '''
    Validates whether the input string is a valid Braille sequence
    Parameters:
        braille_text (str): The input string to validate
    Returns:
        bool: True if valid Braille, False otherwise
    '''
    if len(braille_text) % 6 != 0:
        return False
    for character in braille_text:
        if character not in {'.', 'O'}:
            return False
    return True

def convert_text_to_braille(english_text):
    '''
    Converts English text to its Braille representation
    Parameters:
        english_text (str): The English text to convert
    Returns:
        str: The corresponding Braille string
    '''
    braille_output = ""
    is_numeric = False

    for char in english_text:
        if char.isdigit():
            if not is_numeric:
                is_numeric = True
                braille_output += BRAILLE_FLAGS['number']
            braille_output += ENGLISH_TO_BRAILLE_NUMBERS[char]
            continue

        if char.islower():
            braille_output += ENGLISH_TO_BRAILLE_LETTERS[char]
        elif char in ENGLISH_TO_BRAILLE_SYMBOLS:
            braille_output += ENGLISH_TO_BRAILLE_SYMBOLS[char]
            is_numeric = False
        elif char.isupper():
            braille_output += BRAILLE_FLAGS['capital'] + ENGLISH_TO_BRAILLE_LETTERS[char.lower()]
        else:
            sys.exit(f"Error: Unsupported character '{char}' in input.")

    return braille_output

def convert_braille_to_text(braille_text):
    '''
    Converts Braille string to its English text representation
    Parameters:
        braille_text (str): The Braille string to convert
    Returns:
        str: The corresponding English text
    '''
    english_output = ""
    is_numeric, is_capital = False, False

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]

        if braille_char == BRAILLE_FLAGS['number']:
            is_numeric = True
        elif braille_char == BRAILLE_FLAGS['capital']:
            is_capital = True
        elif braille_char in BRAILLE_TO_ENGLISH_LETTERS:
            if is_numeric:
                english_output += BRAILLE_TO_ENGLISH_NUMBERS.get(braille_char, '?')
            else:
                letter = BRAILLE_TO_ENGLISH_LETTERS[braille_char]
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                english_output += letter
        elif braille_char in BRAILLE_TO_ENGLISH_SYMBOLS:
            english_output += BRAILLE_TO_ENGLISH_SYMBOLS[braille_char]
            is_numeric = False
        else:
            sys.exit("Error: Invalid Braille sequence encountered.")

    return english_output

def main():
    '''
    Main function to handle input and perform translation between English and Braille.
    '''
    input_arguments = sys.argv[1:]
    if not input_arguments:
        sys.exit("Error: No input provided.")

    input_string = ' '.join(input_arguments)
    if validate_braille_input(input_string):
        translated_output = convert_braille_to_text(input_string)
    else:
        translated_output = convert_text_to_braille(input_string)

if __name__ == "__main__":
    main()
