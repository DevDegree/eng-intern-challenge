from typing import List
from src.constants.alphabet_converter import BRAILLE_TO_ENGLISH, BRAILLE_TO_NUMBER
from src.constants.braille_constants import BrailleConstant
from src.constants.english_constants import EnglishConstant
from src.constants.translation_mode import TranslationMode
from src.constants.constants import BRAILLE_CHARACTER_LENGTH
from src.parser.base_parser import BaseParser

class BrailleParser(BaseParser):
    def parse(self, text: str) -> List[List[str]]:
        characters_grouped_by_word = []

        braille_characters = [(text[i:i+BRAILLE_CHARACTER_LENGTH]) for i in range(0, len(text), BRAILLE_CHARACTER_LENGTH)]
        current_word = []
        for character in braille_characters:
            if(character == BrailleConstant.SPACE.value):
                characters_grouped_by_word.append(current_word)
                current_word = []
            else:
                current_word.append(character)
        characters_grouped_by_word.append(current_word)
        return characters_grouped_by_word

    def translate_line(self, characters: List[str]) -> str:
        translated_string = []
        translation_mode = TranslationMode.DEFAULT
        
        for character in characters:
            if(character == BrailleConstant.CAPITAL_FOLLOWS.value):
                translation_mode = TranslationMode.CAPITAL
                continue
            elif(character == BrailleConstant.NUMBER_FOLLOWS.value):
                translation_mode = TranslationMode.NUMBER
                continue

            if(translation_mode == TranslationMode.CAPITAL):
                translated_string.append(BRAILLE_TO_ENGLISH[character])
                translation_mode = TranslationMode.DEFAULT
            elif(translation_mode == TranslationMode.NUMBER):
                translated_string.append(BRAILLE_TO_NUMBER[character])
            else:
                translated_string.append(BRAILLE_TO_ENGLISH[character].lower())
        return translated_string

    def translate_all(self, text: str) -> str:
        parsed_text = self.parse(text)
        words = ["".join(self.translate_line(line)) for line in parsed_text]
        return EnglishConstant.SPACE.value.join(words)