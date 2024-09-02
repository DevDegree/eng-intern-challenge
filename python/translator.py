import sys

# Mapping from English letters, numbers, and symbols to Braille
ENGLISH_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O',  # Special character to indicate a capital letter
    'number': '.O.OOO',   # Special character to indicate that numbers follow
    ' ': '......'         # Representation for a space
}

# Mapping from numbers to Braille
NUMBERS_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

class BrailleDictionary:
    """
    Handles the translation between English characters and their Braille representations.
    """

    def __init__(self, to_braille: dict[str, str]) -> None:
        """
        Initializes the BrailleDictionary with a given dictionary for translating 
        from English to Braille. Also creates a reverse dictionary for translating
        from Braille to English.

        :param to_braille: Dictionary mapping English characters to Braille.
        """
        self.to_braille = to_braille
        self.to_english = {value: key for key, value in to_braille.items()}

    def get_english(self, braille: str) -> str:
        """
        Retrieves the English character corresponding to a given Braille pattern.

        :param braille: Braille pattern string.
        :return: Corresponding English character.
        """
        return self.to_english[braille]

    def get_braille(self, english: str) -> str:
        """
        Retrieves the Braille pattern corresponding to a given English character.

        :param english: English character.
        :return: Corresponding Braille pattern.
        """
        return self.to_braille[english]

class Translator:
    """
    Handles translation between English text and Braille text.
    """

    def __init__(self) -> None:
        """
        Initializes the Translator with dictionaries for both characters and numbers.
        """
        self.brailleCharactersDictionary = BrailleDictionary(ENGLISH_TO_BRAILLE)
        self.brailleNumbersDictionary = BrailleDictionary(NUMBERS_TO_BRAILLE)

    def is_braille(self, string: str) -> bool:
        """
        Determines if a given string is in Braille format.

        :param string: Input string.
        :return: True if the string is in Braille, False otherwise.
        """
        return all(character in {'.', 'O'} for character in string)

    def english_to_braille(self, string: str) -> str:
        """
        Translates English text to Braille.

        :param string: English text to be translated.
        :return: Braille representation of the input text.
        """
        result = ""
        number = False
        for c in string:
            if c.isdigit():
                if not number:
                    result += self.brailleCharactersDictionary.get_braille('number')
                    number = True
                result += self.brailleNumbersDictionary.get_braille(c)
            else:
                number = False
                if c.isupper():
                    result += self.brailleCharactersDictionary.get_braille('capital')
                result += self.brailleCharactersDictionary.get_braille(c.lower())
        return result

    def braille_to_english(self, string: str) -> str:
        """
        Translates Braille text to English.

        :param string: Braille text to be translated.
        :return: English representation of the input Braille.
        """
        capital = False
        number = False
        result = ""
        for i in range(0, len(string), 6):
            character = string[i:i+6]
            english = self.brailleCharactersDictionary.get_english(character)
            if english == 'capital':
                capital = True
            elif english == 'number':
                number = True
            else:
                if english == ' ':
                    number = False
                    result += ' '
                elif capital:
                    result += english.upper()
                    capital = False
                elif number:
                    result += self.brailleNumbersDictionary.get_english(character)
                else:
                    result += english
        return result

def main() -> None:
    """
    The main function to execute the translation between English and Braille.
    Determines the input type (English or Braille) and prints the translation.
    """
    translator = Translator()
    string = " ".join(sys.argv[1:])

    if translator.is_braille(string):
        print(translator.braille_to_english(string))
    else:
        print(translator.english_to_braille(string))

if __name__ == "__main__":
    main()