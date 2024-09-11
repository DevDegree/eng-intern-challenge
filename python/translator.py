import sys

# Mapping from English characters to Braille.
# In Braille, raised dots are represented by 'O' and unraised dots by '.'.
englishToBraille = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    "space": "......",
    "capitalFollows": ".....O",
    "decimalFollows": ".O...O",
    "numberFollows": ".O.OOO",
}

# Mapping from numbers to Braille.
numberToBraille = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

# Reverse mappings for Braille to English/Numbers.
brailleToEnglish = {value: key for key, value in englishToBraille.items()}
brailleToNumber = {value: key for key, value in numberToBraille.items()}

def isBraille(inputText):
    """
    Determines if the input text is in Braille by checking 
    if it's a valid sequence of 'O' (raised dot) and '.' (unraised dot) and length 
    of input is divisible by 6.
    """
    if len(inputText) % 6 != 0:
        return False

    for char in inputText:
        if char not in "O.":
            return False

    return True


def convertEnglishToBraille(inputText):
    """
    Converts the given English text to Braille representation.
    Handles uppercase letters, digits, and spaces.
    """
    outputBraille = ""
    numberMode = False

    for char in inputText:
        if char.isupper():
            outputBraille += englishToBraille["capitalFollows"]
            char = char.lower()

        elif char.isdigit():
            if numberMode == False:
                outputBraille += englishToBraille["numberFollows"]
                numberMode = True

            outputBraille += numberToBraille[char]

        elif char == " ":
            outputBraille += englishToBraille["space"]
            numberMode = False

        if char in englishToBraille:
            outputBraille += englishToBraille[char]

    return outputBraille


def convertBrailleToEnglish(inputText):
    """
    Converts the given Braille text back to English.
    Handles uppercase letters, digits, and spaces.
    """
    chunkLen = 6
    outputEnglish = ""
    capitalMode = False
    numberMode = False

    for idx in range(0, len(inputText), chunkLen):
        currentChunk = inputText[idx : idx + chunkLen]

        if brailleToEnglish[currentChunk] == "capitalFollows":
            capitalMode = True
        elif brailleToEnglish[currentChunk] == "numberFollows":
            numberMode = True
        elif brailleToEnglish[currentChunk] == "space":
            outputEnglish += " "
            numberMode = False
        else:
            if capitalMode:
                outputEnglish += brailleToEnglish[currentChunk].upper()
                capitalMode = False
            elif numberMode:
                outputEnglish += brailleToNumber[currentChunk]
            else:
                outputEnglish += brailleToEnglish[currentChunk]

    return outputEnglish


def main():
    """
    Main function to handle input, check if it's Braille or English, 
    and perform the appropriate conversion.
    """
    try:
        if len(sys.argv) < 2:
            raise ValueError("No text provided for translation.")

        inputText = " ".join(sys.argv[1:])

        if isBraille(inputText):
            print(convertBrailleToEnglish(inputText))
        else:
            print(convertEnglishToBraille(inputText))

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()

