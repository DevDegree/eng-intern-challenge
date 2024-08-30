import re

class LanguageConverter:
    """
    Class for converting text between languages.
    """

    supported_languages = ['english', 'braille']

    def __init__(self):
        """
        Initialize the language detector.
        """
        pass

    def convert(self, text, source_language, target_language):
        """
        Convert the given text from the source language to the target language.
        """
        
        if source_language not in self.supported_languages:
            raise ValueError(f"Unsupported source language '{source_language}'")
        if target_language not in self.supported_languages:
            raise ValueError(f"Unsupported target language '{target_language}'")
        
        try:
            if source_language == target_language:
                return text
            if source_language == 'english' and target_language == 'braille':
                return self.__convert_english_to_braille(text)
            elif source_language == 'braille' and target_language == 'english':
                return self.__convert_braille_to_english(text)
            else:
                raise ValueError(f"Conversion from target language '{target_language}'\
                                to source language '{source_language}' is not supported")
        except ValueError as e:
            raise ValueError(f"Error converting text: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected Error occurred: {str(e)}")
        

    def __convert_braille_to_english(self, braille_text):
        """
        Convert the given Braille text to English.

        Each character is stored as a series of O (the letter O) or . (a period), and is 6 characters long,
        reading left to right, line by line, starting at the top left. 
        When a Braille 'capital follows' symbol is read, assume only the next symbol should be capitalized.
        When a Braille 'number follows' symbol is read, assume all following symbols are numbers until the 
        next space symbol.
        """

        english_text = ""
        isNumber = False

        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i+6]
            

        return english_text

    def __convert_english_to_braille(self, english_text):
        """
        Convert the given English text to Braille.
        """
        braille_text = ""
        for char in text:
            if char.isupper():
                braille_text += "⠠" + char.lower()
            else:
                braille_text += char
        return braille_text