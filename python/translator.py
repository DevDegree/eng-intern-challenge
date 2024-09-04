import sys

class EnglishBrailleTranslatorException(Exception):
    pass

class EnglishBrailleTranslator:
    APLHA_TO_BRAILLE = {
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
        ' ': '......',
        'CAPITAL': '.....O',
    }
    NUMBER_TO_BRAILLE = {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',
        'NUMBER': '.O.OOO',
    }
    BRAILLE_TO_ALPHA = {v: k for k, v in APLHA_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}
    VALID_BRAILLE = ['O', '.']
    BRAILLE_CHAR_LENGTH = 6

    def __init__(self):
        pass

    def __check_if_braille(self, text: str) -> bool:
        """
        Check if the given text is braille or not. 
        Text is only valid Braille if it composed of only 'O' and '.'.

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
                ans += self.APLHA_TO_BRAILLE['CAPITAL']
            elif char.isdigit() and not last_char_was_digit:
                ans += self.NUMBER_TO_BRAILLE['NUMBER']
                last_char_was_digit = True
            elif char == ' ':
                last_char_was_digit = False # Reset digit flag


            ans += self.NUMBER_TO_BRAILLE[char] if char.isdigit() else self.APLHA_TO_BRAILLE[char.lower()]
        
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
            if braille_char == self.APLHA_TO_BRAILLE['CAPITAL']:
                is_capital = True
                continue
            if braille_char == self.NUMBER_TO_BRAILLE['NUMBER']:
                is_number = True
                continue
            
            # Space resets number flag
            if braille_char == self.APLHA_TO_BRAILLE[' ']:
                is_number = False

            char = self.BRAILLE_TO_NUMBER[braille_char] if is_number else self.BRAILLE_TO_ALPHA[braille_char]
            ans += char.upper() if is_capital else char
            is_capital = False # Reset capital flag after every character

        return ans


def main():
    input = " ".join(sys.argv[1:])
    translator = EnglishBrailleTranslator()

    try:
        translation = translator.translate(input)
        print(translation)
    except EnglishBrailleTranslatorException as e:
        print(e)

if __name__ == '__main__':
    main()
