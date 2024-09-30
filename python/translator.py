"""
Author Usaid Malik 
Contact: linkedin.com/in/usaidhmalik github.com/UsaidMalik
Date: 09/29/2024

This is a program that 
takes arguments from the command
line and outputs the corresponding
Braille or English text
"""
import sys
from typing import List, Dict


class Translator:
    """
    A class to translate text between Braille and English, handling capitalization and numbers.

    Attributes:
        _english2Braille (Dict[str, str]): Maps English characters (a-z, space, CAP, NUMFOLLOWS) to Braille.
        _english2BrailleNumeric (Dict[str, str]): Maps English digits (0-9) to Braille.
        _braille2English (Dict[str, str]): Maps Braille characters to English.
        _braille2EnglishNumeric (Dict[str, str]): Maps Braille digits to English.

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
        self._english2BrailleNumeric = {
            "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
            "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
        }

        self._braille2English: Dict[str, str] = {v: k for k, v in self._english2Braille.items()}
        self._braille2EnglishNumeric: Dict[str, str]  =  {v: k for k, v in self._english2BrailleNumeric.items()}


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
        while i < len(sourceText) and i < 6 and sourceText[i] != ".":
            i += 1
        
        """
        In this condition if the iterator is unable to get
        past the 6th character it means that a . was encountered
        and the chosen text is Braille otherwise the chosen text is in English 
        """
        if i < 6:
            return self._Braille2English(sourceText)
        return self._English2Braille(sourceText) 
         

    def _English2Braille(self, englishText: str) -> str:
        """
        Converts English text into its Braille representation.

        Handles capitalization using a special Braille sequence for capital letters. If numbers
        are encountered, a number indicator is inserted.
        params: 
            sourceText (str): The input text to translate to braille
        returns:
            str: The Braille translation of the English input.
        """
        def convert():
            """
            Generator function that translates English text to Braille. It handles capital letters, digits, 
            and other characters by converting them to the corresponding Braille representation.
            
            Yields:
                str: Braille representation of the next character or sequence from the English text.
            """

            i = 0 
            while i < len(englishText):
                char = englishText[i] 
                
                if char.isupper():
                    yield english2BrailleDictionary["CAP"]  # inserting capitalization marker and getting the character
                    yield english2BrailleDictionary[char.lower()] 
                
                elif char.isdigit():
                    yield english2BrailleDictionary["NUMFOLLOWS"]  # Yield the Braille number indicator

                    """
                    Handling consecutive digits by continuing the loop until a non-digit character is found.
                    Instead of using the char variable again, directly accessing sourceText[i] to
                    simplify the code and ensure that the loop updates correctly.

                    Additionally, the loop goes until a non digit is found.
                    The loop will break if the text ends or a non-digit character is encountered. However, 
                    if the number sequence doesn't end with a space, the Braille translation will fail when translating back 
                    from Braille to English. For instance, a sequence like 12A would not be handled in this case and 
                    is assumed by the technical specifications to not be encounted.
                    """
                    while i < len(englishText) and englishText[i].isdigit():
                        yield english2BrailleNumerical[englishText[i]]  
                        i += 1 

                    """Only add the next character that ended the sequence
                     (presumably a space for proper execution)
                     if i am not at the end of the string"""
                    if i < len(englishText):
                        yield english2BrailleDictionary[englishText[i]]
                
                else:
                    yield english2BrailleDictionary[char] 
                
                i += 1  # Move to the next character in the sourceText

        # After the generator has processed all characters, join the yielded Braille characters into a string
        return ''.join(convert())


    def _Braille2English(self, brailleText):
        
        """
        Converts Braille text into its English representation following the specified
        pattern from the technical specifications.
   
        params: 
            brailleText (str): The braille text to translate to english
        returns:
            str: The English translation of the Braille input.
        """

        def convert():
            i = 0
            while i < len(brailleText):
                char = brailleText[i:i+6] # incrementing by 6 since each Braille cell is 6 characters

                # Handle Braille uppercase marker
                if char == ".....O":
                    i += 6 
                    # this assumes the braille is valid and the next character is a letter
                    char = brailleText[i: i + 6] 
                    yield braille2EnglishDictionary[char].upper()

                # Handle Braille numeric marker
                elif char == ".O.OOO":
                    
                    i += 6 # incrementing to move past the numeric marker

                    """
                    Handling the consecutive digits by going through them with a skip 
                    of 6, this assumes that all the next digits are numbers and are
                    valid braille until a space braille character is encountered
                    """                    
                    while i < len(brailleText) and brailleText[i:i + 6] != "......": 
                        yield Braille2EnglishNumerical[brailleText[i:i + 6]] 
                        i += 6

                    if i < len(brailleText):
                        yield " " # yielding a space since my increment stopped at a space assuming valid braille, otherwise would be skipped
                else:
                    yield braille2EnglishDictionary[char] 
                
                i += 6
                
        return ''.join(convert())


def main(argc: int, argv: List[int]) -> None:
    """
    Main function to handle command line arguments and initiate translation.

    Args:
        argc (int): The number of command line arguments passed.
        argv (List[int]): List of command line arguments.
    """

    # If less than two arguments are passed then the translation cannot proceed
    if argc < 2:
        print("IMPROPER USAGE! Correct Usage: python translator.py [source_text]")
        return

    # Join the passed arguments (excluding the script name) to form the source text
    sourceText: str = " ".join(argv[1:])

    translator = Translator()
    translatedText: str = translator.translate(sourceText)

    print(translatedText)



if __name__ == "__main__":
    main(len(sys.argv), sys.argv)