import sys

# english: braille
EngToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......"
}
# numbers: braille 
NumsToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO.."
}
# special characters capital follows and number follows to braille
SpecToBraille = { "Capital": ".....O", "Number": ".O.OOO" }

# static string declaration to prevent using strings in comparisons
CapitalFollows = "Capital"
NumberFollows = "Number"
SpaceChar = " "

# check if the input is Braille
def IsBraille(inputStr):
    brailleChars = ["O", "."]
    for char in inputStr:
        if char not in brailleChars:
            return False
    return True

# check if the input is English
def IsEnglish(inputStr):
    for char in inputStr:
        if not char.isalpha() and not char.isnumeric() and char != SpaceChar:
            return False
    return True

# convert braille to English
def BrailleToEnglish(inputStr):
    # a complete braille input is made up of 6 chars
    if len(inputStr) % 6 != 0:
        print("Incorrect length input, must be a multiple of 6")
        exit()

    # Reverse the english/special/numbers to braille mapping
    brailleToEng = {value: key for key, value in EngToBraille.items()}
    brailleToSpec = {value: key for key, value in SpecToBraille.items()}
    brailleToNums = {value: key for key, value in NumsToBraille.items()}

    # check just to ensure the mapping was valid
    if len(brailleToEng) != len(EngToBraille) or len(brailleToSpec) != len(SpecToBraille) or len(brailleToNums) != len(NumsToBraille):
        print("Error with English/Braille mapping")
        exit()

    # 'number follows' or 'capital follows' flags
    numFlag = False
    capFlag = False

    for i in range(0, len(inputStr), 6):
        substring = inputStr[i:i+6]
        res = ""

        if substring in brailleToSpec:
            if brailleToSpec[substring] == NumberFollows:
                numFlag = True
            elif brailleToSpec[substring] == CapitalFollows:
                capFlag = True
            else:
                print("Error in BRAILLE_TO_SPEC")
                exit()
        elif numFlag and not capFlag:
            if substring in brailleToNums:
                res += brailleToNums[substring]
            elif substring in brailleToEng and brailleToEng[substring] == SpaceChar:
                res += brailleToEng[substring]
                numFlag = False
                capFlag = False
            else:
                print("Invalid braille for a number")
                exit()
        elif capFlag and not numFlag:
            if substring in brailleToEng and brailleToEng[substring] != SpaceChar:
                res += brailleToEng[substring].upper()
                capFlag = False
            else:
                print("Character after 'capital follows' must be a letter")
                exit()
        elif not numFlag and not capFlag:
            if substring in brailleToEng:
                res += brailleToEng[substring]
            else:
                print("Invalid braille for a letter")
                exit()
        else:
            print("Cannot have a number and capital follows next to each other")
            exit()

        print(res, end="")
    print()


# English to braille
def EnglishToBraille(inputStr):
    numFlag = False

    for char in inputStr:
        res = ""

        if char.isalpha() and char.isupper():
            res += SpecToBraille[CapitalFollows]
            res += EngToBraille[char.lower()]
        elif char.isdigit():
            if not numFlag:
                res += SpecToBraille[NumberFollows]
                numFlag = True
            res += NumsToBraille[char]
        elif char == SpaceChar or char.isalpha():
            res += EngToBraille[char]
            if char == SpaceChar:
                numFlag = False  
        else:
            print("Error reading character")
            exit()
        print(res, end="")
    print()

def TranslateInput():
    inputArgs = sys.argv[1:]
    concatRaw = ''.join(inputArgs)
    concatSpaced = ' '.join(inputArgs)

    # if there's no arguments then exit
    if not concatRaw or concatRaw == "":
        print("Error reading input or no input received")
        exit()

    if IsBraille(concatRaw):
        BrailleToEnglish(concatRaw)
    elif IsEnglish(concatSpaced):
        EnglishToBraille(concatSpaced)
    else:
        print("Error with inputs. Only braille OR alpha/numeric/space accepted")
        exit()

if __name__ == "__main__":
    TranslateInput()
