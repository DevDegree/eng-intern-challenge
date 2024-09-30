import sys
from enum import Enum


class Translator:
    """
    Handles the translation of text between Braille and English

    Dictionaries of translations are all self-contained within the class
    """

    class State(Enum):
        """Helper enum class to track the state of translation"""

        INIT = 0
        NUMBER_FOLLOWING = 1
        CAPITAL_FOLLOWING = 2

    CAPITAL_FOLLOWS = "capital follows"
    DECIMAL_FOLLOWS = "decimal follows"
    NUMBER_FOLLOWS = "number follows"
    NUMBER_SEPARATOR = " "
    NUM_CHARS_IN_BRAILLE = 6

    ENGLISH_TO_BRAILLE = {
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
        "^": ".....O",
        "#": ".O.OOO",
        " ": "......",
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        "(": "O.O..O",
        ")": ".O.OO.",
        CAPITAL_FOLLOWS: ".....O",
        DECIMAL_FOLLOWS: ".O...O",
        NUMBER_FOLLOWS: ".O.OOO",
    }

    NUMBER_TO_BRAILLE = {
        "1": ENGLISH_TO_BRAILLE["a"],
        "2": ENGLISH_TO_BRAILLE["b"],
        "3": ENGLISH_TO_BRAILLE["c"],
        "4": ENGLISH_TO_BRAILLE["d"],
        "5": ENGLISH_TO_BRAILLE["e"],
        "6": ENGLISH_TO_BRAILLE["f"],
        "7": ENGLISH_TO_BRAILLE["g"],
        "8": ENGLISH_TO_BRAILLE["h"],
        "9": ENGLISH_TO_BRAILLE["i"],
        "0": ENGLISH_TO_BRAILLE["j"],
    }

    BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}

    def __init__(self, text_to_translate: str) -> None:
        """Constructs a translator with the given text to translate"""
        self.text_to_translate = text_to_translate

    def set_text_to_translate(self, text_to_translate: str) -> None:
        """Sets the text to translate to the provided argument"""
        self.text_to_translate = text_to_translate

    def translate(self) -> str:
        """
        Returns the text the translate current contains translated.
        Will automatically detect the source and destination language.
        """
        if self.is_braille(self.text_to_translate):
            return self.braille_to_english(self.text_to_translate)
        return self.english_char_to_braille(self.text_to_translate)

    def braille_to_english(self, braille_text: str) -> str:
        """Translates the given Braille text to English"""
        state = Translator.State.INIT
        english_text = ""

        for i in range(0, len(braille_text), Translator.NUM_CHARS_IN_BRAILLE):
            braille_char = braille_text[i : i + Translator.NUM_CHARS_IN_BRAILLE]

            # Transition state
            if Translator.BRAILLE_TO_ENGLISH[braille_char] == Translator.NUMBER_FOLLOWS:
                state = Translator.State.NUMBER_FOLLOWING
                continue
            elif (
                Translator.BRAILLE_TO_ENGLISH[braille_char]
                == Translator.CAPITAL_FOLLOWS
            ):
                state = Translator.State.CAPITAL_FOLLOWING
                continue

            # Translate char based on state
            char_to_write = Translator.BRAILLE_TO_ENGLISH[braille_char]

            if state == Translator.State.CAPITAL_FOLLOWING:
                char_to_write = char_to_write.upper()
                state = Translator.State.INIT
            elif state == Translator.State.NUMBER_FOLLOWING:
                if (
                    Translator.BRAILLE_TO_ENGLISH[braille_char]
                    == Translator.NUMBER_SEPARATOR
                ):
                    state = Translator.State.INIT
                    char_to_write = Translator.NUMBER_SEPARATOR
                else:
                    char_to_write = Translator.BRAILLE_TO_NUMBER[braille_char]

            english_text += char_to_write
        return english_text

    def english_char_to_braille(self, english_text: str) -> str:
        """Translates the given English text to Braille"""
        state = Translator.State.INIT
        braille_text = ""

        for char in english_text:
            if char.isupper():
                braille_text += Translator.ENGLISH_TO_BRAILLE[
                    Translator.CAPITAL_FOLLOWS
                ]
                braille_text += Translator.ENGLISH_TO_BRAILLE[char.lower()]
            elif char.isnumeric():
                if state != Translator.State.NUMBER_FOLLOWING:
                    state = Translator.State.NUMBER_FOLLOWING
                    braille_text += Translator.ENGLISH_TO_BRAILLE[
                        Translator.NUMBER_FOLLOWS
                    ]
                braille_text += Translator.NUMBER_TO_BRAILLE[char]
            else:
                if state == Translator.State.NUMBER_FOLLOWING:
                    state = Translator.State.INIT
                    braille_text += Translator.ENGLISH_TO_BRAILLE[" "]
                else:
                    braille_text += Translator.ENGLISH_TO_BRAILLE[char.lower()]

        return braille_text

    def is_braille(self, text: str) -> bool:
        """Returns whether the string provided is Braille"""
        for char in text:
            if char not in ["O", "."]:
                return False
        return True


def main():
    if len(sys.argv) < 2:
        raise IndexError("The programm must supply the text to translate")

    text_to_translate = " ".join(sys.argv[1:])
    translator = Translator(text_to_translate=text_to_translate)
    print(translator.translate())


if __name__ == "__main__":
    main()
