from typing import List
from src.constants.translation_mode import TranslationMode
from src.parser.base_parser import BaseParser
from src.constants.alphabet_converter import ENGLISH_TO_BRAILLE, FOLLOWS_TO_BRAILLE, NUMBER_TO_BRAILLE
from src.constants.braille_constants import BrailleConstant
from src.constants.english_constants import EnglishConstant

class EnglishParser(BaseParser):
    def parse(self, text: str) -> List[List[str]]:
        characters_grouped_by_word = []

        current_word = []
        for character in text:
            if(character == EnglishConstant.SPACE.value):
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
            if(translation_mode != TranslationMode.NUMBER and character.isdigit()):
                translated_string.append(FOLLOWS_TO_BRAILLE[EnglishConstant.NUMBER_FOLLOWS.value])
                translation_mode = TranslationMode.NUMBER
            elif(character.isupper()):
                translation_mode = TranslationMode.CAPITAL

            if(translation_mode == TranslationMode.CAPITAL):        
                translated_string.append(FOLLOWS_TO_BRAILLE[EnglishConstant.CAPITAL_FOLLOWS.value])
                translated_string.append(ENGLISH_TO_BRAILLE[character])
                translation_mode = TranslationMode.DEFAULT
            elif(translation_mode == TranslationMode.NUMBER):
                translated_string.append(NUMBER_TO_BRAILLE[character])
            else:
                translated_string.append(ENGLISH_TO_BRAILLE[character.upper()])
        return translated_string

    def translate_all(self, text: str) -> str:
        parsed_text = self.parse(text)
        words = ["".join(self.translate_line(line)) for line in parsed_text]

        return BrailleConstant.SPACE.value.join(words)