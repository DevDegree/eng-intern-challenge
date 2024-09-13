from translators.translation_class_base import *
from typing import Tuple

class BrailleToEnglishTranslator(Translator):
    def __init__(self, input_string: str) -> None:
        super().__init__(input_string)
        self.letter_translation = {
            "O.....": 'a',
            "O.O...": 'b',
            "OO....": 'c',
            "OO.O..": 'd',
            "O..O..": 'e',
            "OOO...": 'f',
            "OOOO..": 'g',
            "O.OO..": 'h',
            ".OO...": 'i',
            ".OOO..": 'j',
            "O...O.": 'k',
            "O.O.O.": 'l',
            "OO..O.": 'm',
            "OO.OO.": 'n',
            "O..OO.": 'o',
            "OOO.O.": 'p',
            "OOOOO.": 'q',
            "O.OOO.": 'r',
            ".OO.O.": 's',
            ".OOOO.": 't',
            "O...OO": 'u',
            "O.O.OO": 'v',
            ".OOO.O": 'w',
            "OO..OO": 'x',
            "OO.OOO": 'y',
            "O..OOO": 'z',
        }
        self.number_translation = {
            "O.....": '1',
            "O.O...": '2',
            "OO....": '3',
            "OO.O..": '4',
            "O..O..": '5',
            "OOO...": '6',
            "OOOO..": '7',
            "O.OO..": '8',
            ".OO...": '9',
            ".OOO..": '0',
        }
        self.special_translation = {
            "......": " "
        }
        self.capital_follows_braille = ".....O"
        self.number_follows_braille = ".O.OOO"

    def parse_token(self, token: Token) -> str:
        """Translate a given token"""
        braille = ""
        if token.type == TokenType.SPECIAL:
            braille = self.special_translation[token.value]
        elif token.type == TokenType.LETTERS:
            input_string = token.value
            while input_string:
                segment, input_string = self.get_next_braille_segment(input_string)
                if segment == self.capital_follows_braille:
                    letter_segment, input_string = self.get_next_braille_segment(input_string)
                    if letter_segment:
                        braille += self.letter_translation[letter_segment].upper()
                else:
                    braille += self.letter_translation[segment]
        elif token.type == TokenType.NUMBERS:
            input_string = token.value
            while input_string:
                segment, input_string = self.get_next_braille_segment(input_string)
                if segment == self.number_follows_braille:
                    continue
                else:
                    braille += self.number_translation[segment]
        return braille

    def read_word(self, input_str: str) -> Tuple[str, str]:
        """Given that input_str stores a word in it's prefix, extract it

        Returns:
            Tuple[str, str]: First entry is the read word and second is remaining string
        """
        word = ""
        while input_str:
            segment, input_str = self.get_next_braille_segment(input_str)
            if segment not in self.letter_translation and segment != self.capital_follows_braille:
                input_str = segment + input_str
                break
            word += segment
        return [word, input_str]

    def read_number(self, input_str: str) -> str:
        """Given that input_str stores a number in it's prefix, extract it

        Returns:
            Tuple[str, str]: First entry is the read number and second is remaining string
        """
        # Ignore the first segment since it'll be number_follows_braille
        _, input_str = self.get_next_braille_segment(input_str)
        number = ""

        while input_str:
            segment, input_str = self.get_next_braille_segment(input_str)
            if segment not in self.number_translation:
                input_str = segment + input_str
                break
            number += segment
        return [number, input_str]

    def get_next_braille_segment(self, input_str) -> Tuple[str, str]:
        """Helper for getting the next 6 characters forming a braille term"""
        return [input_str[:6], input_str[6:]]

    def get_next_token(self, input_str: str) -> Tuple[Token, str]:
        """Used to get the next token to translate/parse

        Returns:
            Tuple[str, str]: First entry is the read token and second is remaining string
        """
        segment, remaining_str = self.get_next_braille_segment(input_str)
        token = None
        if segment in self.special_translation:
            val = segment
            token = Token(type=TokenType.SPECIAL, value=val)
        elif segment in self.letter_translation or segment == self.capital_follows_braille:
            val, remaining_str = self.read_word(input_str)
            token = Token(type=TokenType.LETTERS, value=val)
        elif segment == self.number_follows_braille:
            val, remaining_str = self.read_number(input_str)
            token = Token(type=TokenType.NUMBERS, value=val)
        return [token, remaining_str]