import sys
from typing import List, Dict
from enum import IntEnum

class SpecialSymbol(IntEnum):
    CAP = 0
    NUM = 1
    DEC = 2
    SPACE = 3

letters = {
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

numbers = {
    '0': letters['j']
}

punctuations = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

symbols = {
    SpecialSymbol.CAP: '.....O',
    SpecialSymbol.DEC: '.O...O',
    SpecialSymbol.NUM: '.O.OOO',
    SpecialSymbol.SPACE: '......'
}

for i in range(1, 10):
    numbers[str(i)] = letters[chr(ord('a')+i-1)]

def encode(string: str) -> str:
    encodedSeq = []

    numEncode = False
    for c in string:
        if c == ' ':
            numEncode = False
            encodedSeq.append(symbols[SpecialSymbol.SPACE])
        elif c.isnumeric():
            if not numEncode:
                encodedSeq.append(symbols[SpecialSymbol.NUM])
                numEncode = True
            encodedSeq.append(numbers[c])
        elif c.isalpha():
            if c.isupper():
                encodedSeq.append(symbols[SpecialSymbol.CAP])
            encodedSeq.append(letters[c.lower()])
        else:
            encodedSeq.append(punctuations[c])

    return ''.join(encodedSeq)

def splitToSix(string: str) -> List[str]:
    result = []
    buffer = []
    for i, c in enumerate(string):
        if i and i%6 == 0:
            result.append(''.join(buffer))
            buffer = []
        buffer.append(c)
    
    if len(buffer):
        result.append(''.join(buffer))
    
    return result

def flipMap(map: Dict[str, str]) -> Dict[str, str]:
    result = {}
    for k, v in map.items():
        result[v] = k
    return result

def decode(string: str) -> str:
    lettersDecode = flipMap(letters)
    numbersDecode = flipMap(numbers)
    punctsDecode = flipMap(punctuations)
    symbolsDecode = flipMap(symbols)

    brailles = splitToSix(string)
    decodedSeq = []

    numDecode = False
    capDecode = False
    for bSymbol in brailles:
        if bSymbol in symbolsDecode:
            capDecode = False

            symbol = symbolsDecode[bSymbol]
            if symbol == SpecialSymbol.CAP:
                capDecode = True
            elif symbol == SpecialSymbol.NUM:
                numDecode = True
            elif symbol == SpecialSymbol.DEC:
                decodedSeq.append('.')
            else: # symbol == space
                decodedSeq.append(' ')
                numDecode = False
        else:
            if numDecode:
                decodedSeq.append(numbersDecode[bSymbol] if bSymbol in numbersDecode else punctsDecode[bSymbol])
            else:
                decodeChar = lettersDecode[bSymbol] if bSymbol in lettersDecode else punctsDecode[bSymbol]
                if capDecode:
                    decodeChar = decodeChar.capitalize()
                decodedSeq.append(decodeChar)
    
            capDecode = False
    
    return ''.join(decodedSeq)

def translate(strInput: str) -> str:
    isInputBraille = True
    if len(strInput) %6 == 0:
        for c in strInput:
            if c != 'O' and c != '.':
                isInputBraille = False
                break
    else:
        isInputBraille = False
    
    if (isInputBraille):
        return decode(strInput)
    return encode(strInput)

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 2:
        inputStr = ' '.join(args[1:])
        print(translate(inputStr))

# testCases = {
#     'Hello world': '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..',
#     '42': '.O.OOOOO.O..O.O...',
#     '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....': 'Abc 123'
# }

# for i, (testInput, expected) in enumerate(testCases.items()):
#     if translate(testInput) == expected:
#         print(f'Test case {i} passed')
#     else:
#         print(f'Test case {i} failed: expected {expected}, got {translate(testInput)}')