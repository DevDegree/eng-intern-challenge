#
# Imports
#
import sys

#
# Constants 
#
ENGLISH_TO_BRAILLE = { #English alphabet and numbers to Braille
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..", 
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.", 
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO", 
    'v': "O.O.OO", 
    'w': ".OOO.O", 
    'x': "OO..OO", 
    'y': "OO.OOO", 
    'z': "O..OOO",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..", 
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
    ' ': "......"
}

BRAILLE_TO_ENGLISH = { #Braille to english alphabet
    "O.....": 'a',
    "O.O...": 'b',
    "OO....": 'c',
    "OO.O..": 'd',
    "O..O..": 'e',
    "OOO...": 'f',
    "OOOO..": 'g',
    "O.OO..": 'h',
    ".OO...": 'i',
    ".OOO..": 'j',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z',
    '......': ' ',
}

BRAILLE_TO_DIGITS = { #Braille to digits 0-9
    "O.....": '1',
    "O.O...": '2',
    "OO....": '3',
    "OO.O..": '4',
    "O..O..": '5',
    "OOO...": '6',
    "OOOO..": '7',
    "O.OO..": '8',
    ".OO...": '9',
    ".OOO..": '0',
}

#Additional Braille constants
BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_SPACE = "......"
BRAILLE_INVALID_STRING = "Invalid braille string"

#
# HELPERS
#


# Returns true if the list of strings should be parsed as a Braille string
def isBraille(args: list[str]) -> bool: 
    rawString = "".join(args)
    numOfO = 0
    numOfDot = 0
    for char in rawString: 
        if char == 'O': 
            numOfO += 1
        elif char == '.': 
            numOfDot +=1
    return numOfO + numOfDot == len(rawString) and len(rawString)%6==0 

# Returns the Braille translation of inputStr
def translateFromEnglish(inputStr: str, conversionDict: dict[str, str]) -> str: 
    result = ""
    length = len(inputStr)
    for i in range(length): 
        char = inputStr[i]
        if char.isalpha() and char.isupper(): # for uppercase lettercase
            result += BRAILLE_CAPITAL_FOLLOWS
            result += conversionDict[char.lower()]
        elif char.isnumeric() and (i==0 or not(inputStr[i-1].isnumeric())):
            result += BRAILLE_NUMBER_FOLLOWS
            result += conversionDict[char]
        else: 
            result += conversionDict[char]
    return result 
        
# Returns the English translation of inputStr, or BRAILLE_INVALID_STRING if the inputted braille string is not valid
def translateFromBraille(inputStr: str, conversionDict: dict[str,str]) -> str: 
    result = ""
    i = 6
    length = len(inputStr)
    isNumber = False
    isCapital = False
    while i <= length: 
        brailleChar = inputStr[i-6:i]
        if brailleChar == BRAILLE_NUMBER_FOLLOWS: 
            isNumber = True
        elif isNumber and brailleChar != BRAILLE_SPACE: 
            result += BRAILLE_TO_DIGITS[brailleChar]
        elif brailleChar == BRAILLE_SPACE: 
            isNumber = False
            result += " "
        elif brailleChar == BRAILLE_CAPITAL_FOLLOWS: 
            isCapital = True
        else: #standard case 
            try:
                currChar = conversionDict[brailleChar]
            except KeyError:
                return BRAILLE_INVALID_STRING
            
            if isCapital: 
                result += currChar.upper()
                isCapital = False
            else: 
                result += currChar
        i += 6
    return result


# main
def main(): 
    args = sys.argv[1:]
    if isBraille(args): 
        result = translateFromBraille("".join(args), BRAILLE_TO_ENGLISH)
        if result == BRAILLE_INVALID_STRING: # if braille translation failed
            print(translateFromEnglish(" ".join(args), ENGLISH_TO_BRAILLE)) #translate as an english string instead
        else: 
            print(result)
    else: 
        print(translateFromEnglish(" ".join(args), ENGLISH_TO_BRAILLE))

# Entry
if __name__ == '__main__':
    main()

