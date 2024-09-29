"""
Braille Translator

Usage:
    python translator.py <text> 
"""

import sys

class BrailleTranslator:
    """
    A class used to translate text between English and Braille.
    """

    # English letters to Braille dictionary
    LETTERS_TO_BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
        'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
        'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
        'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
        'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
        'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    }

    # Numbers to Braille dictionary
    NUMBERS_TO_BRAILLE = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..',
    }

    # Special character Braille translations 
    CAPITAL_BRAILLE = '.....O'
    NUMBER_BRAILLE  = '.O.OOO'
    SPACE_BRAILLE   = '......'

    # Braille to letters dictionary
    BRAILLE_TO_LETTERS = {v: k for k, v in LETTERS_TO_BRAILLE.items()}

    # Braille to numbers dictionary
    BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

    def translate(self, text):
        """
        Translates the given text between English and Braille.
        
        Args:
            text (str): The text to be translated.
        
        Returns:
            str: The translated text.
        """
        if self.isBraille(text):
            return self.brailleToEnglish(text)
        else:
            return self.englishToBraille(text)

    def isBraille(self, text):
        """
        Checks if the given text is in Braille format.
        
        Args:
            text (str): The text to be checked.
        
        Returns:
            bool: True if the text is in Braille format, False otherwise.
        """
        # Checks if text contains only 'O' and '.' and length is a multiple of six
        return all(char in 'O.' for char in text) and len(text) % 6 == 0
    
    def brailleToEnglish(self, text):
        """
        Converts Braille text to English.
        
        Args:
            text (str): The Braille text to be converted.
        
        Returns:
            str: The converted English text.
        """
        # Splits text input into a list of length six strings
        braille = [text[i:i+6] for i in range(0, len(text), 6)]

        english = ''
        capital = False # Capital letter flag
        number = False # Number translation flag

        # Loop through each Braille character
        for char in braille:
            # Translate Braille space to English
            if char == self.SPACE_BRAILLE:
                english += ' '
                # Exit any special modes
                number = False
                capital = False
                continue

            # Enter capital mode
            if char == self.CAPITAL_BRAILLE: 
                capital = True
                continue

            # Enter number mode
            if char == self.NUMBER_BRAILLE:
                number = True
                continue
            
            # Translate Braille number
            if number:
                english += self.BRAILLE_TO_NUMBERS[char]
            # Translate Braille letter
            else:
                c = self.BRAILLE_TO_LETTERS[char]
                if (capital):
                    english += c.upper()
                    capital = False
                else:
                    english += c
        
        return english

    def englishToBraille(self, text):
        """
        Converts English text to Braille.
        
        Args:
            text (str): The English text to be converted.
        
        Returns:
            str: The converted Braille text.
        """
        braille = ''
        number = False

        # Loop through each English character
        for char in text:
            # Translate English space to Braille
            if char == ' ':
                braille += self.SPACE_BRAILLE
                number = False # Exit number mode
                continue

            # Translate digit to Braille
            if char.isdigit():
                if not number:
                    braille += self.NUMBER_BRAILLE
                    number = True # Enter number mode
                braille += self.NUMBERS_TO_BRAILLE[char]
            # Translate English letter to Braille
            elif char.isalpha:
                if number:
                    number = False # Exit number mode
                
                if char.isupper():
                    braille += self.CAPITAL_BRAILLE # Add capital symbol
                braille += self.LETTERS_TO_BRAILLE[char.lower()]

        return braille


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    # Join arguments with a space
    text = ' '.join(sys.argv[1:])
    # Instantiate BrailleTranslator
    translator = BrailleTranslator()
    # Print result
    print(translator.translate(text))
