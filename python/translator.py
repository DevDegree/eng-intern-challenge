from textwrap import wrap

# CONSTANTS
# Hashmaps representing alphabet, numbers, and special characters to braille
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

# Hashmaps (reversed from above) to represent braille mapping to alphbabet, numbers, & special characters
BRAILLE_TO_ALPHABET = {val : key for key, val in ALPHABET.items()}
BRAILLE_TO_NUMBERS = {val : key for key, val in NUMBERS.items()}
BRAILLE_TO_SPECIAL_CHARAS = {val : key for key, val in SPECIAL_CHARAS.items()}

# Convert from Braille - English
def braille_to_eng(braille: str) -> str:
    final_string = ''
    is_capital, is_number = False, False
    
    # Break braille string into groups of 6 
    braille_list = wrap(braille, 6)
    
    for group in braille_list:
        # Check for capital symbol
        if group == SPECIAL_CHARAS['capital']:
            is_capital == True
        # Check if number symbol
        elif group == SPECIAL_CHARAS['number']:
            is_number == True
        elif group == SPECIAL_CHARAS[' ']:
            final_string += " "
            
        
        if is_number:
            while BRAILLE_TO_SPECIAL_CHARAS.get(group) != ' ':
                num = BRAILLE_TO_NUMBERS.get(group)
                final_string += num
            
            is_number = False
        else:
            letter = BRAILLE_TO_ALPHABET.get(group)
            if is_capital:
                final_string += letter.upper()
                is_capital = False
            else :
                final_string += letter
    
    return final_string


    
        
