import sys
from constants import *

class Translator:
    def to_braille(self, s: str) -> bool:
        """
        Determine the type of translation. Returns True if translation is from english to braille. False otherwise

        Arguments:

        s: str
            The string to determine the type of text 
        """
        if all(char in 'O.' for char in s) and len(s) % 6 == 0:
            return False
        return True
    
    def english_to_braille(self, s: str) -> str:
        """
        Translates English to Braille.

        Arguments:

        s: str
            The English string to be translated into Braille
        """
        translation = ""
        num_mode = False
        capital = False

        for c in s:
            # handle a numeric case
            if c.isnumeric():
                if not num_mode:
                    translation += ENGLISH_TO_BRAILLE['number']
                    num_mode = True
                translation += NUMBER_TO_BRAILLE[c]
            # handle a character case
            elif c.isalpha():
                if c.isupper():
                    if not capital:
                        translation += ENGLISH_TO_BRAILLE['capital']
                        capital = True
                c = c.upper()
                translation += ENGLISH_TO_BRAILLE[c]
            # handle a bare space
            elif c == ' ':
                num_mode, capital = False, False
                translation += ENGLISH_TO_BRAILLE['space']
            # not valid 
            else:
                raise Exception(f"Invalid character encountered: ${c}")
        return translation

    def braille_to_english(self, s: str) -> str:
        """
        Translates Braille to English.

        Arguments:

        s: str
            The braille string to be translated into English.
        """
        translation = ''
        capital = False
        num_mode = False

        for i in range(0, len(s), 6):
            c = s[i:i + 6]
            
            # handle capital, change mode
            if c == ENGLISH_TO_BRAILLE['capital']:
                capital = True
            # handle number, change mode
            elif c == ENGLISH_TO_BRAILLE['number']:
                num_mode = True
            # handle space, add a space and reset the mode
            elif c == ENGLISH_TO_BRAILLE['space']:
                translation += ' '
                num_mode = False
            # number mode, append the correct number
            elif num_mode:
                translation += BRAILLE_TO_NUMBER[c]
            # handle a single character
            elif c in BRAILLE_TO_ENGLISH:
                letter = BRAILLE_TO_ENGLISH[c]
                if capital:
                    translation += letter.upper()
                    capital = False
                else:
                    translation += letter.lower()
            else:
                raise Exception(f"Invalid character encountered: ${c}")

        return translation
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Did not provide enough arguments.")
    translator = Translator()
    input_string = sys.argv[1]
    
    # determine type of translation and provide correct translation type
    if translator.to_braille(input_string):
        output = translator.english_to_braille(' '.join(sys.argv[1:]))
    else:
        output = translator.braille_to_english(input_string)
    print(output)