import sys

# Constants for special symbols
CAP_SYMBOL = '.....O'
NUM_SYMBOL = '.O.OOO'

# Base mapping for letters, numbers, and symbols
BASE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Extend with Braille-specific symbols
ENGLISH_TO_BRAILLE = BASE_MAP.copy()
ENGLISH_TO_BRAILLE.update({'cap': CAP_SYMBOL, 'num': NUM_SYMBOL})

# Reverse mapping for Braille-to-English
BRAILLE_TO_ENGLISH = {v: k for k, v in BASE_MAP.items()}
BRAILLE_TO_ENGLISH.update({'.....O': 'cap', '.O.OOO': 'num'})

# Number mappings
LETTER_TO_NUMBER = {chr(97 + i): str(i + 1) for i in range(9)}  # Maps a->1, b->2, ... i->9
LETTER_TO_NUMBER['j'] = '0'

NUMBER_TO_LETTER = {v: k for k, v in LETTER_TO_NUMBER.items()}  # Reverse mapping for Braille, maps 1->a, 2->b, ..., 9->i

# Functions

def to_english(input_str):
    i = 0
    cap = False 
    num = False
    s = ''
    
    if not input_str:
        return "Error: Empty input"
    
    while i < len(input_str):
        braille_letter = input_str[i:i+6]
        if braille_letter not in BRAILLE_TO_ENGLISH:
            return f"Error: Invalid Braille input '{braille_letter}'"

        letter = BRAILLE_TO_ENGLISH[braille_letter]
        if letter == ' ':
            num = False 
    
        if cap:
            s += letter.upper()
            cap = False 
        elif num:
            s += LETTER_TO_NUMBER.get(letter, '')
        elif letter == 'cap':
            cap = True
        elif letter == 'num':
            num = True 
        else:
            s += letter 
        i += 6
    return s
        

def to_braille(input_str):
    s = ''
    num = False 
    
    if not input_str:
        return "Error: Empty input"

    for letter in input_str:
        if letter == ' ':
            num = False 
            s += ENGLISH_TO_BRAILLE[' ']
        elif letter.isdigit():
            if not num:
                s += ENGLISH_TO_BRAILLE['num']
                num = True 
            s += ENGLISH_TO_BRAILLE[NUMBER_TO_LETTER[letter]]
        else:
            if letter.isupper():
                s += ENGLISH_TO_BRAILLE['cap']
                letter = letter.lower()
            s += ENGLISH_TO_BRAILLE.get(letter, '......')  # Maps unknown letters to a space 
    return s

def is_braille(input_str):
    return all(c in "O." for c in input_str)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)
    
    # Combine all arguments into one string in case of spaces
    input_str = " ".join(sys.argv[1:])
    
    if is_braille(input_str):
        print(to_english(input_str))
    else:
        print(to_braille(input_str))


if __name__ == "__main__":
    main()

