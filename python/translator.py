import sys


class Translator:
    """
    A class to translate english text to braille and vice versa
    """
    
    CAPITAL_FOLLOWS = ".....O"
    NUMBER_FOLLOWS = ".O.OOO"
    SPACE = "......"

    def __init__(self) -> None:
        """
        Initializes the Translator instance with required mappings
        """

        # Mappings for English to Braille Translation
        self.ENGLISH_TO_BRAILLE = {
            'a': "O.....",
            'b': "O.O...",
            'c': "OO....",
            'd': "OO.O..",
            'e': "O..O..",
            'f': "OOO...",
            'g': "OOOO..",
            'h': "O.OO..",
            'i': ".OO...",
            'j': ".OOO..",
            'k': "O...O.",
            'l': "O.O.O.",
            'm': "OO..O.",
            'n': "OO.OO.",
            'o': "O..OO.",
            'p': "OOO.O.",
            'q': "OOOOO.",
            'r': "O.OOO.",
            's': ".OO.O.",
            't': ".OOOO.",
            'u': "O...OO",
            'v': "O.O.OO",
            'w': ".OOO.O",
            'x': "OO..OO",
            'y': "OO.OOO",
            'z': "O..OOO",
            ' ': self.SPACE,
            'CAPITAL': self.CAPITAL_FOLLOWS,
            'NUMBER': self.NUMBER_FOLLOWS
        }

        self.NUMBER_TO_BRAILLE = {
            '0': ".OOO..",
            '1': "O.....",
            '2': "O.O...",
            '3': "OO....",
            '4': "OO.O..",
            '5': "O..O..",
            '6': "OOO...",
            '7': "OOOO..",
            '8': "O.OO..",
            '9': ".OO..."
        }

        # Reverse mappings
        self.BRAILLE_TO_ENGLISH = {braille: english for english, braille in self.ENGLISH_TO_BRAILLE.items()
                                   if english not in ['CAPITAL', 'NUMBER']}

        self.BRAILLE_TO_NUMBER = {braille: number for number,
                                  braille in self.NUMBER_TO_BRAILLE.items()}

    def classify_input(self, text) -> str:
        """
        Classifies the [text] as either Braille or English

        :param text: The input text to classify
        :return: 'BRAILLE' if the text is in Braille format, otherwise 'ENGLISH'
        """
        if all(char in "O. " for char in text) and len(text.replace(" ", "")) % 6 == 0:
            return 'BRAILLE'
        return 'ENGLISH'

    def translate_to_braille(self, text) -> str:
        """
        Translates English [text] to Braille

        :param text: The English text to translate
        :return: A string representing the translated Braille text
        """
        result = []

        is_number = False  # tracks whether current translation context is a number

        for char in text:
            if char == ' ':
                result.append(self.ENGLISH_TO_BRAILLE[' '])
                continue

            if char.isupper():
                result.append(self.ENGLISH_TO_BRAILLE['CAPITAL'])
                char = char.lower()
                is_number = False

            if char.isdigit():
                if not is_number:
                    result.append(self.ENGLISH_TO_BRAILLE['NUMBER'])
                    is_number = True
                result.append(self.NUMBER_TO_BRAILLE[char])
            else:
                is_number = False
                result.append(self.ENGLISH_TO_BRAILLE.get(char, ''))

        return ''.join(result)

    def translate_to_english(self, braille) -> str:
        """
        Translates [braille] text to English using for loops

        :param braille: The Braille text to translate
        :return: A string representing the translated English text
        """
        result = []
        is_capital = False  # tracks whether characters should be capitalized
        is_number = False  # tracks whether current translation context is a number

        # Braille Symbol Length
        braille_symbol_length = 6

        # Iterate over the [braille] input for every [symbol_length] characters
        for i in range(0, len(braille), braille_symbol_length):
            symbol = braille[i:i + braille_symbol_length]

            if symbol == self.CAPITAL_FOLLOWS:
                is_capital = True
            elif symbol == self.NUMBER_FOLLOWS:
                is_number = True
            elif symbol == self.SPACE:
                result.append(' ')
                is_number = False
            else:
                if is_number:
                    result.append(self.BRAILLE_TO_NUMBER.get(symbol, ''))
                else:
                    letter = self.BRAILLE_TO_ENGLISH.get(symbol, '')
                    if is_capital:
                        letter = letter.upper()
                        is_capital = False
                    result.append(letter)

        return ''.join(result)


def main() -> None:
    """
    Process CLI arguements to determine input type and translate as needed
    """

    translator = Translator()

    if len(sys.argv) < 2:
        print("ERROR: Missing arguments | Usage: python3 translator.py <str>")
        return

    input_text = ' '.join(sys.argv[1:])
    input_type = translator.classify_input(input_text)

    if input_type == 'BRAILLE':
        print(translator.translate_to_english(input_text))
    else:
        print(translator.translate_to_braille(input_text))


if __name__ == "__main__":
    main()
