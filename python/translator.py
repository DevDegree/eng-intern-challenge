import sys

#Dict maps for eng to braille
numDict = {
            "1":"O.....", "2":"O.O...",
            "3":"OO....", "4": "OO.O..", 
            "5": "O..O..", "6": "OOO...", 
            "7": "OOOO..", "8": "O.OO..",
            "9": ".OO...", "0": ".OOO.." 
        }

specialDict = {
            "capFollows": ".....O",
            " ":"......", 
            "numFollows": ".O.OOO"
            }

alphaDict = {
            "a":"O.....", "b":"O.O...",
            "c":"OO....", "d": "OO.O..",
            "e": "O..O..", "f": "OOO...", 
            "g": "OOOO..", "h": "O.OO..", 
            "i": ".OO...", "j": ".OOO..",
            "k": "O...O.", "l": "O.O.O.",
            "m": "OO..O.", "n": "OO.OO.",
            "o": "O..OO.", "p": "OOO.O.", 
            "q": "OOOOO.", "r": "O.OOO.",
            "s": ".OO.O.", "t": ".OOOO.",
            "u": "O...OO", "v": "O.O.OO",
            "w": ".OOO.O", "x": "OO..OO",
            "y": "OO.OOO", "z": "O..OOO"
            }

#dict maps braille to english just for ease
inv_alphaDict ={v: k for k, v in alphaDict.items()}
inv_specialDict ={v: k for k, v in specialDict.items()}
inv_numDict ={v: k for k, v in numDict.items()}

#Return True if stirng is braille, else false
def isInputBraille(unidentifiedString):
    braille  = set("O" + ".")
    return set(unidentifiedString) <= braille 

#converts 6 char of braille to english or 1 char of english into braille
def converterChar(charVal, dict, isInputBraille):
    if isInputBraille: #output english
        return list(dict.keys())[list(dict.values()).index(charVal)]
    return dict[charVal]

##main running function
def stringFeeder(unidentifiedString):
    isBraille = isInputBraille(unidentifiedString)
    outputstr = ""
    numFlag = False
    capFlag = False
    if(isBraille): #Convert Braille to english
        listOfChars = [unidentifiedString[i:i+6] for i in range (0,len(unidentifiedString), 6)]
        for i in listOfChars:
            if i in inv_specialDict:
                if i == ".O.OOO": #numFollows
                    numFlag = True
                    continue
                elif i == ".....O": #capfollows
                    capFlag =True
                    continue
                else:
                    outputstr+= inv_specialDict[i]
                    numFlag = False
                    continue
            if numFlag == True:
                outputstr += converterChar(i, numDict, isBraille)
            elif capFlag == True:
                outputstr += converterChar(i, alphaDict, isBraille).upper()
                capFlag = False
            else:
               outputstr += converterChar(i, alphaDict, isBraille)
    else: #Convert English to Braille
        for i in unidentifiedString:
            if i.isnumeric():
                if numFlag == False:
                    outputstr += specialDict["numFollows"]
                    numFlag = True
                outputstr += converterChar(i, numDict, isBraille)
            elif i in specialDict:
                if i == " ":
                    if numFlag == True:
                        numFlag = False
                    outputstr += specialDict[" "]
            else: #letter
                if i.isupper():
                    outputstr += specialDict["capFollows"]
                outputstr+= alphaDict[i.lower()]
    return outputstr

if __name__ == '__main__':
    parsed = sys.argv[1:]
    stringified = ' '.join(parsed)
    outputStr = stringFeeder(stringified)
    print(outputStr)