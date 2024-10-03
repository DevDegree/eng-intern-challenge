import sys

lettersToBraille= {
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

brailleToLetters= {val: key for key, val in lettersToBraille.items()}

numbersToBraille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

brailleToNumbers= {val: key for key, val in numbersToBraille.items()}

capitalFollows = '.....O'
numbersFollows = '.O.OOO'
space = '......'

def translate(text):
    if '.' in text:
        print(translateBrailleToLetters(text))
    else:
        print(translateLettersToBraille(text))

def translateBrailleToLetters(text):
    isCapital = False
    isNumber = False

    translatedText = ''
    for i in range(0, len(text), 6):
        brailleValue = text[i:i+6]
        if brailleValue == space:
            translatedText += ' '
            isCapital = False
            isNumber = False
        elif brailleValue == capitalFollows:
            isCapital = True
        elif brailleValue == numbersFollows:
            isNumber = True
        elif isNumber:
            translatedText += brailleToNumbers[brailleValue]
        elif isCapital:
            translatedText += brailleToLetters[brailleValue].upper()
            isCapital = False
        else:
            translatedText += brailleToLetters[brailleValue]
    return translatedText

def translateLettersToBraille(text):
    translatedText = ''
    i = 0
    while i < len(text):
        char = text[i]
        if char.isdigit():
            translatedText += numbersFollows
            while i < len(text) and text[i].isdigit():
                translatedText += numbersToBraille[text[i]]
                i += 1

        elif char == ' ':
            translatedText += space
            i += 1
        elif char == char.upper():
            translatedText += capitalFollows
            translatedText += lettersToBraille[char.lower()]
            i += 1
        else:
            translatedText += lettersToBraille[char]
            i += 1
    return translatedText


if __name__ == '__main__':
    text = ' '.join(sys.argv[1:])
    translate(text)