
import sys
import re

B_TO_E = {
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
        '.....O': 'capital',
        '.O.OOO': 'number',
        '......': ' '
        }
B_TO_E_NUM = {
            'O.....': '1', 
            'O.O...': '2',
            'OO....': '3',
            'OO.O..': '4',
            'O..O..': '5',
            'OOO...': '6',
            'OOOO..': '7',
            'O.OO..': '8',
            '.OO...': '9',
            '.OOO..': '0'}
E_TO_B = {v: k for k, v in B_TO_E.items()}
E_TO_B_NUM = {v: k for k, v in B_TO_E_NUM.items()}

def translate_braille_to_eng(text):
    ret = ''
    isNumber = False
    isCapital = False

    for i in range(0, len(text), 6):
        char = text[i: i + 6]
        if char == '.....O': # Capital follows
            isCapital = True
            continue 
        elif char == '.O.OOO': # Number follows
            isNumber = True
            continue
        elif char == '......': # Space => reset number
            isNumber = False


        if isCapital:
            ret += B_TO_E[char].upper()
            isCapital = False
        elif isNumber:
            ret += B_TO_E_NUM[char]
        else:
            ret += B_TO_E[char]

    return ret

def translate_eng_to_braille(text):
    ret = ''
    isNumber = False
    for i in range(len(text)):
        c = text[i]
        if c.isnumeric():
            if not isNumber:
                ret += E_TO_B['number']
                isNumber = True
            ret += E_TO_B_NUM[c]
        elif c.isupper():
            ret += E_TO_B['capital']
            ret += E_TO_B[c.lower()]
            isNumber = False
        else:
            ret += E_TO_B[c]
            isNumber = False

    return ret

ret = ''
if len(sys.argv[1]) % 6 == 0 and re.match("^[O\.]*$", sys.argv[1]):
    ret = translate_braille_to_eng('......'.join(sys.argv[1:]))
else:
    ret = translate_eng_to_braille(' '.join(sys.argv[1:]))
print(ret)

