#Snowie Gao's Shopify Intern Challenge Submission

import sys

#Create Dictionaries for Braille -> Char, and vice versa
charDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', 
    '.' : '..OO.O', ',' :'..O...','?' :'..O.OO',
    '!':'..OOO.', ':' : '..OO..', ';' : '..O.O.', 
    '-' : '....OO', '/' :'.O..O.', '<' : '.OO..O', 
    '>' : 'O..OO.', '(' : 'O.O..O', ')' : '.O.OO.', 
    ' ': '......'
}

brailleDict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c',
    'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i',
    '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ',
    '..OO.O': '.', '..O...': ',', '..O.OO': '?',
    '..OOO.': '!', '..O..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.': '/', '.O..O': '<',
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
 }

#We need a separate number dictionary, because the braille for these characters are the same as from 'a' to 'j'
numDict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 
    'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', 
    '.OOO..': '0'
}

def charToBraille(str):
    brailleStr = ""
    prevCharNumeric = False
    for char in str:
        if(char.isupper()): #Append capital_follows
            brailleStr += ".....O"
        if(char.isnumeric() and not prevCharNumeric): #If this is the first digit in a number sequence
            prevCharNumeric = True
            brailleStr += ".O.OOO"
        if(char == ' ' and prevCharNumeric): #A space at the end of a number sequence denotes the end of the number
            prevCharNumeric = False
        brailleStr += charDict[char.lower()]
    return brailleStr

def brailleToChar(str):
    charStr = ""
    isNum = False
    isUpper = False
    brailleStr = [str[i:i + 6] for i in range(0, len(str), 6)] #Split the string into groups of 6 characters
    for brailleChar in brailleStr:
        if(isNum):
            if(brailleChar == "......"): #Spaces denote the end of numbers; switch back to the character dictionary
                isNum = False
                charStr += " "
            else:
                charStr += numDict[brailleChar]
        elif brailleChar == ".O.OOO": #capital_follows and number_follows do not code for digits, we only set flags here.
            isNum = True
            continue
        elif brailleChar == ".....O":
            isUpper = True
            continue
        else:
            if isUpper:
                isUpper = False
                charStr += brailleDict[brailleChar].upper()
                continue
            charStr += brailleDict[brailleChar]
    return charStr

def isBraille(str):
    if not ("." in str and "O" in str):
        return False
    for char in str:
        if not (char == "." or char == "O"):
            return False
    return True


if __name__ == '__main__':
    toTranslate = " ".join(sys.argv[1:])
    if(isBraille(toTranslate)):
        print(brailleToChar(toTranslate))
    else:
        print(charToBraille(toTranslate))
