from textwrap import wrap

# Dictionaries for all the braille and english letters/numbers/instructions
brailleToEnglishLetters = {"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
                           "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
                           "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
                           ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
                           "OO.OOO": "y", "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
                           "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
                           ".O.OO.": ")", "......": " "}
brailleToEnglishNumbers = {"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
                           "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}
brailleToEnglishInstructions = {".....O": "Capital", ".O...O": "Decimal", ".O.OOO": "Number"}

englishToBrailleLetters = {v: k for k, v in brailleToEnglishLetters.items()}
englishToBrailleNumbers = {v: k for k, v in brailleToEnglishNumbers.items()}
englishToBrailleInstructions = {v: k for k, v in brailleToEnglishInstructions.items()}

brailleSymbols = ["O", "."]
instructionKeys = list(brailleToEnglishInstructions.keys())


def brailleToEnglish(text):

    # Divide the text into strings of 6 characters
    split = wrap(text, 6)
    newString = ""
    capital = False
    decimal = False
    number = False
    for i in range(len(split)):
        current = split[i]
        # Check for the instruction characters
        if current == instructionKeys[0]:
            capital = True
        elif current == instructionKeys[1]:
            decimal = True
        elif current == instructionKeys[2]:
            number = True
        else:
            # Add a capital or number if specified, otherwise add the corresponding english character
            if capital:
                newString += (brailleToEnglishLetters[split[i]]).upper()
                capital = False
            elif number:
                if current == englishToBrailleLetters[" "]:
                    number = False
                    newString += brailleToEnglishLetters[current]
                elif i == len(split):
                    break
                else:
                    newString += brailleToEnglishNumbers[current]
            else:
                newString += brailleToEnglishLetters[current]
    return newString


# Convert from English to Braille
def englishToBraille(text):
    newString = ""
    firstNumber = True
    for i in range(len(text)):
        current = text[i]
        if current.isupper():
            newString += englishToBrailleInstructions["Capital"]
        if current in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if firstNumber:
                newString += englishToBrailleInstructions["Number"]
                firstNumber = False
            newString += englishToBrailleNumbers[current]
        else:
            firstNumber = True
            newString += englishToBrailleLetters[current.lower()]
    return newString

def brailleChecker(inputString):
    english = False
    for char in inputString:
        if char not in brailleSymbols:
            english = True
            print(englishToBraille(inputString))
    if not english:
        print(brailleToEnglish(inputString))


if __name__ == "__main__":
    text = input()
    brailleChecker(text)

