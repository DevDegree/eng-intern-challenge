"""
Requirements:
- Convert English to Braille
- Convert Braille to English
- Automatically detect language

Observations:
- Braille strings will only contain '.' and 'O'
- Should consider the "fake Braille" case: 
   - String looks like Braille but does not map to valid Braille characters
   - therefore it is English
- Since Braille contains only 2 possible characters, we can represent it in binary
- Each Braille symbol will correspond to a specific 6-bit binary number
"""
import sys


class TranslationError(Exception):
    """
    Custom exception class for translation errors.
    """
    pass


class Translator:
    """
    A class for translating between English and Braille.

    This class provides methods to convert English text to Braille and vice versa,
    as well as detect the language of the input text.

    Attributes:
        english_to_braille_map (dict): Mapping of English characters to Braille binary representations.
        number_to_braille_map (dict): Mapping of numeric characters to Braille binary representations.
        braille_to_number_map (dict): Reverse mapping of Braille binary representations to numeric characters.
        braille_unique_symbols (dict): Mapping of special Braille symbols to their binary representations.
        braille_to_english_map (dict): Reverse mapping of Braille binary representations to English characters.
    """

    def __init__(self):
        self.english_to_braille_map = {
            'a': 0b100000, 'b': 0b101000, 'c': 0b110000, 'd': 0b110100, 'e': 0b100100, 'f': 0b111000, 'g': 0b111100, 'h': 0b101100,
            'i': 0b011000, 'j': 0b011100, 'k': 0b100010, 'l': 0b101010, 'm': 0b110010, 'n': 0b110110, 'o': 0b100110, 'p': 0b111010,
            'q': 0b111110, 'r': 0b101110, 's': 0b011010, 't': 0b011110, 'u': 0b100011, 'v': 0b101011, 'w': 0b011101, 'x': 0b110011,
            'y': 0b110111, 'z': 0b100111,
            ' ': 0b000000, '.': 0b001101,
        }
        self.braille_to_english_map = {v: k for k, v in self.english_to_braille_map.items()}

        self.number_to_braille_map = {            
            '0': 0b011100, '1': 0b100000, '2': 0b101000, '3': 0b110000, '4': 0b110100, '5': 0b100100, '6': 0b111000, '7': 0b111100, 
            '8': 0b101100, '9': 0b011000
        }
        self.braille_to_number_map = {v: k for k, v in self.number_to_braille_map.items()}

        self.braille_unique_symbols = {
            'capital_follows': 0b000001,
            'number_follows': 0b010111,
            'decimal_follows': 0b010001
        }

    def english_to_braille(self, text):
        """
        Converts English text to Braille.

        Args:
            text (str): The English text to be converted.

        Returns:
            str: The Braille representation of the input text.
        """
        result = []
        is_number_mode = False

        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(self._braille_to_dots(self.braille_unique_symbols['capital_follows']))
                    char = char.lower()
                result.append(self._braille_to_dots(self.english_to_braille_map[char]))

            elif char.isdigit():
                if not is_number_mode:
                    result.append(self._braille_to_dots(self.braille_unique_symbols['number_follows']))
                    is_number_mode = True
                result.append(self._braille_to_dots(self.number_to_braille_map[char]))

            elif char == '.' and is_number_mode:
                result.append(self._braille_to_dots(self.braille_unique_symbols['decimal_follows']))
            
            else:
                if is_number_mode:
                    is_number_mode = False
                result.append(self._braille_to_dots(self.english_to_braille_map[char]))

        return ''.join(result)

    def braille_to_english(self, text):
        """
        Converts Braille text to English.

        Args:
            text (str): The Braille text to be converted.

        Returns:
            str: The English representation of the input Braille text.
        """
        result = []
        braille_chars = [text[i:i+6] for i in range(0, len(text), 6)]
        is_capital = False
        is_number = False

        for braille_char in braille_chars:
            binary = self._dots_to_binary(braille_char)

            if binary == self.braille_unique_symbols['capital_follows']:
                is_capital = True
            elif binary == self.braille_unique_symbols['number_follows']:
                is_number = True
            elif binary == self.braille_unique_symbols['decimal_follows']:
                result.append('.')
            else:
                if is_number:
                    char = self.braille_to_number_map.get(binary)
                    if char is None:
                        char = self.braille_to_english_map.get(binary)
                    if char == ' ':
                        is_number = False
                else:
                    char = self.braille_to_english_map.get(binary)

                if char is None:
                    raise TranslationError
                
                if is_capital and char.isalpha():
                    char = char.upper()
                    is_capital = False
                elif not char.isalpha():
                    is_capital = False
                
                result.append(char)

        return ''.join(result)

    def detect_language(self, text):
        """
        Detects whether the input text is in English or Braille.

        Args:
            text (str): The text to be analyzed.

        Returns:
            str: 'braille' if the text is in Braille format, 'english' otherwise.
        """
        if all(c in 'O.' for c in text) and len(text) % 6 == 0:
            return 'braille'
        return 'english'

    def _braille_to_dots(self, binary):
        """
        Converts a binary Braille representation to a dot pattern via bitmask.

        Args:
            binary (int): The binary representation of a Braille character.

        Returns:
            str: The dot pattern representation of the Braille character.
        """
        return ''.join('O' if binary & (1 << (5 - i)) else '.' for i in range(6))

    def _dots_to_binary(self, dots):
        """
        Converts a Braille dot pattern to its binary representation.

        Args:
            dots (str): The dot pattern representation of a Braille character.

        Returns:
            int: The binary representation of the Braille character.
        """
        return sum(1 << (5 - i) for i, dot in enumerate(dots) if dot == 'O')


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        return

    input_text = " ".join(sys.argv[1:])
    translator = Translator()
    
    if translator.detect_language(input_text) == 'braille':
        try:
            result = translator.braille_to_english(input_text)
        except TranslationError:
            result = translator.english_to_braille(input_text)
    else:
        result = translator.english_to_braille(input_text)
    
    print(result)

if __name__ == "__main__":
    main()
