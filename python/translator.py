import sys

brailleDictionary = {
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
    '#': '.O.OOO', 
    '^': '.....O' 
}

reverse = {v: k for k, v in brailleDictionary.items()}
def isBraille(text):
    return all(c in 'O.' for c in text)

def engToBr(text):
    res = ''

    for i in text:
        if i.isupper():
            res += brailleDictionary['^']
            i = i.lower()
        if i.isdigit():
            res += brailleDictionary['#']
        res += brailleDictionary[i]

    return res

def brToEng(text):
    res = ''
    i = 0
    number = False
    capital = False
    while i < len(text):
        symbol = text[i:i+6]

        if symbol == brailleDictionary['#']:
            number = True
            i += 6
            continue
        
        if symbol == brailleDictionary['^']:
            capital = True
            i += 6
            continue

        letter = reverse.get(symbol)
        if letter is not None:
            if capital:
                letter = letter.upper()
                capital = False
            if number:
                if letter.isdigit():
                    res.append(letter)
                number = False
            else:
                res.append(letter)
        i += 6
    return res
    
input = sys.argv[1]

if isBraille(input):
    translated = brToEng(input)
else:
    translated = engToBr(input)

print(translated)