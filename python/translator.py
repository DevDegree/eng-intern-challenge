# Joshua Machado
# joshomac505@gmail.com
# Implemented 2024-09-28

import sys

enToBraille = {
    "codes": {
        "capitalFollows": ".....O",    # Indicates the next letter is capitalized
        "numberFollows": ".O.OOO",     # Indicates a number follows until a space is reached
        " ": "......",                 # Space
    },
    "letters": {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO"
    },
    "numbers" : {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
        "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }
}

# Load the braille to english dictionary
# Allows for mutable dictionary for future symbol additions, and one standard location for all symbols
brailleToEn = {
    "codes": {},
    "letters": {},
    "numbers": {}
}

# Reverse the english to braille dictionary
for category, subdict in enToBraille.items():
    for key, value in subdict.items():
        brailleToEn[category][value] = key


def isValidBraille(inputString):
    # Checks if the input string is a valid braille string
    # Parameters:
        # inputString (str): The string to check
    # Returns:
        # bool
    inputLen = len(inputString)
    
    # Braille input must be a multiple of 6
    if inputLen % 6 != 0:
        return False

    # Check if input string has valid braille mapping
    braillePatterns = set()

    # Iterate through each subdictionary and extract the braille patterns
    for category in enToBraille.values():
        braillePatterns.update(category.values())

    # Check if the input string is all valid braille patterns
    for i in range(0, inputLen, 6):
        brailleSymbol = inputString[i:i+6]
        
        if brailleSymbol not in braillePatterns:
            return False

    return True


def translateToBraille(inputString):
    # Converts the input string from english to braille
    # Parameters:
        # inputString (str): An english string to convert
    # Returns:
        # str: The braille string translation
    outputString = ""
    isPrevNum = False

    for char in inputString:
        # Have at top for handling numberFollows symbol
        if char.isdigit():
            if not isPrevNum:
                outputString += enToBraille["codes"]["numberFollows"]
            outputString += enToBraille["numbers"][char]
            isPrevNum = True
            continue

        isPrevNum = False
        
        if char == " ":
            outputString += enToBraille["codes"][" "]

        elif "A" <= char <= "Z":
            outputString += enToBraille["codes"]["capitalFollows"]
            outputString += enToBraille["letters"][char.lower()]

        elif "a" <= char <= "z":
            outputString += enToBraille["letters"][char]
        
        else:
            raise Exception(f"Invalid character in input string: {char}")
    
    return outputString


def translateToEnglish(inputString):
    # Converts the input string from braille to english
    # Parameters:
        # inputString (str): A braille string to convert
    # Returns:
        # str: The english string translation
    outputString = ""
    isPrevNum = False
    isCapital = False

    for i in range(0, len(inputString), 6):
        brailleSymbol = inputString[i:i+6]
        code = brailleToEn["codes"].get(brailleSymbol, "n/a")

        try:
            if code == "capitalFollows":
                isCapital = True
            elif code == "numberFollows":
                isPrevNum = True
            elif code == " ":
                isPrevNum = False
                outputString += " "
            elif isPrevNum:
                outputString += brailleToEn["numbers"][brailleSymbol]
            elif isCapital:
                outputString += brailleToEn["letters"][brailleSymbol].upper()
                isCapital = False
            else:
                outputString += brailleToEn["letters"][brailleSymbol]
        except KeyError:
            raise Exception(f"Invalid braille symbol: {brailleSymbol}")

    return outputString


def main():
    # Main function to take in input string from command line and translate
    inputString = ' '.join(sys.argv[1:]).strip()
    
    if not inputString:
        print("No input string provided")
        return
    
    try:
        if isValidBraille(inputString):
            translatedString = translateToEnglish(inputString)
        else:
            translatedString = translateToBraille(inputString)
    except Exception as e:
        print(e)
        return
    
    print(translatedString)

if __name__ == '__main__':
    main()
