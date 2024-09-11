NUM = {
    '0': '.OOO..','1': 'O.....','2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..','8': 'O.OO..','9': '.OO...'
}

ALPHA = {
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
    'z': 'O..OOO'
}

PUNC = {
    '.': '..OO.O',',': '..O...','?': '..O.OO','!': '..OOO.',':': '..OO..',';': '..O.O.','-': '....OO','/': '.O..O.',' ': '......',
}

BRAILLE_ALPHA = dict((v, k) for k, v in ALPHA.items())
BRAILLE_NUM = dict((v, k) for k, v in NUM.items())
BRAILLE_PUNC = dict((v, k) for k, v in PUNC.items())


BRAILLE = {'O', '.'}

UPPERCASE = '.....O'
DEC = '.O...O'
NUMBER = '.O.OOO'



def english_to_braille(text: str) -> str:
    res = ''
    num = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                res += UPPERCASE
            res += ALPHA[char.lower()]
        elif char in NUM:
            if not num:
                num = True
                res += NUMBER
            res += NUM[char]
        elif char in PUNC:
            if char == ' ':
                num = False
            res += PUNC[char]

    return res


def braille_to_english(text: str) -> str:
    res = ''
    num = False
    upper = False

    for i in range(0, len(text), 6):
        braille = text[i: i+6]

        if braille == NUMBER:
            num = True
        elif braille == UPPERCASE:
            upper = True
        elif braille == PUNC[' ']:
            res += ' '
            num = False
        elif num:
            if braille == DEC:
                continue
            else:
                res += BRAILLE_NUM[braille]
                num = False
        elif braille in BRAILLE_ALPHA:
            res += BRAILLE_ALPHA[braille].upper() if upper else BRAILLE_ALPHA[braille]
            upper = False
        elif braille in BRAILLE_PUNC:
            res += BRAILLE_PUNC[braille]

    return res



if __name__ == '__main__':
    import sys
    args = sys.argv
    args.pop(0)

    text = ' '.join(args)
    is_braille_input = all(c in BRAILLE or c == ' ' for c in text)
    if is_braille_input:
        res = braille_to_english(text)
    else:
        res = english_to_braille(text)
    print(res)
