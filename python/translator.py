import sys


braille_to_english = {
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
    '..00.0': '.',
    '..0...': ',',
    '..0.00': '?',
    '..000.': '!',
    '..00..': ':',
    '..0.0.': ';',
    '....00': '-',
    '.0..0.': '/',
    '.00..0': '<',
    '0..00.': '>',
    '0.0..0': '(',
    '.0.00.': ')',
    '......': ' ',
}

english_to_braille = {
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
    '.': '..00.0',
    ',': '..0...',
    '?': '..0.00',
    '!': '..000.',
    ':': '..00..',
    ';': '..0.0.',
    '-': '....00',
    '/': '.0..0.',
    '<': '.00..0',
    '>': '0..00.',
    '(': '0.0..0',
    ')': '.0.00.',
    ' ': '......',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}


braille_to_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '.O...O': '.'
}

cap_follow_symbol = '.....O'
dec_follow_symbol = '.O...O'
num_follow_symbol = '.O.OOO'

alpha_braille_symbols = list(braille_to_english.keys())[:26]
numeric_braille_symbols = list(braille_to_num.keys())
all_braille_symbols = list(braille_to_english.keys()) + [cap_follow_symbol, dec_follow_symbol, num_follow_symbol]

# function to split string at every 6 characters
def split_by_6(str):
    return [str[i:i+6] for i in range(0, len(str), 6)]

# function to determine if a string is braille
def is_brail_str(str):
    is_brail = True
    
    # check if the string is divisible by 6 (can't be braille if not)
    if len(str) % 6 != 0:
        is_brail = False

    else:
        # loop the symbols to determine if string is braille
        symbols = split_by_6(str)       
        for i, symbol in enumerate(symbols):

            # check if the symbol is a braille symbol
            if symbol not in all_braille_symbols:
                is_brail = False
                break
            
            # check next symbols to determine if the braille is valid
            elif i != len(symbols) - 1:
                next_symbol = symbols[i+1]

                # check that braille symbil following a capital symbol is a letter symbol
                if symbol == cap_follow_symbol and next_symbol not in alpha_braille_symbols:
                    is_brail = False
                    break
                
                # check that numbers follow a number following symbol
                elif symbol == num_follow_symbol:
                    for j in range(i+1, len(symbols)):
                        next_symbol = symbols[j]

                        if next_symbol == '......':
                            break

                        elif next_symbol not in numeric_braille_symbols:
                            is_brail = False

                    if not is_brail:
                        break

            # check the last symbol (shouldn't be a number following or capital following symbol)
            else:
                if symbol == cap_follow_symbol or symbol == num_follow_symbol:
                    is_brail = False

    return is_brail

# get system input
sys_input = sys.argv[1:]

# check if the system input is empty or not
if len(sys_input) > 0:

    # convert system input to a string
    sys_input_str = ' '.join(sys_input)

    # check if the string is braille
    if is_brail_str(sys_input_str):

        # split braille string at every 6 cgaracters to seperate the braille symbols
        braille_symbols = split_by_6(sys_input_str)

        output_string = ''

        is_cap_following = False
        is_num_following = False

        for symbol in braille_symbols:

            # check if current symbol is proceeded by a capital following symbol
            if is_cap_following:
                output_string += braille_to_english[symbol].upper()
                is_cap_following = False
            
            # check if current symbol is proceeded by a is_num_following
            elif is_num_following:
                if symbol == '......':
                    output_string += ' '
                    is_num_following = False
                else:
                    output_string += braille_to_num[symbol]

            # check if current symbol is a capital following symbol
            elif symbol == cap_follow_symbol:
                is_cap_following = True
            
            # check if current symbol is a number following symbol
            elif symbol == num_follow_symbol:
                is_num_following = True
            
            else:
                output_string += braille_to_english[symbol]
        
        print(output_string)

    else:
        output_string = ''
        reading_numeric = False

        for char in sys_input_str:

            # check if current char is a number and not proceeded by numbers (part of the same number)
            if char.isnumeric() and not reading_numeric:
                reading_numeric = True
                output_string += num_follow_symbol
                output_string += english_to_braille[char]

            # check if current char is part of a number and proceeded by a number (part the same number)
            elif reading_numeric:
                if not char.isnumeric():
                    reading_numeric = False
                output_string += english_to_braille[char]

            # check if the current char is a capital letter
            elif char.isupper():
                output_string += cap_follow_symbol
                output_string += english_to_braille[char.lower()]

            else:
                output_string += english_to_braille[char]

        print(output_string)