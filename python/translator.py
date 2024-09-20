import sys
import re

BrailleToEnglish = { 
    "O.....": "a","O.O...": "b","OO....": "c","OO.O..": "d","O..O..": "e", "OOO...": "f",
    "OOOO..": "g","O.OO..": "h",".OO...": "i",".OOO..": "j","O...O.": "k","O.O.O.": "l",
    "OO..O.": "m","OO.OO.": "n","O..OO.": "o","OOO.O.": "p","OOOOO.": "q","O.OOO.": "r",
    ".OO.O.": "s",".OOOO.": "t","O...OO": "u","O.O.OO": "v",".OOO.O": "w","OO..OO": "x",
    "OO.OOO": "y","O..OOO": "z", "......": " ",".....O": "capitalNext", ".O.OOO": "numberNext"
    }

BrailleToNumber = {
    "O.....": "1","O.O...": "2","OO....": "3","OO.O..": "4","O..O..": "5",
    "OOO...": "6","OOOO..": "7","O.OO..": "8",".OO...": "9",".OOO..": "0",
}

class BrailleTranslator:

    def __init__(self, stringToTranslate:str):
        self.textToTranslate = stringToTranslate
        self.brailleCharacterSize = 6

    """ Determines the type of translation to be done, and then calls the appropriate function
        params: None
        returns: translated string
    """
    def translate(self) -> str:	
        if(re.fullmatch(r"^[O.]+$", self.textToTranslate)):
            return self.braille_to_english(self.textToTranslate)
        else:
            return self.english_to_braille(self.textToTranslate)

    """ Translates english to braille
        params: string to translate
        returns: translated string
    """
    def braille_to_english(self, braille:str) -> str:
        translatedString = ""
        isNumber = False
        isCapital = False
        for i in range(0, len(braille), self.brailleCharacterSize):
            substring = braille[i:i+self.brailleCharacterSize]
            #Checks if the substring is a number or capital letter
            if substring in BrailleToEnglish and BrailleToEnglish[substring] == "numberNext":
                isNumber = True
                continue
            if substring in BrailleToEnglish and BrailleToEnglish[substring] == "capitalNext":
                isCapital = True
                continue

            #If the substring is a space, remove the number flag
            if BrailleToEnglish[substring] == " ":
                isNumber = False

            #Translates the substring to its corresponding english letter
            if isNumber:
                translatedString += BrailleToNumber[substring]
            elif isCapital:
                translatedString += BrailleToEnglish[substring].upper()
                isCapital = False
            else:
                translatedString += BrailleToEnglish[substring]

        return translatedString
    
    """ Translates english to braille
        params: string to translate
        returns: translated string
    """
    def english_to_braille(self, english:str) -> str:
        englishToBrailleDict = {v: k for k, v in BrailleToEnglish.items()}
        numberToBrailleDict = {v: k for k, v in BrailleToNumber.items()}

        translatedString = ""
        isNumber = False

        for char in english:
            if char == " ":
                isNumber = False
            #Digits are translated to braille
            if char.isdigit() or isNumber: 
                if(isNumber == False):
                    translatedString += englishToBrailleDict["numberNext"]
                if char in numberToBrailleDict: translatedString += numberToBrailleDict[char] 
                else: translatedString += BrailleToNumber[englishToBrailleDict[char]] #Translates a letter to its corresponding number in braille
                isNumber = True
                
            #Capital letters are translated to braille
            elif char.isupper(): 
                translatedString += englishToBrailleDict["capitalNext"] + englishToBrailleDict[char.lower()]
            else:
                translatedString += englishToBrailleDict[char]

        return translatedString

def main():
    stringToTranslate = " ".join(sys.argv[1:])
    translator = BrailleTranslator(stringToTranslate)
    print(translator.translate())

if __name__ == "__main__":
    main()  
