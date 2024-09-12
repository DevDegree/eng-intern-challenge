import re

class LanguageDetector:
    """
    Class for automatically detecting the language of a given text.
    """



    def __init__(self, supported_languages):
        """
        Initialize the language detector.
        """
        self.supported_languages = supported_languages
        pass

    def detect(self, text):
        """
        Detect the language of the given text.
        Default language is English.
        """

        language = "english"

        # BRAILLE check
        # Check if the text contains any characters other than . and 0 and length is multiple of 6
        pattern = r'[^.O]'
        match = re.search(pattern, text)
        if match is None and len(text) % 6 == 0:
            language = "braille"
            
        return language