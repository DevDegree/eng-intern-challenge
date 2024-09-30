from enum import Enum
import argparse

class EnglishToBrailleTranslator:
    class _BrailleSpecialSymbols(Enum):
        NUMBER_FOLLOWS = 1
        CAPITAL_FOLLOWS = 2
        DECIMAL_FOLLOWS = 3
        BLANK_SYMBOL = 4

    def __init__(self):
        # English to Braille dictionary for letters, numbers and punctuation
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
            self._BrailleSpecialSymbols.NUMBER_FOLLOWS: ".O.OOO",  # NF: Number follows indicator
            self._BrailleSpecialSymbols.CAPITAL_FOLLOWS: ".....O",  # CF: Capital follows indicator
            self._BrailleSpecialSymbols.DECIMAL_FOLLOWS: ".O...O",  # DF: Decimal follows indicator
            self._BrailleSpecialSymbols.BLANK_SYMBOL: "",
        }


    def translate(self, input_text: str) -> str:
        translated_output_text_list = []
        # The special_symbol_holder variable is used to make sure that the special
        # braille symbols are used only once per character
        special_symbol_holder = self._BrailleSpecialSymbols.BLANK_SYMBOL

        for char in input_text:
            if char.isalpha():
                if char.isupper() and special_symbol_holder != self._BrailleSpecialSymbols.CAPITAL_FOLLOWS:
                    special_symbol_holder = self._BrailleSpecialSymbols.CAPITAL_FOLLOWS
                    translated_output_text_list.append(
                            self.english_to_braille_special_symbols[special_symbol_holder]
                        )

                translated_output_text_list.append(
                    self.english_to_braille_dictionary[char.upper()]
                )


            elif char.isdigit():
                if special_symbol_holder != self._BrailleSpecialSymbols.NUMBER_FOLLOWS:
                    special_symbol_holder = self._BrailleSpecialSymbols.NUMBER_FOLLOWS
                    translated_output_text_list.append(
                        self.english_to_braille_special_symbols[special_symbol_holder]
                    )

                translated_output_text_list.append(self.english_to_braille_dictionary[char])

            else:
                try:
                    translated_output_text_list.append(self.english_to_braille_dictionary[char])
                except KeyError:
                    raise ValueError(f"Unsupported character '{char}' for translation from English to Braille.")

        return "".join(translated_output_text_list)


class BrailleToEnglishTranslator:
    def __init__(self):
        # Braille to English dictionary
        self.braille_to_english_letters_and_punctuations = {
            "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
            "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
            "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
            "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
            "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
            "O..OOO": "Z",

            # Punctuation
            "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
            "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
            "O.O..O": "(", ".O.OO.": ")", "......": " "
        }

        self.braille_to_english_special_symbols = {
            ".O.OOO": "NF", ".....O": "CF", ".O...O": "DF"
        }

        self.braille_to_english_numbers = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
            "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
            ".OOO..": "0"
        }


class Translator:
    def __init__(self):
        self.english_to_braille = EnglishToBrailleTranslator()

    def run(self):
        # Use argparse to get the input from the command line
        parser = argparse.ArgumentParser(description='Translate English to Braille or Braille to English.')
        parser.add_argument('text', nargs='+', help='The text to be translated, either English or Braille.')

        # Parse the command line arguments
        args = parser.parse_args()
        input_text = ' '.join(args.text).strip()  # Concatenate the words to form the full text

        # Translate from English to Braille
        result = self.english_to_braille.translate(input_text)
        print(f"{result}")


if __name__=='__main__':
    translator = Translator()
    try:
        translator.run()
    except ValueError as e:
        print(f"ERROR: {e}")
        exit(1)