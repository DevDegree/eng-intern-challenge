# Shopify Eng Intern Challenge Fall - Winter 2025
# Author: Erik Lundberg
# Email: erik.lundberg32@gmail.com

# Forgive my use of camelcase

charToBraille= {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'capital': '.....O', 'number': '.O.OOO',
}

brailleToChar = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<',
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '.....O': 'capital',
    '.O.OOO': 'number'
}

brailleToNumber= {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

brailleNumbers = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..',
    'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..']

BRAILLE_CHARACTERS = ['O', '.']
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_SPACE = '......'
BRAILLE_LEN = 6

def isBraille(text):
    for letter in text: 
        if letter not in BRAILLE_CHARACTERS:
            return False
    return True

def brailleToSentence(braille):
    result = []
    tokenized = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize = False 
    number = False 
    for token in tokenized:
        if token == BRAILLE_CAPITAL: 
            capitalize = True
        elif token == BRAILLE_NUMBER:
            number = True
        elif token in brailleToNumber and number:
            result.append(brailleToNumber[token])
            capitalize = False
        elif token in brailleToChar:
            result.append(brailleToChar[token])
            if capitalize:
                result[-1] = result[-1].upper()
                capitalize = False
    return "".join(result)

def sentenceToBraille(sentence):
    result = []
    doingNumber = False
    for letter in sentence: 
        if not letter.isnumeric():
            doingNumber = False
            
        if letter.isupper():
            result.append(BRAILLE_CAPITAL)
            result.append(charToBraille[letter.lower()])
        elif letter == " ":
            result.append(BRAILLE_SPACE)
        elif letter.isnumeric():
            if not doingNumber:
                result.append(BRAILLE_NUMBER)
                doingNumber = True
            result.append(charToBraille[letter])
        else:  
            result.append(charToBraille[letter])
    return "".join(result)

import sys 
def main():
    toTranslate = " ".join(sys.argv[1:])
    
    if isBraille(toTranslate):
        return brailleToSentence(toTranslate)
    return sentenceToBraille(toTranslate)

if __name__ == '__main__':
    res = main() 
    print(res)