import sys

# Valid characters in a braille representation
BRAILLE_CHARS = {"O", "."}

# Character conversions to braille representation
CHAR_TO_BRAILLE = {
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

    '.': '..OO.O', 
    ',': '..O...', 
    '?': '..O.OO', 
    '!': '..OOO.', 
    ':': '..OO..',
    ';': '..O.O.', 
    '-': '....OO', 
    '/': '.O..O.', 
    '(': 'O.O..O', 
    ')': '.O.OO.',
    ' ': '......',
}

# Digit conversions to braille representations
NUMBER_TO_BRAILLE = {
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

BRAILLE_TO_CHAR = {} # will contain braille representation conversion to non numeric characters
BRAILLE_TO_NUMBER = {} # will contain braille representation conversion to non numeric characters

for key, value in CHAR_TO_BRAILLE.items():
    BRAILLE_TO_CHAR[value] = key

for key, value in NUMBER_TO_BRAILLE.items():
    BRAILLE_TO_NUMBER[value] = key
    

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

BRAILLE_CHAR_SIZE = 6

def is_braille(text: str) -> bool:
    '''
    Checks if text is a braille representation

    Args:
        (a) text (str) the text to check for braille
    
    Returns:
        True if text is a valid braille representation, false otherwise
    '''
    for i in range(len(input_text)):
        if input_text[i] not in BRAILLE_CHARS: return False
    return True

def to_braille(english_text: str) -> str:
    '''
    Converts English text to equivalent braille representation 

    Args:
        (a) english_text (str) the text to convert to braille
    
    Returns:
        The translated braille representation.
    '''
    braille_text = ''

    token_is_number = False

    for i in range(len(english_text)):
        char = english_text[i]

        if char.isnumeric():
            if not token_is_number:
                # if this is the first character of the numeric token, append the NUMBER_FOLLOWS character
                braille_text += NUMBER_FOLLOWS
            
            braille_text += NUMBER_TO_BRAILLE[char]
            token_is_number = True
        elif char.isupper():
            # if the character is upper case, append the CAPITAL_FOLLOWS character
            braille_text += CAPITAL_FOLLOWS + CHAR_TO_BRAILLE[char.lower()]
            token_is_number = False
        else:
            # for any lowercase alpha character, do a simple conversion
            braille_text += CHAR_TO_BRAILLE[char]
            token_is_number = False
    
    return braille_text

def to_english(braille_text: str) -> str:
    '''
    Converts braille text to equivalent English representation.

    Args:
        (a) braille_text (str) the text to convert to English
    
    Returns:
        The translated English representation.
    '''
    english_text = ''

    current_pos = 0

    token_is_number = False
    capitalize_next = False

    while current_pos < len(braille_text):
        braille_char = braille_text[current_pos:current_pos + BRAILLE_CHAR_SIZE]

        if braille_char == CAPITAL_FOLLOWS: 
            # setup next character to be capitalized if CAPITAL_FOLLOWS character is passed
            capitalize_next = True
        elif braille_char == NUMBER_FOLLOWS:
            # setup next character to be if CAPITAL_FOLLOWS character is passed
            token_is_number = True
        elif braille_char == CHAR_TO_BRAILLE[' ']:
            # if the character is whitespace, a numerical token will end
            english_text += ' '
            token_is_number = False
        else:
            if capitalize_next: 
                # capitalize if the last char was a CAPITAL_FOLLOWS
                english_text += BRAILLE_TO_CHAR[braille_char].upper()
                capitalize_next = False
            elif token_is_number:
                # use numeric translations if last char was a NUMBER_FOLLOWS
                english_text += BRAILLE_TO_NUMBER[braille_char]
            else:
                english_text += BRAILLE_TO_CHAR[braille_char]

        current_pos += BRAILLE_CHAR_SIZE
    
    return english_text

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        print(to_english(input_text))
    else:
        print(to_braille(input_text))