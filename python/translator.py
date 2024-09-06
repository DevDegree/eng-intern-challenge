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

from_braille_dict_special = {
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER',
}

from_braille_dict_char = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': ',',
    '..O...': '.',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
    '.O...O': '.',
}

from_braille_dict_num = {
    '.OOO..': '0',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '......': ' ',
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
    translated_text = ''
    number_state = False
    capitalized_state = False
    num_cells = len(braille_input) // 6
    for i in range(num_cells):
        braille_cell = braille_input[(i * 6) : ((i + 1) * 6)]
        special_type = from_braille_dict_special.get(braille_cell, None)
        
        if special_type == 'CAPITAL':
            capitalized_state = True
        elif special_type == 'NUMBER':
            number_state = True
        else:
            # If current braille cell is not special (e.g., character insert)
            if number_state:
                c = from_braille_dict_num.get(braille_cell, '')
                translated_text += c
                if c == ' ':
                    number_state = False
            else:
                c = from_braille_dict_char.get(braille_cell, '')
                if capitalized_state and c.isalpha():
                    c = c.upper()
                    capitalized_state = False
                
                translated_text += c

    return translated_text

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

if __name__ == '__main__':
    main()

