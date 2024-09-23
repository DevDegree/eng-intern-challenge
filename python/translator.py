'''
Author: Raghav Vasudeva
Email: r2vasude@uwaterloo.ca

Project Overview (Braille Translator):
This program automatically identifies which language to translate to, performs the translation, and then prints the result to the terminal.
It also includes exception checking to ensure the code doesn't process input it does not expect.

Assumptions:
- '>' and 'o' have the same Braille encoding. Therefore, the program will default to choosing 'o' when converting from Braille to English.
- Any Braille input will not have spaces in it.
- The Braille encoding for "decimal follows" is only added if "number_follows" is active.
'''

import sys

# defining key dictionaries and variables
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_PUNCTUATION = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
DECIMAL_FOLLOWS = '.O...O'

ENGLISH_LETTERS = {v: k for k, v in BRAILLE_LETTERS.items()}
ENGLISH_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}
ENGLISH_PUNCTUATION = {v: k for k, v in BRAILLE_PUNCTUATION.items()}

def is_braille(text: str) -> bool:
    '''
    is_braille(text) returns true if the text is a Braille encoding and false otherwise

    Parameters:
    text (str): the input string
    Returns:
    (bool): true if the text is a Braille encoding, and false otherwise
    if all characters in 'text' are either 'O' or '.' then 'text' is a Braille encoding; it is an English encoding otherwise
    '''

    for c in text:
        if c not in 'O.':
            return False
        
    return True

def english_to_braille(text: str) -> str:
    '''
    english_to_braille(text) returns the translated Braille string of the Englist 'text'

    Parameters:
    text (str): the input English string
    Returns:
    (str): the translated Braille string
    
    '''

    result = []
    num_mode = False

    for c in text:
        # if 'c' is a number
        if c.isdigit():
            # checking if we are not currently in num_mode, and appending to the result accordingly
            if not num_mode:
                num_mode = True
                result.append(NUMBER_FOLLOWS)

            result.append(BRAILLE_NUMBERS[c])
        
        # if 'c' is a letter
        elif c.isalpha():
            # checking if it's upper case, and appending to the result accordingly
            if c.isupper():
                result.append(CAPITAL_FOLLOWS)
            
            result.append(BRAILLE_LETTERS[c.lower()])

        # if 'c' is a punctuation symbol
        elif c in BRAILLE_PUNCTUATION:
            if num_mode and c == '.':
                result.append(DECIMAL_FOLLOWS)
            if c == ' ':
                num_mode = False

            result.append(BRAILLE_PUNCTUATION[c])
            
    return ''.join(result)

def braille_to_english(text: str) -> str:
    '''
    braille_to_english(text) returns the translated English string of the Braille 'text'

    Parameters:
    text (str): the input Braille string
    Returns:
    (str): the translated English string
    
    '''

    # Note: at this point, the length of the string must be a multiple of 6, given that each Braille character has length 6
    
    result = []

    num_mode = False

    text_length = len(text)
    i = 0

    while i < text_length:
        c = text[i: i+6]

        # checking if 'c' is the capital_follows symbol
        if c == CAPITAL_FOLLOWS:
            i += 6
            next_c = text[i:i+6]
            result.append(ENGLISH_LETTERS[next_c].upper())
        
        # checking if 'c' is the number_follows symbol
        elif c == NUMBER_FOLLOWS:
            num_mode = True
        
        # checking if 'c' is the decimal_follows symbol
        elif c == DECIMAL_FOLLOWS:
            continue

        # checking if 'c' is a Braille symbol for a number AND we are supposed to be reading numbers
        elif num_mode and c in ENGLISH_NUMBERS:
            result.append(ENGLISH_NUMBERS[c])

        else:
            # checking if 'c' is a symbol for an English letter
            if c in ENGLISH_LETTERS:
                result.append(ENGLISH_LETTERS[c])

            # otherwise 'c' must be a symbol for English punctuation
            elif c in ENGLISH_PUNCTUATION:
                result.append(ENGLISH_PUNCTUATION[c])
            num_mode = False
        
        i += 6

    return ''.join(result)

def main() -> None:
    '''
    The main function processes the input, translates it, and prints the result to the terminal
    No parameters
    Returns None
    '''

    # error checking to make sure sufficient command line arguments are provided
    if len(sys.argv) <= 1:
        print("Usage: python3 translator.py <input_string>")
        sys.exit()

    inp_text = ' '.join(sys.argv[1:])

    if is_braille(inp_text):
        # Braille input is invalid if its length is not divisible by 6 (because each symbol has length 6)
        if len(inp_text) % 6 != 0:
            print("Invalid Braille text")
            sys.exit()

        print(braille_to_english(inp_text))

    else:
        print(english_to_braille(inp_text))

if __name__ == "__main__":
    main()
