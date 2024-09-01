from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple

class TokenType(Enum):
    SPECIAL = 0  # Space or special characters
    LETTERS = 1  # (A-Z)
    NUMBERS = 2   # (0-9)

class Token:
    def __init__(self, type: TokenType, value: str) -> None:
        self.type: TokenType = type
        self.value: str = value

class Translator(ABC):
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    @abstractmethod
    def parse_token(self, token: Token) -> str:
        """
        Translate the given token.

        Args:
            token (Token): The token to translate.

        Returns:
            str: The translated string.
        """
        pass

    @abstractmethod
    def get_next_token(self, input_str: str) -> Tuple[Token, str]:
        """
        Extracts the next token from the input string.

        Args:
            input_str (str): The input string to tokenize.

        Returns:
            Tuple[Token, str]: A tuple containing the next token and the remaining input string.
        """
        pass

    def translate(self) -> str:
        """The key method for translating the input string

        Returns:
            str: Translated string
        """
        input_str = self.input_string
        output = ""
        while input_str:
            token, remaining_input = self.get_next_token(input_str)
            translated = self.parse_token(token)
            output += translated
            input_str = remaining_input
        return output