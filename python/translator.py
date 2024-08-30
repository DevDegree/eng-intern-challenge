import sys

# --------------  GLOBAL CONSTANTS -------------- #

EnglishSpecialSymbolsToBrailleDict = {
    "capitalFollows": ".....O",
    "numberFollows": ".O.OOO",
    "space": "......",
}

EnglishNumsToBrailleDict = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}
EnglishLettersToBrailleDict = {
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
}

# Inverting the EnglishSpecialSymbolsToBrailleDict
BrailleToEnglishSpecialSymbolsDict = {v: k for k, v in EnglishSpecialSymbolsToBrailleDict.items()}

# Inverting the EnglishNumsToBrailleDict
BrailleToEnglishNumsDict = {v: k for k, v in EnglishNumsToBrailleDict.items()}

# Inverting the EnglishLettersToBrailleDict
BrailleToEnglishLettersDict = {v: k for k, v in EnglishLettersToBrailleDict.items()}


# --------------  END OF GLOBAL CONSTANTS -------------- #


# isBraille(string: input) returns true if input string is braille, false otherwise.
# assumes that braille can ONLY contain O or .
def isBraille(input):
    for c in input:
        if (c != 'O' and c != '.'):
            return False
    return True
    

# outputBraille(string: english) takes a string in english, and prints out the braille equivalent IF the string is valid
# effects: prints
def outputBraille(english):
    brailleTextTokens = []
    numberFlag = False
    for symb in english:
        if "a" <= symb and symb<= "z":
            brailleTextTokens.append(EnglishLettersToBrailleDict[symb])
        elif "A" <= symb and symb <= "Z":
            brailleTextTokens.append(EnglishSpecialSymbolsToBrailleDict["capitalFollows"])
            brailleTextTokens.append(EnglishLettersToBrailleDict[symb.lower()])
        elif "0" <= symb and symb <= "9":
            if not numberFlag:
                brailleTextTokens.append(EnglishSpecialSymbolsToBrailleDict["numberFollows"])
                brailleTextTokens.append(EnglishNumsToBrailleDict[symb])
                numberFlag = True
            else:
                brailleTextTokens.append(EnglishNumsToBrailleDict[symb])
        elif symb == " ":
            brailleTextTokens.append(EnglishSpecialSymbolsToBrailleDict["space"])
            numberFlag = False
        else:
            raise Exception(
                "INPUT ERR: The character ", symb,  " is not in the implemeneted BRAILLE dictionary!"
            )
    brailleString = ""
    for item in brailleTextTokens:
        brailleString += item
    print(brailleString)

#
def outputEnglish(braille):
    if len(braille) % 6 != 0:
        raise ValueError("INPUT ERR: Invalid Braille input length")
    else:
        brailleChunks = [braille[i:i+6] for i in range(0, len(braille), 6)]
        englishText = []
        capitalFlag = False
        numberFlag = False
        for chunk in brailleChunks:
            if chunk in BrailleToEnglishSpecialSymbolsDict:
                command = BrailleToEnglishSpecialSymbolsDict[chunk]
                if (command == "capitalFollows"):
                    capitalFlag = True
                elif (command == "numberFollows"):
                    numberFlag = True
                elif (command == "space"):
                    englishText.append(' ')
                    numberFlag = False
            elif chunk in BrailleToEnglishLettersDict:
                if numberFlag:
                    englishText.append(BrailleToEnglishNumsDict[chunk])
                elif capitalFlag:
                    englishText.append(BrailleToEnglishLettersDict[chunk].upper())
                else:
                    englishText.append(BrailleToEnglishLettersDict[chunk])
                    capitalFlag = False
            else:
                raise ValueError(f"INPUT ERR: Unknown Braille pattern: {chunk}")
        print("".join(englishText))

def main():
    arguments = sys.argv[1:]
    # argumentsConcatted is the string to be converted
    argumentsConcatted = " ".join(arguments)
    
    
    if isBraille(argumentsConcatted):
        # convert BRAILLE to ENGLISH
        try:
            outputEnglish(argumentsConcatted)
        except Exception as e:
            print(f"{str(e)}")
    else:
        # convert ENGLISH to BRAILLE
        try:
            outputBraille(argumentsConcatted)
        except Exception as e:
            print(f"{str(e)}")


if __name__ == "__main__":
    main()
