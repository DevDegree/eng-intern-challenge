"""This module handles interactions for BrailleTranslator."""

import sys
from language_utils.language_converter import LanguageConverter
from language_utils.language_detector import LanguageDetector


class BrailleTranslator:
    """
    Class for automatically detecting and applying English <-> Braille translation.
    """

    def __init__(self):
        """
        Initialize the translator, with classes for language detection and translating.
        """
        supported_languages = ["english", "braille"]

        self.language_detector = LanguageDetector(supported_languages)
        self.language_converter = LanguageConverter(supported_languages)

    def translate(self, text):
        """
        Detect the given language, and convert from Braille -> English or English -> Braille.
        """
        result = ""
        try:
            language = self.language_detector.detect(text)
            if language == "english":
                result = self.language_converter.convert(text, "english", "braille")
            if language == "braille":
                result = self.language_converter.convert(text, "braille", "english")
        except ValueError as e:
            raise Exception(f"ERROR: Error parsing input '{text}': {str(e)}")
        except Exception as e:
            raise Exception(f"ERROR: Unexpected Error occurred: {str(e)}")

        return result


def main():
    """
    Main function driver.
    """

    if len(sys.argv) < 2:
        print("Usage: python main.py <english/braille text>")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    translated_text = translator.translate(user_input)
    print(f"{translated_text}")


if __name__ == "__main__":
    main()
