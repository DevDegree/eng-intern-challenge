from typing import List
from braille_mappings import ENGLISH_TO_BRAILLE, NUMBER_MAPPING


class TextState:
    """
    Maintains the state for text to Braille conversion.

    This class processes text characters and maintains the state
    necessary for accurate conversion to Braille, including handling
    capitalization and number mode.
    """

    def __init__(self):
        """Initialize the TextState with empty result and default flags."""
        self._result: List[str] = []
        self._number_mode: bool = False
        self._capital_mode: bool = False

    def process_char(self, char: str) -> None:
        """
        Process a single text character.

        Args:
            char (str): A single text character.

        Raises:
            ValueError: If the character is not found in the Braille mapping.
        """
        if char.isupper():
            self._result.append(ENGLISH_TO_BRAILLE['capital_follows'])
            self._capital_mode = True
            char = char.lower()
        elif self._capital_mode:
            self._capital_mode = False

        if char.isdigit():
            if not self._number_mode:
                self._result.append(ENGLISH_TO_BRAILLE['number_follows'])
                self._number_mode = True
            char = next(k for k, v in NUMBER_MAPPING.items() if v == char)
        elif self._number_mode and char not in [',', '.']:
            self._number_mode = False

        if char in ENGLISH_TO_BRAILLE:
            self._result.append(ENGLISH_TO_BRAILLE[char])
        else:
            raise ValueError(f"Character '{char}' not found in Braille mapping")

    def get_result(self) -> str:
        """
        Get the resulting Braille string.

        Returns:
            str: The Braille representation of the processed text.
        """
        return ''.join(self._result)
