import argparse
from typing import Dict, List


# Dictionary mapping Braille characters to English letters, numbers, and symbols
BR_TO_EN: Dict[str, Dict[str, str]] = {
    "LETTERS": {
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
    },
    "NUMS": {
        ".OOOOO": "0",
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
    },
    "SYMBOLS": {
        "......": " ",
        "..OO.O": ".",
        "..O...": ",",
        "..O.OO": "?",
        "..OOO.": "!",
        "..OO..": ":",
        "..O.O.": ";",
        "....OO": "-",
        ".O..O.": "/",
        ".OO..O": "<",
        "O..OO.": ">",
        "O.O..O": "(",
        ".O.OO.": ")",
        ".....O": "^",
        ".O...O": "%",
        ".O.OOO": "#",
    },
}

# swap key value pairs to get braile to english mapping for easier lookup
EN_TO_BR: Dict[str, Dict[str, str]] = {
    category: {v: k for k, v in mapping.items()}
    for category, mapping in BR_TO_EN.items()
}


class Translator:
    def __init__(self, args: List[str]):
        self.input_data = args

    def is_braille(self) -> bool:
        """
        Function to check if the input text is valid Braille or English

        @param text: The input string to check
        @return: True if the text is valid Braille, False if not
        """

        text = "".join(self.input_data)

        # ensure the text is composed of proper braile chunks
        if len(text) % 6 != 0:
            return False

        # Combine all Braille character mappings for cleaner code
        braille_set = (
            set(BR_TO_EN["LETTERS"]) | set(BR_TO_EN["NUMS"]) | set(BR_TO_EN["SYMBOLS"])
        )

        # Validate each 6-character Braille sequence.
        return all(text[i : i + 6] in braille_set for i in range(0, len(text), 6))

    def convert_to_english(self) -> str:
        """
        Method to convert a string from Braille to English
        @param text: A string of braille represented by '.' and 'O'
        @return: The translated English string
        """
        output = []
        is_capital = is_number = False
        braille_text = "".join(self.input_data)

        braille_chars = [
            braille_text[i : i + 6] for i in range(0, len(braille_text), 6)
        ]  # create chunks of 6 characters

        for braille in braille_chars:

            # detect capitalization
            if braille == EN_TO_BR["SYMBOLS"]["^"]:
                is_capital = True

            # detect number mode
            elif braille == EN_TO_BR["SYMBOLS"]["#"]:
                is_number = True

            # add period
            elif braille == EN_TO_BR["SYMBOLS"]["%"]:
                output.append(".")

            # add number
            elif is_number and braille in BR_TO_EN["NUMS"]:
                output.append(BR_TO_EN["NUMS"][braille])

            # add capital letter
            elif is_capital and braille in BR_TO_EN["LETTERS"]:
                output.append(BR_TO_EN["LETTERS"][braille].upper())
                is_capital = False

            # add lowercase letter
            elif braille in BR_TO_EN["LETTERS"]:
                output.append(BR_TO_EN["LETTERS"][braille])

            # add space
            elif braille == EN_TO_BR["SYMBOLS"][" "]:
                output.append(" ")
                is_number = False

            # add special symbol
            elif braille in BR_TO_EN["SYMBOLS"]:
                output.append(BR_TO_EN["SYMBOLS"][braille])

        return "".join(output)

    def convert_to_braille(self) -> str:
        """
        Method to convert a string from English to Braille
        @param text_list: List of english strings
        @return: Translated Braille string represented by '.' and 'O'
        """
        output = []
        is_number = False
        english_text = " ".join(self.input_data)

        for char in english_text:

            # if number and not in number mode prepend number symbol
            if char.isnumeric() and not is_number:
                output.append(EN_TO_BR["SYMBOLS"]["#"])
                is_number = True

            # Convert the number to Braille equivalent
            if char.isnumeric() and is_number:  #
                output.append(EN_TO_BR["NUMS"][char])

            # Add space and turn number mode False
            elif char == " ":
                output.append(EN_TO_BR["SYMBOLS"][" "])
                is_number = False

            # Convert alphabetic characters to Braille
            elif char.isalpha():
                if char.isupper():
                    output.append(EN_TO_BR["SYMBOLS"]["^"])
                output.append(EN_TO_BR["LETTERS"][char.lower()])

            # convert special symbols
            else:
                output.append(EN_TO_BR["SYMBOLS"].get(char.lower(), ""))

        return "".join(output)

    def translate(self):
        """
        Method to translate from English to Braille or vice versa
        @return: The translated string
        """
        return (
            self.convert_to_english()
            if self.is_braille()
            else self.convert_to_braille()
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument(
        "arguments", nargs="+", help="One or more arguments are required"
    )
    args_list = parser.parse_args().arguments

    translator = Translator(args_list)
    translated = translator.translate()
    print(translated)
