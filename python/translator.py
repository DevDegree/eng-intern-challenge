from enum import Enum
import sys


class Language(Enum):
    """
    Enum to represent the language types used in translation.
    """
    ENGLISH = 0
    BRAILLE = 1

class Translator:
    """
    Translator class for converting between English and Braille.
    """
    ENGLISH_TO_BRAILLE = {
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
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
        "capital_follows": ".....O",
        "number_follows": ".O.OOO",
        " ": "......",
    }

    BRAILLE_TO_ENGLISH_SPECIAL = {
        '.....O': 'capital_follows',
        '.O.OOO': 'number_follows',
        '......': ' ',
    }

    BRAILLE_TO_ENGLISH_NUMBER = {
        '.OOO..': '0',
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9'
    }

    BRAILLE_TO_ENGLISH_LETTER = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',
    }

    def identify_language(self, input: str) -> int:
        """
        Identifies the language of the given input string.

        This function checks the characters in the input string to determine
        whether the language is English or Braille.

        Args:
            input (str): The input string to analyze.

        Returns:
            Language: Returns Language.ENGLISH if the input is identified as English,
                  and Language.BRAILLE if it is identified as Braille.
        """
        for character in input:
            if character != "O" and character != ".":
                return Language.ENGLISH
        # If all characters are either 'O' or '.', the input must be Braille
        return Language.BRAILLE

    def translate_english_to_braille(self, input: str) -> str:
        """
        Translates English text to Braille.

        This function converts an English input string to its Braille representation.

        Args:
            input (str): The English text one needs to translate.

        Returns:
            str: The Braille representation of the input text.
        """
        translation = ""
        is_number = False
        for character in input:
            if 'a' <= character <= 'z':
                translation += self.ENGLISH_TO_BRAILLE[character]
            elif 'A' <= character <= 'Z':
                translation += (
                    self.ENGLISH_TO_BRAILLE["capital_follows"]
                    + self.ENGLISH_TO_BRAILLE[character.lower()]
                )
            elif '0' <= character <= '9':
                # If this is the first number we encounter, update state
                if not is_number:
                    is_number = True
                    translation += (
                        self.ENGLISH_TO_BRAILLE["number_follows"]
                        + self.ENGLISH_TO_BRAILLE[character]
                    )
                else:
                    translation += self.ENGLISH_TO_BRAILLE[character]
            else:
                # Change state back
                is_number = False
                translation += self.ENGLISH_TO_BRAILLE[character]
        return translation

    def translate_braille_to_english(self, input: str) -> str:
        """
        Translates Braille text to English.

        This function converts a Braille input string to its English representation.

        Args:
            input (str): The Braille text one needs to translate.

        Returns:
            str: The English representation of the input text.
        """
        translation = ""
        capitalized = False
        is_number = False

        # Process the string 6 characters at a time
        for i in range(0, len(input), 6):
            character = input[i : i + 6]
            # First check if this is a special character where states need to be updated
            if character in self.BRAILLE_TO_ENGLISH_SPECIAL:
                if self.BRAILLE_TO_ENGLISH_SPECIAL[character] == "capital_follows":
                    capitalized = True
                elif self.BRAILLE_TO_ENGLISH_SPECIAL[character] == "number_follows":
                    is_number = True
                elif self.BRAILLE_TO_ENGLISH_SPECIAL[character] == " ":
                    is_number = False
                    translation += " "
            # If it's not a special braille character, it must be either a letter or a number
            elif is_number:
                translation += self.BRAILLE_TO_ENGLISH_NUMBER[character]
            # If it's a letter, check whether it's capitalized
            elif capitalized:
                capitalized = False
                translation += self.BRAILLE_TO_ENGLISH_LETTER[character].upper()
            else:
                translation += self.BRAILLE_TO_ENGLISH_LETTER[character]
        return translation

    def translate(self, input: str) -> None:
        """
        Translates the input text based on its language.

        This function first identifies whether the input text is in English or Braille,
        then translates and prints it accordingly

        Args:
            input (str): The text to be translated.
        """
        language = self.identify_language(input)

        if language == Language.ENGLISH:
            translation = self.translate_english_to_braille(input)

        elif language == Language.BRAILLE:
            translation = self.translate_braille_to_english(input)

        print(translation)


if __name__ == "__main__":
    # Combine command-line arguments into a single string
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        translator = Translator()
        translator.translate(input_string)
