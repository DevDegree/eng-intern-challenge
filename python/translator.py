"""
Author Usaid Malik 
Date: 09/29/2024

This is a program that 
takes arguments from the command
line and outputs the corresponding
Braille or English test
"""
import sys
from typing import List


# A class based approach will make this easier to do
class Translator:
    """
    This class is the way that translation will occur Bidirectionally
    """

    # A raised dot is represented as O and . is a lowered dot
    # braille characters are encoded  as a 6 character string
    # read right to left, line by line, starting at the top left
    # when a braille capital follows symbol is read (O) # nothing top to left
    # so a . means empty and a O means on
    # ONLY next character is capital 
    # when number follows ALL NEXT CHARS ARE NUMBERS until space
    # all braille characters have a . in them 

    # something is braille IF
    # it is a multiple of 6. 
    # it has ONLY . or O in it

    def __init__(self, sourceText):
        # according to the requirements i must include the entire English alphabet
        # the abiulity to capitalize letters
        # add spaces and the numbers 0 through 9 
        # there is no mention of decimals or using the . 
        # therefore if ANY text given to me has the . it is braille
        # and this can be determined just by looking at the first 6 characters
        # since ALL braille characters of that form have a . 
        self.sourceText = sourceText

    def translate(self):
        # this will check if the first 6 characters have a . in them otherwise it will
        # assume it is english 
        if len(self.sourceText) < 6:
            # if the source text is less than 6 it is english not braille
            return self._English2Braille() 

        i = 0
        while i < 6 and self.sourceText[i] != ".":
            i += 1
        # this check checks to ensure that the chosen text is english 

        if i < 6:
            # if I is les than 6 then it is Braille since it means i encountered a .
            return self._Braille2English()
        else:
            return self._English2Braille() # if i didnt encounter a . it must be english
         

    def _English2Braille(self):
        english2BrailleDictionary = {
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
            " ": "......",
            "CAP": ".....O",
            "NUMFOLLOWS":".O.OOO",
        }

        english2BrailleNumerical = {
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

        def convert():
            i = 0 
            while i < len(self.sourceText):
                char = self.sourceText[i]
                if char.isupper():
                    yield english2BrailleDictionary["CAP"]
                    yield english2BrailleDictionary[char.lower()]
                elif char.isdigit():
                    yield english2BrailleDictionary["NUMFOLLOWS"]
                    """
                    Variable change from char to instead self.sourceText[i]
                    this was done to make the code shorter and have the loop 
                    update the variable in the condition easier
                    additionallly the checks are to ensure the next char is also a digit
                    however if it does not terminate with a space the braille2english will not 
                    work properly as in the case of 12A 
                    """
                    while i < len(self.sourceText) and self.sourceText[i].isdigit(): 
                        yield english2BrailleNumerical[self.sourceText[i]]
                        i += 1

                    if i < len(self.sourceText):
                        yield english2BrailleDictionary[self.sourceText[i]]

                else:
                    yield english2BrailleDictionary[char]
                i += 1
        return ''.join(convert()) 

    def _Braille2English(self):
        braille2EnglishDictionary = {
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
            "......": " ",
            ".....O": "CAP", # i technically don't need these two below but it is good symettry
            ".O.OOO":"NUMFOLLOWS", 

        }

        Braille2EnglishNumerical = {
            ".OOO..": "0",
            "O.....": "1",
            "O.O...": "2",
            "OO....": "3",
            "OO.O..": "4",
            "O..O..": "5",
            "OOO...": "6",
            "OOOO..": "7",
            "O.OO..": "8",
            ".OO...": "9",
        }

        def convert():
            i = 0
            while i < len(self.sourceText):
                char = self.sourceText[i:i+6] # getting the six braille characters
                if char == ".....O":
                    i += 6 # incrementing i to get to the next character
                    nextChar = self.sourceText[i: i + 6] # this assumes the braille is valid
                    yield braille2EnglishDictionary[nextChar].upper() # the capitalized character that was found
                elif char == ".O.OOO":
                    # this means evertyhign after is a num until i hit a space character
                    i += 6 # incrementing to see the next braille numbers
                    while char != "......" and i < len(self.sourceText): # i keep going until my braille is a space or i reach the end of the string
                        char = self.sourceText[i:i + 6]
                        yield Braille2EnglishNumerical[char] 
                        i += 6
                    yield " " # yielding a space since my increment stopped at one and the next increment will move past it
                else:
                    yield braille2EnglishDictionary[char] # yielding the normal character
                
                i += 6 # incrementing to the next character once the loop ends
    
def main(argc: int, argv: List[int]):
    if argc < 2:
        print("IMPROPER USAGE! Correct Usage: python translator.py [source_text]")
        return
    sourceText = " ".join(argv[1:]) # getting the source text passed in an joining via a space
    translator = Translator(sourceText)
    translatedText = translator.translate()
    print(translatedText)

if __name__ == "__main__":
    argv = sys.argv # this is in a variable so i dont call sys.argv twice
    main(len(argv), argv)
    # passing in the source text from the CLI