import argparse

ALPHA_TO_BRAILLE = {
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

BRAILLE_TO_ALPHA = {v: k for k, v in ALPHA_TO_BRAILLE.items()}

NUM_TO_BRAILLE = {
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

BRAILLE_TO_NUM = {v: k for k, v in NUM_TO_BRAILLE.items()}

# Assume only the next symbol is capital
CAPITAL_FOLLOWS = ".....O"

# Assume all following symbols are numbers until the next space symbol
NUMBER_FOLLOWS = ".O.OOO"

SPACE = "......"


class InvalidInputError(Exception):
    """Error for invalid input text."""

    # For characters like '<'
    def __init__(self, text: str, length: int):
        self.text = text
        self.length = length
        super().__init__(f"Invalid input text: '{text}' with length {length}.")


class UnknownBrailleError(Exception):
    """Error for any unknown or unsupported Braille characters."""

    def __init__(self, char: str):
        self.char = char
        super().__init__(f"Unknown or Unsupported Braille: {self.char}")


class BrailleTranslator:
    """
    Provides English to Braille translations, and vice versa.
    """

    def __init__(self, text: str):
        self.text = text

    def _valid_braille(self):
        """
        Checks if the input is valid Braille.

        For Braille, the length of the input must be a multiple of six.
        """
        if (len(self.text) % 6) != 0:
            raise InvalidInputError(self.text, len(self.text))

    def _detect_braille(self) -> bool:
        """Detects if the inputted text is Braille."""

        for char in self.text:
            if char in ALPHA_TO_BRAILLE or char in NUM_TO_BRAILLE:
                return False

        self._valid_braille()

        first_char = self.text[:6]

        if (
            first_char in BRAILLE_TO_ALPHA
            or first_char in BRAILLE_TO_NUM
            or first_char == CAPITAL_FOLLOWS
            or first_char == NUMBER_FOLLOWS
            or first_char == SPACE
        ):
            return True
        else:
            raise UnknownBrailleError(first_char)

    def b2e(self) -> str:
        """Translates the input Braille text to English."""

        # Split the text into strings of length 6 to get the braille characters
        braille = [self.text[i : i + 6] for i in range(0, len(self.text), 6)]
        english = []
        capital_follows = False
        number_follows = False

        # Ignore unsupported characters instead of outputting an error
        for char in braille:
            if char == CAPITAL_FOLLOWS:
                capital_follows = True
                continue
            elif char == NUMBER_FOLLOWS:
                number_follows = True
                continue
            elif char == SPACE:
                english.append(" ")
                number_follows = False
                continue

            if number_follows:
                english.append(BRAILLE_TO_NUM.get(char, ""))
            else:
                translated_char = BRAILLE_TO_ALPHA.get(char, "")
                if translated_char and capital_follows:
                    translated_char = translated_char.upper()
                    capital_follows = False
                english.append(translated_char)

        return "".join(english)

    def e2b(self) -> str:
        """Translates the input English text to Braille."""

        english = ""

        for char in self.text:
            if char.isalpha():
                if char.isupper():
                    english += CAPITAL_FOLLOWS

                english += ALPHA_TO_BRAILLE[char.lower()]

            elif char.isnumeric():
                english += NUMBER_FOLLOWS
                english += NUM_TO_BRAILLE[char]

            elif char.isspace():
                english += SPACE

        return english

    def translate(self) -> str:
        """Translates the input text based on its type (Braille or English)."""
        if self._detect_braille():
            return self.b2e()
        else:
            return self.e2b()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="English to Braille translations, and vice versa."
    )
    parser.add_argument("text", nargs=argparse.REMAINDER, help="The text to translate")

    args = parser.parse_args()

    text = " ".join(args.text)
    translator = BrailleTranslator(text)

    try:
        translated = translator.translate()
        print(translated)
    except (InvalidInputError, UnknownBrailleError) as e:
        print(e)
