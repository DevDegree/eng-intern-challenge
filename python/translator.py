import sys

symbolHash = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", 
    "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
    " ": "......"
}

def checkEnglish(input):
    english = False
    if (
        len(set(input)) > 2 
        or len(input) < 6
        or ("O" not in input and "." not in input)
        ):
        english = True
    return english

def englishToBraille(input):
    braille = ""
    numOnly = False

    for i in input:
        if i == " ":
            numOnly = False
        elif i.isupper():
            braille += ".....O"
        elif i.isnumeric() and not numOnly:
            numOnly = True
            braille += ".O.OOO"
        braille += symbolHash[i.lower()] 
    return braille

def brailleToEnglish(input):
    english = ""
    capitalNxt = False
    numNxt = False
    for i in range(0, len(input), 6):
        process = input[i:i+6]
        if process == "......" and numNxt:
            numNxt = False
            continue
        elif process == ".....O":
            capitalNxt = True
            continue
        elif process == ".O.OOO":
            numNxt = True
            continue

        symbol = list(symbolHash.keys())[list(symbolHash.values()).index(process)]
        if capitalNxt:
            english += symbol.upper()
            capitalNxt = False
        elif numNxt:
            english += str(ord(symbol) - 96)
        else:
            english += symbol
    
    return english

if __name__ == "__main__":  

    userInput = ""
    args = sys.argv

    for i in range(1, len(args)):
        if i != len(args) - 1:
            userInput += args[i] + " "
        else:
            userInput += args[i]
        
    if checkEnglish(userInput):
        returnString = englishToBraille(userInput)
    else:
        returnString = brailleToEnglish(userInput)

    print(returnString, end='')