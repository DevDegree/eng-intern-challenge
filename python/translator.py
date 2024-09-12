import sys
import re

# Map letters an symbols to their braille equivalent
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

# Since numbers share the same braille as letters, have a separate dictionary
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

# Go through each letter in a string
# Parse each argument individually and then append a spaces between arguments (function only needs to process a single word)
# Cases: capital letter - append the capital character before the actual letter
# number - append number and then look at numList
# lowercase - proceed as normal
def englishToBraille(input):
    brailleString = ""
    i = 0
    while i < len(input):
        if input[i].isupper():
            # append the capital marker
            brailleString += ".....O"
            # append the lowercase letter
            brailleString += englishBrailleDict[input[i].lower()]
            i += 1
        # If a number is encountered
        elif input[i].isnumeric():
            # append the number marker but loop through the rest of the input until a space is encountered
            brailleString += ".O.OOO"
            while (i < len(input) and input[i] != " "):
                brailleString += numberDict[int(input[i])]
                i += 1
        else: 
            brailleString += englishBrailleDict[input[i]]
            i += 1

    print(brailleString)

# For english words, insert a space between each argument
inputString = ' '.join(sys.argv[1:])

# First verify if the given string is braille or english and run the corresponding function
def translator(inputString):
    if (re.match('^[O.]+$', inputString)):
        brailleToEnglish(inputString)
    else: 
        englishToBraille(inputString)

translator(inputString)

