import sys
import textwrap

del sys.argv[0]

BTOE = {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
        'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
        '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
        'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
        'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
        'OO.OOO': 'y', 'O..OOO': 'z', '......': ' '}
BTOE_NUM = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
            'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
            '.OO...': '9', '.OOO..': '0'}
ETOB = {v: k for k, v in BTOE.items()}
ETOB_NUM = {v: k for k, v in BTOE_NUM.items()}
FIRST = True

for arg in sys.argv:
    if all(c in ['O', '.'] for c in arg) and len(arg) % 6 == 0:
        # arg is braille
        chars = textwrap.wrap(arg, 6)
        i = 0
        while i < len(chars):
            if chars[i] == '.....O':
                # capital follows
                if i+1 < len(chars):
                    print(BTOE[chars[i+1]].capitalize(), end='')
                i += 2
            elif chars[i] == '.O.OOO':
                # number follows
                i += 1
                while i < len(chars) and chars[i] != '......':
                    print(BTOE_NUM[chars[i]], end='')
                    i += 1
            else:
                # regular character
                print(BTOE[chars[i]], end='')
                i += 1
    else:
        # arg is english
        if FIRST:
            FIRST = False
        else:
            print('......', end='')
        num = False
        for ch in arg:
            if ch in ETOB_NUM and not num:
                num = True
                print('.O.OOO', end='')
                print(ETOB_NUM[ch], end='')
            elif ch in ETOB_NUM and num:
                print(ETOB_NUM[ch], end='')
            elif ch.isupper():
                print('.....O', end='')
                print(ETOB[ch.lower()], end='')
            else:
                if num:
                    num = False
                print(ETOB[ch], end='')
