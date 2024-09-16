from exceptions import EmptyInputError, IncompleteBrailleSequenceError, InvalidBrailleCharacterError
from typing import List

class InputTextProcessor:
    """
    Class to process Braille input and validate its format.

    Attributes:
        valid_braille (set): Set of valid Braille characters.
        cell_size (int): Size of a Braille cell.
        text (str): The input text to be processed.
    """

    valid_braille = set(['O', '.'])
    cell_size = 6

    def __init__(self, text: str):
        """
        Initializes the InputTextProcessor with the given text.

        Args:
            text (str): The input text to be processed.

        Raises:
            EmptyInputError: If the input text is empty.
        """
        if not text:
            raise EmptyInputError()
        self.text = text

    def braille_to_cells(self, text: str) -> List[str]:
        """
        Converts a string of Braille text into a list of Braille cells.

        Args:
            text (str): The Braille text to be converted.

        Returns:
            List[str]: A list of Braille cells.
        """
        return [text[i : i + self.cell_size] for i in range(0, len(text), self.cell_size)]

    def is_valid_braille(self, text: str) -> bool:
        """
        Validates if the given text is a valid Braille sequence.

        Args:
            text (str): The Braille text to be validated.

        Returns:
            bool: True if the text is a valid Braille sequence, False otherwise.

        Raises:
            InvalidBrailleCharacterError: If the text contains invalid Braille characters.
            IncompleteBrailleSequenceError: If the text length is not a multiple of the cell size.
        """
        chars = set(text)
        if not chars <= self.valid_braille:
            raise InvalidBrailleCharacterError(chars - self.valid_braille)
        if len(text) % self.cell_size != 0:
            raise IncompleteBrailleSequenceError(len(text))
        return True
    
    def contains_only_braille(self, text: str) -> bool:
        """
        Checks if the given text consists only of valid Braille characters.

        Args:
            text (str): The text to be checked.

        Returns:
            bool: True if the text consists only of valid Braille characters, False otherwise.
        """
        return set(text) <= self.valid_braille

    