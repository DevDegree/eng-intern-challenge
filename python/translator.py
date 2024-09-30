from enum import Enum
import argparse


from enum import Enum

class BrailleSpecialSymbols(Enum):
    """
    Enum to represent special Braille symbols used in translation.

    Attributes:
        NUMBER_FOLLOWS (int): Indicates that numbers follow.
        CAPITAL_FOLLOWS (int): Indicates that a capital letter follows.
        DECIMAL_FOLLOWS (int): Indicates that a decimal follows.
        BLANK_SYMBOL (int): Represents a blank symbol.
    """
    NUMBER_FOLLOWS = 1
    CAPITAL_FOLLOWS = 2
    DECIMAL_FOLLOWS = 3
    BLANK_SYMBOL = 4


class EnglishToBrailleTranslator:
    """
    A class to handle translation from English to Braille.

    This class provides methods to translate English text to Braille text.
    It uses dictionaries to map English characters to their corresponding Braille symbols.
    """

    def __init__(self):
        """
        Initialize the EnglishToBrailleTranslator with dictionaries for letters, numbers, punctuation, and special symbols.
        """
        # English to Braille dictionary for letters, numbers, and punctuation
        self.english_to_braille_dictionary = {
            # Letters
            "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..",
            "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
            "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
            "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
            "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO",
            "Z": "O..OOO",

            # Numbers
            "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
            "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
            "9": ".OO...", "0": ".OOO..",

            # Punctuation
            ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
            ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
            "(": "O.O..O", ")": ".O.OO.", " ": "......"
        }

        # English to Braille dictionary for special symbols
        self.english_to_braille_special_symbols = {
            BrailleSpecialSymbols.NUMBER_FOLLOWS: ".O.OOO",  # NF: Number follows indicator
            BrailleSpecialSymbols.CAPITAL_FOLLOWS: ".....O",  # CF: Capital follows indicator
            BrailleSpecialSymbols.DECIMAL_FOLLOWS: ".O...O",  # DF: Decimal follows indicator
            BrailleSpecialSymbols.BLANK_SYMBOL: "",
        }

    def translate(self, input_text: str) -> str:
        """
        Translate the given English text to Braille.

        Args:
            input_text (str): The English text to be translated.

        Returns:
            str: The translated Braille text.
        """
        translated_output_text_list = []
        # The special_symbol_holder variable is used to make sure that the special
        # braille symbols are used only once per character
        special_symbol_holder = BrailleSpecialSymbols.BLANK_SYMBOL

        for char in input_text:
            if char.isalpha():
                if char.isupper() and special_symbol_holder != BrailleSpecialSymbols.CAPITAL_FOLLOWS:
                    special_symbol_holder = BrailleSpecialSymbols.CAPITAL_FOLLOWS
                    translated_output_text_list.append(
                        self.english_to_braille_special_symbols[special_symbol_holder]
                    )

                translated_output_text_list.append(
                    self.english_to_braille_dictionary[char.upper()]
                )

            elif char.isdigit():
                if special_symbol_holder != BrailleSpecialSymbols.NUMBER_FOLLOWS:
                    special_symbol_holder = BrailleSpecialSymbols.NUMBER_FOLLOWS
                    translated_output_text_list.append(
                        self.english_to_braille_special_symbols[special_symbol_holder]
                    )

                translated_output_text_list.append(self.english_to_braille_dictionary[char])

            else:
                try:
                    translated_output_text_list.append(self.english_to_braille_dictionary[char])
                except KeyError:
                    raise ValueError(f"Unsupported English character '{char}' for translation from English to Braille.")

        return "".join(translated_output_text_list)


