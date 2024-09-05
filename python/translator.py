import sys

braille_to_eng = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'CAP', '.O.OOO': 'NUM', '......': ' '
}
braille_to_num = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
eng_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'CAP': '.....O', 'NUM': '.O.OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def braille_translate(input):
    res = ''
    i = 0
    isNum = False
    while i < len(input):
        c = input[i:i+6]
        if braille_to_eng[c] == 'CAP':
            i += 6
            c = input[i:i+6]
            res += braille_to_eng[c].upper()
        elif braille_to_eng[c] == ' ':
            isNum = False
            res += ' '
        elif braille_to_eng[c] == 'NUM':
            isNum = True
        elif isNum:
            res += braille_to_num[c]
        else:
            res += braille_to_eng[c]
        i += 6
    return res

def eng_translate(input):
    res = ''
    isNum = False
    for c in input:
        if ord('A') <= ord(c) <= ord('Z'):
            res += eng_to_braille['CAP'] + eng_to_braille[c.lower()]
        elif not isNum and ord('.') <= ord(c) <= ord('9'):
            isNum = True
            res += eng_to_braille['NUM'] + eng_to_braille[c]
        elif isNum and ord('.') <= ord(c) <= ord('9'):
            res += eng_to_braille[c]
        elif c == ' ':
            isNum = False
            res += eng_to_braille[c]
        else:
            res += eng_to_braille[c]
    return res

if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    if len(input) % 6 == 0 and all(c in 'O.' for c in input):
        #braile to eng
        print(braille_translate(input))
    else:
        # eng to braile
        print(eng_translate(input))