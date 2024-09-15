import sys

SET_BRAILLE = {'.', 'O'}
ENG_TO_BRAILLE = {
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
}
NUM_TO_BRAILLE = {
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
braille_to_eng = {v: k for k, v in ENG_TO_BRAILLE.items()}
braille_to_num = {v: k for k, v in NUM_TO_BRAILLE.items()}
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

def is_braille(s):
    return set(s).issubset(SET_BRAILLE)

def translateBraille(s):
    eng = []
    num = False
    capital = False
    i = 0
    while (i + 5) < len(s):
        brl = s[i:i+6]
        i = i + 6
        if brl == ENG_TO_BRAILLE[' ']:
            num = False
            capital = False
            eng.append(' ')
        elif brl == BRAILLE_CAPITAL:
            capital = True
            num = False
        elif brl == BRAILLE_NUMBER:
            num = True
            capital = False
        elif num:
            eng.append(braille_to_num[brl])
        elif capital:
            c = braille_to_eng[brl]
            eng.append(c.upper())
            capital = False
        else:
            eng.append(braille_to_eng[brl])
    return "".join(eng)

def translateEng(s):
    brl = []
    num = False
    i = 0
    while i < len(s):
        c = s[i]
        i = i + 1
        if c.isnumeric():
            if num is False:
                num = True
                brl.append(BRAILLE_NUMBER)
            brl.append(NUM_TO_BRAILLE[c])
        elif c.isupper():
            num = False
            brl.append(BRAILLE_CAPITAL)
            brl.append(ENG_TO_BRAILLE[c.lower()])
        else:
            num = False
            brl.append(ENG_TO_BRAILLE[c])
    return "".join(brl)


def translate(s):
    if is_braille(s):
        return translateBraille(s)
    else:
        return translateEng(s)

s = []
i = 1
while i < len(sys.argv):
    s.append(sys.argv[i])
    i = i + 1
print(translate(" ".join(s)))