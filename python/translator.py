import sys
from textwrap import wrap

# Class for custom two way dictionary
class TwoWayDict(dict):
    def __init__(self, map):
        for key, value in map.items():
            self[key] = value
            
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

# Two way dictionary for alphabet mapping
alphabet_dict: TwoWayDict = TwoWayDict({
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
})

# Two way dictionary for number mapping
num_dict: TwoWayDict = TwoWayDict({
    '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
})

# Returns True if input string is in Braille
#   Braille is determined by if all chars are O or . and length is a multiple of 6
def is_braille(input_str: str) -> bool:
    return all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0

# Translates from Braille to English
def translate_from_braille(input_str: str) -> str:
    is_cap: bool = False
    is_num: bool = False

    # Separate the input string into 6 char chunks (Braille chars)
    chunkated_str: list[str] = wrap(input_str, 6)
    result: str = ''
    for c in chunkated_str:
        if c == '......':
            is_cap = False
            is_num = False
            result = f'{result} '
            continue
        elif c == '.....O':
            is_cap = True
            continue
        elif c == '.O.OOO':
            is_num = True
        elif is_num:
            result = f'{result}{num_dict[c]}'
        elif is_cap:
            result = f'{result}{alphabet_dict[c].upper()}'
            is_cap = False
        else:
            result = f'{result}{alphabet_dict[c]}'

    return result 

# Translates from English to Braille
def translate_to_braille(input_str: str) -> str:
    result: str = ''
    # is_num_braille_exist is True when '.O.OOO' is still
    #   valid for the current char
    is_num_braille_exist = False
    for c in input_str:
        # Number case
        if c in '0123456789':
            if not is_num_braille_exist:
                result = f'{result}.O.OOO'
                is_num_braille_exist = True
            result = f'{result}{num_dict[c]}'
        # Alphabet case
        else:
            if c.isupper():
                result = f'{result}.....O'
            elif c == ' ':
                # Reset is_num_braille_exist when ' ' is encountered
                is_num_braille_exist = False
            result = f'{result}{alphabet_dict[c.lower()]}'

    return result

def main():
    # Put together the input string from individual args
    input_str = sys.argv[1] if len(sys.argv) >= 2 else '' 
    for i in range(2, len(sys.argv)):
        input_str = f'{input_str} {sys.argv[i]}'
    
    if is_braille(input_str):
        # The input is Braille
        translated_text = translate_from_braille(input_str)
    else:
        # The input is English
        translated_text = translate_to_braille(input_str)
    
    print(translated_text)

main()
