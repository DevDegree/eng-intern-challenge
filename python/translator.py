import sys

# CONSTANTS
CAP = 'capital'
SPACE = ' '
DECIMAL = 'decimal'
LEFTARROW = '<'
RIGHTARROW = '>'
LEFTBRACKET = '('
RIGHTBRACKET = ')'
COMMA = ','
COLON = ':'
SEMICOLON = ';'
QUESTIONMARK = '?'
EXCLAMATION = '!'
FULLSTOP = '.'
HYPHEN = '-'
FORWARDSLASH = '/'
NUMBER = 'number'

# Define Braille dictionary for alphabet, numbers, and special characters
braille_dict = {
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
    CAP: '.....O',
    SPACE: '......',
    DECIMAL: '.0...0',
    NUMBER: '.0.000',
    LEFTARROW: '.0.0.0',
    RIGHTARROW: '0..0.0',
    LEFTBRACKET: '0.0..0',
    RIGHTBRACKET: '.0.00.',
    HYPHEN: '....00',
    COLON: '....00',
    SEMICOLON: '..0.0.',
    FULLSTOP: '..00.0',
    QUESTIONMARK: '..0.00',
    EXCLAMATION: '..000.',
    COMMA: '00.000',
    FORWARDSLASH: '.0..0.'
}

# Reverse braille dict to enable reverse lookup from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def get_representation(char: str) -> str:
    """Returns Braille representation of a character or its English equivalent."""
    dict_to_use = reverse_braille_dict if len(char) == 6 else braille_dict
    return dict_to_use[char]

def is_braille(input_str: str) -> bool:
    """Check if input is in Braille format."""
    return all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_text = ''
    for char in text:
        if char.isupper():
            braille_text += get_representation(CAP) + get_representation(char.lower())
        elif char.isdigit():
            chr_rep = None
            if int(char) == 0:
                chr_rep = 'j'
            else:
                chr_rep = chr(ord('a') + int(char) - 1)
            braille_text += get_representation(NUMBER) + get_representation(chr_rep)
        elif char == SPACE:
            braille_text += get_representation(SPACE)
        else:
            braille_text += get_representation(char)
    return braille_text

def translate_to_english(braille):
    """Translate Braille to English."""
    english_text = ''
    i = 0
    capitalize_next = False
    is_number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == get_representation(CAP):
            capitalize_next = True
        elif symbol == get_representation(NUMBER):
            is_number_mode = True
        elif symbol == get_representation(SPACE):
            english_text += ' '
            is_number_mode = False  # Reset number mode after a space
        else:
            letter = get_representation(symbol)
            if capitalize_next:
                letter = letter.upper()
                capitalize_next = False
            if is_number_mode:
                if letter == 'j':
                    letter = '0'
                else:
                    letter = str(ord(letter) - ord('a') + 1)
            english_text += letter
        i += 6
    return english_text

def main():
    # Get the input string from command line arguments
    input_str = SPACE.join(sys.argv[1:])
    
    try:
        if is_braille(input_str):
            # Input is in Braille, translate to English
            print(translate_to_english(input_str))
        else:
            # Input is in English, translate to Braille
            print(translate_to_braille(input_str))
    except KeyError:
        print("Invalid input.")
    except Exception as e:
        print(f"An unforeseen error occurred: {e}")

if __name__ == "__main__":
    main()
