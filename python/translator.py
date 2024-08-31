import sys

ENG_TO_BRAILLE = {
    # Alphabet
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', 
    # Follow Indicators + Space
    'cap': '.....O', 'num': '.O.OOO', ' ': '......'
}
NUM_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
BRAILLE_TO_ENG = {val: key for key, val in ENG_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {val: key for key, val in NUM_TO_BRAILLE.items()}

def isEnglish(text):
    for char in text:
        if char not in 'O.':
            return True
    return False

def translateBrailleToEnglish(text):
    i = 0
    res = ""
    while i < len(text):
        curr = text[i:i+6]
        if curr == ENG_TO_BRAILLE['cap']:
            i += 6
            if i < len(text):
                curr = text[i:i+6]
                res += BRAILLE_TO_ENG[curr].upper()
        elif curr == ENG_TO_BRAILLE['num']:
            i += 6
            while i < len(text):
                curr = text[i:i+6]
                if curr == ENG_TO_BRAILLE[' ']:
                    res += ' '
                    break
                res += BRAILLE_TO_NUM[curr]
                i += 6
        else:
            res += BRAILLE_TO_ENG[curr]
        i += 6
    return res

def translateEnglishToBraille(text):
    i = 0
    res = ""
    while i < len(text):
        curr = text[i]
        if curr.isupper():
            res += ENG_TO_BRAILLE['cap'] + ENG_TO_BRAILLE[curr.lower()]
        elif curr.isdigit():
            res += ENG_TO_BRAILLE['num'] + NUM_TO_BRAILLE[curr]
            i += 1
            while i < len(text):
                curr = text[i]
                if curr == ' ':
                    res += ENG_TO_BRAILLE[' ']
                    break
                res += NUM_TO_BRAILLE[curr]
                i += 1
        else:
            res += ENG_TO_BRAILLE[curr]
        i += 1
    return res

if __name__ == "__main__":
    text = ' '.join(sys.argv[1:])
    if isEnglish(text):
        print(translateEnglishToBraille(text))
    else:
        print(translateBrailleToEnglish(text))
