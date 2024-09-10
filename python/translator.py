import sys
import re


# First verify if the given string is braille or english and run the corresponding function
def translator(inputString):
    if (re.match('^[O.]+$', inputString)):
        brailleToEnglish(inputString)
    else: 
        englishToBraille(inputString)

englishBrailleDict = {
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

charList = list(englishBrailleDict.keys())
brailleList = list(englishBrailleDict.values())

numberDict = {
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO..",
}

numList = list(numberDict.keys())
brailleNumList = list(numberDict.values())

# Go through every 6 characters and translate using the dictionary
def brailleToEnglish(input):
    englishString = ""
    i = 0
    while i < len(input):
        # Process first braille character
        braille = input[i: i + 6]
        i += 6
        # If capital marker found, append next character as capital and increment
        if (braille == ".....O"):
            braillePosition = brailleList.index(input[i: i + 6])
            englishString += charList[braillePosition].capitalize()
            i += 6
        # If number marker found use the number dictionary. Loop until a space is encountered and increment
        elif (braille == ".O.OOO"): 
            while (input[i: i + 6] != "......" and i < len(input)):
                brailleNumPosition = brailleNumList.index(input[i: i + 6])
                englishString += str(numList[brailleNumPosition])
                i += 6
        # If no markers, then the character is lowercase
        else:
            braillePosition = brailleList.index(braille)
            englishString += charList[braillePosition]
    print(englishString)

#Go through each letter in a string
def englishToBraille(english):
    print("english detected")

translator(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
