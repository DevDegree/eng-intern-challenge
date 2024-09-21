"""
Braille Translator Module

This module provides functionality to translate between English text and Braille.
It supports translation of lowercase and uppercase letters, numbers, spaces, and some special characters.

The main components of this module are:
1. BrailleMapper: A class containing all the necessary mapping constants.
2. BrailleTranslator: The main class that performs the actual translation.

Usage:
    from command line: python translator.py <string_to_translate>
    as a module: from translator import BrailleTranslator
                 result = BrailleTranslator.translate(text)

"""

from typing import Dict, List
import sys

class BrailleMapper:
    """
    A class to store all the mapping constants required for Braille translation.

    This class contains class variables that map Braille patterns to English characters,
    and vice versa. It also includes special symbols and number mappings.
    """

    BRAILLE_TO_ENGLISH: Dict[str, str] = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '......': ' ', '..O...': '.', '....O.': ':', '..O.O.': ';',
        '.OO..O': '!', '..OO..': '(', '..OOO.': ')', '..O.OO': '?', '.....O': '^',
        '.O..O.': '/', 'O....O': '#', '.O.O..': '\'', '.OO.OO': '-', '.O..OO': '>',
        'O..O.O': '<', 'OO.O.O': '*', '.O.O.O': '@', '..OO..': '('
    }
    ENGLISH_TO_BRAILLE: Dict[str, str] = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
    CAPITAL_SYMBOL: str = '.....O'
    NUMBER_SYMBOL: str = '.O.OOO'
    NUMBER_MAP: Dict[str, str] = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }

class BrailleTranslator:
    """
    A class that provides methods for translating between English and Braille.

    This class contains static methods for translating from Braille to English,
    from English to Braille, and a main translation method that determines
    the direction of translation based on the input.
    """

    @staticmethod
    def braille_to_english(braille: str) -> str:
        """
        Translate Braille to English.

        This method takes a string of Braille characters (represented by 'O' and '.')
        and translates it to English text. It handles capitalization, numbers, and some special characters.

        Args:
            braille (str): A string of Braille characters to be translated.

        Returns:
            str: The translated English text.

        Raises:
            ValueError: If the input contains characters other than 'O' and '.'.
        """
        if not set(braille).issubset({'O', '.'}):
            raise ValueError("Invalid Braille input. Only 'O' and '.' are allowed.")

        result: List[str] = []
        i: int = 0
        capitalize_next: bool = False
        number_mode: bool = False
        last_char: str = ''

        while i < len(braille):
            if len(braille) - i < 6:
                break  # Stop if there's not enough characters left for a full Braille symbol

            symbol: str = braille[i:i+6]
            
            if symbol == BrailleMapper.CAPITAL_SYMBOL:
                capitalize_next = True
                i += 6
                continue
            
            if symbol == BrailleMapper.NUMBER_SYMBOL:
                number_mode = True
                i += 6
                continue
            
            if symbol == '......':
                result.append(' ')
                number_mode = False
                i += 6
                continue
            
            char: str = BrailleMapper.BRAILLE_TO_ENGLISH.get(symbol, '')
            
            if number_mode:
                char = BrailleMapper.NUMBER_MAP.get(char, char)
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            # Special handling for '>' character
            if char == '>' and last_char == '<':
                char = 'o'
            
            result.append(char)
            last_char = char
            i += 6

        return ''.join(result)

    @staticmethod
    def english_to_braille(text: str) -> str:
        """
        Translate English to Braille.

        This method takes a string of English text and translates it to Braille.
        It handles uppercase letters, numbers, spaces, and some special characters.

        Args:
            text (str): A string of English text to be translated.

        Returns:
            str: The translated Braille text (represented by 'O' and '.').
        """
        result: List[str] = []
        number_mode: bool = False

        for char in text:
            if char.isdigit():
                if not number_mode:
                    result.append(BrailleMapper.NUMBER_SYMBOL)
                    number_mode = True
                # Convert digit to corresponding letter, then to Braille
                result.append(BrailleMapper.ENGLISH_TO_BRAILLE[next(k for k, v in BrailleMapper.NUMBER_MAP.items() if v == char)])
            elif char.isalpha():
                if number_mode:
                    result.append('......')  # Space to end number mode
                    number_mode = False
                if char.isupper():
                    result.append(BrailleMapper.CAPITAL_SYMBOL)
                result.append(BrailleMapper.ENGLISH_TO_BRAILLE[char.lower()])
            elif char == ' ':
                result.append('......')  # Space in Braille
                number_mode = False
            else:
                if char in BrailleMapper.ENGLISH_TO_BRAILLE:
                    result.append(BrailleMapper.ENGLISH_TO_BRAILLE[char])
                else:
                    raise ValueError(f"Character '{char}' is not supported in this Braille system.")
        
        return ''.join(result)

    @classmethod
    def translate(cls, text: str) -> str:
        """
        Translate between English and Braille.

        This method determines whether the input is English or Braille
        and calls the appropriate translation method.

        Args:
            text (str): The text to be translated (either English or Braille).

        Returns:
            str: The translated text.

        Raises:
            ValueError: If the input is neither valid English nor valid Braille.
        """
        if set(text).issubset({'O', '.'}):
            return cls.braille_to_english(text)
        else:
            return cls.english_to_braille(text)

def main(args: List[str]) -> None:
    """
    Main function to handle command-line usage of the translator.

    This function parses command-line arguments, performs the translation,
    and prints the result.

    Args:
        args (List[str]): Command-line arguments (including script name).

    Returns:
        None
    """
    if len(args) < 2:
        print("Usage: python translator.py <string_to_translate>")
        sys.exit(1)

    input_string: str = ''.join(args[1:])  # Remove spaces between arguments

    try:
        result = BrailleTranslator.translate(input_string)
        print(result, end='')
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
