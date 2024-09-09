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
        "0.....": "a",
        "0.0...": "b",
        "00....": "c",
        "00.0..": "d",
        "0..0..": "e",
        "000...": "f",
        "0000..": "g",
        "0.00..": "h",
        ".00...": "i",
        ".000..": "j",
        "0...0.": "k",
        "0.0.0.": "l",
        "00..0.": "m",
        "00.00.": "n",
        "0..00.": "o",
        "000.0.": "p",
        "00000.": "q",
        "0.000.": "r",
        ".00.0.": "s",
        ".0000.": "t",
        "0...00": "u",
        "0.0.00": "v",
        ".000.0": "w",
        "00..00": "x",
        "00.000": "y",
        "0..000": "z",
    }
    BRAILLE_TO_NUM = {
        "0.....": "1",
        "0.0...": "2",
        "00....": "3",
        "00.0..": "4",
        "0..0..": "5",
        "000...": "6",
        "0000..": "7",
        "0.00..": "8",
        ".00...": "9",
        ".000..": "0",
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
