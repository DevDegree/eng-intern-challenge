import sys

brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

brailleNumbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capitalFollows = '.....O'
numberFollows = '.O.OOO'

englishAlphabet = {val: k for k, val in brailleAlphabet.items()}
englishNumbers = {val: k for k, val in brailleNumbers.items()}

def isBraille(text):
    validChar = {'O', '.'}
    valid = True
    for char in text:
        if char not in validChar:
            valid = False
            break
    return valid


def englishToBraille(text):
    result = []
    translatingNumber = False

    for char in text:
        if char.isdigit() and not translatingNumber:
            
            result.append(numberFollows)
            translatingNumber = True

        if char.isalpha():
            if translatingNumber:
                result.append(' ')
                translatingNumber = False
                
            if char.isupper():
                result.append(capitalFollows)
                
            result.append(brailleAlphabet[char.lower()])
            
        elif char.isdigit():
            result.append(brailleNumbers[char])
    
        elif char == ' ':
            result.append(brailleAlphabet[' '])
            translatingNumber = False
    
    return ''.join(result)

def brailleToEnglish(brailleText):
    result = []
    i = 0
    length = len(brailleText)
    translatingNumber = False
    while i < length:
        
        brailleChar = brailleText[i:i+6]
        
        if brailleChar == capitalFollows:
            
            i += 6
            followingBrailleChar = brailleText[i:i+6]
            result.append(englishAlphabet[followingBrailleChar].upper())
            
        elif brailleChar == numberFollows:
            
            translatingNumber = True
            
        elif brailleChar == '......':
            
            result.append(' ')
            translatingNumber = False
            
        else:
            if translatingNumber:
                result.append(englishNumbers[brailleChar])
            else:
                result.append(englishAlphabet[brailleChar])
        i += 6

    return ''.join(result)

def main():
    text = ' '.join(sys.argv[1:])

    if isBraille(text):
        print(brailleToEnglish(text))
    else:
        print(englishToBraille(text))

if __name__ == "__main__":
    main()
