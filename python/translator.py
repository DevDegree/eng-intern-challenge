"""
Translator module for conversion of text in English and Braille.
Converting alphabetic and numeric translation(case sensitive).
"""
import sys

class BrailleTranslator:
    """
    A class that translates between English and Braille.
    Supports both alphabetic and numeric translation (case-sensitive).
    """
    def __init__(self):
        """
        Initializes the BrailleTranslator with translation dictionaries.
        Sets up mappings for Braille interpretation, Braille to English (alphabets and numbers),
        and English to Braille (alphabets and numbers).
        """
        self.braille_interprete = {
            '.....O':'capital',  # Capital follows
            '.O.OOO':'number',   # Number follows
        }
        self.braille_translator_alpha = {
            'O.....':'a',
            'O.O...':'b',
            'OO....':'c',
            'OO.O..':'d',
            'O..O..':'e',
            'OOO...':'f',
            'OOOO..':'g',
            'O.OO..':'h',
            '.OO...':'i',
            '.OOO..':'j',
            'O...O.':'k',
            'O.O.O.':'l',
            'OO..O.':'m',
            'OO.OO.':'n',
            'O..OO.':'o',
            'OOO.O.':'p',
            'OOOOO.':'q',
            'O.OOO.':'r',
            '.OO.O.':'s',
            '.OOOO.':'t',
            'O...OO':'u',
            'O.O.OO':'v',
            '.OOO.O':'w',
            'OO..OO':'x',
            'OO.OOO':'y',
            'O..OOO':'z',
        }
        self.braille_translator_num = {
            'O.....':'1',
            'O.O...':'2',
            'OO....':'3',
            'OO.O..':'4',
            'O..O..':'5',
            'OOO...':'6',
            'OOOO..':'7',
            'O.OO..':'8',
            '.OO...':'9',
            '.OOO..':'0',
        }
        self.english_translator_alpha ={v: k for k, v in self.braille_translator_alpha.items()}
        self.english_translator_num ={v: k for k, v in self.braille_translator_num.items()}

    def validate_braille(self, braille_string):
        """
        Validates if the input Braille string has a length that is a multiple of 6.

        Args:
            braille_string (str): The Braille string to validate.

        Raises:
            ValueError: If the string length is not a multiple of 6.
        """
        if len(braille_string) % 6 != 0:
            raise ValueError("Braille string must be of 6 character . or O")

    def detect_language(self, input_string):
        """
        Detects whether the input string is in Braille or English.

        Args:
            input_string (str): The string to analyze.

        Returns:
            str: 'braille' or 'english' depending on the detected language.

        Raises:
            ValueError: If unsupported characters are detected.
        """
        braille_chars = set('O.')
        first_char = input_string[0]
        
        if first_char in braille_chars:
            if set(input_string) <= braille_chars:
                return 'braille'
        elif first_char.isalnum() or first_char.isspace():
            if all(c.isalnum() or c.isspace() for c in input_string):
                return 'english'
        
        raise ValueError("Unsupported character detected. Only (O,.) or alphanumeric is accepted")

    def split_braille(self, braille_string):
        """
        Splits the Braille string into chunks of 6 characters.

        Args:
            braille_string (str): The Braille string to split.

        Returns:
            list: A list of 6-character Braille chunks.
        """
        return [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]

    def braille_translator(self, braille_string):
        """
        Translates Braille into English text.

        Args:
            braille_string (str): The Braille string to translate.

        Returns:
            str: The translated English text.

        Raises:
            ValueError: If the Braille string is invalid.
        """
        self.validate_braille(braille_string)
        result = []
        chunks = self.split_braille(braille_string)
        modes = {'number': False, 'capital': False}
        
        for chunk in chunks:
            if chunk in ('......', '.....O', '.O.OOO'):
                modes = {'number': chunk == '.O.OOO', 'capital': chunk == '.....O'}
                if chunk == '......':
                    result.append(' ')
            elif modes['number']:
                result.append(self.braille_translator_num.get(chunk, ''))
            else:
                letter = self.braille_translator_alpha.get(chunk, '')
                result.append(letter.upper() if modes['capital'] else letter)
                modes['capital'] = False
        
        return ''.join(result)

    def english_translator(self, input_string):
        """
        Translates English into Braille text.

        Args:
            input_string (str): The English string to translate.

        Returns:
            str: The translated Braille text.
        """
        result = []
        is_number_mode = False
        
        for char in input_string:
            if char.isalpha():
                if char.isupper(): result.append('.....O' + self.english_translator_alpha[char.lower()])
                else: result.append(self.english_translator_alpha[char])
            elif char.isdigit():
                if not is_number_mode:
                    result.append('.O.OOO')
                    is_number_mode = True
                result.append(self.english_translator_num[char])
            elif char == ' ':
                is_number_mode = False
                result.append('......')
        
        return ''.join(result)

    def translate(self, input_string):
        """
        Detects the language of the input and translates accordingly.

        Args:
            input_string (str): The string to translate.

        Returns:
            str: The translated string (English to Braille or Braille to English).

        Raises:
            ValueError: If the language is unsupported or if translation fails.
        """
        translators = {
            'english': self.english_translator,
            'braille': self.braille_translator
        }
        translator = translators.get(self.detect_language(input_string))
        if not translator:
            raise ValueError("Unsupported language")
        return translator(input_string)

def main():
    """
    Main entry point for the translator program.
    Processes command-line arguments and performs the translation.

    Usage:
        python3 translator.py <input_to_translate>

    Prints:
        The translated text or an error message.

    Exits:
        With an error message if invalid arguments are provided or an error occurs during translation.
    """
    if len(sys.argv) < 2: sys.exit("Usage: python3 translator.py <input_to_translate>")

    translator = BrailleTranslator()
    try: print(translator.translate(' '.join(sys.argv[1:])))
    except ValueError as error: sys.exit(f"Error: {error}")

if __name__ == "__main__": main()
