import sys 
from textwrap import wrap

# Indicators
CAP_INDICATOR = '.....O'
NUM_INDICATOR = '.O.OOO'
DEC_INDICATOR = '.O...O'

ALNUM_TO_BRAILLE = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Symbols
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '(': 'O.O..O',
    ')': '.O.OO.', ' ': '......',
}

LETTER_TO_NUMSYM = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
    'h': '8', 'i': '9', 'j': '0', 'o': '>', 'DEC': '.',
}

BRAILLE_TO_ALNUM = {v: k for k, v in ALNUM_TO_BRAILLE.items()}
NUMSYM_TO_LETTER = {v: k for k, v in LETTER_TO_NUMSYM.items()}

def translate_from_braille_to_alnum(braille: str) -> str:
    braille = wrap(braille, 6)

    next_is_cap = False
    is_num = False
    result = []

    for c in braille:
        if c == CAP_INDICATOR:
            next_is_cap = True
            # continue
        elif c == NUM_INDICATOR:
            is_num = True
            # continue
        
        else:
            val = BRAILLE_TO_ALNUM.get(c, c)

            if is_num: 
                if val.isspace():
                    is_num = False
                if val == DEC_INDICATOR:
                    val = '.'
                else:
                    val = LETTER_TO_NUMSYM.get(val, val)

            elif next_is_cap and val.isalpha():
                    val = val.upper()
                    next_is_cap = False
        
            result.append(val)

    return ''.join(result)

def translate_from_alnum_to_braille(alnum: str) -> str:
    result = []
    is_num = False
   
    for c in alnum:

        if c.isdigit() or c == '>': # add number indicator as needed
            c = NUMSYM_TO_LETTER.get(c, c)

            if not is_num:
                is_num = True
                result.append(NUM_INDICATOR)

        elif c.isalpha() and c.isupper(): # add caps indicator as needed
            result.append(CAP_INDICATOR)
            c = c.lower()
        
        elif is_num and not c.isdigit(): # add decimal indicator as needed
            if c == '.':
                c = DEC_INDICATOR
            else: # break out of numbers as needed
                is_num = False
                if c != ' ':
                    result.append(ALNUM_TO_BRAILLE.get(' '))

        result.append(ALNUM_TO_BRAILLE.get(c, c))

    return ''.join(result)

def is_braille(s: str) -> bool:
    return (
        len(s) % 6 == 0 # check if divisible by 6
        and all(c in 'O.' for c in s) # check if string only contains 'O.'
        and all(c in BRAILLE_TO_ALNUM # check if chars are valid braille
                or c in [CAP_INDICATOR, NUM_INDICATOR, DEC_INDICATOR] 
                for c in wrap(s, 6)
            )
        )

def translate(s: str):
    return translate_from_braille_to_alnum(s) if is_braille(s) else translate_from_alnum_to_braille(s)

if __name__ == "__main__":
    inp = " ".join(sys.argv[1::])
    out = translate(inp)
    print(out)
