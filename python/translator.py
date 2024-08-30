import sys
class Translations:
    """
    This class contains the translation dictionaries for the Braille Translator.
    """
    # Defining CONSTANTs
    ENGLISH_TO_BRAILLE = {
            "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
            "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
            "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
            "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
            "y": "OO.OOO", "z": "O..OOO"
    }
    # Invert the dictionary
    BRAILLE_TO_ENGLISH = {i: j for j, i in ENGLISH_TO_BRAILLE.items()}

    NUMBER_TO_BRAILLE = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
        "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }

    BRAILLE_TO_NUMBER = {i: j for j, i in NUMBER_TO_BRAILLE.items()}

    SYMBOLS_TO_BRAILLE = {
        ".": "..OO.O", ",": ".O....", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
        "/": ".O..O.", "<": ".O..O.", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
    }
    BRAILLE_TO_SYMBOLS = {i: j for j, i in SYMBOLS_TO_BRAILLE.items()}

    INDICATIONS_TO_BRAILLE = {
        "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO", "space": "......"
    }

    BRAILLE_TO_INDICATIONS = {i: j for j, i in INDICATIONS_TO_BRAILLE.items()}
    
class Translator:
    """
    This class translates English text to Braille and vice versa.
    """
    def is_braille(self, text):
        """
        This method checks if the given text is in Braille.
        @param text: The text to check.
        @return: True if the given text is in Braille, False otherwise.
        """
        for char in text:
            if char not in "O.":
                return False
        return True
    
    def get_braille_chunk(self, text, index):
        """
        This method returns a chunk of 6 characters from the given text starting from the given index.
        @param text: The text to get the chunk from.
        @param index: The index to start the chunk from.
        @return: The chunk of 6 characters from the given text starting from the given index.
        """
        return text[index:index + 6]
    

    def translate_braille(self, text):
        """
        This method translates Braille text to English.
        @param text: The Braille text to translate.
        @return: The English translation of the given text.
        """
        index = 0
        output = ""
        is_capital = False
        is_number  = False
        while index < len(text):
            braille_chunk = self.get_braille_chunk(text, index)
            index += 6
            if braille_chunk in Translations.BRAILLE_TO_INDICATIONS:
                if Translations.BRAILLE_TO_INDICATIONS[braille_chunk] == "capital":
                    is_capital = True
                elif Translations.BRAILLE_TO_INDICATIONS[braille_chunk] == "number":
                    is_number = True
                elif Translations.BRAILLE_TO_INDICATIONS[braille_chunk] == "decimal":
                    output += "."
                elif Translations.BRAILLE_TO_INDICATIONS[braille_chunk] == "space":
                    output += " "
                    is_number = False
                continue
            elif is_number:
                output += Translations.BRAILLE_TO_NUMBER[braille_chunk]
            else:
                if is_capital:
                    output += Translations.BRAILLE_TO_ENGLISH[braille_chunk].upper()
                    is_capital = False
                else:
                    output += Translations.BRAILLE_TO_ENGLISH[braille_chunk]
        return output

    def translate_english(self, text):
        """
        This method translates English text to Braille.
        @param text: The English text to translate.
        @return: The Braille translation of the given text.
        """
        output = ""
        is_digit = False
        for char in text:
            if char == " ":
                output += "......"
                is_digit = False
            elif char.isdigit():
                if not is_digit:
                    output += Translations.INDICATIONS_TO_BRAILLE["number"]
                    is_digit = True
                output += Translations.NUMBER_TO_BRAILLE[char]
            elif char.isalpha():
                if char.isupper():
                    output += Translations.INDICATIONS_TO_BRAILLE["capital"]
                output += Translations.ENGLISH_TO_BRAILLE[char.lower()]
        return output

    def translate(self, text):
        """
        This method translates the given text to the appropriate language.
        @param text: The text to translate.
        @return: The translation of the given text.
        """
        if self.is_braille(text):
            return self.translate_braille(text)
        return self.translate_english(text)

if __name__ == "__main__":
    translator = Translator()
    translation = translator.translate(" ".join(sys.argv[1:]))
    print(translation)
