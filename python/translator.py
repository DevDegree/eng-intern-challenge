import sys

class BrailleTranslator:
    def __init__(self):
        """
            Special character constants
        """
        self._CAPITAL_FOLLOWS = ".....O"
        self._NUMBER_FOLLOWS = ".O.OOO"
        self._SPACE = "......"

        """
            Dictionaries that map english characters to braille and vice versa. 
        """
        self._english_to_braille_alpha = {
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
            "z": "O..OOO"
        }
        self._braille_to_english_alpha = {
            val: key for key, val in self._english_to_braille_alpha.items()
        }
        
        self._english_to_braille_digits = {
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
        self._braille_to_english_digits = {
            val: key for key, val in self._english_to_braille_digits.items()
        }

    def _braille_to_english(self, text):
        """
            Special Cases
            1. We will assume that letter characters (k-z) and the capital follows character 
               will not appear while numbers are being read.
        """
        english_text = ""
        number_follows = False
        capital_follows = False

        for i in range(0, len(text), 6):
            braille_char = text[i:i+6]

            # special characters
            if (braille_char == self._CAPITAL_FOLLOWS):
                capital_follows = True

            elif (braille_char == self._NUMBER_FOLLOWS):
                number_follows = True

            elif (braille_char == self._SPACE):
                english_text += " "
                number_follows = False

            # numbers
            elif (number_follows):
                english_text += self._braille_to_english_digits[braille_char]

            # letters
            elif (capital_follows):
                english_text += self._braille_to_english_alpha[braille_char].upper()
                capital_follows = False
            else:
                english_text += self._braille_to_english_alpha[braille_char]
        
        return english_text

    def _english_to_braille(self, text):
        """
            Special Cases
            1. We will assume that letters will not immediately follow numbers.
                ie. "123abc" is invalid, but "123 abc" is valid.
        """
        braille_text = ""
        number_follows = False

        for char in text:
            if (char.isalpha()):
                if (char.isupper()):
                    braille_text += self._CAPITAL_FOLLOWS
                braille_text += self._english_to_braille_alpha[char.lower()]
                
            elif (char.isdigit()):
                if (not number_follows):
                    number_follows = True
                    braille_text += self._NUMBER_FOLLOWS
                braille_text += self._english_to_braille_digits[char]

            # Must be a space
            else:
                number_follows = False
                braille_text += self._SPACE

        return braille_text

    def is_braille(self, text):
        """
            Observe that all braille characters contain at least one dot.
        """
        return '.' in text
    
    def translate(self, text):
        if (self.is_braille(text)):
            return self._braille_to_english(text)
        else:
            return self._english_to_braille(text)
        
if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    brailleTranslator = BrailleTranslator()
    print(brailleTranslator.translate(text))