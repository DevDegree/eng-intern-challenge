import sys


class Translator:
    """
    Class that translates.
    """

    # Contains braille characters and their equivalent in English.
    BRAILLE_DICT = {
        "O.....": "a1",
        "O.O...": "b2",
        "OO....": "c3",
        "OO.O..": "d4",
        "O..O..": "e5",
        "OOO...": "f6",
        "OOOO..": "g7",
        "O.OO..": "h8",
        ".OO...": "i9",
        ".OOO..": "j0",
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
        ".....O": "capital",
        ".O.OOO": "number",
        "......": " "
    }

    # How many characters make uo a braille character.
    CHARACTER_LENGTH = 6

    capitalFlag = False
    numberFlag = False
    spaceFlag = False

    def translate(self, text) -> str:
        """
        Translates either from Braille to English, or the inverse accordingly.
        :param text: The text to convert.
        :return: The converted text.
        """

        # A braille character at the beginning shall indicate the text is Braille.
        if text[0: 6] in self.BRAILLE_DICT:
            return self.translateBraille(text)
        else:
            return self.translateEnglish(text)

    def translateBraille(self, text) -> str:
        """
        Translates from Braille to English.
        :param text: The braille text to translate.
        :return: The translated text.
        """

        outputText = ""

        # Loop through each group of 6 characters.
        for char in (text[i: i + self.CHARACTER_LENGTH] for i in range(0, len(text), self.CHARACTER_LENGTH)):
            try:

                character = self.BRAILLE_DICT[char]

                # Detecting a space should indicate the end of numbers.
                if self.spaceFlag:
                    if self.numberFlag:
                        self.numberFlag = False
                    self.spaceFlag = False

                if len(character) == 2:
                    # For braille characters that represent both a character and a number,
                    # The equivalent is both of them
                    # To the left is the character, to the right is the number.
                    # The numberFlag will determine which should be used.
                    character = character[1] if self.numberFlag else character[0]

                if character == "capital":
                    self.capitalFlag = True
                    continue  # Continue loop to avoid adding 'character'.
                elif character == "number":
                    self.numberFlag = True
                    if self.capitalFlag:
                        self.capitalFlag = False
                    continue  # Continue loop to avoid adding 'number'.
                elif character == " ":
                    self.spaceFlag = True
                    if self.capitalFlag:
                        self.capitalFlag = False
                elif self.capitalFlag:
                    character = character.capitalize()

                if self.capitalFlag:
                    self.capitalFlag = False

                outputText += character
            except KeyError:
                print("THE TEXT CONTAINS INCORRECT CHARACTERS!")
                return "\u0000"  # Return the null character.
        return outputText

    def translateEnglish(self, text) -> str:
        """
        Translates from English to Braille.
        :param text: The English text to translate.
        :return: The translated text.
        """

        outputText = ""
        char = ""
        i = 0

        # Determines whether the braille character that indicates the start of numbers,
        # has been writen.
        initialNumberBrailleWriten = False
        while i < len(text):

            # Char being 'capital' will indicate the capital flag braille character,
            # has already been writen.
            if text[i].isupper() and not char == "capital":
                self.capitalFlag = True
                i -= 1  # The actual character won't be writen on first try, so 'i' is decremented.

            char = text[i]
            character = ""
            if self.capitalFlag:
                self.capitalFlag = False
                char = "capital"
            if text[i].isnumeric() and not initialNumberBrailleWriten:
                char = "number"
                initialNumberBrailleWriten = True
                i -= 1  # The actual character won't be writen on first try, so 'i' is decremented.
            elif not text[i].isnumeric() and initialNumberBrailleWriten:
                initialNumberBrailleWriten = False

            for k, v in self.BRAILLE_DICT.items():

                # For characters that are represented by the same braille character,
                # Check if any of them is matching.
                if len(v) == 2 and (v[0] == char.lower() or v[-1] == char.lower()):
                    character = k
                    break
                elif v == char.lower():
                    character = k
                    break
            outputText += character
            i += 1
        return outputText


def main():
    """
    Entry point for the script.
    :return: Nothing.
    """

    text = ""
    for i in range(1, len(sys.argv)):
        text += sys.argv[i] + " "

    # Remove redundant " " at the end.
    print(Translator().translate(text[0: len(text) - 1]))


if __name__ == '__main__':
    main()
