import sys

# Dictionaries to handle Braille to letter/number mapping
brailleLetters = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..",
    "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
    "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO",
    "Z": "O..OOO", " ": "......"
}

brailleDigits = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

brailleIndicators = {
    "capital": ".....O",
    "number": ".O.OOO"
}

# Function to decode single braille charater to its english equivalent
def translateBraille(brailleChar, currentMode, shouldCapitalize):
    #capital mode
    if currentMode == "capital":
        for letter, braille in brailleLetters.items():
            if braille == brailleChar:
                return letter.upper() if shouldCapitalize else letter.lower()

    #number mode
    if currentMode == "number":
        for digit, braille in brailleDigits.items():
            if braille == brailleChar:
                return digit

    #case for unknown characters
    return '?' 

#function that handles string of braille input and translates it to english
def brailleToEnglish(inputBraille):
    mode = ""
    capitalizeNext = False
    output = ""

    for i in range(0, len(inputBraille), 6):
        brailleChar = inputBraille[i:i + 6]

        # Check if the current character indicates a mode change
        modeChanged = False
        for modeKey, braille in brailleIndicators.items():
            if braille == brailleChar:
                mode = modeKey
                capitalizeNext = True
                modeChanged = True
                break

        if mode and not modeChanged:
            output += translateBraille(brailleChar, mode, capitalizeNext)
            capitalizeNext = False  # Reset capitalization after use

    print(output)

#function for english to braille
def englishToBraille(words):
    output = ""
    mode = ""

    #checks if characters is number switches modes and adds the digit to output
    for word in words:
        for char in word:
            if char.isdigit():
                if mode != "number":
                    mode = "number"
                    output += brailleIndicators["number"]

                output += brailleDigits[char]
            else:
                if char.isupper():
                    output += brailleIndicators["capital"]
                    output += brailleLetters[char.upper()]
                else:
                    output += brailleLetters[char.upper()]

        output += brailleLetters[" "]  # Add space after each word

    print(output[:-6])  # Remove the last added space

if __name__ == '__main__':
    input_text = ""
    try:
        if len(sys.argv) > 2:
            englishToBraille(sys.argv[1:])
            sys.exit()
        else:
            input_text = sys.argv[1]
    except IndexError:
        sys.exit()

    # Check if the input is Braille
    if all(char in 'O.' for char in input_text) and len(input_text) % 6 == 0:
        brailleToEnglish(input_text)
    else:
        englishToBraille([input_text])