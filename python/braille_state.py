from typing import List
from braille_mappings import BRAILLE_TO_ENGLISH, NUMBER_MAPPING
from config import VALID_BRAILLE_CHARS


class BrailleState:
    """
    Maintains the state for Braille to text conversion.

    This class processes Braille characters and maintains the state
    necessary for accurate conversion to text, including handling
    capitalization and number mode.
    """

    def __init__(self):
        """Initialize the BrailleState with empty result and default flags."""
        self._result: List[str] = []
        self._capitalize_next: bool = False
        self._number_mode: bool = False

    def process_char(self, char: str) -> None:
        """
        Process a single Braille character.

        Args:
            char (str): A 6-character Braille string.

        Raises:
            ValueError: If the input is not a valid Braille character.
        """
        if len(char) != 6 or not set(char).issubset(VALID_BRAILLE_CHARS):
            raise ValueError(f"Invalid Braille character: {char}")
        if char == '.....O':  # Capital follows
            self._capitalize_next = True
        elif char == '.O.OOO':  # Number follows
            self._number_mode = True
        elif char in BRAILLE_TO_ENGLISH:
            letter = BRAILLE_TO_ENGLISH[char]
            if letter == ' ':
                self._number_mode = False
                self._result.append(letter)
            elif self._number_mode and letter in NUMBER_MAPPING:
                self._result.append(NUMBER_MAPPING[letter])
            else:
                if self._capitalize_next:
                    letter = letter.upper()
                    self._capitalize_next = False
                self._result.append(letter)

    def get_result(self) -> str:
        """
        Resets the state to its initial values.
        """
        return ''.join(self._result)
