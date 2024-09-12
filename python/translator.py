# Done by Karen Florian Esquivel 

import string
import sys 
from textwrap import wrap

global dictBrailleEng
letters = list(string.ascii_lowercase)
braille = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..', 'O...O.', 'O.O.O.', 'OO..O.', 
'OO.OO.', 'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO']
dictBrailleEng = dict(zip(letters, braille))

global capitalFollows
capitalFollows = '.....O'

global numberFollows
numberFollows = '.O.OOO'

global space 
space = '......'

def checkType():
    if (len(sys.argv) > 2):
        convertToBraille(' '.join(sys.argv[1:]))
    else:
        userInput = sys.argv[1]
        isEnglish = False
        for i in userInput: 
            if (i != 'O' and i != '.'):
                isEnglish = True

        if isEnglish == True: 
            convertToBraille(userInput)
        else:
            convertToEnglish(userInput)


def convertToEnglish(brailleStr):
    seperatedCharacters = wrap(brailleStr, 6)
    output = ""
    isCapital = False
    isNumber = False
    
    for bChar in seperatedCharacters:
        if (bChar == capitalFollows):
            isCapital = True
        elif (bChar == numberFollows):
            isNumber = True
        elif (bChar == space):
            isNumber = False
            output += ' '
        else: 
            for letter, braille in dictBrailleEng.items():
                if (braille == bChar):
                    if (isCapital == True): 
                        output += letter.capitalize()
                        isCapital = False
                    elif (isNumber == True):
                        number = list(dictBrailleEng.keys()).index(letter) + 1
                        output += str(number)
                    else: 
                        output += letter
    
    print(output)


def convertToBraille(engStr): 
    output = ""
    isNumeric = False; 

    for char in engStr: 
        if (char.isdigit()):
            if (isNumeric == False): 
                output += numberFollows
            isNumeric = True; 
            output += list(dictBrailleEng.items())[int(char)-1][1]

        elif (char == ' '):
            isNumeric = False; 
            output += space

        else: 
            if (char.isupper()):
                output += capitalFollows
            
            for letter, braille in dictBrailleEng.items():
                if (letter == char.lower()):
                    output += braille

    print(output)


checkType()
