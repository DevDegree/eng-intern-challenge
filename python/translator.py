"""
Braille Translator

Author: Polly Liu (polly.liu@uwaterloo.ca)
Date: Saturday, Aug 31, 2024

"""


# imports
import sys
import translator_constants
from translator_constants import CAPITAL_FOLLOWS, NUMBER_FOLLOWS, SPACE
import translator_tests as translator_tests




class Translator:
    def __init__(self):
        """
        Initializes a new instance of the Translator class.
        """
        pass

    # ------------------------ Class Methods ------------------------
    def is_braille(self, text: str) -> bool:
        """
        Determines if the given text is Braille.

        Args:
            text (str): The text to check.

        Returns:
            bool: True if the text is Braille, False otherwise.
        """
        return set(text).issubset({"O", "."}) # is braille if strictly composed of "O" and "."


    def english_to_braille(self, text: str) -> str:
        """
        Converts English text to Braille.

        Args:
            text (str): The English text to convert.

        Returns:
            str: The converted Braille text.
        Raises:
            ValueError: If an invalid English character is found.
        """
        ret = "" # translated braille text return value
        length = len(text)
        number_mode = False
        for i in range(length):
            char = text[i]
            if char is SPACE:
                ret += translator_constants.SPECIAL_TO_BRAILLE[SPACE]
                number_mode = False # reset number mode on space
            elif char.isnumeric() or number_mode:
                if not number_mode: # beginning of number mode (ends on space)
                    ret += translator_constants.SPECIAL_TO_BRAILLE[NUMBER_FOLLOWS]
                    ret += translator_constants.NUMBER_TO_BRAILLE[char]
                    number_mode = True
                else : # in number mode, all symbols are numbers (until space)
                    ret += translator_constants.NUMBER_TO_BRAILLE[char]
            elif char.isupper():
                ret += translator_constants.SPECIAL_TO_BRAILLE[CAPITAL_FOLLOWS]
                ret += translator_constants.ENGLISH_TO_BRAILLE[char.lower()]
            elif char in translator_constants.ENGLISH_TO_BRAILLE:
                ret += translator_constants.ENGLISH_TO_BRAILLE[char]
            else:
                raise ValueError("[Invalid english] character not found: {}".format(char))
                
        return ret
        

    def braille_to_english(self, text: str) -> str:
        """
        Converts Braille text to English.

        Args:
            text (str): The Braille text to convert.

        Returns:
            str: The converted English text.

        Raises:
            ValueError: If the length of the Braille text is not divisible by 6 or if an invalid Braille character is found.
        """
        length = len(text)
        if (length % 6 != 0):
            raise ValueError("[Invalid braille] length not divisible by 6: " + text)
        
        ret = "" # translated braille return value
        to_capitalize = False
        is_number = False
        for letter in range(0, length, 6):
            braille = text[letter:letter+6] # take in 6 chars at a time (size of one braille letter)
            if braille in translator_constants.BRAILLE_TO_SPECIAL:
                if braille == "......": # SPACE in braille
                    ret += translator_constants.BRAILLE_TO_SPECIAL[braille]
                    is_number = False # reset number mode on space
                elif braille == ".....O": # CAPITAL FOLLOWS in braille
                    to_capitalize = True
                elif braille == ".O.OOO": # NUMBER FOLLOWS in braille
                    is_number = True
            elif to_capitalize:
                if braille in translator_constants.BRAILLE_TO_ENGLISH:
                    ret += translator_constants.BRAILLE_TO_ENGLISH[braille].upper()
                    to_capitalize = False
                else:
                    raise ValueError("[Invalid braille] capital letter not found: {}".format(braille))
            elif is_number:
                if braille in translator_constants.BRAILLE_TO_NUMBER:
                    ret += translator_constants.BRAILLE_TO_NUMBER[braille]
                else:
                    raise ValueError("[Invalid braille] number not found: {}".format(braille))
            elif braille in translator_constants.BRAILLE_TO_ENGLISH:
                ret += translator_constants.BRAILLE_TO_ENGLISH[braille]
            else:
                raise ValueError("[Invalid braille] letter not found: {}".format(braille))

        return ret




def main():
    text = ' '.join(sys.argv[1:])
    translator = Translator()

    if translator.is_braille(text):
        print(translator.braille_to_english(text))
    else:
        print(translator.english_to_braille(text))
    
    # extra tests
    from translator_tests import run_tests
    run_tests()




if __name__ == '__main__':
    main()
