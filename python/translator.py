"""
Author Usaid Malik 
Date: 09/29/2024

This is a program that 
takes arguments from the command
line and outputs the corresponding
Braille or English test
"""
import sys
from typing import List. Dict


class Translator:
    """
    This class will translate source text from Braille to English 
    and vice versa all that needs to be done is to instaniate the class
    and call the translate method passing in the source text as a parameter
    to translate

    Attributes:
        _english2Braille Dict[str, str]: Private method that is a 
        Dictionary containing the mappings of english characters to the 
        corresponding Braille characters without numbers

        _english2BrailleNumeric Dict[str, str]: Private method that is a  
        Dictionary containing the mappings of english numbers to the corresponding
        Braille numbers

        _braille2English Dict[str, str]: Private method that is a 
        Dictionary containing the mappings of Braille characters read from top 
        left to right line by line to the corresponding english characters without numbers

         _braille2EnglishNumeric Dict[str, str]: Private method that is a 
        Dictionary containing the mappings of Braille numbers read from top 
        left to right line by line to the corresponding english numbers

    Methods:
         translate(): Determines if the source text is Braille or English and translates it accordingly.
        _English2Braille(): Private method that translates the source text from English to Braille.
        _Braille2English(): Private method that translates the source text from Braille to English.
    """


    def __init__(self):
        """
        Initializes the Translator class.
        """
        self._english2Braille = {
            "a": "O.....",  "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
            "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
            "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", 
            "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
            "y": "OO.OOO", "z": "O..OOO", " ": "......", "CAP": ".....O", "NUMFOLLOWS":".O.OOO", }

        """I don't technically need this dict since all keys are unique in 
          english2braille but it makes it easier to generate _braille2EnglishNumeric
        """
        self._english2BrailleNumeric{
            "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
            "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
        }

        self._braille2English: Dict[str, str] = {v: k for k, v in self._english2Braille.items()}
        self._braille2EnglishNumeric =  {v: k for k, v in self._english2BrailleNumeric.items()}


    def translate(self, sourceText: str) -> str:
        """
        Translates the source text from either Braille or English to the opposite language

        The function first checks if the source text is in Braille by looking for Braille patterns
        in the first six characters. Based on the pattern, it either calls the Braille-to-English 
        or English-to-Braille method.
        params: 
            sourceText (str): The input text that is either in English or Braille.

        returns:
            str: The translated text in either Braille or English.
        """

        """
        This loop goes through the first six charaacters and sees if a . is 
        present. This is because the technical requirements don't require
        the translation of the english . therefore a . CANNOT show up 
        in an English text. if a . does show up it MUST be Braille. 
        Since the technical specifications only require the translation of 
        numbers (not including decimals), spaces, and capital and lowercase
        letters the following loop looks for that . to determine if it is Braille 
        """
        i = 0
        while i < 6 and self.sourceText[i] != ".":
            i += 1
        

        """
        In this condition of the iterator is unable to get
        past the 6th character it means that a . was encountered
        and the chosen text is braille otherwise the chosen text is in english 
        """
        if i < 6:
            return self._Braille2English()
        return self._English2Braille() 
         

    def _English2Braille(self, sourceText):
        
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

    def _Braille2English(self, sourceText):

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
                    while i < len(self.sourceText) and self.sourceText[i:i + 6] != "......": # i keep going until my braille is a space or i reach the end of the string
                        yield Braille2EnglishNumerical[self.sourceText[i:i + 6]] 
                        i += 6

                    if i < len(self.sourceText):
                        yield " " # yielding a space since my increment stopped at one and the next increment will move past it
                else:
                    yield braille2EnglishDictionary[char] # yielding the normal character
                
                i += 6 # incrementing to the next character once the loop ends
        return ''.join(convert())
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