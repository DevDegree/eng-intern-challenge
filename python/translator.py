# QUESTIONS:
    # There were no instructions regarding decimal follows and the non alphanumeric symbols in
    # the alphabet.
    # I wasn't sure if we needed to implement this portion, but I chose to implement decimal
    # follows to behave like capital follows and for this to appear before any special character.
    # The 'O' character has the same braille translation as the '>' character.

import sys

# English to Braille mappings
e_to_b_alpha = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

e_to_b_num = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

e_to_b_sym = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# Braille to English mappings
b_to_e_alpha = {v: k for k, v in e_to_b_alpha.items()}
b_to_e_num = {v: k for k, v in e_to_b_num.items()}
b_to_e_sym = {v: k for k, v in e_to_b_sym.items()}

# Special characters for capitalization and numbers
CAPITAL_FOLLOWS = '.....O' # Following character is a capital
NUMBER_FOLLOWS = '.O.OOO'  # Follow characters are numeric until we read a SPACE character
DECIMAL_FOLLOWS = '.O...O' # Behaves like capital follows
SPACE = '......'

def braille_to_english(braille_str):
    english_str = ''
    capital_follows = False
    number_follows = False
    decimal_follows = False

    for x in range(0, len(braille_str), 6):
        character = braille_str[x:x+6]

        if character == CAPITAL_FOLLOWS:
            capital_follows = True
        elif character == NUMBER_FOLLOWS:
            number_follows = True
        elif character == DECIMAL_FOLLOWS:
            decimal_follows = True
        elif character == SPACE:
            if not number_follows:
                english_str += ' '
            number_follows = False
        elif number_follows and character in b_to_e_num:
            num_char = b_to_e_num[character]
            english_str += num_char
        elif decimal_follows and character in b_to_e_sym:
            sym_char = b_to_e_sym[character]
            english_str += sym_char
            decimal_follows = False
        elif character in b_to_e_alpha:
            english_char = b_to_e_alpha[character]

            if (capital_follows):
                english_char = english_char.upper()
                capital_follows = False
            
            english_str += english_char

    return english_str

def english_to_braille(english_str):
    braille_str = ''
    number_follows = False

    for x in range(0, len(english_str)):
        character = english_str[x]

        if character.isnumeric():
            if not number_follows:
                braille_str += NUMBER_FOLLOWS
                number_follows = True
            braille_str += e_to_b_num[character]
        elif character.isspace():
            braille_str += SPACE
            number_follows = False
        else:
            if number_follows:
                # Add terminating space
                braille_str += SPACE
                number_follows = False

            if character.isupper():
                braille_str += CAPITAL_FOLLOWS
                braille_str += e_to_b_alpha[character.lower()]
            elif character in e_to_b_alpha:
                braille_str += e_to_b_alpha[character]
            elif character in e_to_b_sym:
                braille_str += DECIMAL_FOLLOWS
                braille_str += e_to_b_sym[character]

    return braille_str

if __name__ == "__main__":
    # Combine all arguments into a single input string
    input_str = ' '.join(sys.argv[1:])

    if len(input_str) % 6 == 0 and all(c in 'O.' for c in input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))
