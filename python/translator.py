import sys
from typing import List
from input_text_processor import InputTextProcessor
from braille_translation_service import BrailleTranslationService

class TranslationController:
    """
    A controller class for handling translation between English text and Braille.
    This class utilizes the BrailleTranslationService to perform translations and 
    processes the input text to determine whether it is in Braille or English.
    Attributes:
        braille_service (BrailleTranslationService): An instance of the BrailleTranslationService 
                                                     used for performing the actual translations.
    """

    def __init__(self):
        """
        Initializes the TranslationController with a BrailleTranslationService instance.
        """
        self.braille_service = BrailleTranslationService()
    
    def translate(self, text: str) -> str:
        """
        Translates the given text between English and Braille.

        Args:
            text (str): The input text to be translated.

        Returns:
            str: The translated text.

        Raises:
            InvalidBrailleCharacterError: If the Braille text contains invalid characters.
            IncompleteBrailleSequenceError: If the Braille text length is not a multiple of the cell size.
        """
        input_processor = InputTextProcessor(text)
        input_contains_braille = input_processor.contains_only_braille(text)

        if input_contains_braille:
            if input_processor.is_valid_braille(text):
                split_cells = input_processor.braille_to_cells(text)
                return self.translate_to_english(split_cells)
        else:
            return self.translate_to_braille(text)

    def translate_to_braille(self, text: str) -> str:
        """
        Translates English text to Braille.

        Args:
            text (str): The English text to be translated.

        Returns:
            str: The Braille representation of the input text.
        """
        translated = []

        # Passing around an iterator to allow for lookahead when translating Capital and Number symbols
        english_char_iterator = iter(text)

        for char in english_char_iterator:
            braille_cell = self.braille_service.english_to_braille(char, english_char_iterator)
            translated.append(braille_cell)
        
        return ''.join(translated)

    def translate_to_english(self, split_cells: List[str]) -> str:
        """
        Translates Braille cells to English text.

        Args:
            split_cells (List[str]): A list of Braille cells to be translated.

        Returns:
            str: The English representation of the Braille cells.
        """
        translated = []

        # Passing around an iterator to allow for lookahead when translating Capital and Number symbols
        braille_char_iterator = iter(split_cells)

        for braille_char in braille_char_iterator:
            english_char = self.braille_service.braille_to_english(braille_char, braille_char_iterator)
            translated.append(english_char)
        
        return ''.join(translated)


def main():
    """
    Main function to handle command-line input and perform translation.
    """
    words = [argument.strip() for argument in sys.argv[1:]]
    input_text = ' '.join(words)
    translator = TranslationController()
    
    result = translator.translate(input_text)
    print(result)

if __name__ == "__main__":
    main()