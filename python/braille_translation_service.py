import json
from typing import Iterator

from exceptions import UnsupportedBrailleCharacterError, UnsupportedEnglishCharacterError

class BrailleTranslationService:
    """
    BrailleTranslationService is a class that provides methods to translate between English text and Braille.

    Attributes:
        CAPITAL_FOLLOWS_SYMBOL (str): Braille symbol indicating the following character is capitalized.
        NUMBER_FOLLOWS_SYMBOL (str): Braille symbol indicating the following characters are numbers.
        SPACE_SYMBOL (str): Braille symbol for space.
        LETTER_TO_NUMBER_MAP (dict): Mapping from letters to their corresponding numbers in Braille.
        NUMBER_TO_LETTER_MAP (dict): Mapping from numbers to their corresponding letters in Braille.
        ENGLISH_TO_BRAILLE_MAP (dict): Mapping from English characters to their corresponding Braille symbols.
        BRAILLE_TO_ENGLISH_MAP (dict): Mapping from Braille symbols to their corresponding English characters.
    """
    def __init__(self, braille_mapping_json='braille_mapping.json'):
        """
        Initializes the BrailleTranslationService with mappings from a JSON file.

        Args:
            braille_mapping_json (str): Path to the JSON file containing Braille mappings.
        """
        with open(braille_mapping_json, 'r') as file:
            data = json.load(file)

        # Load special symbols
        self.CAPITAL_FOLLOWS_SYMBOL = data['SPECIAL_SYMBOLS']['CAPITAL_FOLLOWS']
        self.NUMBER_FOLLOWS_SYMBOL = data['SPECIAL_SYMBOLS']['NUMBER_FOLLOWS']
        self.SPACE_SYMBOL = data['ENGLISH_TO_BRAILLE_MAP'][' ']

        # Load mappings
        self.LETTER_TO_NUMBER_MAP = data['LETTER_TO_NUMBER_MAP']
        self.NUMBER_TO_LETTER_MAP = { number: letter for letter, number in self.LETTER_TO_NUMBER_MAP.items() }
        self.ENGLISH_TO_BRAILLE_MAP = data['ENGLISH_TO_BRAILLE_MAP']
        self.BRAILLE_TO_ENGLISH_MAP = { braille: english for english, braille in self.ENGLISH_TO_BRAILLE_MAP.items() }

    # Character Translation Methods
    def english_to_braille(self, char: str, char_iterator: Iterator[str]) -> str:
        """
        Translates a single English character to its corresponding Braille representation.
        Handles capitalization and numeric sequences.

        Args:
            char (str): The English character to be translated.
            char_iterator (Iterator[str]): An iterator over the remaining characters in the input string.

        Returns:
            str: The Braille representation of the given English character.

        Raises:
            UnsupportedEnglishCharacterError: If the english character is not supported in the Braille mapping.
        """
        # Handle special follow symbols
        if char.isupper():
            return self.CAPITAL_FOLLOWS_SYMBOL + self.ENGLISH_TO_BRAILLE_MAP[char.lower()]
        if char.isdigit():
            return self.NUMBER_FOLLOWS_SYMBOL + self._get_braille_digits(char, char_iterator)

        # Handle regular characters
        if char in self.ENGLISH_TO_BRAILLE_MAP:
            return self.ENGLISH_TO_BRAILLE_MAP.get(char, '')
        raise UnsupportedEnglishCharacterError(char)

    def braille_to_english(self, cell: str, cell_iterator: Iterator[str]) -> str:
        """
        Translates a single Braille cell to its corresponding English character.
        Handles capitalization and numeric sequences.

        Args:
            cell (str): The Braille cell to be translated.
            cell_iterator (Iterator[str]): An iterator over the remaining Braille cells in the input string.

        Returns:
            str: The English representation of the given Braille cell.

        Raises:
            UnsupportedBrailleCharacterError: If the Braille cell is not supported.
        """
        # Handle special follow symbols
        if cell == self.CAPITAL_FOLLOWS_SYMBOL:
            return self._cell_to_capital_letter(next(cell_iterator))
        if cell == self.NUMBER_FOLLOWS_SYMBOL:
            return self._get_english_digits(cell_iterator)
        
        # Handle regular characters
        if cell in self.BRAILLE_TO_ENGLISH_MAP:
            return self.BRAILLE_TO_ENGLISH_MAP.get(cell, '')
        raise UnsupportedBrailleCharacterError(cell)

    # Helper methods
    def _get_english_digits(self, cell_iterator: Iterator[str]) -> str:
        """
        Helper method to translate a sequence of Braille cells representing digits to English digits.

        Args:
            cell_iterator (Iterator[str]): An iterator over the Braille cells.

        Returns:
            str: The English numeric corresponding to the Braille cell and terminating space.

        Raises:
            UnsupportedBrailleCharacterError: If a Braille cell is not supported.
        """
        numeric_digits = []
        
        # Iterate over the cells using the cell_iterator
        while True:
            try:
                cell = next(cell_iterator)
                if cell == self.SPACE_SYMBOL:
                    # Ensure "nexted" space char is included in final output
                    numeric_digits.append(' ')
                    break
                numeric_digits.append(self._cell_to_numeric_digit(cell))
            except StopIteration:
                break

        return ''.join(numeric_digits)

    def _get_braille_digits(self, digit: str, digit_iterator: Iterator[str])  -> str:
        """
        Helper method to translate a sequence of English digits to their corresponding Braille cells.

        Args:
            digit (str): The first English digit to be translated.
            digit_iterator (Iterator[str]): An iterator over the remaining English digits.

        Returns:
            str: The Braille cell corresponding to the English numeric and the terminating char.
        
        Raises:
            UnsupportedEnglishCharacterError: If an English character is not supported.
        """
        # A number always has at least one digit
        braille_cells = [self._numeric_digit_to_cell(digit)]

        # Iterate over the remaining digits
        while True:
            try:
                digit = next(digit_iterator)
                if not digit.isdigit():
                    # Ensure "nexted" non-digit char is included in final output
                    if digit not in self.ENGLISH_TO_BRAILLE_MAP:
                        raise UnsupportedEnglishCharacterError(digit)
                    braille_cells.append(self.ENGLISH_TO_BRAILLE_MAP.get(digit, ''))
                    break

                braille_cells.append(self._numeric_digit_to_cell(digit))
            except StopIteration:
                break

        return ''.join(braille_cells)

    def _cell_to_capital_letter(self, braille_cell: str) -> str:
        """
        Helper method to translate a Braille cell to its corresponding capital English letter.

        Args:
            braille_cell (str): The Braille cell to be translated.

        Returns:
            str: The capital English letter corresponding to the Braille cell.

        Raises:
            UnsupportedBrailleCharacterError: If the Braille cell is not supported.
        """
        if braille_cell not in self.BRAILLE_TO_ENGLISH_MAP:
            raise UnsupportedBrailleCharacterError(braille_cell)
        return self.BRAILLE_TO_ENGLISH_MAP.get(braille_cell, '').upper()

    def _cell_to_numeric_digit(self, braille_cell: str) -> str:
        """
        Helper method to translate a Braille cell to its corresponding English digit.

        Args:
            braille_cell (str): The Braille cell to be translated.

        Returns:
            str: The English digit corresponding to the Braille cell.

        Raises:
            UnsupportedBrailleCharacterError: If the Braille cell is not supported.
        """
        if braille_cell not in self.BRAILLE_TO_ENGLISH_MAP:
            raise UnsupportedBrailleCharacterError(braille_cell)
        letter = self.BRAILLE_TO_ENGLISH_MAP.get(braille_cell, '')
        return self.LETTER_TO_NUMBER_MAP.get(letter, '')
    
    def _numeric_digit_to_cell(self, digit: str) -> str:
        """
        Helper method to translate an English digit to its corresponding Braille cell.

        Args:
            digit (str): The English digit to be translated.

        Returns:
            str: The Braille cell corresponding to the English digit.
        """
        letter = self.NUMBER_TO_LETTER_MAP.get(digit, '')
        braille = self.ENGLISH_TO_BRAILLE_MAP.get(letter, '')
        return braille