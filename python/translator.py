from textwrap import wrap

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
letterValues = list(brailleToEnglishLetters.values())
instructionKeys = list(brailleToEnglishInstructions.keys())
text = input()


def brailleChecker(inputString):
    for char in inputString:
        if char not in brailleSymbols:
            return False
    return True


brailleChecker(text)


def brailleToEnglish(text):
    split = wrap(text, 6)
    newString = ""
    capital = False
    decimal = False
    number = False
    for i in range(len(split)):
        current = split[i]
        if current == instructionKeys[0]:
            capital = True
        elif current == instructionKeys[1]:
            decimal = True
        elif current == instructionKeys[2]:
            number = True
        else:
            if capital:
                newString += (brailleToEnglishLetters[split[i]]).upper()
                capital = False
            elif number:
                if current == englishToBrailleLetters[" "] or i == len(split):
                    number = False
                newString += brailleToEnglishNumbers[current]
            else:
                newString += brailleToEnglishLetters[current]
    return newString


print(brailleToEnglish(text))
# checkString = ""
# translatedText = ""
