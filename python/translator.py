"""
This script is a braille translator that allows a user
to translate from Braille to English or vice versa
"""

import sys


class Translator:
    """Translate from braille to english or vice versa"""

    braille_letters = {
        # English letters
        "O.....": "A",
        "O.O...": "B",
        "OO....": "C",
        "OO.O..": "D",
        "O..O..": "E",
        "OOO...": "F",
        "OOOO..": "G",
        "O.OO..": "H",
        ".OO...": "I",
        ".OOO..": "J",
        "O...O.": "K",
        "O.O.O.": "L",
        "OO..O.": "M",
        "OO.OO.": "N",
        "O..OO.": "O",
        "OOO.O.": "P",
        "OOOOO.": "Q",
        "O.OOO.": "R",
        ".OO.O.": "S",
        ".OOOO.": "T",
        "O...OO": "U",
        "O.O.OO": "V",
        ".OOO.O": "W",
        "OO..OO": "X",
        "OO.OOO": "Y",
        "O..OOO": "Z",
        # Space
        "......": " ",
    }

    braille_numbers = {
        # Digits (numbers follow the number sign)
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
        # Space
        "......": " ",
    }

    # Special characters dictionary
    special_chars_to_braille = {
        ".": "..OO.O",  # Period
        ",": "..O...",  # Comma
        "?": "..O.OO",  # Question mark
        "!": "..OOO.",  # Exclamation mark
        ":": "..OO..",  # Colon
        ";": "..O.O.",  # Semicolon
        "-": "....OO",  # Hyphen
        "/": ".O..O.",  # Slash
        "<": ".OO..O",  # Less than
        ">": "O..OO.",  # Greater than
        "(": "O.O..O",  # Left parenthesis
        ")": ".O.OO.",  # Right parenthesis
    }

    # Reverse mapping for English & Numbers to Braille
    english_to_braille = {v: k for k, v in braille_letters.items()}
    english_to_braille_numbers = {v: k for k, v, in braille_numbers.items()}
    braille_to_special_chars = {v: k for k, v, in special_chars_to_braille.items()}

    # Follow on special symbols
    capital_sign = ".....O"
    number_sign = ".O.OOO"  # Number sign
    decimal_sign = ".O...O"  # Decimal point sign
    space_braille = "......"

    def translate_to_english(self, braille):
        """
        Translates Braille text to English text.

        Args:
            braille (str): inputted braille text

        Returns:
            english_output (str): english text

        """
        braille_chars = [braille[i : i + 6] for i in range(0, len(braille), 6)]
        english_output = ""
        is_number = False  # To track if we're decoding numbers
        is_capital = False  # To track if the next character is capital

        for char in braille_chars:
            if char == self.number_sign:
                is_number = True
                continue
            if char == self.decimal_sign:
                # english_output += "."
                is_number = True  # Assume numbers follow after a decimal
                continue
            if char == self.capital_sign:
                is_capital = True
                continue
            if char == self.space_braille:
                english_output += " "
                is_number = False  # Reset number mode after space
                continue

            if is_number:
                number = self.braille_numbers.get(char)
                if number:
                    english_output += number
                else:
                    english_output += self.braille_to_special_chars.get(char)
            else:
                letter = self.braille_letters.get(char)
                if letter:
                    if is_capital:
                        letter = letter.upper()
                        is_capital = False
                    else:
                        letter = letter.lower()
                    english_output += letter
                else:
                    english_output += self.braille_to_special_chars.get(char, "?")

        return english_output

    def translate_to_braille(self, english):
        """
        Translates English text to Braille text.

        Args:
            english (str): inputted english string

        Returns:
            braille_output (str): braille string
        """

        braille_output = ""
        is_number = False

        i = 0
        while i < len(english):
            char = english[i]

            if char == " ":
                # Add space in Braille
                braille_output += self.space_braille
                is_number = False  # Reset number mode after space
            elif char in self.special_chars_to_braille:
                # Add special characters
                braille_output += self.special_chars_to_braille[char]
            elif char.isdigit():
                # Determine if it's a number with or without a decimal
                if not is_number:
                    # Check ahead to see if a decimal exists
                    # before the next space or letter
                    next_characters = english[i:]
                    if "." in next_characters.split()[0]:
                        # If there is a decimal, add the decimal sign
                        braille_output += self.decimal_sign
                    else:
                        # Otherwise, use the number sign
                        braille_output += self.number_sign
                    is_number = True

                # Add corresponding Braille digit
                braille_output += self.english_to_braille_numbers[char]
            elif char.isalpha():
                if char.isupper():
                    # Add capital sign for uppercase letters
                    braille_output += self.capital_sign
                # Add corresponding Braille letter (uppercase or lowercase)
                braille_output += self.english_to_braille[char.upper()]
                # Reset number mode when switching back to letters
                is_number = False
            else:
                raise ValueError(f"Unrecognized character: '{char}'")

            i += 1

        return braille_output


def translate_input():
    """
    Main function to take a user's input and print out the translation (either
    from braille to english or vice versa)
    """
    translator = Translator()

    if len(sys.argv) < 2:
        print("Please provide an input for translation")
        return

    user_input = " ".join(sys.argv[1:])

    if all(x in "O." for x in user_input):
        translation = translator.translate_to_english(user_input)
    else:
        translation = translator.translate_to_braille(user_input)

    print(translation)


if __name__ == "__main__":
    translate_input()
