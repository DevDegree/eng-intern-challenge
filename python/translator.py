import sys

ENG_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

PUNCT_TO_BRAILLE = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......',
}

INT_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

CAPITAL = '.....O'
NUMBER = '.O.OOO'
DECIMAL = '.O...O'
SPACE = '......'
O = 'O..OO.'

BRAILLE_TO_ENG = dict(zip(ENG_TO_BRAILLE.values(), ENG_TO_BRAILLE.keys()))

BRAILLE_TO_INT = dict(zip(INT_TO_BRAILLE.values(), INT_TO_BRAILLE.keys()))
BRAILLE_TO_INT[DECIMAL] = '.'  # adding decimal as symbol

BRAILLE_TO_PUNCT = dict(zip(PUNCT_TO_BRAILLE.values(), PUNCT_TO_BRAILLE.keys()))

def translate_eng_to_braille(input):
    result = ''
    is_number = False

    for i in range(len(input)):
        c = input[i]
        if c in INT_TO_BRAILLE:
            if not is_number:
                result += NUMBER
                is_number = True
            result += INT_TO_BRAILLE[c]
        elif c == '.' and i < len(input) - 1 and input[i + 1].isdigit():
            # if '.' is followed by a number it is decimal
            # we don't check is_number here becasue we assume we might have ' .5'
            result += DECIMAL
        elif c in ENG_TO_BRAILLE:
            result += ENG_TO_BRAILLE[c]
        elif c.isupper():
            result += CAPITAL + ENG_TO_BRAILLE[c.lower()]
            is_number = False
        elif c in PUNCT_TO_BRAILLE:
            result += PUNCT_TO_BRAILLE[c]
            if c == ' ':
                is_number = False
        else:
            print("Invalid input")
            return None

    return result

def translate_braille_to_eng(input):
    result = ''

    is_capital = False
    is_number = False

    for c in range(0, len(input), 6):
        segment = input[c:c + 6]
        if segment == CAPITAL:
            is_capital = True
        elif segment == NUMBER:
            is_number = True
        elif segment == SPACE:
            is_number = False
            result += ' '
        elif segment in BRAILLE_TO_PUNCT and not is_capital:
            if segment == O:
                # letter 'o' and '>' have the same braille code, so here we decide what to choose
                prev = input[c - 6:c] if c > 0 else ''
                next = input[c + 6:c + 12] if c < len(input) - 1 else ''
                if prev in BRAILLE_TO_ENG or next in BRAILLE_TO_ENG or next == CAPITAL:
                    # assuming letter 'o' is never standalone
                    result += 'o'
                else:
                    # assuming '>' can't have a letter next to it
                    result += '>'
            else:
                result += BRAILLE_TO_PUNCT[segment]
        elif is_number:
            result += BRAILLE_TO_INT[segment]
        elif segment in BRAILLE_TO_ENG:
            if is_capital:
                result += BRAILLE_TO_ENG[segment].upper()
                is_capital = False
            else:
                result += BRAILLE_TO_ENG[segment]
        else:
            print("Invalid input")
            return None

    return result

def is_braille(input):
    braille_chars = ".O"
    for c in input:
        if not c in braille_chars:
            return False
    return True

if len(sys.argv) > 1:
    inp = ' '.join(sys.argv[1:])
    if is_braille(inp):
        eng = translate_braille_to_eng(inp)
        print(eng)
    else:
        br = translate_eng_to_braille(inp)
        print(br)
else:
    print("No arguments were passed.")