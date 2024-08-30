import sys


class BrailleMapping:
    """Maps Braille symbols to their correspoding English characters and vice-versa."""

    NUMBER_FOLLOWS: str = ".O.OOO"
    CAPITAL_FOLLOWS: str = ".....O"

    ENGLISH_TO_BRAILLE_CHARS: dict[str, str] = {
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

    # TODO: check if other characters need to be included
    BRAILLE_TO_ENGLISH_CHARS: dict[str, str] = {
        v: k for k, v in ENGLISH_TO_BRAILLE_CHARS.items()
    }

    ENGLISH_TO_BRAILLE_NUMBERS = {
        "0": ".OOO..",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
    }

    BRAILLE_TO_ENGLISH_NUMBERS: dict[str, str] = {
        v: k for k, v in ENGLISH_TO_BRAILLE_NUMBERS.items()
    }

    @staticmethod
    def get_braille(char: str, is_number: bool = False) -> str:
        if is_number:
            return BrailleMapping.ENGLISH_TO_BRAILLE_NUMBERS[char]
        elif char.isupper():
            return (
                BrailleMapping.CAPITAL_FOLLOWS
                + BrailleMapping.ENGLISH_TO_BRAILLE_CHARS[char.lower()]
            )
        else:
            return BrailleMapping.ENGLISH_TO_BRAILLE_CHARS[char]

    @staticmethod
    def get_english(braille: str, is_number: bool = False, is_caps=False) -> str:
        if is_number:
            return BrailleMapping.BRAILLE_TO_ENGLISH_NUMBERS[braille]
        elif is_caps:
            return BrailleMapping.BRAILLE_TO_ENGLISH_CHARS[braille].upper()
        else:
            return BrailleMapping.BRAILLE_TO_ENGLISH_CHARS[braille]


class Translator:
    """Translator for Braille text to English and vice-versa."""

    @staticmethod
    def english_to_braille(text: str) -> str:
        """Return the translation of the English text to Braille.

        args:
            - text: the English text to be translated
        """
        # no set way to handle 1212HDHBH
        words = text.split(" ")
        braille_words = []
        for word in words:
            braille_word = []
            is_number = word.isnumeric()
            if is_number:
                braille_word.append(BrailleMapping.NUMBER_FOLLOWS)

            for c in word:
                braille_word.append(BrailleMapping.get_braille(c, is_number=is_number))
            braille_words.append("".join(braille_word))

        return BrailleMapping.get_braille(" ").join(braille_words)

    @staticmethod
    def braille_to_english(text: str) -> str:
        """Return the translation of the Braille text to English.

        text must be a valid Braille encoding.

        args:
            - text: the Braille text to be translated
        """


class InputTypeClassifier:
    """Identifies whether a string is Braille or English."""

    @staticmethod
    def is_braille(text: str) -> bool:
        return "." in text


def main():
    input = " ".join(sys.argv[1:])

    print(sys.argv[1:])
    if InputTypeClassifier.is_braille(input):
        translated = Translator.braille_to_english(input)
    else:
        translated = Translator.english_to_braille(input)

    print(translated)


if __name__ == "__main__":
    main()
