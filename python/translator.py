import sys

letterToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

numberToBraille = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

brailleToLetter = {v: k for k, v in letterToBraille.items()}
brailleToNumber = {v: k for k, v in numberToBraille.items()}

capitalFollows = ".....O"
numberFollows = ".O.OOO"
space = "......"

def isBraille(inString):
    if(len(inString) % 6 != 0):
        return False
    for x in inString:
        if(x != '.' and x != 'O'):
            return False
    return True

def brailleToEnglish(inString):
    groupsOfSix = [inString[i:i+6] for i in range(0, len(inString), 6)]
    outString = ""
    isCapital = False
    isNumber = False
    for x in groupsOfSix:
        if x == capitalFollows:
            isCapital = True
        elif x == numberFollows:
            isNumber = True
        elif x == space:
            isNumber = False
            outString = outString + ' '
        elif isNumber == True:
            outString = outString + brailleToNumber.get(x)
        else:
            char = brailleToLetter.get(x)
            if isCapital == True:
                outString = outString + char.upper()
                isCapital = False
            else:
                outString = outString + char
    return outString

def englishToBraille(inString):
    outString = ""
    isNumber = False
    for x in inString:
        if x.isnumeric():
            if(isNumber == False):
                outString = outString + numberFollows
                isNumber == True
            outString = outString + numberToBraille.get(x)
        elif x == ' ':
            isNumber == False
            outString = outString + space
        elif x.isupper():
            outString = outString + capitalFollows + letterToBraille.get(x.lower())
        else:
            outString = outString + letterToBraille.get(x)
    return outString

def main():
    inputText = text = ' '.join(sys.argv[1:])
    if isBraille(inputText):
        print(brailleToEnglish(inputText))
        return
    print(englishToBraille(inputText))
    return

if __name__ == "__main__":
    main()