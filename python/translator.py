import sys
from enum import Enum

class TokenType(Enum):
    SPECIAL = 0  # Space or special characters
    LETTERS = 1  # (A-Z)
    NUMBERS = 2   # (0-9)

class Token:
    def __init__(self, type: TokenType, value: str) -> None:
        self.type: TokenType = type
        self.value: str = value

class Translator:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def parse_token(self, token: Token) -> str:
        """
        Translate the given token.

        Args:
            token (Token): The token to translate.

        Returns:
            str: The translated string.
        """
        pass

    def get_next_token(self, input_str: str) -> tuple[Token, str]:
        """
        Extracts the next token from the input string.

        Args:
            input_str (str): The input string to tokenize.

        Returns:
            tuple[Token, str]: A tuple containing the next token and the remaining input string.
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
# class EnglishToBrailleTranslator(Translator):
#     def __init__(self, input_string: str) -> None:
#         super().__init__(input_string)
#         self.letter_translation = {
#             'a': "O.....",
#             'b': "O.O...",
#             'c': "OO....",
#             'd': "OO.O..",
#             'e': "O..O..",
#             'f': "OOO...",
#             'g': "OOOO..",
#             'h': "O.OO..",
#             'i': ".OO...",
#             'j': ".OOO..",
#             'k': "O...O.",
#             'l': "O.O.O.",
#             'm': "OO..O.",
#             'n': "OO.OO.",
#             'o': "O..OO.",
#             'p': "OOO.O.",
#             'q': "OOOOO.",
#             'r': "O.OOO.",
#             's': ".OO.O.",
#             't': ".OOOO.",
#             'u': "O...OO",
#             'v': "O.O.OO",
#             'w': ".OOO.O",
#             'x': "OO..OO",
#             'y': "OO.OOO",
#             'z': "O..OOO",
#         }
#         self.number_translation = {
#             '1': "O.....",
#             '2': "O.O...",
#             '3': "OO....",
#             '4': "OO.O..",
#             '5': "O..O..",
#             '6': "OOO...",
#             '7': "OOOO..",
#             '8': "O.OO..",
#             '9': ".OO...",
#             '0': ".OOO..",
#         }
#         self.special_translation = {
#             " ": "......"
#         }
#         self.capital_follows_braille = ".....O"
#         self.number_follows_braille = ".O.OOO"

#     def parse_token(self, token: Token) -> str:
#         """Translate a given token"""
#         braille = ""
#         if token.type == TokenType.SPECIAL:
#             braille = self.special_translation[token.value]
#         elif token.type == TokenType.LETTERS:
#             # Handle the upper and lower cases
#             for c in token.value:
#                 if c.isupper():
#                     braille += self.capital_follows_braille
#                 braille += self.letter_translation[c.lower()]
#         elif token.type == TokenType.NUMBERS:
#             braille += self.number_follows_braille
#             for c in token.value:
#                 braille += self.number_translation[c.lower()]
#         return braille

#     def read_word(self, input_str: str) -> tuple[str, str]:
#         """Given that input_str stores a word in it's prefix, extract it"""
#         for i in range(len(input_str)):
#             if not input_str[i].isalpha():
#                 break
#         if input_str[i].isalpha(): i += 1
#         return [input_str[:i], input_str[i:]]

#     def read_number(self, input_str: str) -> str:
#         """Given that input_str stores a number in it's prefix, extract it"""
#         for i in range(len(input_str)):
#             if not input_str[i].isdigit():
#                 break
#         if input_str[i].isdigit(): i += 1
#         return [input_str[:i], input_str[i:]]

