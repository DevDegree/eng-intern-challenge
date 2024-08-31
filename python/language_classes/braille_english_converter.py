import json
import re
from utils.bidirectional_map import BidirectionalMap


class BrailleEnglishConverter:
    """
    Class for converting between Braille and English.
    """

    def __init__(self, json_file) -> None:
        """
        Initialize the converter with the mappings between Braille and English.
        Creates mappings for letters, numbers, and special characters, and stores each in a BidirectionalMap.
        This allows for a single source of truth for the mappings, and easy access to the mappings in both directions.
        """
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.letters = BidirectionalMap(data.get("letters"))
                self.numbers = BidirectionalMap(data.get("numbers"))
                self.special_chars = BidirectionalMap(data.get("special_chars"))
        except FileNotFoundError:
            raise FileNotFoundError(f"File {json_file} not found.")
        except Exception as e:
            raise Exception(f"Unexpected Error occurred: {str(e)}")

    def convert_braille_to_english(self, braille_text):
        """
        Convert the given Braille text to English.

        Each character is stored as a series of O (the letter O) or . (a period), and is 6 characters long,
        reading left to right, line by line, starting at the top left.
        When a Braille 'capital follows' symbol is read, assume only the next symbol should be capitalized.
        When a Braille 'number follows' symbol is read, assume all following symbols are numbers until the
        next space symbol.
        """

        # Check if the string contains any characters other than . and O
        pattern = r"[^.O]"
        match = re.search(pattern, braille_text)
        if match is not None:
            raise ValueError(
                f"aInvalid character '{match.group()}' found in Braille text."
            )

        # Check if the string is a multiple of 6 characters long
        if len(braille_text) % 6 != 0:
            raise ValueError("Braille text is not a multiple of 6 characters long.")

        english_text = ""
        is_number = False
        is_capital = False

        for i in range(0, len(braille_text), 6):
            english_char = ""
            # get the next 6 characters
            braille_char = braille_text[i : i + 6]

            if self.special_chars.get_key(braille_char) is not None:
                # if the character is a special character
                special_char = self.special_chars.get_key(braille_char)

                if special_char == "capital_follows":
                    is_capital = True
                elif special_char == "number_follows":
                    is_number = True
                elif special_char == "space":
                    is_number = False
                    english_char = " "
            elif is_number:
                # if the character is a number
                english_number = self.numbers.get_key(braille_char)
                if english_number is None:
                    raise ValueError(
                        f"Unable to find number '{braille_char}' found in Braille text."
                    )

                english_char = english_number
            else:
                # if the character is a letter
                english_letter = self.letters.get_key(braille_char)
                if english_letter is None:
                    raise ValueError(
                        f"Unable to find letter '{braille_char}' found in Braille text."
                    )

                if is_capital:
                    english_letter = english_letter.upper()
                    is_capital = False

                english_char = english_letter

            if english_char is not None:
                english_text += english_char
            else:
                raise ValueError(f"Tried to add None when using {braille_char}")

        return english_text

    def convert_english_to_braille(self, english_text):
        """
        Convert the given English text to Braille.
        Upper case letters are prefixed with a 'capital follows' symbol.
        Numbers are prefixed with a 'number follows' symbol.
        """
        braille_text = ""
        is_number_mode = False

        for char in english_text:
            braille_char = ""

            if char == " ":
                braille_char = self.special_chars.get_value("space")
            elif char.isalpha():
                lower_char = char.lower()
                braille_char = self.letters.get_value(lower_char)
                if char.isupper():
                    capital_follows = self.special_chars.get_value("capital_follows")
                    if capital_follows is None or braille_char is None:
                        raise ValueError(
                            f"Unable to find 'capital_follows' and {braille_char} special character."
                        )

                    braille_char = capital_follows + braille_char
            elif char.isnumeric():
                braille_char = self.numbers.get_value(char)
                if not is_number_mode:
                    number_follows = self.special_chars.get_value("number_follows")
                    if number_follows is None:
                        raise ValueError(
                            "Unable to find 'number_follows' special character."
                        )
                    is_number_mode = True

                    braille_text += number_follows
            if braille_char is not None:
                braille_text += braille_char
            else:
                raise ValueError(f"Tried to add None when using {braille_char}")

        return braille_text
