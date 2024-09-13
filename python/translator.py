import sys

# Braille encoding for letters, numbers, and special symbols
brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def textToBraille(text):
    result = []
    isNumber = False
    for char in text:
        if char.isdigit():
            if not isNumber:
                result.append(brailleDict['number'])
                isNumber = True
        else:
            isNumber = False
            if char.isupper():
                result.append(brailleDict['capital'])
        result.append(brailleDict[char.lower()])
    return ''.join(result)

def brailleToText(braille):
    letterDict = {v: k for k, v in brailleDict.items() if len(k) == 1 and k.isalpha()}
    numberDict = {v: k for k, v in brailleDict.items() if len(k) == 1 and k.isdigit()}
    
    result = []
    i = 0
    isNumber = False
    capitalizeNext = False
    
    while i < len(braille):
        char = braille[i:i+6]
        i += 6
        
        if char == brailleDict['number']:
            isNumber = True
        elif char == brailleDict['capital']:
            capitalizeNext = True
        elif char == brailleDict[' ']:
            result.append(' ')
            isNumber = False
        else:
            if isNumber and char in numberDict:
                result.append(numberDict[char])
            elif char in letterDict:
                letter = letterDict[char]
                if capitalizeNext:
                    letter = letter.upper()
                    capitalizeNext = False
                result.append(letter)
                isNumber = False
    
    return ''.join(result)

def detect_and_translate(input_str):
    if set(input_str) <= {'O', '.'}:
        return brailleToText(input_str)
    else:
        return textToBraille(input_str)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <'text'>")
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])
    print(detect_and_translate(input_text))
