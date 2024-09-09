# Translator
# Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
# For Braille, each character is stored as a series of O (the letter O) or . (a period).
# Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below.
# When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
# When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
# Braille Alphabet
# Letters a through z
# The ability to capitalize letters
# Numbers 0 through 9
# The ability to include spaces ie: multiple words

import sys


class BrailleTranslator:
    BRAILLE_TO_ALPHA = {
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
    }
    BRAILLE_TO_NUM = {
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
    ALPHA_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ALPHA.items()}
    NUM_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_NUM.items()}
    CAPITAL_FOLLOWS = ".....0"
    NUMBER_FOLLOWS = ".0.000"
    SPACE_BRAILLE = "......"

    @staticmethod
    def convert_to_braille(text: str) -> str:
        braille = ""
        new_num = True
        for char in text:
            if char.isalpha():
                if char.isupper():
                    braille += BrailleTranslator.CAPITAL_FOLLOWS
                braille += BrailleTranslator.ALPHA_TO_BRAILLE[char.lower()]
            elif char.isdigit():
                if new_num:
                    braille += BrailleTranslator.NUMBER_FOLLOWS
                    new_num = False
                braille += BrailleTranslator.NUM_TO_BRAILLE[char]
            elif char.isspace():
                braille += BrailleTranslator.SPACE_BRAILLE
                new_num = True
            else:
                raise ValueError(f"Invalid character: {char}")
        return braille

    @staticmethod
    def convert_to_english(braille: str) -> str:
        english = ""
        is_capital = False
        is_number = False
        for i in range(0, len(braille), 6):
            symbol = braille[i : i + 6]
            if symbol == BrailleTranslator.CAPITAL_FOLLOWS:
                is_capital = True
                continue
            elif symbol == BrailleTranslator.NUMBER_FOLLOWS:
                is_number = True
                continue
            elif symbol == BrailleTranslator.SPACE_BRAILLE:
                english += " "
                is_capital = False
                is_number = False
                continue
            elif (
                symbol not in BrailleTranslator.BRAILLE_TO_ALPHA
                and symbol not in BrailleTranslator.BRAILLE_TO_NUM
            ):
                raise ValueError(f"Invalid Braille symbol: {symbol}")

            if is_capital:
                english += BrailleTranslator.BRAILLE_TO_ALPHA[symbol].upper()
                is_capital = False
            elif is_number:
                english += BrailleTranslator.BRAILLE_TO_NUM[symbol]
            else:
                english += BrailleTranslator.BRAILLE_TO_ALPHA[symbol]
        return english

    @staticmethod
    def is_english(text: str) -> bool:
        return any(char.isalpha() for char in text)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python3 translator.py <input>")
        sys.exit(1)

    text = " ".join(args)
    if BrailleTranslator.is_english(text):
        print(BrailleTranslator.convert_to_braille(text))
    else:
        print(BrailleTranslator.convert_to_english(text))


if __name__ == "__main__":
    main()
