import sys
import re

BRAIL_ALPHABET = set(['.', '0'])
BRAIL_VALUES = {
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
    'capital_follows': '.....O',  # Braille prefix for capital letters
    'decimal_follows': '.O...O',  # Braille prefix for decimal points
    'number_follows': '.O.OOO',   # Braille prefix for numbers
    ' ': '......', # Braille for space
}

BRAIL_NUMBERS = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

REVERSE_BRAIL_VALUES = {v: k for k, v in BRAIL_VALUES.items()}
REVERSE_BRAIL_NUMBERS = {v: k for k, v in BRAIL_NUMBERS.items()}

def decode_brail(code: str) -> str:
    # get every 6 characters from code
    code_list = re.findall('.{6}', code)
    string_list = []
    next_cap = False
    next_num = False
    next_dec = False
    
    for code in code_list:
        if code in BRAIL_VALUES:
            if code == BRAIL_VALUES['capital_follows']:
                next_cap = True
            elif code == BRAIL_VALUES['number_follows']:
                next_num = True
            elif code == BRAIL_VALUES['decimal_follows']:
                next_dec = True
            else:
                if next_cap:
                    string_list.append(REVERSE_BRAIL_VALUES[code].upper())
                    next_cap = False
                elif next_num:
                    string_list.append(REVERSE_BRAIL_NUMBERS[code])
                elif next_dec:
                    string_list.append('.')
                    next_dec = False
                else:
                    if code == BRAIL_VALUES[' '] and next_num:
                        next_num = False
                    string_list.append(REVERSE_BRAIL_VALUES[code])
        else:
            print(f'Unknown code: {code}')
            exit(1)
                
            
    return ''.join(string_list)

def decode_eng(code: str) -> str:
    code_list = list(code)
    string_list = []
    
    code_index = 0
    
    next_num = False
    
    while code_index < len(code_list):
        code = code_list[code_index]
        # check if the code is a capital letter
        if code.isupper():
            string_list.append(BRAIL_VALUES['capital_follows'])
            code = code.lower()
            string_list.append(BRAIL_VALUES[code])
        elif code.isdigit():
            if not next_num:
                string_list.append(BRAIL_VALUES['number_follows'])
                next_num = True
            string_list.append(BRAIL_NUMBERS[code])
        elif code == '.':
            string_list.append(BRAIL_VALUES['decimal_follows'])
        else:
            if code == ' ' and next_num:
                next_num = False
            string_list.append(BRAIL_VALUES[code])
            
        code_index += 1
    
    return ''.join(string_list)
    

def main():
    args = sys.argv[1:]
    code = ' '.join(args)
    flag = 0
    
    if len(code) < 6:
        flag = 1
    else:
        for char in code:
            if char not in BRAIL_ALPHABET:
                flag = 1
                break

    if flag == 0:
        print(decode_brail(code))
    else:
        print(decode_eng(code))
    
    
if __name__ == '__main__':
    main()
    
