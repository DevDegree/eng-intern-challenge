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

    
        

# main
def main(): 
    args = sys.argv[1:]
    print(isBraille(args)) 

# Entry
if __name__ == '__main__':
    main()

