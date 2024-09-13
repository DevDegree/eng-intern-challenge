import sys
from abc import abstractmethod, ABC
from typing import List

BRAILLE_ALPHABET = {
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
}
BRAILLE_NUMBERS = {
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
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
BRAILLE_SPACE = '......'


def is_braille(input_strs: List[str]) -> bool:
    """Check if all strings in the input list are valid Braille."""
    for input_str in input_strs:
        if len(input_str) % 6 != 0:  # Valid Braille will be divisible by 6 because each 'letter' is 6 chars
            return False
        if not all(char in '.O' for char in input_str):
            return False
    return True


class TranslationStrategy(ABC):
    """Abstract base class for translation strategies.

    This class defines the interface for translating a list of strings.
    """

    @abstractmethod
    def translate(self, input_str: List[str]) -> str:
        pass


class EnglishToBrailleStrategy(TranslationStrategy):
    """Concrete strategy for translating English text to Braille."""

    @staticmethod
    def translate_element(input_str: str):
        """Translate a single English string to Braille."""
        num_code_prepended = False
        translated = []
        for char in input_str:
            if char.isupper():
                translated.append(CAPITAL_FOLLOWS + BRAILLE_ALPHABET[char.lower()])
            elif char.isnumeric():
                if not num_code_prepended:
                    translated.append(NUMBER_FOLLOWS)
                    num_code_prepended = True
                translated.append(BRAILLE_NUMBERS[char])
            elif char == ' ':
                translated.append(BRAILLE_SPACE)
                num_code_prepended = False  # 'number mode' should be reset after a space
            else:
                translated.append(BRAILLE_ALPHABET[char])
        return ''.join(translated)

    def translate(self, input_strs: List[str]) -> str:
        """Translate a list of English strings to Braille."""
        translated_all = []
        for input_str in input_strs:
            translated_all.append(self.translate_element(input_str))
        return BRAILLE_SPACE.join(translated_all)


class BrailleToEnglishStrategy(TranslationStrategy):
    """Concrete strategy for translating Braille text to English."""

    def __init__(self):
        """Initialize the Braille to English strategy with reversed mappings for simplicity."""
        self.braille_english_letters = {v: k for k, v in BRAILLE_ALPHABET.items()}
        self.braille_english_nums = {v: k for k, v in BRAILLE_NUMBERS.items()}

    def translate_element(self, input_str: str):
        """Translate a single Braille string to English."""
        num_mode = False
        is_capital = False
        translated = []

        for i in range(0, len(input_str), 6):
            char = input_str[i: i + 6]
            if char == BRAILLE_SPACE:
                translated.append(' ')
                num_mode = False  # Reset number mode after a space
            elif is_capital:
                translated.append(self.braille_english_letters[char].upper())
                is_capital = False
            elif char == CAPITAL_FOLLOWS:
                is_capital = True
            elif num_mode:
                translated.append(self.braille_english_nums[char])
            elif char == NUMBER_FOLLOWS:
                num_mode = True
            else:
                translated.append(self.braille_english_letters[char])

        return ''.join(translated)

    def translate(self, input_strs: List[str]) -> str:
        """Translate a list of Braille strings to English."""
        translated_all = []
        for input_str in input_strs:
            translated_all.append(self.translate_element(input_str))
        return ' '.join(translated_all)


class Translator:
    """Context class that uses a translation strategy to translate input text."""

    def __init__(self, strategy: TranslationStrategy):
        self._strategy = strategy

    def translate(self, input_strs: List[str]) -> str:
        return self._strategy.translate(input_strs)


def main():
    if len(sys.argv) < 2:
        print("Usage: translator.py <text_to_translate>")

    input_text = sys.argv[1:]  # Skip the first argument (script name)

    # Assign translation strategy based on input text
    if is_braille(input_text):
        strategy = BrailleToEnglishStrategy()
    else:
        strategy = EnglishToBrailleStrategy()

    translator = Translator(strategy)
    translation = translator.translate(input_text)
    print(translation)


if __name__ == '__main__':
    main()
