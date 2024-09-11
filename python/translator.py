"""
Translator module for conversion of text in English and Braille.
Converting alphabetic and numeric translation(case sensitive).
"""
import sys

class BrailleTranslator:
    """
    A class that translate between English and Braille
    """
    def __init__(self):
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
        Validate if the input in Braille is the string length of a multiple of 6.
        Raise an error if the string is not a multiple of 6
        """
        if len(braille_string) % 6 != 0:
            raise ValueError("Braille string must be of 6 character . or O")

    def detect_language(self, input_string):
        """
        Detect if the input string is in Braille or English
        Will return 'braille' if the string is Braille or 'english' otherwise
        """
        if all(char in ['O', '.'] for char in input_string):
            return 'braille'
        if all(char.isalnum() or char.isspace() for char in input_string):
            return 'english'

        raise ValueError("Unsupported car detected. Only (O,.) or aplhanumeric is accepted")

    def split_braille(self, braille_string):
        """
        Split the Braille string into chunks of 6 characters
        Return a list of 6 character chunks from the Braille string
        """
        result = []
        for i in range(0, len(braille_string), 6):
            result.append(braille_string[i:i+6])
        return result

    def braille_translator(self, braille_string):
        """
        Translate Braille into English text.
        Verify first if it is capital or a number to properly translate
        If it is a space it will remove the capital or number mode
        If it is a number it will translate from the number dictionary
        If it is a capital letter it will convert the letter in uppercase
        Return the translated English string
        """
        self.validate_braille(braille_string)
        result = []
        chunks = self.split_braille(braille_string)
        is_number_mode = False
        is_capital_mode = False

        for chunk in chunks:
            if chunk in self.braille_interprete:
                if self.braille_interprete[chunk] == 'capital':
                    is_capital_mode = True
                    continue
                if self.braille_interprete[chunk] == 'number':
                    is_number_mode = True
                    continue
            elif chunk == '......':
                is_number_mode = False
                is_capital_mode = False
                result.append(' ')
            else:
                if is_number_mode:
                    if chunk in self.braille_translator_num:
                        result.append(self.braille_translator_num[chunk])
                elif chunk in self.braille_translator_alpha:
                    letter = self.braille_translator_alpha[chunk]
                    if is_capital_mode:
                        letter = letter.upper()
                        is_capital_mode = False
                    result.append(letter)


        return ''.join(result)

    def english_translator(self, input_string):
        """
        Translate English into Braille text.
        Verify if it is a letter if so it verify if capital first
        Append capital follows if capital only
        Verify if it is a number if it doesnt already has the number mode
        It will append the number follows
        If it is a space it will remove the number mode and append space
        Return the translated Braille string
        """
        result = []
        is_number_mode = False

        for char in input_string:
            if char.isalpha():
                if char.isupper():
                    result.append('.....O')
                    char = char.lower()
                result.append(self.english_translator_alpha[char])
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
        Detect which language is the input string and translate it accordingly.
        Return the translated string in the targeted language (Braille or English)
        Raise error if the language use is not Braille or English
        """
        language = self.detect_language(input_string)
        if language == 'english':
            return self.english_translator(input_string)
        if language == 'braille':
            return self.braille_translator(input_string)

        raise ValueError("Unsupported language")


def main():
    """
    Main entry point for the translator program. It processes command-line arguments.
    After translation completed, it prints the results.
    Raise error if the braille string is invalid or if it is not a supported language.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input_to_translate>")
        return

    input_string = ' '.join(sys.argv[1:])

    translator = BrailleTranslator()

    try:
        translate_text = translator.translate(input_string)
        print(translate_text)
    except ValueError as error:
        print(f"error: {error}")

if __name__ == "__main__":
    main()
