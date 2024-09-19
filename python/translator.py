import sys
from typing import Dict


class Translator:

    def __init__(self) -> None:
        self.capital_follows = ".....O"
        self.decimal_follows = ".O...O"
        self.numbers_follows = ".O.OOO"
        letters = "qwertyuiopasdfghjklzxcvbnm"

        self.english_to_braille_mapping = {
            "capital": self.capital_follows,
            "decimal": self.decimal_follows,
            "numbers": self.numbers_follows,
            ".": "..OO.O",
            ",": "..O...",
            "?": "..O.OO",
            "!": "..OOO.",
            ":": "..OO..",
            ";": "..O.O.",
            "-": "....OO",
            "/": ".O..O.",
            "<": ".OO..O",
            ">": "O..OO.",
            "(": "O.O..O",
            ")": ".O.OO.",
            " ": "......"
        }

        # Assign letters to english to braille mapping
        self._english_mapping(letters)

        # Invert english to braille mapping to get braille to english
        self.braille_to_english_mapping = {
            value: key for key, value in self.english_to_braille_mapping.items()
        }

    def _english_mapping(self, letters: str) -> None:
        # Starting braille code representing "a" in braille
        base_braille_code = 0x2801

        for letter in letters:
            # Convert the letter into a braille letter
            offset = ord(letter) - ord("a")
            braille_letter = chr(base_braille_code + offset)

            # Convert the braille letter into a binary string representation
            unicode_code_point = ord(braille_letter)
            dot_pattern = unicode_code_point - base_braille_code - 1
            binary_representation = f"{dot_pattern:06b}"

            # Convert binary string representation to desired ./O representation
            binary_representation = binary_representation.replace("1", "O")
            binary_representation = binary_representation.replace("0", ".")
            string_representation = binary_representation[::-1]

            # Add uppercase and lowercase letter to self.english_to_braille
            self.english_to_braille_mapping[letter] = string_representation
            capital_letter = letter.upper()
            braille_capital = self.capital_follows + string_representation
            self.english_to_braille_mapping[capital_letter] = braille_capital

            # Letters a to i and numbers 1 to 9 are the same in braille
            if "a" <= letter <= "i":
                number = f"{offset + 1}"
                self.english_to_braille_mapping[number] = string_representation

            elif letter == "j":
                number = f"{0}"
                self.english_to_braille_mapping[number] = string_representation

    def english_to_braille(self, english_text: str) -> str:
        """Converts given string in English english_text and returns
        Braille text

        :param english_text:
        :return:
        """
        pass

    def braille_to_english(self, braille_text: str) -> str:
        """Converts given string in Braille braille_text and returns
        English text

        :param braille_text:
        :return:
        """
        pass


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing Argument. Need Braille text or English text")

    # Parse the command line arguments and store full text
    system_arguments = sys.argv[1:]
    string_to_translate = " ".join(system_arguments)

    # Check if string is braille or english
    raised_count = string_to_translate.count("O")
    lowered_count = string_to_translate.count(".")

    is_braille_text = raised_count + lowered_count == len(string_to_translate)
    length_divides_six = len(string_to_translate) % 6 == 0

    if is_braille_text and length_divides_six:
        current_language = "BRAILLE"
    else:
        current_language = "ENGLISH"

    translator = Translator()
    print(translator.english_to_braille_mapping)

