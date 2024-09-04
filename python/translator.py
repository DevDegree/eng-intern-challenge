import sys


class Translator:
    _BRAILLE_READ_LEN = 6
    _DEFAULT_MAP_VAL = ""

    BRAILLE_CAPITALIZE_FOLLOWS = ".....O"
    BRAILLE_NUMBER_FOLLOWS = ".O.OOO"
    BRAILLE_SPACE_FOLLOWS = "......"

    ALPHA_ENG_TO_BRAILLE_MAP = {
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
    }

    def __init__(self) -> None:
        pass

    def _get_number_encoding(self, char: str) -> str:
        """Converts a number (0-9) to its corresponding letter (a-j) and vice versa.

        The symbols for 1-9 is the same as the symbols for a-i. Thus, we can obtain the number's
        unicode value, using `ord()`, offset by the unicode for 0. This allows us to to obtain
        the mapping between numbers and letters. We also specially handle "j" and "0"
        as `ord("j") != ord("0") == ord(":")`.
        """
        offset = ord("0")
        unicode = ord(char)

        if char.isnumeric():
            as_letter = (
                chr(unicode + offset) if unicode in range(ord("1"), ord(":")) else "j"
            )

            return as_letter

        as_number = (
            chr(unicode - offset) if unicode in range(ord("a"), ord("j")) else "0"
        )

        return as_number

    def _is_braille(self, input_str: str) -> bool:
        """Checks to see if the text is Braille.
        - Could use better checks but we assume length and character sets are valid.
        """
        chunkable = len(input_str) % self._BRAILLE_READ_LEN == 0
        all_zero_dots = set(input_str) == set("O.")
        return chunkable and all_zero_dots

    def translate(self, input_str: str) -> str:
        """Converts a string from English to Braille, or vice versa.
        We assume the English and Braille can only consist of the
        alphanumeric values [Aa-Zz][0-9], including whitespaces.
        The Braille text should consists of only `O`s and `.` alongside
        additional symbols that denote capitalization and whitespace.

        Args:
            input_str (str): the string to be translated.

        Returns:
            str: the translated string.
        """
        return (
            self.translate_braille_to_eng(input_str)
            if self._is_braille(input_str)
            else self.translate_eng_to_braille(input_str)
        )

    def translate_eng_to_braille(self, input_str: str) -> str:
        """Converts a string from English to Braille.

        Args:
            input_str (str): the string to be translated.

        Returns:
            str: the translated string.
        """
        encoding = []

        encoding_number = False

        for char in input_str:

            if char == " ":
                encoding_number = False
                encoding.append(self.BRAILLE_SPACE_FOLLOWS)
                continue

            if char.isnumeric():
                char = self._get_number_encoding(char)

                if not encoding_number:
                    encoding_number = True
                    encoding.append(self.BRAILLE_NUMBER_FOLLOWS)

            if char.isupper():
                encoding.append(self.BRAILLE_CAPITALIZE_FOLLOWS)
                char = char.lower()

            encoding.append(
                self.ALPHA_ENG_TO_BRAILLE_MAP.get(char, self._DEFAULT_MAP_VAL)
            )

        return "".join(encoding)

    def translate_braille_to_eng(self, input_str: str) -> str:
        """Converts a string from Braille to English.

        Args:
            input_str (str): the string to be translated.

        Returns:
            str: the translated string.
        """
        chars = []

        is_number = capitalize = False

        ALPHA_BRAILLE_TO_ENG_MAP = {
            enc: char for char, enc in self.ALPHA_ENG_TO_BRAILLE_MAP.items()
        }

        for i in range(0, len(input_str), self._BRAILLE_READ_LEN):
            token = input_str[i : i + self._BRAILLE_READ_LEN]

            if token == self.BRAILLE_SPACE_FOLLOWS:
                is_number = False
                chars.append(" ")

            elif token == self.BRAILLE_NUMBER_FOLLOWS:
                is_number = True

            elif token == self.BRAILLE_CAPITALIZE_FOLLOWS:
                capitalize = True

            else:
                char = ALPHA_BRAILLE_TO_ENG_MAP.get(token, self._DEFAULT_MAP_VAL)

                if is_number:
                    char = self._get_number_encoding(char)

                elif capitalize:
                    char = char.capitalize()
                    capitalize = False

                chars.append(char)

        return "".join(chars)


def main():
    input_str = " ".join(sys.argv[1:])
    translator = Translator()
    print(translator.translate(input_str))


if __name__ == "__main__":
    main()
