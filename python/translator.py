import sys

NUMBER_FOLLOWS = ".O.OOO"
CAPITAL_FOLLOWS = ".....O"

ALPHABETS_TO_BRAILLE = {
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
    " ": "......",
}

NUMBERS_TO_BRAILLE = {
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

BRAILLE_TO_ALPHABETS = {v: k for k, v in ALPHABETS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}


class BrailleTranslator:
    """
    A class to translate between English and Braille strings.

    Attributes:
        input_string (str): The string to be translated
    """

    def __init__(self, input_string):
        """
        Initializes the BrailleTranslator with the input string

        Args:
            input_string (str): The input string from command
        """
        self.input_string = input_string

    def is_braille(self):
        """
        Determines if the input string is in Braille.

        Returns:
            bool: True if the string is in Braille, False otherwise.
        """
        return all(char in "O." for char in self.input_string)

    def braille_to_english(self):
        """
        Converts a Braille string to English

        Returns:
            str: The translated English string
        """
        result = []
        number_flag = False
        capital_flag = False
        for i in range(0, len(self.input_string), 6):
            char = self.input_string[i : i + 6]
            if char == NUMBER_FOLLOWS:
                number_flag = True
                continue
            if char == CAPITAL_FOLLOWS:
                capital_flag = True
                continue
            if BRAILLE_TO_ALPHABETS[char] == " ":
                number_flag = False
            if number_flag:
                result.append(BRAILLE_TO_NUMBERS[char])
            elif char in BRAILLE_TO_ALPHABETS:
                if capital_flag:
                    result.append(BRAILLE_TO_ALPHABETS[char].upper())
                    capital_flag = False
                else:
                    result.append(BRAILLE_TO_ALPHABETS[char])

        return "".join(result)

    def english_to_braille(self):
        """
        Converts an English string to Braille string

        Returns:
            str: The translated Braille string
        """
        result = []
        add_number_indicator = False
        for char in self.input_string:
            if char.isdigit():
                if not add_number_indicator:
                    result.append(NUMBER_FOLLOWS)
                    add_number_indicator = True
                result.append(NUMBERS_TO_BRAILLE[char])
            elif char == " ":
                add_number_indicator = False
                result.append(ALPHABETS_TO_BRAILLE[char])
            elif char.isalpha():
                if char.isupper():
                    result.append(CAPITAL_FOLLOWS)
                result.append(ALPHABETS_TO_BRAILLE[char.lower()])

        return "".join(result)

    def translate(self):
        """
        Translates the input string between Braille and English

        Returns:
            str: The translated string in the opposite language, Braille-English or vise versa.
        """
        if self.is_braille():
            return self.braille_to_english()
        else:
            return self.english_to_braille()


def main():
    """
    The main function processes command line arguments and calls translation to print the result.
    """
    if len(sys.argv) < 2:
        return
    argument_list = " ".join(sys.argv[1:])
    translator = BrailleTranslator(argument_list)
    print(translator.translate())


if __name__ == "__main__":
    main()
