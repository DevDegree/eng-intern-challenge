import sys

brailleDict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..", "#": ".O.OOO", "^": ".....O"
}


engDict = {val: key for key, val in brailleDict.items()}

def isBrailleInput(inputStr):
    validBrailleChars = {"O", ".", " "}
    return set(inputStr).issubset(validBrailleChars)


def numOrCharTranslator(char, isNumberMode):
    for key, value in brailleDict.items():
        if value == char:
            if isNumberMode and key.isdigit():
                return key
            elif not isNumberMode and key.isalpha():
                return key
    return None


def brailleToEnglish(brailleStr):
    engOutput = []
    isNumberMode = False
    i = 0
    while i < len(brailleStr):
        char = brailleStr[i:i+6]
        if char == brailleDict["#"]:
            isNumberMode = True
        elif char == brailleDict["^"]:
            i += 6
            nextChar = brailleStr[i:i+6]
            for key, value in brailleDict.items():
                if value == nextChar and key.isalpha():
                    engOutput.append(key.upper())
        else:
            translatedChar = numOrCharTranslator(char, isNumberMode)
            if translatedChar:
                engOutput.append(translatedChar)
            if char == "......":  
                isNumberMode = False
                engOutput.append(" ")
        i += 6

    return "".join(engOutput)


def englishToBraille(englishStr):
    brailleOutput = []
    isNumSequence = False
    for char in englishStr:
        if char.isdigit():
            if not isNumSequence:
                brailleOutput.append(brailleDict["#"])
                isNumSequence = True
            brailleOutput.append(brailleDict[char])
        elif char == " ":
            isNumSequence = False  
            brailleOutput.append(brailleDict[char])
        elif char.isupper():
            brailleOutput.append(brailleDict["^"])
            brailleOutput.append(brailleDict[char.lower()])
        else:
            brailleOutput.append(brailleDict[char])
            
    return "".join(brailleOutput)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <string1> <string2> ...")
        return

    inputStr = " ".join(sys.argv[1:])

    if isBrailleInput(inputStr):
        print(brailleToEnglish(inputStr))
    else:
        print(englishToBraille(inputStr))

if __name__ == "__main__":
    main()
