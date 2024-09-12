from language_classes.braille_english_converter import BrailleEnglishConverter

class LanguageConverter:
    """
    Class for converting text between languages.
    """



    def __init__(self,supported_languages):
        """
        Initialize the language detector.
        """
        self.supported_languages = supported_languages

        # add more converters here as needed
        self.braille_english_converter = BrailleEnglishConverter("./translate_data/english_to_braille.json")
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
            elif source_language == 'english' and target_language == 'braille':
                return self.braille_english_converter.convert_english_to_braille(text)
            elif source_language == 'braille' and target_language == 'english':
                return self.braille_english_converter.convert_braille_to_english(text)
            else:
                raise ValueError(f"Conversion from target language '{target_language}'\
                                to source language '{source_language}' is not supported")
        except ValueError as e:
            raise ValueError(f"Error converting text: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected Error occurred: {str(e)}")
        

    