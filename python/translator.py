import re
import sys

# Dictionaries for letters, numbers, and punctuation to Braille
ALPHABET_TO_BRAILLE = {
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....',
    'd': 'OO.O..', 
    'e': 'O..O..',
    'f': 'OOO...', 
    'g': 'OOOO..',
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.', 
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'
}

NUMBERS_TO_BRAILLE = {
    '0': '.OOO..',
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..',
    '8': 'O.OO..', 
    '9': '.OO...'
}

PUNCTUATION_TO_BRAILLE = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.', 
    '(': 'O.O..O', 
    ')': '.O.OO.'
}

# Global state variables for mode tracking
mode = "alpha"  # Keeps track of whether we're in letter, number, or punctuation mode
result = ""  # Holds the translation result

def translate(input_string):
    """
    Main translation function that checks if input is Braille or English and translates accordingly.
    """
    global result
    result = ""
    
    if is_braille(input_string):
        translate_braille_to_english(input_string)
    else:
        translate_english_to_braille(input_string)

def is_braille(input_string):
    """
    Check if the input string contains only Braille characters (O and .).
    """
    braille_chars = {'O', '.'}
    return all(char in braille_chars or char.isspace() for char in input_string)

def translate_english_to_braille(input_string):
    """
    Translate English characters to Braille.
    """
    global mode, result
    mode = "alpha"
    
    for char in input_string:
        if char.isalpha():  # Handling letters
            if char.isupper():  # Handling uppercase letters
                result += '.....O'  # Capital letter marker in Braille
            result += ALPHABET_TO_BRAILLE[char.lower()]  # Add corresponding Braille
        elif char.isdigit():  # Handling numbers
            if mode != "nums":
                result += ".O.OOO"  # Switch to number mode
                mode = "nums"
            result += NUMBERS_TO_BRAILLE[char]
        elif char in PUNCTUATION_TO_BRAILLE:  # Handling punctuation
            if mode != "deci":
                result += ".O...O"  # Switch to punctuation mode
                mode = "deci"
            result += PUNCTUATION_TO_BRAILLE[char]
        elif char == " ":
            result += "......"  # Space in Braille

def translate_braille_to_english(braille_string):
    """
    Translate Braille characters to English.
    """
    global mode, result
    mode = "alpha"
    position = 0
    
    # Process Braille in chunks of 6 (Braille characters)
    while position <= len(braille_string) - 6:
        braille_chunk = braille_string[position:position + 6]
        
        if braille_chunk == ".O.OOO":  # Switch to number mode
            mode = "nums"
        elif braille_chunk == ".O...O":  # Switch to punctuation mode
            mode = "deci"
        elif braille_chunk == "......":  # Space in Braille
            result += " "
        else:
            decode_braille_chunk(braille_chunk)
        
        position += 6

def decode_braille_chunk(braille_chunk):
    """
    Decodes a single Braille chunk based on the current mode.
    """
    global mode, result
    
    if mode == "alpha":
        if braille_chunk == ".....O":  # Capital letter marker
            next_chunk = result[-6:]  # Look at the next chunk for the capital letter
            result += ALPHABET_TO_BRAILLE[next_chunk].upper()
        else:
            result += get_english_character_from_braille(braille_chunk, ALPHABET_TO_BRAILLE)
    elif mode == "nums":
        result += get_english_character_from_braille(braille_chunk, NUMBERS_TO_BRAILLE)
        mode = "alpha"  # Switch back to alpha mode after processing numbers
    elif mode == "deci":
        result += get_english_character_from_braille(braille_chunk, PUNCTUATION_TO_BRAILLE)
        mode = "alpha"  # Switch back to alpha mode after punctuation

def get_english_character_from_braille(braille_chunk, braille_dict):
    """
    Find the English character for a given Braille chunk in the provided Braille dictionary.
    """
    for key, value in braille_dict.items():
        if value == braille_chunk:
            return key
    return '?'  # Return '?' for unrecognized Braille characters

# Entry point for running the translator script via command-line
if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    translate(input_string)
    print(result)
