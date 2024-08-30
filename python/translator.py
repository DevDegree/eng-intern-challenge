import sys
from typing import Dict, List

BRAILLE_ENCODINGS: Dict[str, str] = {
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
    't': '.OO.O.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......',
    '&': '.....O',  # Capital follows
    '#': '.O.OOO'   # Number follows
}
def translate_braille_to_english(user_input: str) -> str:
    """Translates a braille string to English.

    Keyword arguments:
    user_input -- the user's braille argument
    """

    braille_symbols = []
    english_translation = ''
    numbers_mode = False

    for i in range(0, len(user_input), 6):
        braille_symbols.append(user_input[i: i + 6])

    i = 0
    while i < len(braille_symbols):
        symbol = braille_symbols[i]

        # Check for "space" symbol
        if symbol == BRAILLE_ENCODINGS[' ']:
            numbers_mode = False

        # Check for "capital follows" symbol
        if symbol == BRAILLE_ENCODINGS['&']:
            capitalize_next = True
            i += 1
            continue

        # Check for "number follows" symbol
        if symbol == BRAILLE_ENCODINGS['#']:
            numbers_mode = True
            i += 1
            continue

        letter = get_letter_from_braille(symbol, numbers_mode)
        if capitalize_next:
            letter = letter.upper()
            capitalize_next = False
        
        english_translation += letter
        i += 1
    
    return english_translation

def get_duplicate_chars_from_braille(braille_symbol: str) -> List[str]:
    """Returns all keys  associated with a given braille symbol.
    
        Keyword arguments:
        braille_symbol -- a length-6 braille string
    """

    return [char for char, symbol in BRAILLE_ENCODINGS.items() if symbol == braille_symbol]

def get_letter_from_braille(braille_symbol: str, numbers_mode: bool) -> str:
    """Returns the english letter associated with the braille symbol.
    
        Keyword arguments:
        braille_symbol -- a length-6 braille string
        numbers_mode -- a boolean that checks if we are currently in a series of numbers
    """

    duplicate_chars = get_duplicate_chars_from_braille(braille_symbol)    # may contain a letter and a digit

    if len(duplicate_chars) == 0:
        raise ValueError(f"The braille symbol {braille_symbol} was not recognized.")
    
    chosen_char = duplicate_chars[-1] if numbers_mode else duplicate_chars[0]
    return chosen_char

def translate_english_to_braille(user_input: str) -> str:
    """Translates an English string to braille.
    
        Keyword arguments:
        user_input -- the user's braille argument
    """
    braille_translation = ''
    numbers_mode = False

    for char in user_input:

        if char == ' ':
            numbers_mode = False

        if char.isupper():
            braille_translation += BRAILLE_ENCODINGS['&']
            char = char.lower()
        
        if char.isdigit() and numbers_mode == False:
            braille_translation += BRAILLE_ENCODINGS['#']
            numbers_mode = True

        braille_translation += BRAILLE_ENCODINGS[char]
    
    return braille_translation

def main(): 
    user_input = ' '.join(sys.argv[1:])
    if len(user_input) % 6 == 0 and all(c in 'O.' for c in user_input):
        result = translate_braille_to_english(user_input)
    else:
        result = translate_english_to_braille(user_input)
    
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: translator.py requires 1 or more string arguments.")
        sys.exit(1)
    else:
        main()