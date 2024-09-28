import sys

'''
Victor Nguyen, Eng Intern Challenge Fall - Winter 2025

Translator
    - Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
    - For Braille, each character is stored as a series of O (the letter O) or . (a period).
    - Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below.
    - When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
    - When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
Braille Alphabet
    - Letters a through z
    - The ability to capitalize letters
    - Numbers 0 through 9
    - The ability to include spaces ie: multiple words

'''

brailleDict = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "cap",  # Capital follows
    ".O.OOO": "num",  # Number follows
    "......": " "     # Space
}

numberDict = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

def isBrailleInput(userInput: str):
    userInput = userInput.upper()  # Convert input to uppercase
    if (len(userInput) % 6) != 0:
        return False
    for character in userInput:
        if character not in ["O", "."]:
            return False
    return True
    
def translateBraille(braille: str):
    capitalFollows = False
    numberFollows = False
    count = 0
    translation = ""
    brailleLetter = ""
    engChar = ""

    for character in braille:
        brailleLetter += character
        count += 1 # increment counter
        
        if count == 6:
            if numberFollows: # number
                if brailleDict.get(brailleLetter) == " ": #check whether to end number follows
                    numberFollows = False
                else: # add number
                    engChar = numberDict.get(brailleLetter)
                    translation += engChar
            else: # not number
                engChar = brailleDict.get(brailleLetter)
                if engChar == "cap": # capitalize next letter
                    capitalFollows = True
                elif engChar == "num": # next symbols are a number
                    numberFollows = True
                else:
                    if capitalFollows: # capitalize letter
                        engChar = engChar.upper()
                        capitalFollows = False
                    translation += engChar

            count = 0 # reset counter
            brailleLetter = "" 


    return translation

def translateEnglish(english: str):
    braille = ""
    numberFollows = False

    revBrailleDict = {v: k for k, v in brailleDict.items()}
    revNumberDict = {v: k for k, v in numberDict.items()}

    for character in english:
        if character.isnumeric():
            if not numberFollows:
                braille += ".O.OOO" # num
                numberFollows = True
            brailleNum = revNumberDict.get(character)
            braille += brailleNum
        else:
            if numberFollows: 
                numberFollows = False
            if character.isupper():
                braille += ".....O"
                character = character.lower()
            braille += revBrailleDict.get(character)

    return braille    


def main():
    if len(sys.argv) < 2:
        print("Usage: translator.py <string>")
        return
    
    userInput = " ".join(sys.argv[1:])
    
    if isBrailleInput(userInput):
        print(translateBraille(userInput))
    else:
        print(translateEnglish(userInput))
        

if __name__ == "__main__":
    main()