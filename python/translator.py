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
    'capital' : '.....O', 'number':'.O.OOO', ' ':'......'
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
    ')': '.O.OO.'
}

# Hashmaps (reversed) to represent braille mapping to alphbabet, numbers, special characters, & punctuation
BRAILLE_TO_ALPHABET = {val : key for key, val in ALPHABET.items()}
BRAILLE_TO_NUMBERS = {val : key for key, val in NUMBERS.items()}
BRAILLE_TO_SPECIAL_CHARAS = {val : key for key, val in SPECIAL_CHARAS.items()}
BRAILLE_TO_PUNCTUATION = {val: key for key, val in PUNCTUATION.items()}

# Convert from Braille - English
def braille_to_eng(braille: str) -> str:
    # Variable for final string to be returned & states to track capital letters & numbers
    final_string = ''
    is_capital, is_number = False, False
    
    # Break braille string into groups of 6 to read properly
    braille_list = wrap(braille, 6)
    
    # Check through conditions to create English translation of Braille
    for group in braille_list:
        # Change states of capital tracker & number tracker if braille symbols encountered
        # If space braille encountered add space & change is_number to false to indicate no more numbers
        if group == SPECIAL_CHARAS['capital']:
            is_capital = True
        elif group == SPECIAL_CHARAS['number']:
            is_number = True
        elif group == SPECIAL_CHARAS[' ']:
            is_number = False
            final_string += " "
        
        # If number (more than 1), add to result
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
        # In all other cases, inputted braille must be punctuation
        else:
            final_string += BRAILLE_TO_PUNCTUATION.get(group)
    
    return final_string


# Convert from English -> Braille
def eng_to_braille(text: str) -> str:
    # Variable for final string to be returned & states to track capital letters & numbers
    final_string = ''
    is_number= False
    
    for chara in text:
        # If alphabetical, determine if uppercase special character required otherwise add corresponding braille character as normal
        # If previous characters were numbers, add space & change number state to false
        if chara.isalpha():
            if is_number:
                final_string += '......'
                is_number = False
            if chara.isupper():
                final_string += '.....O'
            final_string += ALPHABET.get(chara.lower())
        # If first number encountered, add number symbol & number to braille then change number state to true
        elif chara.isdigit() and is_number == False:
            final_string += '.O.OOO' + NUMBERS.get(chara)
            is_number = True
        # If physical space encountered, add space character 
        elif chara == ' ':
            final_string += "......"
        # If number state true, add numbers as normal
        elif is_number:
            final_string += NUMBERS.get(chara)
        # Add punctuation as last option
        else:
            final_string += PUNCTUATION.get(chara)
    
    return final_string

# Return true if all characters in inputted string are braille characters
def check_for_braille(input: str) -> bool:
    return all(char in {'.', 'O'} for char in input)

# Run program, performing proper fn depending on input
if __name__ == '__main__':
    joined_args = ' '.join(sys.argv[1:])

    if check_for_braille(joined_args):
        print(braille_to_eng(joined_args))
    else:
        print(eng_to_braille(joined_args))