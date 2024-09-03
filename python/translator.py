import sys

VALID_BRAILLE_CHARS = "O."
BRAILLE_CHAR_LEN = 6

CAPITAL_FOLLOWS = "<CAPITAL>"
NUMBER_FOLLOWS = "<NUMBER>"

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
    CAPITAL_FOLLOWS: ".....O",
    NUMBER_FOLLOWS: ".O.OOO",
    " ": "......",
}
ENGLISH_DIGITS_TO_BRAILLE = {
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
    " ": "......",
}

BRAILLE_TO_ENGLISH = dict((braille, eng) for eng, braille in ENGLISH_TO_BRAILLE.items())
BRAILLE_TO_ENGLISH_DIGITS = dict(
    (braille, eng) for eng, braille in ENGLISH_DIGITS_TO_BRAILLE.items()
)


def is_braille(text: str):
    """Returns True if text is in braille, and False otherwise.
    Text is considered braille if it contains only the characters '.' and 'O'.
    """
    return all(c in VALID_BRAILLE_CHARS for c in text)


class BrailleTranslationError(Exception):
    pass


class BrailleToEnglishTranslator:
    def __init__(self):
        self.i = 0

    def translate(self, text: str):
        """Translates a string of Braille into English."""
        if len(text) % BRAILLE_CHAR_LEN != 0:
            raise BrailleTranslationError(
                f"Invalid input: Braille text must be a multiple of {BRAILLE_CHAR_LEN}."
            )
        self._reset_state()

        translated = ""
        while char := self._read_char(text):
            if char == CAPITAL_FOLLOWS:
                letter = self._read_char(text)
                if letter is None:
                    raise BrailleTranslationError(
                        "Invalid input: trailing capital follows character"
                    )
                translated += letter.upper()
            elif char == NUMBER_FOLLOWS:
                translated += self._read_number(text)
            else:
                translated += char

        return translated

    def _read_char(self, text: str, number: bool = False):
        """Read the next Braille character (chunk of 6 chars).
        Returns None if there is nothing left to read.
        An exception is raised if the Braille character is invalid.
        """
        if self.i >= len(text):
            return None

        braille_char = text[self.i : self.i + BRAILLE_CHAR_LEN]
        if braille_char not in BRAILLE_TO_ENGLISH:
            raise BrailleTranslationError(
                f"Invalid input: Braille character '{braille_char}' does not correspond to any English character."
            )
        self.i += BRAILLE_CHAR_LEN
        if number:
            return BRAILLE_TO_ENGLISH_DIGITS[braille_char]
        else:
            return BRAILLE_TO_ENGLISH[braille_char]

    def _read_number(self, text: str):
        """Reads a number in braille until a space or end of input is encountered.
        An exception is raised if a non-digit character that isn't a space if encountered.
        """
        num = ""
        while char := self._read_char(text, number=True):
            if char == " ":
                num += char
                break

            if not char.isdigit():
                raise BrailleTranslationError(
                    f"Invalid input: expected digit, got '{char}'"
                )

            num += char

        return num

    def _reset_state(self):
        self.i = 0


class EnglishTranslationError(Exception):
    pass


class EnglishToBrailleTranslator:
    def __init__(self):
        self.i = 0

    def translate(self, text: str):
        """Translate a string in English into Braille."""
        self._reset_state()
        translated = ""

        while self.i < len(text):
            char = text[self.i]
            if char.isupper():
                braille_char = ENGLISH_TO_BRAILLE[char.lower()]
                translated += ENGLISH_TO_BRAILLE[CAPITAL_FOLLOWS] + braille_char
                self.i += 1
            # Numbers
            elif char.isdigit():
                translated += ENGLISH_TO_BRAILLE[NUMBER_FOLLOWS] + self._read_number(
                    text
                )
            # Valid character
            elif char in ENGLISH_TO_BRAILLE:
                translated += ENGLISH_TO_BRAILLE[char]
                self.i += 1
            # Invalid character
            else:
                raise EnglishTranslationError(
                    f"Invalid character '{char}', Only letters, numbers and spaces are supported."
                )

        return translated

    def _read_number(self, text: str):
        """Read the next number from the input and convert it into Braille."""
        num = ""
        while self.i < len(text) and text[self.i].isdigit():
            num += ENGLISH_DIGITS_TO_BRAILLE[text[self.i]]
            self.i += 1
        return num

    def _reset_state(self):
        self.i = 0


def main():
    # Read the whole input as a single string
    text = " ".join(sys.argv[1:]).strip()

    if is_braille(text):
        print(BrailleToEnglishTranslator().translate(text))
    else:
        print(EnglishToBrailleTranslator().translate(text))


if __name__ == "__main__":
    main()
