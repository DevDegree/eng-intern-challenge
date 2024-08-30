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
        """Convert an English character to its corresponding Braille encoding.

        Args:
            char (str): The English character to convert.
            is_number (bool, optional): Flag indicating if the character is a number. Defaults to False.

        Returns:
            str: The Braille representation of the given character.
        """
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
        """Convert a Braille encoding to its corresponding English character.

        Args:
            braille (str): The Braille encoding to convert.
            is_number (bool, optional): Flag indicating if the Braille encoding represents a number. Defaults to False.
            is_caps (bool, optional): Flag indicating if the character is uppercase. Defaults to False.

        Returns:
            str: The English character corresponding to the Braille encoding.
        """
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
        """Translate English text to Braille.

        Args:
            text (str): The English text to translate.

        Returns:
            str: The Braille translation of the given text.
        """
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
        """Translate Braille text to English.

        Args:
            text (str): The Braille text to translate.

        Returns:
            str: The English translation of the given Braille text.
        """
        BRAILLE_LENGTH = 6
        english_characters = []
        is_number = False
        is_caps = False

        for i in range(0, len(text), BRAILLE_LENGTH):
            braille = text[i : i + BRAILLE_LENGTH]
            if braille == BrailleMapping.NUMBER_FOLLOWS:
                is_number = True
                continue
            if braille == BrailleMapping.CAPITAL_FOLLOWS:
                is_caps = True
                continue
            if braille == BrailleMapping.get_braille(" "):
                is_number = False

            character = BrailleMapping.get_english(
                braille, is_number=is_number, is_caps=is_caps
            )
            english_characters.append(character)
            is_caps = False

        return "".join(english_characters)


class InputTypeClassifier:
    """Identifies whether a string is Braille or English.
    
    Assumes inputs are of correct format (no invalid Braille or invalid English is inputted),     
    """

    @staticmethod
    def is_braille(text: str) -> bool:
        """Check if the given text is Braille according to the requirements.
        
        A string of text is Braille if and only if it contains '.'. 
        This follows because all in-scope Braille characters contain at least one '.'.

        Args:
            text (str): The text to check.

        Returns:
            bool: True if the text is Braille, False if it is English.
        """
        return "." in text


def main():
    """Main function for translating input text between English and Braille.

    Reads input from command line arguments and prints the translation.
    """
    input = " ".join(sys.argv[1:])

    if InputTypeClassifier.is_braille(input):
        translated = Translator.braille_to_english(input)
    else:
        translated = Translator.english_to_braille(input)

    print(translated)


if __name__ == "__main__":
    main()
