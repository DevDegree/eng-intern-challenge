import sys

# This second lookup table is used for the conversion from English to Braille.
# I added it to keep an O(1) lookup
brailleToEnglishStringLookup = {
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
    "......": " ",
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OOO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")"
}

brailleToEnglishNumberLookup = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

englishToBrailleStringLookup = {
    "capital": ".....O",
    "decimal": ".O...O",
    "number":  ".O.OOO",
    " ": "......",
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
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO."
}

englishToBrailleNumberLookup = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

def isBraille(input):
  # If the input isn't a multiple of 6
  # then we know it's a conversion from English to braille (braille comes in 6-symbol-strings)
    if len(input) % 6 != 0:
        return False
    
    # Go through input and return false if found any character other than 'O' or '.'
    for i in range(len(input)):
         currentChar = input[i]
         if currentChar != 'O' and currentChar != '.':
             return False
         
    return True


def convertToEnglish(braille):
    finalResult = ""
    isNextCharNumber = False
    isNextCharCapital = False
    isNextCharDecimal = False
    
    currentStartIndex = 0
    currentEndIndex = 6

    # Loop through each braille symbol (6-character-string)
    while currentEndIndex <= len(braille) :
        currentSymbol = braille[currentStartIndex:currentEndIndex]
        currentStartIndex += 6
        currentEndIndex += 6
        symbolInEnglish = brailleToEnglishStringLookup[currentSymbol]

        # If there is a 'Number Follows' flag, 
        # skip to the next iteration of the loop and add the number(s) that follow(s)
        if symbolInEnglish == "number":
            isNextCharNumber = True
            continue

        # Not exactly sure if a 'Decimal Follows' flag comes right before a decimal or right before a decimal dot, 
        # but I made it work basically like the 'Number Follows' flag
        if symbolInEnglish == "decimal":
            isNextCharDecimal = True
            continue

        # If there is a 'Capital Follows' flag.
        # skip to the next iteration of the loop and only capitalize the next character
        if symbolInEnglish == "capital":
            isNextCharCapital = True
            continue

        if isNextCharCapital:
            finalResult += symbolInEnglish.upper()
            isNextCharCapital = False
        elif isNextCharDecimal:
            if symbolInEnglish == ".":
                finalResult += symbolInEnglish
                continue
            if symbolInEnglish == " ":
                isNextCharDecimal = False
                finalResult += " "
                continue
            finalResult += brailleToEnglishNumberLookup[currentSymbol]
        elif isNextCharNumber:
            if symbolInEnglish == " ":
                isNextCharNumber = False
                finalResult += " "
                continue
            finalResult += brailleToEnglishNumberLookup[currentSymbol]
        else:
            finalResult += symbolInEnglish

    return finalResult


def convertToBraille(englishPhrase):
    finalResult = ""
    isNextCharNumber = False

    # Loop through characters
    for i in range(len(englishPhrase)):
        currentChar = englishPhrase[i]

        # If character is uppercase, add 'Capital Follows' flag in braille
        if currentChar.isupper():
            finalResult += englishToBrailleStringLookup["capital"]

        # If character is a number, add 'Number Follows' flag in braille
        if currentChar.isnumeric() and not(isNextCharNumber):
            finalResult += englishToBrailleStringLookup["number"]
            isNextCharNumber = True

        # If character is a space, we can set the 'Number Follows' flag once again 
        if currentChar == " ":
            # If it's a space, we should check if a number follows
            isNextCharNumber = False

        if isNextCharNumber:
            finalResult += englishToBrailleNumberLookup[currentChar]
        else:    
            finalResult += englishToBrailleStringLookup[currentChar.lower()]

    return finalResult


input = sys.argv[1]
if isBraille(input):
    print(convertToEnglish(input))
else:
    print(convertToBraille(input))

''' Inputs to try:
- Input: Hello world
- Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

- Input: 42
- Output: .O.OOOOO.O..O.O...

- Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
- Output: Abc 123
'''
