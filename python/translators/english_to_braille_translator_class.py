from translators.translation_class_base import *
from typing import Tuple

class EnglishToBrailleTranslator(Translator):
    def __init__(self, input_string: str) -> None:
        super().__init__(input_string)
        self.letter_translation = {
            'a': "O.....",
            'b': "O.O...",
            'c': "OO....",
            'd': "OO.O..",
            'e': "O..O..",
            'f': "OOO...",
            'g': "OOOO..",
            'h': "O.OO..",
            'i': ".OO...",
            'j': ".OOO..",
            'k': "O...O.",
            'l': "O.O.O.",
            'm': "OO..O.",
            'n': "OO.OO.",
            'o': "O..OO.",
            'p': "OOO.O.",
            'q': "OOOOO.",
            'r': "O.OOO.",
            's': ".OO.O.",
            't': ".OOOO.",
            'u': "O...OO",
            'v': "O.O.OO",
            'w': ".OOO.O",
            'x': "OO..OO",
            'y': "OO.OOO",
            'z': "O..OOO",
        }
        self.number_translation = {
            '1': "O.....",
            '2': "O.O...",
            '3': "OO....",
            '4': "OO.O..",
            '5': "O..O..",
            '6': "OOO...",
            '7': "OOOO..",
            '8': "O.OO..",
            '9': ".OO...",
            '0': ".OOO..",
        }
        self.special_translation = {
            " ": "......"
        }
        self.capital_follows_braille = ".....O"
        self.number_follows_braille = ".O.OOO"

    def parse_token(self, token: Token) -> str:
        """Translate a given token"""
        braille = ""
        if token.type == TokenType.SPECIAL:
            braille = self.special_translation[token.value]
        elif token.type == TokenType.LETTERS:
            # Handle the upper and lower cases
            for c in token.value:
                if c.isupper():
                    braille += self.capital_follows_braille
                braille += self.letter_translation[c.lower()]
        elif token.type == TokenType.NUMBERS:
            braille += self.number_follows_braille
            for c in token.value:
                braille += self.number_translation[c.lower()]
        return braille

    def read_word(self, input_str: str) -> Tuple[str, str]:
        """Given that input_str stores a word in it's prefix, extract it

        Returns:
            Tuple[str, str]: First entry is the read word and second is remaining string
        """
        for i in range(len(input_str)):
            if not input_str[i].isalpha():
                break
        if input_str[i].isalpha(): i += 1
        return [input_str[:i], input_str[i:]]

    def read_number(self, input_str: str) -> Tuple[Token, str]:
        """Given that input_str stores a number in it's prefix, extract it

        Returns:
            Tuple[str, str]: First entry is the read number and second is remaining string
        """
        for i in range(len(input_str)):
            if not input_str[i].isdigit():
                break
        if input_str[i].isdigit(): i += 1
        return [input_str[:i], input_str[i:]]

    def get_next_token(self, input_str: str) -> Tuple[Token, str]:
        """Used to get the next token to translate/parse

        Returns:
            Tuple[str, str]: First entry is the read token and second is remaining string
        """
        c = input_str[0]
        special_chars = [" "]
        if c.isdigit():
            val, remaining_str = self.read_number(input_str)
            token = Token(type=TokenType.NUMBERS, value=val)
        elif c.isalpha():
            val, remaining_str = self.read_word(input_str)
            token = Token(type=TokenType.LETTERS, value=val)
        elif c in special_chars:
            remaining_str = input_str[1:]
            token = Token(type=TokenType.SPECIAL, value=c)
        return [token, remaining_str]