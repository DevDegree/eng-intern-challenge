from textwrap import wrap
import sys

# CONSTANTS
# Hashmaps representing alphabet, numbers, special characters, and punctuation to braille
ALPHABET = {
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
}

NUMBERS =  {
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
}

SPECIAL_CHARAS = {
    'capital' : '.....0', 'number':'.0.000', ' ':'......'
}

PUNCTUATION = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.O..O.',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

# Hashmaps (reversed from above) to represent braille mapping to alphbabet, numbers, special characters, & punctuation
BRAILLE_TO_ALPHABET = {val : key for key, val in ALPHABET.items()}
BRAILLE_TO_NUMBERS = {val : key for key, val in NUMBERS.items()}
BRAILLE_TO_SPECIAL_CHARAS = {val : key for key, val in SPECIAL_CHARAS.items()}
BRAILLE_TO_PUNCTUATION = {val: key for key, val in PUNCTUATION.items()}

# Convert from Braille - English
def braille_to_eng(braille: str) -> str:
    # variable to be returned & state tracking for capitals & numbers
    final_string = ''
    is_capital, is_number = False, False
    
    # Break braille string into groups of 6 for readability
    braille_list = wrap(braille, 6)
    
    for group in braille_list:
        # Check for special character symbols, changing states if necessary 
        if group == BRAILLE_TO_SPECIAL_CHARAS['.....0']:
            is_capital = True
        elif group == BRAILLE_TO_SPECIAL_CHARAS['.0.000']:
            is_number = True
        elif group == BRAILLE_TO_SPECIAL_CHARAS['......']:
            final_string += " "
            is_number = False
        # Add numbers to string
        elif is_number:
            final_string += BRAILLE_TO_NUMBERS.get(group)
        # If alphabet, check if uppercase otherwise add letter normally
        elif group in BRAILLE_TO_ALPHABET:
            letter = BRAILLE_TO_ALPHABET.get(group)
            if is_capital:
                final_string += letter.upper()
                is_capital = False
            else:
                final_string += letter
        # Add punctuation
        else:
            punc = BRAILLE_TO_PUNCTUATION.get(group)
            final_string += punc
    
    return final_string


# Convert from English -> Braille
def eng_to_braille(text: str) -> str:
    # variable to be returned & state tracking for numbers
    final_string = ''
    is_number = False
    
    for chara in text:
        # If alphabetical, determine if uppercase special character requiredr
        if chara in ALPHABET:
            if chara.isupper():
                final_string += '.....0'
            final_string += ALPHABET.get(chara)
        # Add more than 1 number
        elif is_number:
            if BRAILLE_TO_SPECIAL_CHARAS.get(chara) != ' ':
                final_string += NUMBERS.get(chara)
            else:
                is_number = False
        # Check if 1st number encountered    
        elif chara.isdigit():
            final_string += '.0.000' + NUMBERS.get(chara)
            is_number == True
        # Check for spaces & punctuation
        elif chara == SPECIAL_CHARAS[' ']:
            final_string += "......"
        else:
            final_string += PUNCTUATION.get(chara)
    
    return final_string

# Check if inputted text was braille
def check_for_braille(input: str) -> bool:
    return all(char in {'.', '0'} for char in input)

# Run program
if __name__ == '__main__':
    joined_args = ' '.join(sys.argv[1:])

    if check_for_braille(joined_args):
        print(braille_to_eng(joined_args))
    else:
        print(eng_to_braille(joined_args))