import sys
BRAILLETRANSLATIONS = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "..OO.O": ".",
    "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
    ".O.OO.": ")", "......": " ", ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number"
}
BRAILLENUMBERS = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"}

ENGLISHTRANSLATIONS = {BRAILLETRANSLATIONS[key] : key for key in BRAILLETRANSLATIONS}
ENGLISHTRANSLATIONS.update({"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."})

#function to determine input type; returns True for Braille and False for English
def isBraille(text: str) -> bool:
    if len(text)%6:
        return False
    for symbol in text:
        if symbol == 'O' or '.':
            continue
        else:
            return False
    return True

def translateBraille(braille: str) -> str:
    isCap = False
    isNum = False
    english = "" #result
    index = 0
    while index < len(braille):
        letter = BRAILLETRANSLATIONS[braille[index:index+6]]
        if letter == "capital":
            isCap = True
        elif letter == "decimal":
            english += "."
        elif letter == "number":
            isNum = True
        elif isCap:
            english += letter.upper()
            isCap = False
        elif isNum:
            if letter == " ":#since space is the indicator that input is not numbers
                isNum = False
            else:
                english += BRAILLENUMBERS[letter]
        else:
            english += letter
        index += 6
    
    return english

def translateEnglish(english: str) -> str:
    braille = ""
    isNum = False
    for letter in english:
        brailleCell = ENGLISHTRANSLATIONS[letter.lower()]
        if letter.isupper():
            if isNum:
                isNum = False
                braille += ENGLISHTRANSLATIONS[" "] #adds space character to indicate end of numbers
            braille += ENGLISHTRANSLATIONS["capital"] + brailleCell
        elif letter.isnumeric():
            if not isNum:
                isNum = True
                braille += ENGLISHTRANSLATIONS["number"]
            braille += brailleCell
        else:
            if isNum:
                if letter == ".": #if period is used between numbers we can assume it is a decimal
                    braille += ENGLISHTRANSLATIONS["decimal"]
                else:
                    isNum = False
                    braille += ENGLISHTRANSLATIONS[" "] + brailleCell
            else:
                braille += brailleCell
    
    return braille

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) #ensures spaces are shown in text

    if isBraille(text):
        print(translateBraille(text))
    else:
        print(translateEnglish(text))