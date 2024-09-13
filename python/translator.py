import sys

ENGLISH_TO_BRAILLE = {
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

NUMBER_TO_BRAILLE = {
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

SPACE = '......'
CAPITAL_FOLLOWS = '.....0'
NUMBER_FOLLOWS = '.0.000'

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

def isBraille(str):
    return len(str) % 6 == 0 and all(c in 'O.' for c in str)

def translateToEnglish(str):
    res = []
    braille = [str[i:i + 6] for i in range(0, len(str), 6)]
    cap_mode = False
    num_mode = False

    for br in braille:
        if br == CAPITAL_FOLLOWS:
            cap_mode = True
        elif br == NUMBER_FOLLOWS:
            num_mode = True
        elif br == SPACE:
            res.append(' ')
        else:
            if cap_mode:
                res.append(BRAILLE_TO_ENGLISH[br].upper())
                cap_mode = False
            elif num_mode:
                res.append(BRAILLE_TO_NUMBER[br])
                num_mode = False
            else:
                res.append(BRAILLE_TO_ENGLISH[br])


    return ''.join(res)

def translateToBraille(str):
    res = []

    for c in str:
        if c.isupper():
            res.append(CAPITAL_FOLLOWS)
            res.append(ENGLISH_TO_BRAILLE[c.lower()])
        elif c.isdigit():
            res.append(NUMBER_FOLLOWS)
            res.append(NUMBER_TO_BRAILLE[c])
        elif c == ' ':
            res.append(SPACE)
        else:
            res.append(ENGLISH_TO_BRAILLE[c.lower()])

    return ''.join(res)


if __name__ == '__main__':
    input_str = ' '.join(sys.argv[1:])

    if isBraille(input_str):
        print(translateToEnglish(input_str))
    else:
        print(translateToBraille(input_str))
    