### Mohammed Omer Munam
### omer_munam@yahoo.com
### Shopify Engineering Assessment

import sys

#Initialization of all mappings and special symbols
capitalFollows = ".....O"
numberFollows = ".O.OOO"
decimalFollows = ".O...O"
space = "......"
symbolDict = {
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
    ")": ".O.OO.",
}
alphabetDict = {
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
    "z": "O..OOO" 
}
numbersDict = {
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

###
# Implementation
###
def getEnglishFromBrailleDictionary(dict, value):
    for key, val in dict.items():
        if value == val:
            return key
    return None

def processBraille(list):
    input = ''.join(list)
    result = ""
    if len(input) % 6 != 0:         # input must be of appropriate length i.e. multiple of 6
        raise Exception("Invalid Braille!!")
    
    numberRunning = False
    nextCapital = False
    while input:
        read = input[:6]
        input = input[6:]
        if read == space:
            numberRunning = False
            result += " "
        elif read == numberFollows:
            numberRunning = True
        elif read == capitalFollows:
            nextCapital = True
        else:
            if numberRunning:
                key = getEnglishFromBrailleDictionary(numbersDict, read)
            else:
                key = getEnglishFromBrailleDictionary(alphabetDict, read) or \
                      getEnglishFromBrailleDictionary(symbolDict, read)
            if key is not None:
                result += key.upper() if nextCapital else key
                nextCapital = False
    return result

def processEnglish(list):
    input = ' '.join(list)
    result = ""
    numberRunning = False
    for char in input:
        if char.islower():
            result += alphabetDict[char]
        elif char.isupper():
            result += capitalFollows
            result += alphabetDict[char.lower()]
        elif char.isdigit():
            if not numberRunning:
                numberRunning = True
                result += numberFollows
            result += numbersDict[char]
        elif char.isspace():
            numberRunning = False
            result += space
        else:
            result += symbolDict[char]
    return result

def checkIfInputBraille(input):
    s = input.replace('O', '').replace('.', '')     # After removing all 'O' and '.' nothing should remain if it is Braille
    return len(s) == 0

def getArguments():
    if (len(sys.argv) < 2):
        raise Exception("Invalid Input.")
    tempList = []
    for arg in sys.argv[1:]:        # ignoring first argument as that is the script name
        tempList.append(arg)
    return tempList

def main():
    list = getArguments()

    isBraille = checkIfInputBraille(list[0])
    if isBraille:
        output = processBraille(list)
    else:
        output = processEnglish(list)
    
    print(output) # Final output print


if __name__ == "__main__":
    main()