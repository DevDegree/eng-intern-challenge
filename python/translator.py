import sys
import re


class Translator:

    def __init__(self) -> None:
        self.capital_follows = ".....O"
        self.decimal_follows = ".O...O"
        self.numbers_follows = ".O.OOO"
        letters = "qwertyuiopasdfghjklzxcvbnm"

        self.letter_to_braille_offset = {
            'a': 0x01, 'b': 0x03, 'c': 0x09, 'd': 0x19, 'e': 0x11,
            'f': 0x0B, 'g': 0x1B, 'h': 0x13, 'i': 0x0A, 'j': 0x1A,
            'k': 0x05, 'l': 0x07, 'm': 0x0D, 'n': 0x1D, 'o': 0x15,
            'p': 0x0F, 'q': 0x1F, 'r': 0x17, 's': 0x0E, 't': 0x1E,
            'u': 0x25, 'v': 0x27, 'w': 0x3A, 'x': 0x2D, 'y': 0x3D, 'z': 0x35
        }

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
        base_braille_code = 0x2800

        for letter in letters:
            # Convert the letter into a braille letter
            offset = ord(letter) - ord("a") + 1
            braille_letter = self._letter_to_braille(letter)

            # Convert the braille letter into a binary string representation
            unicode_code_point = ord(braille_letter)
            dot_pattern = unicode_code_point - base_braille_code
            block = f"{dot_pattern:06b}"
            binary_representation = block[:4:3] + block[1:5:3] + block[2:6:3]

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
                number = f"{offset}"
                self.english_to_braille_mapping[number] = string_representation

            elif letter == "j":
                number = f"{0}"
                self.english_to_braille_mapping[number] = string_representation

    def _letter_to_braille(self, character: str) -> str:

        braille_base = 0x2800  # Starting point for Braille Unicode characters
        return chr(braille_base + self.letter_to_braille_offset[character])

    def english_to_braille(self, english_text: str) -> str:
        """Converts given string in English english_text and returns
        Braille text

        :param english_text:
        :return:
        """
        braille_string = ""
        numbers = False
        for character in english_text:
            if character.isnumeric() and not numbers:
                print("character.isnumeric() and not numbers")
                braille_string += self.numbers_follows
                numbers = True

            elif character == "." and numbers:
                print("character == \".\" and numbers")
                braille_string += self.decimal_follows

            elif not character.isnumeric() and numbers:
                print("not character.isnumeric() and numbers")
                braille_string += self.english_to_braille_mapping[character]
                numbers = False

            else:
                print("else")
                braille_string += self.english_to_braille_mapping[character]

        return braille_string

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

    # Conditions for text to be braille
    is_braille_text = raised_count + lowered_count == len(string_to_translate)
    length_divides_six = len(string_to_translate) % 6 == 0

    translator = Translator()

    # Assumption is text will be english
    if is_braille_text and length_divides_six:
        current_language = "BRAILLE"
    else:
        translated_string = translator.english_to_braille(string_to_translate)
        print(translated_string)

