import sys

class EnglishBrailleTranslatorException(Exception):
    pass

class EnglishBrailleTranslator:
    ENGLISH_TO_BRAILLE = {
        'a': '0.....',
        'b': '0.0...',
        'c': '00....',
        'd': '00.0..',
        'e': '0..0..',
        'f': '000...',
        'g': '0000..',
        'h': '0.00..',
        'i': '.00...',
        'j': '.000..',
        'k': '0...0.',
        'l': '0.0.0.',
        'm': '00..0.',
        'n': '00.00.',
        'o': '0..00.',
        'p': '000.0.',
        'q': '00000.',
        'r': '0.000.',
        's': '.00.0.',
        't': '.0000.',
        'u': '0...00',
        'v': '0.0.00',
        'w': '.000.0',
        'x': '00..00',
        'y': '00.000',
        'z': '0..000',
        '1': '0.....',
        '2': '0.0...',
        '3': '00....',
        '4': '00.0..',
        '5': '0..0..',
        '6': '000...',
        '7': '0000..',
        '8': '0.00..',
        '9': '.00...',
        '0': '.000..',
        '.': '..00.0',
        ',': '..0...',
        '?': '..0.00',
        '!': '..000.',
        ':': '..00..',
        ';': '..0.0.',
        '-': '....00',
        '/': '.0..0.',
        '<': '.00..0',
        '>': '0..00.',
        '(': '0.0..0',
        ')': '.0.00.',
        ' ': '......',
        'CAPITAL': '.....0',
        'NUMBER': '.0.000',
    }
    BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
    VALID_BRAILLE = ['0', '.']
    BRAILLE_CHAR_LENGTH = 6

    def __init__(self):
        pass

    def __check_if_braille(self, text: str) -> bool:
        """
        Check if the given text is braille or not. 
        Text is only valid Braille if it composed of only '0' and '.'.

        :param text: The text to check.
        :return: True if the text is braille, False otherwise.
        """
        return all(c in self.VALID_BRAILLE for c in text)
    
    def translate(self, input: str) -> str:
        """
        Translate the given input to braille.

        :param input: The input to translate.
        :return: The translated input in the opposite language of the input.
        """

        if not self.__check_if_braille(input):
            return self.__english_to_braille(input)
        
        # Ensure Braille input is of valid length
        if len(input) % self.BRAILLE_CHAR_LENGTH != 0:
            raise EnglishBrailleTranslatorException('Invalid Braille Input')

        return self.__braille_to_english(input)
        
    def __english_to_braille(self, text: str) -> str:
        """
        Translate the given text to braille.

        :param text: The English text to translate.
        :return: The translated text in Braille.
        """
        ans = ''
        last_char_was_digit = False
        for char in text:
            if char.isupper():
                ans += self.ENGLISH_TO_BRAILLE['CAPITAL']
            elif char.isdigit() and not last_char_was_digit:
                ans += self.ENGLISH_TO_BRAILLE['NUMBER']
                last_char_was_digit = True
            elif char == ' ':
                last_char_was_digit = False # Reset digit flag


            ans += self.ENGLISH_TO_BRAILLE[char.lower()]
        
        return ans        

    def __braille_to_english(self, text: str) -> str:
        """
        Translate the given text to english.

        :param text: The Braille text to translate.
        :return: The translated text in English.
        """

        ans = ''
        index = 0
        is_capital = False
        is_number = False
        while index < len(text):
            braille_char = text[index:index + self.BRAILLE_CHAR_LENGTH]
            index += self.BRAILLE_CHAR_LENGTH

            # Check for special characters
            if braille_char == self.ENGLISH_TO_BRAILLE['CAPITAL']:
                is_capital = True
                continue
            if braille_char == self.ENGLISH_TO_BRAILLE['NUMBER']:
                is_number = True
                continue

            char = self.BRAILLE_TO_ENGLISH.get(braille_char)
            print(char, braille_char, index)
            ans += char.upper() if is_capital else char
            is_capital = False
            if char.isspace():
                is_number = False

        return ans


def main():
    input = sys.argv[1]
    translator = EnglishBrailleTranslator()

    try:
        translation = translator.translate(input)
        print(translation)
    except EnglishBrailleTranslatorException as e:
        print(e)

if __name__ == '__main__':
    main()
