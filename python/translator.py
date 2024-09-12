#Frederick Berube
#2024-08-29

import sys

brailleNumberToEnglishMap = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0" 
}

brailleToEnglishMap = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", 
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", 
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", 
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z", 

    ".....O": "capital follows", ".O.OOO": "number follows", "......": " ",


    # Decimals not currently supported by application but could be added at later date
    # "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    # "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    # ".OO..O": "<", "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",
    #  ".O...O": "decimal follows"
}

englishToBrailleMap = {v: k for k, v in brailleToEnglishMap.items()}
englishNumberToBrailleMap = {v: k for k, v in brailleNumberToEnglishMap.items()}

def isBraille(inputStr: str) -> bool:
    """Returns a boolean which represents wether the provided input string represents braille text or not"""
    if len(inputStr) % 6 != 0:
        #All braille text must contain a multiple of 6 characters
        return False 

    for c in inputStr:
        if c not in set(("O",".")): 
            #Braille text only contains '.' or 'o'
            return False 

    return True

def translateToEnglish(inputStr: str) -> str:
    """Returns the braille text translated into English"""
    res = ""
    brailleCharsSeperated = [inputStr[i:i+6] for i in range(0, len(inputStr), 6)]
    numberFollows = False
    capitalizeNext = False

    for c in brailleCharsSeperated:
        if brailleToEnglishMap[c] == "capital follows":
            capitalizeNext = True
        elif brailleToEnglishMap[c] == "number follows":
            numberFollows = True
        elif brailleToEnglishMap[c] == " ":
            numberFollows = False
            res += " "
        else:
            if numberFollows:
                res += brailleNumberToEnglishMap[c]
            elif capitalizeNext:
                res += brailleToEnglishMap[c].upper()
                capitalizeNext = False
            else:
                res += brailleToEnglishMap[c]
    return res

def translateToBraille(inputStr: str) -> str:
    """Returns the English text translated into braille"""     

    res = ""
    digitFollows = False
    for c in inputStr:
        if c.isupper():
            res += englishToBrailleMap["capital follows"]
            res += englishToBrailleMap[c.lower()]
        elif c.isdigit():
            if not digitFollows:
                res += englishToBrailleMap["number follows"]
                digitFollows = True
            res += englishNumberToBrailleMap[c]
        else: 
            if digitFollows:
                digitFollows = False
            res += englishToBrailleMap[c]

    return res

if __name__ == '__main__':
    if len(sys.argv) == 1: 
        sys.exit("Invalid command line arguments.")

    inputStr = " ".join(sys.argv[1:])

    if isBraille(inputStr):
        print(translateToEnglish(inputStr))
    else:
        print(translateToBraille(inputStr))