class BrailleToEnglishTranslator:
    """
    A class to handle translation from Braille to English.

    This class provides methods to translate Braille text to English text.
    It uses dictionaries to map Braille symbols to their corresponding English characters.
    """

    def __init__(self):
        """
        Initialize the BrailleToEnglishTranslator with dictionaries for letters, numbers, and punctuation.
        """
        # Braille to English dictionary for letters and space
        self.braille_to_english_letters_and_space = {
            "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
            "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
            "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
            "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
            "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
            "O..OOO": "Z", "......": " ",
        }

        # Braille to English dictionary for punctuation
        self.braille_to_english_punctuations = {
            "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
            "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
            "O.O..O": "(", ".O.OO.": ")",
        }

        # Braille to English dictionary for numbers
        self.braille_to_english_numbers = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
            "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
            ".OOO..": "0"
        }

        # Braille to English dictionary for special symbols
        self.braille_to_english_special_symbols = {
            ".O.OOO": BrailleSpecialSymbols.NUMBER_FOLLOWS,
            ".....O": BrailleSpecialSymbols.CAPITAL_FOLLOWS,
            ".O...O": BrailleSpecialSymbols.DECIMAL_FOLLOWS,
            "": BrailleSpecialSymbols.BLANK_SYMBOL
        }

    def translate(self, input_text: str) -> str:
        """
        Translate the given Braille text to English.

        Args:
            input_text (str): The Braille text to be translated.

        Returns:
            str: The translated English text.
        """
        # Initialize the list to store the translated output characters
        translated_output_text_list = []
        # Flag to indicate if the next character should be capitalized
        capital_symbol_just_activated = False
        # Dictionary to use for translation, initially set to letters and space
        dictionary_to_use_for_translation = self.braille_to_english_letters_and_space

        for i in range(0, len(input_text), 6):
            braille_char = input_text[i:i+6] # Extract the current braille character

            # Check if the braille character is a special symbol
            # and use the appropriate dictionary
            if braille_char in self.braille_to_english_special_symbols:
                if self.braille_to_english_special_symbols[braille_char] == BrailleSpecialSymbols.NUMBER_FOLLOWS\
                        or self.braille_to_english_special_symbols[braille_char] == BrailleSpecialSymbols.DECIMAL_FOLLOWS:
                    dictionary_to_use_for_translation = self.braille_to_english_numbers

                elif self.braille_to_english_special_symbols[braille_char] == BrailleSpecialSymbols.CAPITAL_FOLLOWS:
                    dictionary_to_use_for_translation = self.braille_to_english_letters_and_space
                    capital_symbol_just_activated = True

                continue

            # Translate the braille character using the current dictionary,
            # If not found, try to translate using the punctuation dictionary
            # Raise an error if the braille character is unsupported
            try:
                english_char = dictionary_to_use_for_translation[braille_char]
            except KeyError:
                try:
                    english_char = self.braille_to_english_punctuations[braille_char]
                except KeyError:
                    raise ValueError(f"Unsupported Braille character '{braille_char}' for translation from Braille to English.")

            # Capitalize the character if the capital symbol was just activated
            if capital_symbol_just_activated:
                english_char = english_char.upper()
                capital_symbol_just_activated = False
            else:
                english_char = english_char.lower()

            translated_output_text_list.append(english_char)

        return "".join(translated_output_text_list)


class Translator:
    """
    A class to handle translation between English and Braille.

    This class provides methods to translate text from English to Braille and vice versa.
    It determines the type of input text and uses the appropriate translator.
    """

    def __init__(self):
        """
        Initialize the Translator with English to Braille and Braille to English translators.
        """
        self.english_to_braille = EnglishToBrailleTranslator()
        self.braille_to_english = BrailleToEnglishTranslator()

    def translate(self, input_text: str) -> str:
        """
        Translate the given input text from English to Braille or Braille to English.

        Args:
            input_text (str): The text to be translated.

        Returns:
            str: The translated text.
        """
        # Translate from English to Braille
        if not self._is_braille(input_text):
            return self.english_to_braille.translate(input_text)

        return self.braille_to_english.translate(input_text)

    def _is_braille(self, text: str) -> bool:
        """
        Check if the input text is Braille.

        Args:
            text (str): The text to be checked.

        Returns:
            bool: True if the text is Braille, False otherwise.
        """
        # Check if the input is Braille (contains only 'O' and '.' characters)
        return all(char in ('O', '.') for char in text)


if __name__=='__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Translate English to Braille or Braille to English.')
    parser.add_argument('text', nargs='+', help='The text to be translated, either English or Braille.')
    args = parser.parse_args()

    input_text = ' '.join(args.text).strip()  # Concatenate the words to form the full text

    translator = Translator()
    try:
        print(f"{translator.translate(input_text)}")
    except ValueError as e:
        print(f"ERROR: {e}")
        exit(1)