#     def get_next_token(self, input_str: str) -> tuple[Token, str]:
#         """Used to get the next token to translate/parse"""
#         c = input_str[0]
#         special_chars = [" "]
#         if c.isdigit():
#             val, remaining_str = self.read_number(input_str)
#             token = Token(type=TokenType.NUMBERS, value=val)
#         elif c.isalpha():
#             val, remaining_str = self.read_word(input_str)
#             token = Token(type=TokenType.LETTERS, value=val)
#         elif c in special_chars:
#             remaining_str = input_str[1:]
#             token = Token(type=TokenType.SPECIAL, value=c)
#         return [token, remaining_str]
# class BrailleToEnglishTranslator(Translator):
#     def __init__(self, input_string: str) -> None:
#         super().__init__(input_string)
#         self.letter_translation = {
#             "O.....": 'a',
#             "O.O...": 'b',
#             "OO....": 'c',
#             "OO.O..": 'd',
#             "O..O..": 'e',
#             "OOO...": 'f',
#             "OOOO..": 'g',
#             "O.OO..": 'h',
#             ".OO...": 'i',
#             ".OOO..": 'j',
#             "O...O.": 'k',
#             "O.O.O.": 'l',
#             "OO..O.": 'm',
#             "OO.OO.": 'n',
#             "O..OO.": 'o',
#             "OOO.O.": 'p',
#             "OOOOO.": 'q',
#             "O.OOO.": 'r',
#             ".OO.O.": 's',
#             ".OOOO.": 't',
#             "O...OO": 'u',
#             "O.O.OO": 'v',
#             ".OOO.O": 'w',
#             "OO..OO": 'x',
#             "OO.OOO": 'y',
#             "O..OOO": 'z',
#         }
#         self.number_translation = {
#             "O.....": '1',
#             "O.O...": '2',
#             "OO....": '3',
#             "OO.O..": '4',
#             "O..O..": '5',
#             "OOO...": '6',
#             "OOOO..": '7',
#             "O.OO..": '8',
#             ".OO...": '9',
#             ".OOO..": '0',
#         }
#         self.special_translation = {
#             "......": " "
#         }
#         self.capital_follows_braille = ".....O"
#         self.number_follows_braille = ".O.OOO"

#     def parse_token(self, token: Token) -> str:
#         """Translate a given token"""
#         braille = ""
#         if token.type == TokenType.SPECIAL:
#             braille = self.special_translation[token.value]
#         elif token.type == TokenType.LETTERS:
#             input_string = token.value
#             while input_string:
#                 segment, input_string = self.get_next_braille_segment(input_string)
#                 if segment == self.capital_follows_braille:
#                     letter_segment, input_string = self.get_next_braille_segment(input_string)
#                     if letter_segment:
#                         braille += self.letter_translation[letter_segment].upper()
#                 else:
#                     braille += self.letter_translation[segment]
#         elif token.type == TokenType.NUMBERS:
#             input_string = token.value
#             while input_string:
#                 segment, input_string = self.get_next_braille_segment(input_string)
#                 if segment == self.number_follows_braille:
#                     continue
#                 else:
#                     braille += self.number_translation[segment]
#         return braille

#     def read_word(self, input_str: str) -> tuple[str, str]:
#         """Given that input_str stores a word in it's prefix, extract it"""
#         word = ""
#         while input_str:
#             segment, input_str = self.get_next_braille_segment(input_str)
#             if segment not in self.letter_translation and segment != self.capital_follows_braille:
#                 input_str = segment + input_str
#                 break
#             word += segment
#         return [word, input_str]

#     def read_number(self, input_str: str) -> str:
#         """Given that input_str stores a number in it's prefix, extract it"""
#         # Ignore the first segment since it'll be number_follows_braille
#         _, input_str = self.get_next_braille_segment(input_str)
#         number = ""

#         while input_str:
#             segment, input_str = self.get_next_braille_segment(input_str)
#             if segment not in self.number_translation:
#                 input_str = segment + input_str
#                 break
#             number += segment
#         return [number, input_str]

#     def get_next_braille_segment(self, input_str) -> tuple[str, str]:
#         """Helper for getting the next 6 characters forming a braille term"""
#         return [input_str[:6], input_str[6:]]

#     def get_next_token(self, input_str: str) -> tuple[Token, str]:
#         """Used to get the next token to translate/parse"""
#         segment, remaining_str = self.get_next_braille_segment(input_str)
#         token = None
#         if segment in self.special_translation:
#             val = segment
#             token = Token(type=TokenType.SPECIAL, value=val)
#         elif segment in self.letter_translation or segment == self.capital_follows_braille:
#             val, remaining_str = self.read_word(input_str)
#             token = Token(type=TokenType.LETTERS, value=val)
#         elif segment == self.number_follows_braille:
#             val, remaining_str = self.read_number(input_str)
#             token = Token(type=TokenType.NUMBERS, value=val)
#         return [token, remaining_str]

def translate(input_string: str) -> str:
    # Deterine whether we are translating from english or braille
    # if len(input_string) % 6 == 0 and all(c in ".O" for c in input_string) :
    #     # Case 1: We are working with braille data
    #     translator = BrailleToEnglishTranslator(input_string)
    # else:
    #     # Case 2: We are working with english data
    # translator = EnglishToBrailleTranslator(input_string)
    print("bar")

print("foo")
translate("")