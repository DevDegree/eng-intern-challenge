import sys

from braille_translator import BrailleTranslator 
from helpers import detect_language

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 translator.py <text to translate (english/braille)>")
        sys.exit(1)

    translator = BrailleTranslator()

    for idx, input_text in enumerate(args):
        language = detect_language(input_text)
        
        try:
            if language == "Braille":
                translated_text = translator.translate_to_english(input_text)
            else:
                translated_text = translator.translate_to_braille(input_text)
        except Exception as e:
            print(f"Error translating '{input_text}': {e}", file=sys.stderr)
            continue
        
        print(translated_text, end="")
        if idx < len(args) - 1:
            print(translator.english_to_braille_dict[' '], end="")

if __name__ == "__main__":
    main()
