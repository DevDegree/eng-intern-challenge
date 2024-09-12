import sys
# dictionaries
alphaToBrailleDict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.",
    "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", " ": "......", "capital":".....O", "number":".O.OOO"
}
brailleToAlphaDict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i",  ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q","O.OOO.": "r",".OO.O.": "s",".OOOO.": "t","O...OO": "u",
    "O.O.OO": "v",".OOO.O": "w","OO..OO": "x","OO.OOO": "y","O..OOO": "z","......": " ", ".....O": "capital", ".O.OOO": "number"
}
brailToNumDict = {
    ".OOO..": "0","O.....": "1","O.O...": "2","OO....": "3","OO.O..": "4","O..O..": "5",
    "OOO...": "6","OOOO..": "7","O.OO..": "8",".OO...": "9"
}

# English to Braille function
def alphaToBraille(rawText):
    translatedText = ''
    isNumber = False
    for char in rawText:
        if char.isupper():
           translatedText = translatedText + alphaToBrailleDict.get("capital")
        elif char.isnumeric() and isNumber == False:
            isNumber = True
            translatedText = translatedText + alphaToBrailleDict.get("number")
        elif char == " ":
            isNumber = False
        translatedText = translatedText + alphaToBrailleDict.get(char.lower())
    print(translatedText)

# Braille to English function
def brailleToAlpha(rawText):
    translatedText = ''
    isNumber = False
    isCapital = False
    for i in range(0, len(rawText), 6):
        if rawText[:6] == alphaToBrailleDict.get("capital"):
            isCapital = True
            rawText = rawText[6:]
            continue
        elif rawText[:6] == alphaToBrailleDict.get("number"):
            isNumber = True
            rawText = rawText[6:]
            continue
        elif rawText[:6] == alphaToBrailleDict.get(" "):
            isNumber = False

        if isCapital:   
            translatedText = translatedText + brailleToAlphaDict.get(rawText[:6]).capitalize()
        elif isNumber:   
            translatedText = translatedText + brailToNumDict.get(rawText[:6])
        else:
            translatedText = translatedText + brailleToAlphaDict.get(rawText[:6])

        isCapital = False
        rawText = rawText[6:]
    print(translatedText)

# getting the rawText (input) from the command line arguments
rawText = ''
for n in range(1, len(sys.argv)):
    if n == 1:
        rawText = rawText + sys.argv[n]
    else:
        rawText = rawText + " " + sys.argv[n]
        
# finding which translation to make        
if len(rawText) == rawText.count(".") + rawText.count("O"):
    brailleToAlpha(rawText)
else:
    alphaToBraille(rawText)
