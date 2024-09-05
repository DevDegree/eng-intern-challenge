import sys
from typing import Tuple


class EnglishAlphabetMapper:
    def __init__(self):
        self.letters_and_symbols = {
            " ": "......",
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
            "number_follows": ".O.OOO",
            "capital_follows": ".....O",
        }
        self.nums = {
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
        }


class BrailleAlphabetMapper:
    def __init__(self):
        self.letters_and_symbols = {
            "......": " ",
            "O.....": "a",
            "O.O...": "b",
            "OO....": "c",
            "OO.O..": "d",
            "O..O..": "e",
            "OOO...": "f",
            "OOOO..": "g",
            "O.OO..": "h",
            ".OO...": "i",
            ".OOO..": "j",
            "O...O.": "k",
            "O.O.O.": "l",
            "OO..O.": "m",
            "OO.OO.": "n",
            "O..OO.": "o",
            "OOO.O.": "p",
            "OOOOO.": "q",
            "O.OOO.": "r",
            ".OO.O.": "s",
            ".OOOO.": "t",
            "O...OO": "u",
            "O.O.OO": "v",
            ".OOO.O": "w",
            "OO..OO": "x",
            "OO.OOO": "y",
            "O..OOO": "z",
            ".O.OOO": "number_follows",
            ".....O": "capital_follows",
        }
        self.nums = {
            "O.....": "1",
            "O.O...": "2",
            "OO....": "3",
            "OO.O..": "4",
            "O..O..": "5",
            "OOO...": "6",
            "OOOO..": "7",
            "O.OO..": "8",
            ".OO...": "9",
            ".OOO..": "0",
        }


class EnglishToBrailleTranslator:
    def __init__(self, message):
        self.message = message
        self.english_alphabet = EnglishAlphabetMapper()
        self.translated_messsage = None
        self.number_follows = (
            None  # this might break something -> we might need to start at True??
        )
        self.capital_follows = None

    def translate(self) -> str:
        translated_word_list = []
        message_length = len(self.message)
        for i in range(0, message_length):
            # english_word in self.message:
            english_word = self.message[i]
            for char in english_word:
                braille_char = ""
                # when we need to translate numbers
                if not char.isdigit():
                    self.number_follows = False
                if self.number_follows:
                    if self.english_alphabet.nums[char]:
                        braille_char = self.english_alphabet.nums[char]
                    else:
                        self.number_follows = False
                # check if we are going to need to translate a number for the first time
                if char.isdigit() and not self.number_follows:
                    self.number_follows = True
                    # store 'number follows' and the number
                    braille_char = f"""{self.english_alphabet.letters_and_symbols['number_follows']}{self.english_alphabet.nums[char]}"""

                # check if we need to translate captial letters
                self.capital_follows = char.isupper()
                if self.capital_follows:
                    braille_char = f"""{self.english_alphabet.letters_and_symbols["capital_follows"]}{self.english_alphabet.letters_and_symbols[char.lower()]}"""

                # otherwise, we're printing lowercase alphabetical/symbolic characters
                elif not self.number_follows and not self.capital_follows:
                    braille_char = self.english_alphabet.letters_and_symbols[char]

                translated_word_list.append(braille_char)
            #  append spaces after every word except for the last word
            if i < message_length - 1:
                braille_char = self.english_alphabet.letters_and_symbols[" "]
                translated_word_list.append(braille_char)

        self.translated_messsage = "".join(translated_word_list)
        return self.translated_messsage


class BrailleToEnglishTranslator:
    def __init__(self, message):
        self.message = message
        self.braille_alphabet = BrailleAlphabetMapper()
        self.translated_messsage = None
        self.number_follows = (
            None  # this might break something -> we might need to start at True??
        )
        self.capital_follows = None

    def translate(self) -> str:
        message_length = len(self.message[0])
        translated_word_list = []
        for i in range(0, message_length, 6):
            braille_char = self.message[0][i : i + 6]
            english_char = ""

            # check if we are going to need to print a number
            if (
                self.braille_alphabet.letters_and_symbols[braille_char]
                == "number_follows"
            ):
                self.number_follows = True
                continue

            # when we need to translate numbers
            if self.number_follows:
                if braille_char in self.braille_alphabet.nums:
                    english_char = self.braille_alphabet.nums[braille_char]
                else:
                    self.number_follows = False

            # check if we need to print captial letters
            if (
                self.braille_alphabet.letters_and_symbols[braille_char]
                == "capital_follows"
            ):
                self.capital_follows = True
                continue

            # print the capital version of the letters
            if self.capital_follows:
                english_char = self.braille_alphabet.letters_and_symbols[
                    braille_char
                ].upper()
                self.capital_follows = False

            # otherwise, we're printing lowercase alphabetical/symbolic characters
            elif not self.number_follows and not self.capital_follows:
                english_char = self.braille_alphabet.letters_and_symbols[braille_char]

            translated_word_list.append(english_char)
        self.translated_messsage = "".join(translated_word_list)
        return self.translated_messsage


class InputValidator:
    def __init__(self, message):
        self.message = message
        self.english = True
        self.braille = True
        self.english_alphabet = EnglishAlphabetMapper()
        self.braille_alphabet = BrailleAlphabetMapper()

    def validate(self) -> Tuple[bool, bool]:
        # check if its braille, if not, then we can assume its english
        for word in self.message:
            # we could be encountering a potential braille word
            if len(word) == 6:
                # if we're translating an english word and the word appears in the braille language, then it cannot be an english phrase
                if (
                    self.english
                    and word in self.braille_alphabet.letters_and_symbols
                    or word in self.braille_alphabet.nums
                ):
                    self.english = False
                #  otherwise, we ARE translating an english word, meaning it can't be a braille word
                else:
                    self.braille = False
            # if we're translating an english word, we do it character by character
            if self.english:
                # self.braille = False -> this does not work on first try -> FIX
                for char in word:
                    new_char = char
                    if not char.isdigit():
                        new_char = char.lower()  # could be a capital letter if not a
                    if (
                        new_char not in self.english_alphabet.letters_and_symbols
                        and new_char not in self.english_alphabet.nums
                    ):
                        self.english = False
            # if we're tranlating a braille word, we just check if the word doesn't appear in the braille mapping -> we have to process word in chunks of 6 characters
            if self.braille:
                # self.english = False -> this does not work on first try -> FIX
                # loop through the word to process in batches

                for i in range(0, len(word), 6):
                    braille_char = word[i : i + 6]
                    if (
                        braille_char not in self.braille_alphabet.letters_and_symbols
                        and braille_char not in self.braille_alphabet.nums
                    ):
                        self.braille = False
            else:
                break

        return self.braille, self.english


class Translator:
    def __init__(self, message: str):
        self.message = message
        self.translated_messsage = None

    def translate(self) -> str:
        braille, english = InputValidator(self.message).validate()
        if braille:
            self.translated_messsage = BrailleToEnglishTranslator(
                self.message
            ).translate()

        elif english:
            self.translated_messsage = EnglishToBrailleTranslator(
                self.message
            ).translate()
        else:
            raise ValueError(
                "Provided input was invalid. Either invalid braille, english or a mix of the two was present."
            )

        return self.translated_messsage


if __name__ == "__main__":
    message = sys.argv[1:]
    translator = Translator(message=message)
    translated_message = translator.translate()
    print(translated_message)
