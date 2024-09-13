import sys

## Braille to English mapper
to_eng = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '..OO.O': '.',
    '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-',
    '.O..O.': '/', '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')', '......': ' '
}

## English to Braille mapper
to_braille = {}
for k, v in to_eng.items():
    to_braille[v] = k

def is_braille(input):
    return all(ch in ".O" for ch in input) and len(input) % 6 == 0

def eng_to_braille(s):
    res = ""
    is_num = False ## Keeps track of whether we are in a number sequence or not
    for ch in s:
        if ch.isupper():
            res += to_braille['capital']
            ch = ch.lower()
            res += to_braille[ch]
        elif ch.isdigit():
            if not is_num:
                res += to_braille['number']
                is_num = True
            if ch == '0':
                res += to_braille['j']
            else:
                res += to_braille[chr(ord(ch) + 48)]
        elif ch == ' ':
            is_num = False ## This ensures that we reset when required
            res += to_braille[ch]
        else:
            res += to_braille[ch]

    return res


def braille_to_eng(s):
    res = ""
    capital = False
    number = False
    for i in range(0, len(s), 6):
        cur = to_eng[s[i:i+6]]

        if cur == 'capital':
            capital = True
            continue
        elif cur == 'number':
            number = True
            continue
        elif cur == ' ':
            number = False
            res += ' '
            continue

        if number:
            if cur == 'j':
                res += '0'
            else:
                res += chr(ord(cur) - 48)
        elif capital:
            res += cur.upper()
            capital = False
        else:
            res += cur
        
    return res


if __name__ == '__main__':
    s = ' '.join(sys.argv[1:])

    if is_braille(s):
        res = braille_to_eng(s)
    else:
        res = eng_to_braille(s)
    
    print(res, end='')