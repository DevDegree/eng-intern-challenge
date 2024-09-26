# Mihir Patel
# September 25th, 2024

#Variables for the input and the output, account for system input
import sys

StartingString = ''.join(sys.argv[1:])
FinalTranslation = ""
#Dictionaries to store values based on what is input
EnglishToBraille = {

    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",

    "A": ".....OO.....",
    "B": ".....OO.O...",
    "C": ".....OOO....",
    "D": ".....OOO.O..",
    "E": ".....OO..O..",
    "F": ".....OOOO...",
    "G": ".....OOOOO..",
    "H": ".....OO.OO..",
    "I": ".....O.OO...",
    "J": ".....O.OOO..",
    "K": ".....OO...O.",
    "L": ".....OO.O.O.",
    "M": ".....OOO..O.",
    "N": ".....OOO.OO.",
    "O": ".....OO..OO.",
    "P": ".....OOOO.O.",
    "Q": ".....OOOOOO.",
    "R": ".....OO.OOO.",
    "S": ".....O.OO.O.",
    "T": ".....O.OOOO.",
    "U": ".....OO...OO",
    "V": ".....OO.O.OO",
    "W": ".....O.OOO.O",
    "X": ".....OOO..OO",
    "Y": ".....OOO.OOO",
    "Z": ".....OO..OOO",

    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": "O..OOO",

    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"

}

BrailleToEnglish = {
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



    '.....OO.....': 'A', 
    '.....OO.O...': 'B', 
    '.....OOO....': 'C', 
    '.....OOO.O..': 'D', 
    '.....OO..O..': 'E', 
    '.....OOOO...': 'F', 
    '.....OOOOO..': 'G', 
    '.....OO.OO..': 'H', 
    '.....O.OO...': 'I', 
    '.....O.OOO..': 'J', 
    '.....OO...O.': 'K', 
    '.....OO.O.O.': 'L', 
    '.....OOO..O.': 'M', 
    '.....OOO.OO.': 'N', 
    '.....OO..OO.': 'O', 
    '.....OOOO.O.': 'P', 
    '.....OOOOOO.': 'Q', 
    '.....OO.OOO.': 'R', 
    '.....O.OO.O.': 'S', 
    '.....O.OOOO.': 'T', 
    '.....OO...OO': 'U', 
    '.....OO.O.OO': 'V', 
    '.....O.OOO.O': 'W', 
    '.....OOO..OO': 'X', 
    '.....OOO.OOO': 'Y', 
    '.....OO..OOO': 'Z',

    "..OO.O" :".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
    
}

#Extra number dictionary for binary since you can have repeating values
BrailleToNumber = {
    
    ".OOO..": "0",
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    "O..OOO": "9"
    
}


#Checking if there are only O and . in the input string
if all(char in {'O', '.'} for char in StartingString):
    i = 0
    #Start loop
    while i < len(StartingString):
        #Create a local variable called Braille which takes the first 6 chars in the string
        Braille = StartingString[i:i + 6]
        #if statement to create capital letters
        if Braille == ".....O":
            if (i + 12 <= len(StartingString)):
                Braille = StartingString[i + 6:i + 12]
                FinalTranslation += BrailleToEnglish[".....O" + Braille]
                i += 12
        #an elif statement incase you want to only start entering numbers
        elif Braille == ".O.OOO":  
            NumberInputs = True
            i += 6
            while NumberInputs and i + 6 <= len(StartingString):
                Braille = StartingString[i:i + 6]
                FinalTranslation += BrailleToNumber[Braille]
                i += 6 
        #an elif statement to stop the number mode when theres a space
        elif Braille == "......": 
            NumberInputs = False
            FinalTranslation += BrailleToEnglish[Braille]
            i += 6
        #else just add the char using the dictionary into the final string
        else:
            NumberInputs = False 
            FinalTranslation += BrailleToEnglish[Braille]
            i += 6
# The statement for when the input string is not only O and .
else:
    i = 0
    #More number mode to check if they're only entering numbers
    NumberMode = False  
    while i < len(StartingString):
        if StartingString[i].isdigit():
            if not NumberMode:
                #Adds the braille for the number mode
                FinalTranslation += ".O.OOO"  
                NumberMode = True 
            FinalTranslation += EnglishToBraille[StartingString[i]]
            i += 1
        #Otherwise just search the dictionary and add to the final string
        else:
            NumberMode = False 
            FinalTranslation += EnglishToBraille[StartingString[i]]
            i += 1
    
#Output the final string
print(FinalTranslation)