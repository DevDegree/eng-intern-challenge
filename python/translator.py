import sys
import re


class Translator:
    """
    A Translator class that is capable of handling any translation from Braille to English and vice versa.
    """

    _ENGLISH_TO_BRAILLE = {
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
        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ':': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '(': 'O.O..O',
        ')': '.O.OO.',
        ' ': '......',
        'capital': '.....O',
        'number': '.O.OOO',
    }

    _NUMBER_TO_BRAILLE = {
        '0': '.OOO..',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
    }

    _BRAILLE_TO_ENGLISH = {v: k for k, v in _ENGLISH_TO_BRAILLE.items()}
    _BRAILLE_TO_NUMBER = {v: k for k, v in _NUMBER_TO_BRAILLE.items()}

    def __init__(self, text: str):
        self.text: str = text 

    def check_if_braille(self) -> bool:
        """
        This function checks if provided text is a valid Braille text.

        Returns:
            bool: True if the text is valid Braille, otherwise False
        """
        braille_characters = {'O', '.', ' '}
        return all(char in braille_characters for char in self.text) and len(self.text.replace(' ', '')) % 6 == 0
    
    def translate_braille_to_english(self) -> str:
        """
        This function translates Braille text to English.

        Returns:
            str: Translated English text
        """
        number_flag: bool = False
        capital_flag: bool = False
        translation = []

        english_to_braille = self._ENGLISH_TO_BRAILLE
        braille_to_english = self._BRAILLE_TO_ENGLISH
        braille_to_number = self._BRAILLE_TO_NUMBER

        tokens = re.findall(r'\s{6}|.{6}', self.text)

        for token in tokens:
            if token == english_to_braille['number']:
                number_flag = True
                
            elif token == english_to_braille['capital']:
                capital_flag = True
                number_flag = False
                
            elif token == english_to_braille[' ']:
                translation.append(' ')
                number_flag = False

            else:   
                char = braille_to_number.get(token) if number_flag else braille_to_english.get(token)

                if capital_flag:
                    char = char.upper()
                    capital_flag = False 
                
                if not char.isdigit():
                    number_flag = False

                translation.append(char)

        return ''.join(translation)
    
    def translate_english_to_braille(self) -> str:
        """
        This function translates English text to Braille.

        Returns:
            str: Translated Braille text
        """
        english_to_braille = self._ENGLISH_TO_BRAILLE
        number_to_braille = self._NUMBER_TO_BRAILLE
        translation = []

        number_flag: bool = False
        for char in self.text:
            if char == ' ':
                number_flag = False
                translation.append(english_to_braille[' '])
            elif char.isdigit():
                if not number_flag:
                    number_flag = True
                    translation.append(english_to_braille['number'])
                translation.append(number_to_braille[char])
            else:
                if number_flag:
                    number_flag = False
                if char.isupper():
                    translation.append(english_to_braille['capital'])
                    char = char.lower()
                translation.append(english_to_braille[char])
        
        return ''.join(translation)

def get_text_from_args() -> str:
    """
    This function gets input from command line.

    Returns:
        str: Concatenated text from command line
    """
    args = sys.argv[1:]
    return ' '.join(args) if args else ''
    
def main():
    """
    This is a main function determines if text is Braille or English and runs translator.
    """
    text = get_text_from_args()
    if not text:
        return
    translator = Translator(text)

    if translator.check_if_braille():
        result = translator.translate_braille_to_english()
    else:
        result = translator.translate_english_to_braille()

    print(result)


if __name__ == '__main__':
    main()
