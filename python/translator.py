import sys


class Translator:
    """ This class is used for translating Braille to English as well as English to Braille"""

    def __init__(self) -> None:
        self.alpha_numeric_to_braille = {
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
            '.': '..OO.O',
            ',': '..O...',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '<': '.OO..O',
            '(': 'O.O..O',
            ')': '.O.OO.',
            'CapitalFollows': '.....O',
            'DecimalFollows': '.O...O',
            'numberFollows': '.O.OOO'
        }

        self.braille_to_alpha_numeric = {v: k for k, v in self.alpha_numeric_to_braille.items()}
        self.letter_to_digit = {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8',
            'i': '9',
            'j': '0'
        }
        self.digit_to_letter = {v: k for k, v in self.letter_to_digit.items()}

    def check_braille_input(self, input_string):
        """
    This function is used to check if the input string is in Braille format.
    :param input_string: The input string in braille to be checked.
    :return: True if the input string is in Braille format, False otherwise.
    """
        unique_chars = set(input_string)
        chars = {'.', 'O'}
        length_check = len(input_string) % 6 == 0
        return unique_chars == chars and length_check

    def get_language(self, input_string):
        """
      This function is used to get the language of the input string.
      :param input_string: The input string to be checked.
      :return: The language of the input string Baraille or English.
      """
        return 'ENG' if not self.check_braille_input(input_string) else 'BRA'

    def tokenize(self, input_string):
        """
    This function is used to tokenize the input string.
    :param input_string: The input string to be tokenized.
    :return: A list of tokens.
    """
        tokens = []

        for i in range(0, len(input_string), 6):
            tokens.append(input_string[i:i + 6])
        return tokens

    def translate_braille_to_english(self, braille_text_input):
        """"
      This function is used to translate the input string from Braille to English.
      :param braille_text_input: The input string in braille to be translated.
      :return: The translated string in English.
    """
        # Initialize variables
        translated_text = ""
        capital_follow = False
        decimal_follow = False
        number_follow = False

        # Tokenize the input string
        tokens = self.tokenize(braille_text_input)

        # Translate tokens
        for token in tokens:
            if token in self.braille_to_alpha_numeric:
                char = self.braille_to_alpha_numeric[token]

                if char == 'CapitalFollows':
                    capital_follow = True  # Raise the flag to capitalize the character
                    continue
                elif char == 'DecimalFollows':
                    decimal_follow = True  # Raise the flag for decimal input
                    translated_text += '.'
                    continue
                elif char == 'numberFollows':
                    number_follow = True  # Raise the flag for number input
                    continue
                elif char == ' ':
                    number_follow = False
                    decimal_follow = False
                    translated_text += ' '
                    continue
                else:
                    if capital_follow:
                        translated_text += char.upper()
                        capital_follow = False

                    elif decimal_follow:
                        translated_text += self.letter_to_digit[char]

                    elif number_follow:
                        translated_text += self.letter_to_digit[char]

                    else:
                        translated_text += char

        return translated_text

    def translate_english_to_braille(self, input_string):

        translated_text = ""
        capital_follow = False
        decimal_follow = False
        number_follow = False
        for char in input_string:
            if char.lower() in self.alpha_numeric_to_braille or char in self.digit_to_letter:
                if char.isupper():
                    translated_text += self.alpha_numeric_to_braille["CapitalFollows"]
                    translated_text += self.alpha_numeric_to_braille[char.lower()]

                elif char.isdigit():
                    if not number_follow:
                        translated_text += self.alpha_numeric_to_braille["numberFollows"]
                        translated_text += self.alpha_numeric_to_braille[self.digit_to_letter[char]]
                        number_follow = True
                    else:
                        translated_text += self.alpha_numeric_to_braille[self.digit_to_letter[char]]
                else:
                    translated_text += self.alpha_numeric_to_braille[char]
                    capital_follow = False
                    decimal_follow = False
                    number_follow = False

            else:
                print(f"Invalid character: {char}")
        return translated_text

    def translate_text(self, input_string):
        """
        This function is used to translate the input string from Braille to English or English to Braille based on the language detected.
        :param input_string: The input string to be translated.
        :return: The translated string.
      """
        language = self.get_language(input_string)
        if language == 'ENG':
            return self.translate_english_to_braille(input_string)
        else:
            return self.translate_braille_to_english(input_string)


if __name__ == '__main__':
    input_string = ' '.join(sys.argv[1:])
    translator = Translator()
    print(translator.translate_text(input_string))

