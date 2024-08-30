import sys
from language_classes.language_converter import LanguageConverter
from language_classes.language_detector import LanguageDetector

class BrailleTranslator:
    """
    Class for automatically detecting and applying English <-> Braille translation.
    """

    def __init__(self):
        """
        Initialize the translator, with classes for language detection and translating.
        """
        self.languageDetector = LanguageDetector()
        self.languageConverter = LanguageConverter()


    def translate(self, text):
        """
        Detect the given language, and convert it either from Braille -> English or English -> Braille.
        """
        try: 
            language = self.languageDetector.detect(text)
            if language == 'english':
                return self.languageConverter.convert(text, 'english', 'braille', )
            elif language == 'braille':
                return self.languageConverter.convert(text, 'braille', 'english')
        except ValueError as e:
            raise Exception(f"ERROR: Error parsing input '{text}': {str(e)}")
        except Exception as e:
            raise Exception(f"ERROR: Unexpected Error occurred: {str(e)}")

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <english/braille>")
        sys.exit(1)
    
    translator = BrailleTranslator()
    user_input = sys.argv[1]
    translated_text = translator.translate(user_input)
    print(f"{translated_text}")
    
    

if __name__ == "__main__":
    main()
