import sys

textToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

brailleToText = {v: k for k, v in textToBraille.items()}

capitalNotation = '.....O'
numberNotation = '.O.OOO'

def isBraille(inputString):
    for char in inputString:
        if char not in "O.":
            return False
    return True

def translateToEnglish(braille):
    result = []
    isCapital = False
    isDigit = False
    
    for i in range(0, len(braille), 6):
        currentCharacter = braille[i:i+6]
        if currentCharacter == capitalNotation:
            isCapital = True
        elif currentCharacter == numberNotation:
            isDigit = True
        else:
            char = brailleToText.get(currentCharacter, '')
            if isCapital:
                char = char.upper()
                isCapital = False
            if char == ' ':
                isDigit = False
            if isDigit:
                char = str(ord(char) - 96)
            result.append(char)
    
    return ''.join(result)

def digitToChar(char):
    if(char == '0'):
        return 'j'
    return (chr(ord(char) + 48))

def translateToBraille(text):
    result = []
    isDigit = False
    
    for char in text:
        if char.isupper():
            result.append(capitalNotation)
            char = char.lower()
        if char.isdigit():
            if(not isDigit):
                result.append(numberNotation)
                isDigit = True
            char = digitToChar(char)
        if char == ' ':
            isDigit = False
        result.append(textToBraille[char])
    
    return ''.join(result)

def main():
    inputString = " ".join(sys.argv[1:])

    if isBraille(inputString):
        translatedString = translateToEnglish(inputString)
    else:
        translatedString = translateToBraille(inputString)
    
    print(translatedString)

if __name__ == "__main__":
    main()
