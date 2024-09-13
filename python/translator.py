import sys
from typing import List


class LanguageProcessor:
    """
    A class to process and translate between English and Braille, as well as between letters and numbers.
    """
    def __init__(self) -> None:
        self.letter_to_number = { "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0" }
        self.number_to_letter = { number: letter for letter, number in self.letter_to_number.items() }
        self.english_to_braille = {
            "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
            "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
            "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
            "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
            "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
            "z": "O..OOO", " ": "......", "CAPITAL": ".....O", "NUMBER": ".O.OOO",
        }
        self.braille_to_english = { braille: english for english, braille in self.english_to_braille.items() }
        

    def get_chunks(self, string: str) -> List[str]:
        """
        Splits a string into chunks of 6 characters. A chunk correspond to a Braille representation.

        Args:
            string (str): The string input to be divided into 6-character chunks.
        Returns:
            List[str]: A list of substrings, each 6 characters long.
        Raises:
            ValueError: If the string length is not divisible by 6, so it prevents the index error.
        """
        if len(string) % 6 != 0:
            raise ValueError("String length must be a multiple of 6")

        return [string[index : index + 6] for index in range(0, len(string), 6)]

    def is_english(self, string: str) -> bool:
        """
        Determines if the input string is in English or Braille.
        Checks if the string length is divisible by 6 if not it should be English. 
        Then verifies if each chunk matches a known Braille pattern and if not le string should be English.

        Args:
            string (str): The input string to check.
        Returns:
            bool: True if the string is in English, False if it is in Braille.
        """
        if len(string) % 6 != 0:
            return True
        chunks = self.get_chunks(string)
        for chunk in chunks:
            if chunk not in self.braille_to_english:
                return True
        return False


class TranslationService:
    """
    A class for translating text between English and Braille it uses the LanguageProcessor to process inputs.
    """
    def __init__(self) -> None:
        self.processor = LanguageProcessor()

    def translate(self, string: str) -> str:
        """
        Translates the given string to either Braille or English.
        If the string is detected as English, it is translated to Braille. 
        Otherwise, it is translated from Braille to English.

        Args:
            string (str): The input string to be translated.

        Returns:
            str: The translated string in Braille or English.
        """
        if self.processor.is_english(string):
            return self._translate_to_braille(string)
        return self._translate_to_english(string)

    def _translate_to_english(self, string: str) -> str:
        """
        Translates a Braille string to English.

        Args:
            string (str): The Braille string to be translated.

        Returns:
            str: The translated English text.
        """
        result = ""
        chunks = self.processor.get_chunks(string)
        index = 0
        while index < len(chunks):
            current_chunk = self.processor.braille_to_english[chunks[index]]

            # if the current chunk refers to CAPITAL, only the next character should be in uppercase.
            if current_chunk == "CAPITAL":
                index += 1
                result += self.processor.braille_to_english[chunks[index]].upper()
            
            # if the current chunk refers to NUMBER, all the following characters should be numbers until a space is found or
            # the index became out of range. When this condition is met, if the index is still in range, space is added to the result.
            elif current_chunk == "NUMBER":
                index += 1
                while index < len(chunks) and self.processor.braille_to_english[chunks[index]] != " ":
                    letter = self.processor.braille_to_english[chunks[index]]
                    result += self.processor.letter_to_number[letter]
                    index += 1
                
                if index < len(chunks):
                    result += " "

            # the current chunk refers directly to a letter and is added to the result
            else:
                result += self.processor.braille_to_english[chunks[index]]
            index += 1
        return result

    def _translate_to_braille(self, string: str) -> str:
        """
        Translates an English string to Braille.

        Args:
            string (str): The English string to be translated.

        Returns:
            str: The translated Braille string.
        """
        result = ""

        # flag for knowing if the current character is a new number so a NUMBER Braille representation should be added.
        new_number = True

        # loop for every character in the input string.
        for character in string:
            
            # if the character is a number, the NUMBER representation is added only if the number flag is True.
            # The braille representation is then converted as a letter and then as number using the mappings in the 
            # LangugageProcessor class. 
            if character.isnumeric():
                if new_number:
                    result += self.processor.english_to_braille["NUMBER"]
                    new_number = False
                letter = self.processor.number_to_letter[character]
                result += self.processor.english_to_braille[letter]

            # if the character is not a number, the new_number flag is set to True
            else:
                new_number = True
                if character.isalpha():
                    # if the character is in uppercase, the representaiton of capital letter is added.
                    if character.isupper():
                        result += self.processor.english_to_braille["CAPITAL"]
                    result += self.processor.english_to_braille[character.lower()]
            
                elif character == " ":
                    result += self.processor.english_to_braille[character]
                
                # if the character is not a letter, number or space, a error is risen 
                # (the technical requirements do not include special characters)
                else:
                    return "Special characters are not supported in this tool"
        return result



class CommandLineInterface:
    """
    A class for launching the command line tool
    """
    def __init__(self) -> None:
        self.service = TranslationService()
    

    def run(self):
        """
        Executes the translation process based on command-line arguments.

        Usage:
            The method expects command-line arguments to be passed when running 
            the script. For example: python translator.py "text to translate".
        """
        if len(sys.argv) > 1:
            # each argument is stripped to prevent multiple spaces between words or combinations of numbers and words.
            arguments = [arg.strip() for arg in sys.argv[1:]]
            input_string = ' '.join(arguments)
            try:
                output_string = self.service.translate(input_string)
                print(output_string)
            # The special character error is catched 
            except ValueError as exception:
                # The error message is printed to the user explaining that special characters are not handled by this tool.
                print(exception)


if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.run()
