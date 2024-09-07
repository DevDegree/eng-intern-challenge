"""
Matthew Cheverie
Shopify Internship Challenge
This program is a translator that converts English text to Braille and Braille to English.
Assumes that the input is either English or Braille, not a mix of both.
Also assumes that only english letters (a,z or A-Z), numbers (0-9), spaces as per the git repo instructions.
"""

import sys

class Translator:
    """
    This class is used to represent the translator object which is used to translate English to Braille and Braille to English.

    Attributes:
    eng_to_br_letters (dict): A dictionary that maps English letters to Braille letters.
    eng_to_br_nums (dict): A dictionary that maps English numbers to Braille numbers.
    eng_to_br_spec (dict): A dictionary that maps English special characters to Braille special characters.
    br_to_eng_letters (dict): A dictionary that maps Braille letters to English letters.
    br_to_eng_nums (dict): A dictionary that maps Braille numbers to English numbers.

    Methods:
    __init__(self): Constructor for the Translator class.
    eng_to_braille(self, text): Function to convert English text to Braille.
    braille_to_eng(self, text): Function to convert Braille text to English.
    isEnglish(self, text): Function to check if the text is in English.
    """

    def __init__(self):
        #Constructor for the Translator class. Initializes the dictionaries for English to Braille and Braille to English translations.

        # Dictionary for English letters to braille letters
        self.eng_to_br_letters = {
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
        }

        # Dictionary for English numbers to braille numbers
        self.eng_to_br_nums = {
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

        #Dictionary for English special characters to braille special characters
        self.eng_to_br_spec = {
            " ": "......",
            "^": ".....O",
            "#": ".O.OOO"
        }

        # Dictionary for braille to English
        self.br_to_eng_letters ={
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
        }

        # Dictionary for braille to English
        self.br_to_eng_nums ={
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



    def eng_to_braille(self, text):
        """
        Function to translate the text parameter from English to Braille.

        Parameters:
            text (str): The text to be translated from English to Braille.

        Returns:
            str: The translated text in Braille.

        Notes:
            - braille variable is the string that will be returned
            - digitCount is used to keep track of the number of digits in the text to ensure that the 'number follows' braille character is only added once
        """

        braille = ""
        digitCount = 0

        # Loop through each character in the text
        for char in text:
            if char.isalpha():
                if char.isupper():
                    braille += self.eng_to_br_spec["^"]
                braille += self.eng_to_br_letters[char.lower()]
            elif char.isdigit() and digitCount ==0:
                braille += self.eng_to_br_spec["#"]
                braille += self.eng_to_br_nums[char]
                digitCount += 1
            elif char.isdigit():
                braille += self.eng_to_br_nums[char]
            elif char == " ":
                braille += self.eng_to_br_spec[" "]
                digitCount = 0
        return braille


    def braille_to_eng(self, text):
        """
        Function to translate the text parameter from braille to english.

        Parameters:
            text (str): The text to be translated from braille to english.

        Returns:
            str: The translated text in English.

        Notes:
            - english variable is the string that will be returned
            - digit is used if we are in the digit state i.e. the 'number follows' braille character has been found and a space has not been seen yet
            - caps is used if we are in the caps state i.e. the '^' braille character has been found
        """

        english = ""
        digit = False
        caps = False
        # Split the braille text into a list of 6 characters
        words = [text[i:i+6] for i in range(0, len(text), 6)]

        for word in words:
            if word == "......":
                digit = False
                english += " "
            elif word == ".O.OOO":
                digit = True
            elif word == ".....O":
                caps = True
            elif digit:
                english += self.br_to_eng_nums.get(word, "")
            else:
                if caps:
                    english += self.br_to_eng_letters.get(word, "").upper()
                    caps = False
                else:
                    english += self.br_to_eng_letters.get(word, "")
        return english


    def isEnglish(self, text):
        """
        Function to check if given input is in English.

        Parameters:
            text (str): The word to be checked if it is in English.

        Returns:
            bool: True if the text is in English, False otherwise
        """
        braille_chars = {'O', '.'}
        if set(text) - braille_chars:
            return True
        return False


def main():

    # Create a translator object
    translator = Translator()

    # Assume text is not english
    engCheck = False

    # check each argument to see if it is in English or not, break from loop if english found. If braile, loop only runs once
    for args in sys.argv[1:]:
        engCheck = translator.isEnglish(args)
        if engCheck:
            break

    # If the text is in English, translate to Braille, otherwise translate to English
    if engCheck:
        sentence = ' '.join(sys.argv[1:])   # Join all the arguments into a single sentence
        translations = translator.eng_to_braille(sentence)
        print(translations)
    else:
        print(translator.braille_to_eng(sys.argv[1]))


if __name__=="__main__":
    main()
