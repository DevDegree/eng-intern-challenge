import sys

def isBraille(string):
    return all(char in {'o', '.'} for char in string) 

def charToBraille(char):
    brailleMap = {
    'a': 'o.....',
    'b': 'o.o...',
    'c': 'oo....',
    'd': 'oo.o..',
    'e': 'o..o..',
    'f': 'ooo...',
    'g': 'oooo..',
    'h': 'o.oo..',
    'i': '.oo...',
    'j': '.ooo..',
    'k': 'o...o.',
    'l': 'o.o.o.',
    'm': 'oo..o.',
    'n': 'oo.oo.',
    'o': 'o..oo.',
    'p': 'ooo.o.',
    'q': 'ooooo.',
    'r': 'o.ooo.',
    's': '.oo.o.',
    't': '.oooo.',
    'u': 'o...oo',
    'v': 'o.o.oo',
    'w': '.ooo.o',
    'x': 'oo..oo',
    'y': 'oo.ooo',
    'z': 'o..ooo',
    '1': 'o.....',
    '2': 'o.o...',
    '3': 'oo....',
    '4': 'oo.o..',
    '5': 'o..o..',
    '6': 'ooo...',
    '7': 'oooo..',
    '8': 'o.oo..',
    '9': '.oo...',
    '0': '.ooo..',
    ' ': '......'
}
    return brailleMap.get(char.lower(), 'ERROR').upper()

def brailleToChar(braille):
    engMap = {
    'o.....': 'a',
    'o.o...': 'b',
    'oo....': 'c',
    'oo.o..': 'd',
    'o..o..': 'e',
    'ooo...': 'f',
    'oooo..': 'g',
    'o.oo..': 'h',
    '.oo...': 'i',
    '.ooo..': 'j',
    'o...o.': 'k',
    'o.o.o.': 'l',
    'oo..o.': 'm',
    'oo.oo.': 'n',
    'o..oo.': 'o',
    'ooo.o.': 'p',
    'ooooo.': 'q',
    'o.ooo.': 'r',
    '.oo.o.': 's',
    '.oooo.': 't',
    'o...oo': 'u',
    'o.o.oo': 'v',
    '.ooo.o': 'w',
    'oo..oo': 'x',
    'oo.ooo': 'y',
    'o..ooo': 'z',
    'o.....' : '1',
    'o.o...' : '2',
    'oo....' : '3',
    'oo.o..' : '4',
    'o..o..' : '5',
    'ooo...' : '6',
    'oooo..' : '7',
    'o.oo..' : '8',
    '.oo...' : '9',
    '.ooo..' : '0',
    '......': ' '
    }
    return engMap.get(braille.lower(), 'ERROR')

def engToBraille(string):
    translation = []
    numeric = False
    for char in string:
        if char.isupper():
            translation.append('.....O')
        elif char.isnumeric() and not numeric:
            translation.append('.O.OOO')
            numeric = True
        translation.append(charToBraille(char))
    return ''.join(translation)

def brailleToEng(input):
    translation = []
    for string in input.split('......'):
        translation.append(''.join(brailleToChar(c) for c in string))
    return ''.join(translation)

input = []
for line in sys.argv:
    if line == 'translator.py':
        continue
    input.append(line)

braille = False
if isBraille(input[0]):
    braille = True
output = []
for line in input:
    if braille:
        output.append(brailleToEng(line))
    else:
        output.append(engToBraille(line))
if braille:
    print(' '.join(output))
else:
    print('......'.join(output))
