import sys


class Translator:
    NUMBER_INDICATOR = "_NUMBER_INDICATOR"
    CAPITAL_INDICATOR = "_CAPITAL_INDICATOR"
    DECIMAL_INDICATOR = "_DECIMAL_INDICATOR"

    BRAILLE_TO_CHAR = {
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

    BRAILLE_TO_NUMBER = {
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

    BRAILLE_TO_SYMBOL = {
        "..O...": ".",
        "..OO.O": ",",
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
        "......": " ",
    }

    BRAILLE_TO_INDICATOR = {
        ".O.OOO": NUMBER_INDICATOR,
        ".....O": CAPITAL_INDICATOR,
        ".O...O": DECIMAL_INDICATOR,
    }

    CHAR_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_CHAR.items()}
    NUMBER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBER.items()}
    SYMBOL_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_SYMBOL.items()}
    INDICATOR_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_INDICATOR.items()}

    @classmethod
    def translate(cls, string: str) -> str:
        """
        Translates a string to the "other" language.
        English -> Braille
        Braille -> English
        """
        if cls.is_braille_precheck(string):
            try:
                # This might fail if a sequence of braille characters is not valid english
                return cls.to_english(string)
            except Exception as _:
                # It is a sequence of braille characters, but cannot be converted to english.
                # We treate this as an english string of `O`s and `.`s and convert it to braille
                pass

        return cls.to_braille(string)

    @classmethod
    def is_braille_precheck(cls, string: str) -> bool:
        """
        Note that this does not guarantee that the string is valid braille, translation may still fail.

        Preconditions for checking if a string is braille:
        - String must be a multiple of 6 characters long
        - Each character must be `O` or `.`
        """
        if len(string) % 6 != 0:
            return False

        for char in string:
            if char not in [".", "O"]:
                return False

        return True

    @classmethod
    def to_english(cls, string: str) -> str:
        """
        Convert the given string to english.

        Raises:
            ValueError: If the string cannot be converted to english.
        """
        result = ""

        number_flag = False
        capital_flag = False

        for idx in range(0, len(string), 6):
            braille_window = string[idx : idx + 6]

            # Valid number, stay with number flag
            if number_flag and braille_window in cls.BRAILLE_TO_NUMBER:
                result += cls.BRAILLE_TO_NUMBER[braille_window]
            # Number flag is set, but `braille_window` is not a number
            elif number_flag:
                raise ValueError(f"Not a braille number: {braille_window}")
            # Valid indicator, set flag
            elif braille_window in cls.BRAILLE_TO_INDICATOR:
                indicator = cls.BRAILLE_TO_INDICATOR[braille_window]
                if indicator == cls.NUMBER_INDICATOR:
                    number_flag = True
                elif indicator == cls.CAPITAL_INDICATOR:
                    capital_flag = True
                # DECIMAL_INDICATOR is not documented in the challenge
                elif indicator == cls.DECIMAL_INDICATOR:
                    pass
            # Valid character, add to result depending on capital flag
            elif braille_window in cls.BRAILLE_TO_CHAR:
                char = cls.BRAILLE_TO_CHAR[braille_window]
                result += char.upper() if capital_flag else char
                # Reset capital flag after use
                capital_flag = False
            # Valid symbol, add to result
            elif braille_window in cls.BRAILLE_TO_SYMBOL:
                symbol = cls.BRAILLE_TO_SYMBOL[braille_window]
                result += symbol
                # Reset number flag after a space
                if symbol == " ":
                    number_flag = False
            else:
                raise ValueError(f"Not a valid braille window: {braille_window}")

        return result

    @classmethod
    def to_braille(cls, string: str) -> str:
        """
        Convert the given string to braille.

        Raises:
            ValueError: If the string cannot be converted to braille.
        """
        result = ""

        number_flag = False

        for char in string:
            if char.isspace():
                result += cls.SYMBOL_TO_BRAILLE[char]
                number_flag = False
            elif char.isdigit():
                if not number_flag:
                    number_flag = True
                    result += cls.INDICATOR_TO_BRAILLE[cls.NUMBER_INDICATOR]
                result += cls.NUMBER_TO_BRAILLE[char]
            elif char.isupper() and char.lower() in cls.CHAR_TO_BRAILLE:
                result += cls.INDICATOR_TO_BRAILLE[cls.CAPITAL_INDICATOR]
                result += cls.CHAR_TO_BRAILLE[char.lower()]
            elif char in cls.CHAR_TO_BRAILLE:
                result += cls.CHAR_TO_BRAILLE[char]
            elif char in cls.SYMBOL_TO_BRAILLE:
                result += cls.SYMBOL_TO_BRAILLE[char]
            else:
                raise ValueError(f"Not a valid character: {char}")

        return result


def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate")
        sys.exit(1)

    to_translate = " ".join(sys.argv[1:])
    result = Translator.translate(to_translate)
    print(result)


if __name__ == "__main__":
    main()
