
import sys

from abc import ABC, abstractmethod
from enum import Enum

#######################################################
# Constants
#######################################################
class Languages(Enum):
    BRAILLE = 1
    ENGLISH = 2
    
class Constants:
    BRAILLE_CHAR_LENGTH = 6
    ENG_TO_BRAILLE_MAP = {
        'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
        'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
        'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
        'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
        'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
        'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
        'y': 'OO.OOO',    'z': 'O..OOO',    '.': '..OO.O',    ' ': '......'
    }
    BRAILLE_TO_ENG_MAP = {v: k for k, v in ENG_TO_BRAILLE_MAP.items()}

    ENG_TO_BRAILLE_NUMBERS = {
        '1': 'O.....',    '2': 'O.O...',    '3': 'OO....',    '4': 'OO.O..',
        '5': 'O..O..',    '6': 'OOO...',    '7': 'OOOO..',    '8': 'O.OO..',
        '9': '.OO...',    '0': '.OOO..'
    }
    BRAILLE_TO_ENG_NUMBERS = {v: k for k, v in ENG_TO_BRAILLE_NUMBERS.items()}
    
    class BrailleFollows:
        CAPITAL = ".....O"
        NUMBER = ".O.OOO"
        DECIMAL = ".O...O"
    
#######################################################
# Language Detection
#######################################################
class DetectorStrategy(ABC):
    def __init__(self, sentence: str) -> None:
        self.sentence = sentence

    @abstractmethod
    def valid(self,) -> bool:
        ...

class Braille(DetectorStrategy):
    def is_multiple_of_6(self) -> bool:
        return len(self.sentence) % Constants.BRAILLE_CHAR_LENGTH == 0
    
    def contain_only_O_or_dot(self) -> bool:
        return all(char in {'O', '.'} for char in self.sentence)

    def is_valid_sequence(self) -> bool:
        instructions = Constants.BrailleFollows

        index = 0
        while index < len(self.sentence):
            sequence = self.sentence[index:index + Constants.BRAILLE_CHAR_LENGTH]
            if sequence not in (instructions.CAPITAL, instructions.NUMBER, instructions.DECIMAL)\
                and sequence not in Constants.BRAILLE_TO_ENG_MAP:
                return False
            index += Constants.BRAILLE_CHAR_LENGTH
        return True
    
    def valid(self) -> bool:
        return self.is_multiple_of_6() and self.contain_only_O_or_dot() and self.is_valid_sequence()

class English(DetectorStrategy):
    def all_valid_character(self) -> bool:
        return all(char.lower() in Constants.ENG_TO_BRAILLE_MAP or char.isdigit() for char in self.sentence)
    
    def valid(self) -> bool:
        return self.all_valid_character()

class LanguageDetector:
    def __init__(self, sentence: str) -> None:
        self.sentence = sentence
        self.detected_language = None

    def detect_language(self) -> Languages:
        if Braille(self.sentence).valid():
            self.detected_language = Languages.BRAILLE
        elif English(self.sentence).valid(): 
            self.detected_language = Languages.ENGLISH
        else:
            raise ValueError("Invalid sentence")
        
#######################################################
# Language Translation Strategy Pattern
#######################################################
class TranslatorStrategy(ABC):
    @abstractmethod
    def translate(self, sentence: str) -> str:
        ...

class BrailleToEnglishTranslation(TranslatorStrategy):
    def next_char(self, sentence: str, index: int) -> str:
        return sentence[index + Constants.BRAILLE_CHAR_LENGTH:index + Constants.BRAILLE_CHAR_LENGTH * 2]
    
    def get_english(self, char: str, number: bool = False) -> str:
        return (Constants.BRAILLE_TO_ENG_NUMBERS if number else Constants.BRAILLE_TO_ENG_MAP).get(char)
    
    def get_current_char(self, sentence: str, index: int) -> str:
        return sentence[index:index + Constants.BRAILLE_CHAR_LENGTH]
    
    def translate(self, sentence: str) -> str:
        instructions = Constants.BrailleFollows
        translated = []
        
        index = 0
        is_number_mode = False
        while index < len(sentence):
            char = self.get_current_char(sentence, index)

            if char in (instructions.CAPITAL, instructions.NUMBER, instructions.DECIMAL):
                next_char = self.next_char(sentence, index)
                if char == instructions.CAPITAL:
                    translated.append(self.get_english(next_char).upper())
                elif char == instructions.NUMBER:
                    is_number_mode = True
                    translated.append(self.get_english(next_char, is_number_mode))
                else: # DECIMAL
                    translated.append(self.get_english(next_char))    
                index += Constants.BRAILLE_CHAR_LENGTH
            elif char == "......":
                is_number_mode = False
                translated.append(self.get_english(char))
            else:
                translated.append(self.get_english(char, is_number_mode))

            index += Constants.BRAILLE_CHAR_LENGTH
        
        return "".join(translated)

class EnglishToBrailleTranslation(TranslatorStrategy):
    def translate(self, sentence: str) -> str:
        translated = []
        is_num = False

        for char in sentence:
            if char.isdigit():
                if not is_num:
                    translated.append(Constants.BrailleFollows.NUMBER)
                    is_num = True
                translated.append(Constants.ENG_TO_BRAILLE_NUMBERS[char])
            elif char.isalpha():
                is_num = False
                if char.isupper():
                    translated.append(Constants.BrailleFollows.CAPITAL)
                    translated.append(Constants.ENG_TO_BRAILLE_MAP[char.lower()])
                else:
                    translated.append(Constants.ENG_TO_BRAILLE_MAP[char])
            else:
                if char == " ":
                    is_num = False
                if char == "." and is_num:
                    translated.append(Constants.BrailleFollows.DECIMAL)
                translated.append(Constants.ENG_TO_BRAILLE_MAP[char])
        
        return "".join(translated)

class Translator:
    def __init__(self, language_detector: LanguageDetector):
        self.language_detector = language_detector
        self.translation_strategy = None
    
    def set_translation_strategy(self, strategy: TranslatorStrategy):
        self.translation_strategy = strategy
    
    def translate(self, sentence: str) -> str:
        self.language_detector.detect_language()
        detected_language = self.language_detector.detected_language
        
        if detected_language == Languages.BRAILLE:
            self.set_translation_strategy(BrailleToEnglishTranslation())
        elif detected_language == Languages.ENGLISH:
            self.set_translation_strategy(EnglishToBrailleTranslation())
        else:
            raise ValueError(f"Translation from {detected_language} not supported.")
        
        return self.translation_strategy.translate(sentence)
        
    
if __name__ == "__main__":
    input = " ".join(sys.argv[1:]).strip()
    language_detector = LanguageDetector(input)
    translation = Translator(language_detector).translate(input)
    print(translation)