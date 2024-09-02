# Imports

import string
import sys

# Compose arguments into single string

inputText = ""

for arg in sys.argv[1:]:
    if sys.argv.index(arg) < len(sys.argv) - 1:
        inputText += str(arg) + " "
    else:
        inputText += str(arg)

# Define English to Braille dictionaries and characters

englishCharacters = list(string.ascii_lowercase)
englishNumbers = list(string.digits)

brailleCharacters = [
    "O.....",
    "O.O...",
    "OO....",
    "OO.O..",
    "O..O..",
    "OOO...",
    "OOOO..",
    "O.OO..",
    ".OO...",
    ".OOO..",
    "O...O.",
    "O.O.O.",
    "OO..O.",
    "OO.OO.",
    "O..OO.",
    "OOO.O.",
    "OOOOO.",
    "O.OOO.",
    ".OO.O.",
    ".OOOO.",
    "O...OO",
    "O.O.OO",
    ".OOO.O",
    "OO..OO",
    "OO.OOO",
    "O..OOO",
]

brailleNumbers = [
    ".OOO..",
    "O.....",
    "O.O...",
    "OO....",
    "OO.O..",
    "O..O..",
    "OOO...",
    "OOOO..",
    "O.OO..",
    ".OO...",
]

englishBrailleCharacters = dict(zip(englishCharacters, brailleCharacters))
englishBrailleNumbers = dict(zip(englishNumbers, brailleNumbers))

brailleCapitalIndicator = ".....O"
brailleNumberIndicator = ".O.OOO"
brailleSpaceIndicator = "......"

# Check if input is Braille or English

isBraille = False
brailleCheckText = inputText[:6]
if (
    brailleCheckText in englishBrailleCharacters.values()
    or brailleCheckText in englishBrailleNumbers.values()
    or brailleCheckText == brailleCapitalIndicator
    or brailleCheckText == brailleNumberIndicator
    or brailleCheckText == brailleSpaceIndicator
):
    isBraille = True

outputString = ""

# Parse and convert Braille to English

if isBraille:

    inputStringList = []
    isNumber = False
    isUpper = False

    for x in range(int(len(inputText) / 6)):
        inputStringList.append(inputText[x * 6 : x * 6 + 6])

    for x in inputStringList:
        if x == brailleSpaceIndicator:
            isNumber = False
            outputString += " "
        elif x == brailleCapitalIndicator:
            isUpper = True
        elif x == brailleNumberIndicator:
            isNumber = True
        elif isNumber:
            outputString += list(englishBrailleNumbers.keys())[brailleNumbers.index(x)]
        elif isUpper:
            isUpper = False
            outputString += list(englishBrailleCharacters.keys())[
                brailleCharacters.index(x)
            ].upper()
        else:
            outputString += list(englishBrailleCharacters.keys())[
                brailleCharacters.index(x)
            ]

# Parse and convert English to Braille

else:

    prevChar = ""

    for x in inputText:
        if prevChar.isnumeric() and x.isnumeric():
            outputString += englishBrailleNumbers.get(x)
        elif x.isnumeric():
            outputString += brailleNumberIndicator + englishBrailleNumbers.get(x)
        elif x == " ":
            outputString += brailleSpaceIndicator
        elif x.isupper():
            outputString += brailleCapitalIndicator + englishBrailleCharacters.get(
                x.lower()
            )
        else:
            outputString += englishBrailleCharacters.get(x)

        prevChar = x

print(outputString)
