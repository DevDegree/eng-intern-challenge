# translator.py

# Author: Tarek Ibrahim
# Email: tarekibrahim3@cmail.carleton.ca
# Date: 2024-09-12

# Required modules
import sys


class BrailleTranslator:
    def __init__(self):
        """
        Initialize the BrailleTranslator with mappings for English to Braille and Braille to English.
        """
        self.braille_flags = {
            "CAPITAL": ".....O",
            "DECIMAL": ".O...O",
            "NUMBER": ".O.OOO",
        }
        self.english_to_braille = {
            "a": "O.....",            "b": "O.O...",            "c": "OO....",
            "d": "OO.O..",            "e": "O..O..",            "f": "OOO...",
            "g": "OOOO..",            "h": "O.OO..",            "i": ".OO...",
            "j": ".OOO..",            "k": "O...O.",            "l": "O.O.O.",
            "m": "OO..O.",            "n": "OO.OO.",            "o": "O..OO.",
            "p": "OOO.O.",            "q": "OOOOO.",            "r": "O.OOO.",
            "s": ".OO.O.",            "t": ".OOOO.",            "u": "O...OO",
            "v": "O.O.OO",            "w": ".OOO.O",            "x": "OO..OO",
            "y": "OO.OOO",            "z": "O..OOO",            "1": "O.....",
            "2": "O.O...",            "3": "OO....",            "4": "OO.O..",
            "5": "O..O..",            "6": "OOO...",            "7": "OOOO..",
            "8": "O.OO..",            "9": ".OO...",            "0": ".OOO..",
            ".": "..OO.O",            ",": "..O...",            "?": "..O.OO",
            "!": "..OOO.",            ":": "..OO..",            ";": "..O.O.",
            "-": "....OO",            "/": ".O..O.",            "<": ".OO..O",
            ">": "O..OO.",            "(": "O.O..O",            ")": ".O.OO.",
            " ": "......",
        }

        # Ensure input_string length is a multiple of 6
        self.braille_to_english = self._create_reverse_mapping()

    def _create_reverse_mapping(self):
        """
        Create a reverse mapping from Braille to English.

        Returns:
        dict: A dictionary mapping Braille strings to lists of English characters.
        """
        # braille_to_english = {v: k for k, v in english_to_braille.items()}
        braille_to_english = {}
        for char, braille in self.english_to_braille.items():
            if braille not in braille_to_english:
                braille_to_english[braille] = []
            braille_to_english[braille].append(char)
        return braille_to_english

    def is_braille(self, input_string):
        """
        Determine if the input string is in Braille format.

        Parameters:
        input_string (str): The string to be checked if it is in Braille format.

        Returns:
        bool: True if the input string is in Braille format, False otherwise.
        """
        valid_chars = {"O", "."}
        for char in input_string:
            if char not in valid_chars:
                return False
        return True

    def translate_to_braille(self, input_string):
        """
        Translate English input string to Braille.

        Parameters:
        input_string (str): The English string to be translated to Braille.

        Returns:
        str: The translated Braille string.
        """
        braille_output = []
        number_context = False
        for char in input_string:
            # handle 3 cases: decimal, number, and capital
            if char == ".":
                braille_output.append(self.braille_flags["DECIMAL"])
                continue
            elif char.isdigit() and not number_context:
                braille_output.append(self.braille_flags["NUMBER"])
                braille_output.append(self.english_to_braille.get(char, ""))
                number_context = True
                continue
            elif char.isupper():
                braille_output.append(self.braille_flags["CAPITAL"])
                char = char.lower()

            braille_output.append(self.english_to_braille.get(char, ""))

        return "".join(braille_output)

    def translate_to_english(self, input_string):
        """
        Translate Braille input string to English.

        Parameters:
        input_string (str): The Braille string to be translated to English.

        Returns:
        str: The translated English string.
        """
        english_output = []
        number_next = False
        capital_next = False
        decimal_next = False

        # Ensure input_string length is a multiple of 6
        check = 0
        if len(input_string) % 6 != 0:
            check = len(input_string)

        for i in range(0, (len(input_string) - check), 6):
            braille_char = input_string[i : i + 6]

            if braille_char == "......":  # SPACE
                number_next = False
                english_output.append(" ")
                continue
            elif braille_char == self.braille_flags["CAPITAL"]:
                capital_next = True
                continue
            elif braille_char == self.braille_flags["NUMBER"]:
                number_next = True
                continue
            elif braille_char == self.braille_flags["DECIMAL"]:
                decimal_next = True
                continue

            if number_next:
                english_output.append(self.braille_to_english[braille_char][1])
            elif capital_next:
                english_output.append(self.braille_to_english[braille_char][0].upper())
                capital_next = False
            elif decimal_next:
                english_output.append(".")
                decimal_next = False
            else:
                # Handle the error gracefully
                if braille_char in self.braille_to_english:
                    english_output.append(self.braille_to_english[braille_char][0])
        return "".join(english_output)

    def process_input(self):
        """
        Handle command-line input and direct to the appropriate translation function.
        """
        if len(sys.argv) == 1:
            return
        else:
            input_string = ""
            for arg in sys.argv[1:]:
                input_string += arg + " "
            input_string = input_string.strip()  # Remove the trailing space

            if self.is_braille(input_string):
                translated = self.translate_to_english(input_string)
            else:
                translated = self.translate_to_braille(input_string)

            print(translated)


if __name__ == "__main__":
    translator = BrailleTranslator()
    translator.process_input()
