import sys
from enum import Enum


class BrailleState(Enum):
    LETTER = 1
    NUMBER = 2
    DECIMAL = 3


# map braille character to O for raised dot and . for empty space
# the first 2 chars are the top row, the next 2 chars are the middle row, and the last 2 chars are the bottom row
braille_default_map = {
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
    ' ': '......',
    # punctuation marks are not in scope, but included anyways here
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    # '>': 'O..OO.',  # either this is incorrect or 'o' is incorrect
    '(': 'O.O..O',
    ')': '.O.OO.',
    'cap': '.....O',
    'dec': '.O...O',  # this logic also not in scope but we'll implement it anyways
    'num': '.O.OOO',
}
braille_number_map = {
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
inverted_braille_default_map = {v: k for k, v in braille_default_map.items()}
inverted_braille_number_map = {v: k for k, v in braille_number_map.items()}


def encode_braille(text):
    current_state = BrailleState.LETTER
    output = ''
    for c in text:
        if current_state == BrailleState.LETTER:
            # if is number, insert "number follows"
            if c.isdigit():
                output += braille_default_map['num']
                current_state = BrailleState.NUMBER
        elif current_state == BrailleState.NUMBER:
            # if is decimal point, insert "decimal follows"
            if c == '.':
                output += braille_default_map['dec']
                current_state = BrailleState.DECIMAL
                continue
            # space ends number
            elif c == ' ':
                current_state = BrailleState.LETTER
        elif current_state == BrailleState.DECIMAL:
            # space ends decimal
            if c == ' ':
                current_state = BrailleState.LETTER

        # capital follows only applies to next letter
        if c.isupper():
            output += braille_default_map['cap']
            c = c.lower()

        # use number map if in number mode
        number_braille = braille_number_map.get(c, None) if current_state != BrailleState.LETTER else None
        if number_braille:
            output += number_braille
        else:
            if c not in braille_default_map:
                print('Invalid character: ' + c)
                sys.exit()
            output += braille_default_map.get(c)
    return output


def decode_braille(braille, length):
    current_state = BrailleState.LETTER
    next_is_capital = False
    output = ''
    for i in range(length):
        braille_char = braille[6*i:6*(i+1)]
        if braille_char not in inverted_braille_default_map and braille_char not in inverted_braille_number_map:
            print('Invalid braille character: ' + braille_char)
            sys.exit()

        default_c = inverted_braille_default_map.get(braille_char, None)
        number_c = inverted_braille_number_map.get(braille_char, None)
        if default_c == 'cap':
            next_is_capital = True
            continue
        elif default_c == 'num':
            current_state = BrailleState.NUMBER
            continue
        elif default_c == 'dec':
            assert current_state == BrailleState.NUMBER, 'Invalid braille: decimal point must follow a number'
            output += '.'
            current_state = BrailleState.DECIMAL
            continue
        elif default_c == ' ':
            current_state = BrailleState.LETTER

        if current_state == BrailleState.LETTER:
            if next_is_capital:
                output += default_c.upper()
                next_is_capital = False
            else:
                output += default_c
        else:
            output += number_c
    return output


n = len(sys.argv)
if n < 2:
    print('Usage: python translator.py <text>')
    sys.exit()

input_text = ' '.join(sys.argv[1:])

braille_to_text_length = None
if set(list(input_text)) - {'.', 'O'} == set():
    braille_to_text_length = len(input_text) // 6
    if braille_to_text_length * 6 != len(input_text):
        braille_to_text_length = None

if braille_to_text_length is not None:
    print(decode_braille(input_text, braille_to_text_length))
else:
    print(encode_braille(input_text))

