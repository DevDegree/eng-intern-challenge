# Requirements: 
'''
EDGE CASES: 
    - decimal follows symbol - need to make sure that you use the decimal symbol not just period when you're translating a decimal from English to Braille
        this also has to work when you do numbers like .65 where there is no number before the decimal follows symbol. This should translate to decmial follows, 6, 5. 
    - string that is all O and . and length multiple of 6 but is not valid Braille - should just read it as English after trying Braille in that case


'''

# Imports
import sys

# Constants 
ENGLISH_TO_BRAILLE = {
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
    '.': "..OO.O", 
    ',': "..O...", 
    '?': "..O.OO", 
    '!': "..OOO.", 
    ':': "..OO..", 
    ';': "..O.O.", 
    '-': "....OO",
    '/': ".O..O.", 
    '<': ".OO..O", 
    '>': "O..OO.", 
    '(': "O.O..O", 
    ')': ".O.OO.", 
    ' ': "......"
}

BRAILLE_TO_ENGLISH = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}

BRAILLE_TO_DIGITS = {
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

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_DECIMAL_FOLLOWS = ".O...O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"

# Helpers

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

def translateFromEnglish(inputStr: str, conversionDict: dict[str, str]) -> str: 
    result = ""
    for i in range(len(inputStr)): 
        char = inputStr[i]
        if char.isalpha() and char.isupper(): # for uppercase lettercase
            result += BRAILLE_CAPITAL_FOLLOWS
            result += conversionDict[char.lower()]
        elif (char.isnumeric() or char == ".") and (i == 0 or not(inputStr[i-1].isnumeric() or inputStr[i-1] == ".")): 
            result += BRAILLE_NUMBER_FOLLOWS
            if char == ".": 
                result += BRAILLE_DECIMAL_FOLLOWS
            else: 
                result += conversionDict[char]
        elif char == "." and char != inputStr[-1] and inputStr[i+1].isnumeric():
            result += BRAILLE_DECIMAL_FOLLOWS
        else: 
            result += conversionDict[char]
    return result 
        

# main
def main(): 
    args = sys.argv[1:]
    if isBraille(args): 
        pass
    else: 
        print(translateFromEnglish(" ".join(args), ENGLISH_TO_BRAILLE))

# Entry
if __name__ == '__main__':
    main()

