englishToBraille = {
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
    ' ': '......'
}

brailleToEnglish = {v: k for k, v in englishToBraille.items()}
brailleToNumbers = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}
capitalFollows = '.....O'
numberFollows = '.O.OOO'

def convertEnglishToBraille(englishString):
    output =''
    isCurrentNumber = False
    for c in englishString:
        if c.isnumeric():
            if isCurrentNumber == False:
                output+=numberFollows
                isCurrentNumber = True
        else:
            isCurrentNumber = False
        if c.isalpha() and c.isupper():
            output+=capitalFollows
            c = c.lower()
        output+=englishToBraille.get(c)
    return output

def convertBrailleToEnglish(brailleString):
    output = ''
    batch=''
    nextIsCapital = False
    nextIsNumber = False
    for b in brailleString:
        batch+=b
        if len(batch) == 6:
            if batch == capitalFollows:
                nextIsCapital = True
            elif batch == numberFollows:
                nextIsNumber = True
            else:
                if nextIsNumber:
                    if batch == englishToBraille.get(' '):
                        nextIsNumber = False
                        output+=' '
                    else:
                        output+=brailleToNumbers.get(batch)
                else:
                    toAdd = brailleToEnglish.get(batch)
                    if nextIsCapital:
                        toAdd = toAdd.upper()
                        nextIsCapital=False
                    output+=toAdd
            batch=''
    return output

import sys
input = sys.argv
inputString = ""
input.pop(0)
for i in input:
    inputString += i
    inputString+=' '
#remove trailing space
inputString = inputString[:-1]

#Determine if the input is english
isEnglish = False
for i in inputString:
    if (i != '.') and (i != 'O'):
        isEnglish = True
        break
#It also could be the case that we want to convert '...' or 'O' to Braille.
#Check if the input string is at least 6 symbols long.
if len(inputString) < 6:
    isEnglish = True
if isEnglish:
    print(convertEnglishToBraille(inputString))
else:
    print(convertBrailleToEnglish(inputString))