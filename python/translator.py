import sys

CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '.O.OOO'

ALPHA_TRANSLATION = {
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
    ' ': '......'
}

NUM_TRANSLATION = {
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

REVERSE_ALPHA_TRANSLATION = {v: k for k, v in ALPHA_TRANSLATION.items()}
REVERSE_NUM_TRANSLATION = {v: k for k, v in NUM_TRANSLATION.items()}

# INPUT: String of braille with each character being 6 chars long
# OUTPUT: Return a string of english characters
def braille_to_english(input_str):
    res = ''
    i = 0
    next_capital = False
    number_mode = False
    while i < len(input_str):
        curr_str = input_str[i:i+6]
        if curr_str == CAPITAL_INDICATOR:
            next_capital = True
        elif curr_str == NUMBER_INDICATOR:
            number_mode = True
        else:
            if number_mode:
                if curr_str in REVERSE_NUM_TRANSLATION:
                    res += REVERSE_NUM_TRANSLATION[curr_str]
                else:
                    number_mode = False
                    if curr_str in REVERSE_ALPHA_TRANSLATION:
                        char = REVERSE_ALPHA_TRANSLATION[curr_str]
                        res += char.upper() if next_capital else char
                        next_capital = False
            else:
                if curr_str in REVERSE_ALPHA_TRANSLATION:
                    char = REVERSE_ALPHA_TRANSLATION[curr_str]
                    res += char.upper() if next_capital else char
                    next_capital = False
        i += 6
    return res

# INPUT: String of english characters
# OUTPUT: String of braille with every 6 chars indicating a letter or a indicator
def english_to_braille(input_str):
    res = ''
    number_mode = False
    for c in input_str:
        if c.isupper():
            res += CAPITAL_INDICATOR
            res += ALPHA_TRANSLATION[c.lower()]
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                res += NUMBER_INDICATOR
                number_mode = True
            res += NUM_TRANSLATION[c]
        else:
            if c.lower() in ALPHA_TRANSLATION:
                res += ALPHA_TRANSLATION[c.lower()]
            number_mode = False
    return res

def main():
    input_str = ' '.join(sys.argv[1:])
    
    if not input_str:
        print('No input provided.')
        return
    elif set(input_str).issubset({'O', '.'}):
        if len(input_str) % 6 != 0:
            print('Invalid input provided.')
            return
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == '__main__':
    main()