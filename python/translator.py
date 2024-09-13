from typing import Literal
from braille_translator import BrailleTranslator 
from helpers import detect_language
import sys

args = sys.argv[1:]

translator = BrailleTranslator()

for idx, input_string in enumerate(args):
    language: Literal["Braille", "English"] = detect_language(input_string)
    
    if language == "Braille":
        translated_text = translator.translate_to_english(input_string)
    else:
        translated_text = translator.translate_to_braille(input_string)
    
    print(translated_text, end="")
    if idx < len(args) - 1:
        # Add a Braille space between translated arguments
        print(translator.english_to_braille_dict[' '], end="")
