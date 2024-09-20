import sys
from brailleEnglishUtils import *
from enum import Enum

#TODO TEST command line

class Language(Enum):
    BRAILLE = 0
    ENGLISH = 2

class BrailleMode(Enum):
    NORMAL = 0
    CAPITAL = 1
    NUMBER = 2
    
#Checks if string is in English or in Braille
#Assumes Braille if all characters are O or . and input length is a multiple of 6 
#     and not some obscure English sentence.
def language(inputStr):
    if len(inputStr)%6 != 0:
        return Language.ENGLISH
    for char in inputStr:
        if char != 'O' and char != '.':
            return Language.ENGLISH
    return Language.BRAILLE

#Translate Braille character to English
def to_english(char, mode):
    modeChange = mode_change(char)
    if(modeChange == ModeChange.SPACE):
        return " ", BrailleMode.NORMAL
    if(modeChange == ModeChange.CAPITAL):
        return "", BrailleMode.CAPITAL
    if(modeChange == ModeChange.NUMBER):
        return "", BrailleMode.NUMBER
        
    engChar = brailleToEng(char)
    if(mode == BrailleMode.NORMAL):
        return engChar, BrailleMode.NORMAL
    if(mode == BrailleMode.CAPITAL):
        return engChar.upper(), BrailleMode.NORMAL
    if(mode == BrailleMode.NUMBER):
        return to_number(engChar), BrailleMode.NUMBER

    #default return
    return None, mode
    
def braille_to_english(inputStr):
    englishOut = ''
    currMode = BrailleMode.NORMAL
    
    for i in range(0, len(inputStr), 6):
        currChar = inputStr[i:i+6]
        engChar, currMode = to_english(currChar, currMode)
        englishOut += engChar
    return englishOut
    
#Translate English character to Braille
def to_braille(char, mode):
    if(char.isalpha()):
        prefix = mode_to_braille(ModeChange.CAPITAL) if char.isupper() else ''
        return prefix + eng_to_braille(char.lower()), BrailleMode.NORMAL
    if(char == ' '):
        return  mode_to_braille(ModeChange.SPACE), BrailleMode.NORMAL
    if(char.isnumeric()):
        prefix =  mode_to_braille(ModeChange.NUMBER) if mode == BrailleMode.NORMAL else ''
        return prefix + num_to_braille(char), BrailleMode.NUMBER

    #default return
    return None, mode
    
def english_to_braille(inputStr):
    brailleOut = ''
    currMode = BrailleMode.NORMAL
    
    for i in range(0, len(inputStr)):
        currChar = inputStr[i]
        brailleString, currMode = to_braille(currChar, currMode)
        brailleOut += brailleString
    return brailleOut

#assume input has been cleaned and no strange cases like 123abc or capital follows into number follows etc. 
if __name__ == '__main__':
    #Assumes that all arguments are separated by a single space
    inputStr = ' '.join(sys.argv[1:])
    
    lang = language(inputStr)
    if (lang == Language.BRAILLE):
        print(braille_to_english(inputStr))
    if (lang == Language.ENGLISH):
        print(english_to_braille(inputStr))
