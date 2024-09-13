import re
import sys

brailleToEng = {
    'O.....': 'a', 
    'O.O...': 'b', 
    'OO....': 'c', 
    'OO.O..': 'd', 
    'O..O..': 'e',
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j',
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n', 
    'O..OO.': 'o',
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's', 
    '.OOOO.': 't',
    'O...OO': 'u', 
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x', 
    'OO.OOO': 'y',
    'O..OOO': 'z', 
    '......': ' ',   
    '.....O': 'cap', 
    '.O...O':'dec', 
    '.O.OOO': 'num'     
}

engToBraille = {alpha: braille for braille, alpha in brailleToEng.items()}
engToBraille.pop('cap')
engToBraille.pop('dec')
engToBraille.pop('num')

numbersToBraille = {
    '0': '.OOO..', 
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....',
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..',
    '8': 'O.OO..', 
    '9': '.OO...' 
}

engToBraille.update(numbersToBraille)

def isBraille(test):
    return bool(re.match(r'^[O.]+$', test))

def convertToBraille(inputStr):
    output = ''

    #Flag to track if we're in a number sequence
    isNum = False

    #Loop through each character in the input
    for i in range(0, len(inputStr)):
        char = inputStr[i]

        #Check for uppercase letters and add a capitalization prefix
        if (re.match(r'^[A-Z]+$', char) and char != ' '):
            output += '.....O'

        #Check if the character is a number
        if (re.match(r'^[0-9]+$', char)):
            if not isNum:
                output += '.O.OOO'
                isNum = True
            output += numbersToBraille[char]
        else:
            if (isNum):
                isNum = False
            if (char == ' '):
                output += '......'
            else:
                char = char.lower()
                output += engToBraille[char] or ''
    return output

def convertToEng(inputStr):
    output = ''

    isCap = False
    isNum = False

    #Process input in chunks of 6 characters (each Braille symbol)
    for i in range(0, len(inputStr), 6):
        slice = inputStr[i: i + 6]

        if (slice == '.....O'):
            isCap = True
            continue

        if (slice == '.O.OOO'):
            isNum = True
            continue

        if (slice == '......' and not isNum):
            output += ' '
            continue

        char = next((key for key, value in numbersToBraille.items() if value == slice), None) if isNum else brailleToEng.get(slice)

        if (isCap and char):
            char = char.upper()
            isCap = False

        output += char or ''
        if (slice == '......' and isNum):
            isNum = False; 
    
    return output

def translate(inputStr):
    return convertToEng(inputStr) if isBraille(inputStr) else convertToBraille(inputStr)

inputString = ' '.join(sys.argv[1:])
print(translate(inputString))
