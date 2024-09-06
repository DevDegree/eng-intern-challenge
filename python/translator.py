import sys
import re

# Dictionaries used for braille translations
to_braille_dict = {
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
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    ',': '..OO.O',
    '.': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}


def check_if_braille(input_text):
   # If input string is not a multiple of six characters, then it cannot be braille
   if len(input_text) % 6 != 0:
       return False

   # If the input string only contains the characters 'O' and '.', then it is considered to be braille
   return bool(re.match('^[O.]+$', input_text))

def translate_to_braille(english_input):
    translated_text = ''
    number_state = False
    for c in english_input:
        # Handle numbers
        if c.isnumeric():
            if not number_state:
                number_state = True
                translated_text += '.O.OOO'

        if c == ' ':
            number_state = False

        # Handle capitalized characters
        if c.isupper():
            translated_text += '.....O'
            translated_text += to_braille_dict.get(c.lower(), '')
        else:
            translated_text += to_braille_dict.get(c, '')

    return translated_text

def translate_from_braille(braille_input):
    return ''

def main():
    # Parse input from command line
    if len(sys.argv) <= 1:
        print('')
        return
    
    input_text = ' '.join(sys.argv[1:])

    # Check if command line input is braille or not
    is_braille = check_if_braille(input_text)

    # Perform translation
    output = ''
    if is_braille:
        output = translate_from_braille(input_text)
    else:
        output = translate_to_braille(input_text)

    # Output result
    print(output)

if __name__ == "__main__":
    main()

