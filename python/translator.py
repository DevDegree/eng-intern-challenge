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

    NUM_ENG_TO_BRAILLE_MAP = {
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

    def __init__(self) -> None:
        pass

    def _is_braille(self, input_str: str) -> bool:
        """Checks to see if the text is braille.
        - Could use better checks but we assume length character sets are valid.
        """
        chunkable = len(input_str) % self._BRAILLE_READ_LEN == 0
        all_zero_dots = set(input_str) == set("O.")
        return chunkable and all_zero_dots

    def translate(self, input_str: str) -> str:
        """Converts a string from English to Braille, or vice versa.
        We assume the English and Braille can only consist of the
        alphanumeric values [Aa-Zz][0-9], including whitespaces.
        The Braille text should consists of only `O`s and `.` alongisde
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

            if char.isnumeric() and not encoding_number:
                encoding_number = True
                encoding.append(self.BRAILLE_NUMBER_FOLLOWS)

            if char.isupper():
                encoding.append(self.BRAILLE_CAPITALIZE_FOLLOWS)
                char = char.lower()

            encoding.append(
                self.NUM_ENG_TO_BRAILLE_MAP.get(char, self._DEFAULT_MAP_VAL)
                if encoding_number
                else self.ALPHA_ENG_TO_BRAILLE_MAP.get(char, self._DEFAULT_MAP_VAL)
            )

        return "".join(encoding)

    def translate_braille_to_eng(self, input_str: str) -> str:
        """Converts a string from Braille to English.

        Args:
            input_str (str): the string to be translated.

        Returns:
            str: the translated string.
        """
        words = []

        is_number = capitalize = False

        ALPHA_BRAILLE_TO_ENG_MAP = {
            enc: word for word, enc in self.ALPHA_ENG_TO_BRAILLE_MAP.items()
        }

        NUM_BRAILLE_TO_ENG_MAP = {
            enc: num for num, enc in self.NUM_ENG_TO_BRAILLE_MAP.items()
        }

        for i in range(0, len(input_str), self._BRAILLE_READ_LEN):
            token = input_str[i : i + self._BRAILLE_READ_LEN]

            if token == self.BRAILLE_SPACE_FOLLOWS:
                is_number = False
                words.append(" ")

            elif token == self.BRAILLE_NUMBER_FOLLOWS:
                is_number = True

            elif token == self.BRAILLE_CAPITALIZE_FOLLOWS:
                capitalize = True

            else:
                word = (
                    NUM_BRAILLE_TO_ENG_MAP.get(token, self._DEFAULT_MAP_VAL)
                    if is_number
                    else ALPHA_BRAILLE_TO_ENG_MAP.get(token, self._DEFAULT_MAP_VAL)
                )

                if not is_number and capitalize:
                    word = word.capitalize()
                    capitalize = False

                words.append(word)

        return "".join(words)


def main():
    input_str = " ".join(sys.argv[1:])
    translator = Translator()
    print(translator.translate(input_str))


if __name__ == "__main__":
    main()
