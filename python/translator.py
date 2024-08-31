import logging
import argparse
from enum import Enum
import logging
from collections import Counter

# Add a handler for output to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set handler level to DEBUG

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
console_handler.setFormatter(formatter)

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Default level is INFO

# Add the handler to the logger
logger.addHandler(console_handler)

def configure_logging(debug):
    if debug:
        logger.setLevel(logging.DEBUG)

# Exceptions
class TranslationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Enums
class SpecialBrailleChar(Enum):
    CAPITAL = ".....O"
    NUMBER = ".O.OOO"

special_braille_chars = {char.value for char in SpecialBrailleChar}

# Preprocessed Constants
english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"
}

english_numbers_to_braille = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}
braille_to_english = {value : key for key, value in english_to_braille.items()}
braille_to_english_numbers = {value : key for key, value in english_numbers_to_braille.items()}

# Helper Functions
def is_text_supported_in_language(text, supported_language_chars):
    """
    Check if a text contains only digits or characters in the supported languageset.

    Args:
        text (str): The input text.
        supported_language_chars (set/dict): Valid characters for the language.

    Returns:
        bool: True if supported, False otherwise.
    """
    for letter in text:
        if not(letter.isdigit() or letter.lower() in supported_language_chars):
            return False
    
    return True

def is_text_braille(text):
    """
    Check if a text is valid Braille representation.

    Args:
        text (str): The input text.

    Returns:
        bool: True if valid Braille, False otherwise.
    """
    if not (len(text) % 6 == 0):
        return False

    letters = Counter(text)
    
    if len(letters) > 2:
        return False

    for letter in letters.keys():
        if letter not in {'.', 'O'}:
            return False
    
    return True
    
def parse_braille_string_to_language(braille_text, braille_to_language, braille_to_numbers):
    """
    Translate Braille text to a language using provided mappings.

    Args:
        braille_text (str): The Braille text to translate.
        braille_to_language (dict): Mapping from Braille patterns to language characters.
        braille_to_numbers (dict): Mapping from Braille patterns to numbers.

    Returns:
        str: Translated text in the target language.
    
    Raises:
        TranslationError: If Braille patterns cannot be translated or are used incorrectly.
    """
    i = 0
    translated_text = ''
    letters = [braille_text[i: i + 6] for i in range(0, len(braille_text), 6)]
    total_letters = len(letters)
    logger.debug("Began parsing braille to desired language.")
    
    while i < total_letters:
        letter = letters[i]
        logger.debug(f"Translating Letter: {letter}")
        if letter not in braille_to_language or letter not in special_braille_chars:
            raise TranslationError(f"Unable to translate the following letter {letter}")
        
        letter_translation = braille_to_language[letter]
        if letter_translation == SpecialBrailleChar.CAPITAL.value:
            if i + 1 >= total_letters:
                raise TranslationError(f"Invalid use of captial follows in braille. Requires a letter to follow the use of the capital follows character")
            
            i += 1
            cap_letter = braille_to_language[letters[i]]
            translated_text += cap_letter.upper()
        elif letter_translation == SpecialBrailleChar.NUMBER.value:
            while i + 1 < total_letters and letters[i + 1] in braille_to_numbers:
                i += 1
                translated_text += braille_to_numbers[letters[i]]
        else:
            translated_text += letter_translation
        logger.debug(f"Updated translation string: {translated_text}")
        i += 1

    return translated_text

def parse_language_to_braille(text, language_to_braille, number_to_braille):
    """
    Convert text to Braille using provided mappings.

    Args:
        text (str): The input text to convert.
        language_to_braille (dict): Mapping from language characters to Braille patterns.
        number_to_braille (dict): Mapping from digits to Braille patterns.

    Returns:
        str: Braille representation of the text.
    
    Raises:
        TranslationError: If text contains characters that cannot be translated.
    """
    i = 0
    braille_translation = ""
    logger.debug("Began parsing language to braille.")
    while i < len(text):
        letter = text[i]
        logger.debug(f"Translating Letter: {letter}")
        if letter not in number_to_braille and letter.lower() not in language_to_braille :
            raise TranslationError(f"Unable to translate the following letter {letter}")
        
        if letter.isdigit():
            braille_translation += SpecialBrailleChar.NUMBER.value
            braille_translation += number_to_braille[letter]
            while i + 1 < len(text) and text[i + 1].isdigit():
                i += 1
                braille_translation += number_to_braille[text[i]]
        elif letter.isupper():
            braille_translation += SpecialBrailleChar.CAPITAL.value
            braille_translation += language_to_braille[letter.lower()]
        else:
            braille_translation += language_to_braille[letter]
        
        logger.debug(f"Updated braille translation string: {braille_translation}")
        i += 1
    
    return braille_translation
         
def translate_text(text):
    """
    Translate text between Braille and English.

    Args:
        text (str): The input text to translate.

    Returns:
        str: Translated text in the target language.

    Raises:
        TranslationError: If the text is not in a supported format for translation.
    """
    if is_text_braille(text):
        logger.debug("Text is valid Braille.")
        return parse_braille_string_to_language(text, braille_to_english, braille_to_english_numbers)
    elif is_text_supported_in_language(text, english_to_braille):
        logger.debug("Text is valid English.")
        return parse_language_to_braille(text, english_to_braille, english_numbers_to_braille)
    else:
        raise TranslationError(f"Unable to translate input text. Note that only basic Braille/English are supported.")
    
def main():
    parser = argparse.ArgumentParser(
        prog="Braille Translator",
        description="CLI tool that will translate english to braille and vice versa",
        epilog="Thanks for using my tool. Made with love for the Shopify Eng Intern Challenge. :)"
    )
    
    parser.add_argument('input_text_to_translate', nargs='+', help="String that we want translated. Input string can be either Braille/English and the program will translate it automatically.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")
    
    arguments = parser.parse_args()
    configure_logging(arguments.debug)
    
    logger.debug(f"Captured Arguments: {arguments}")
    
    # added below but note that argparse enforces that an argument is passed in. 
    if not arguments.input_text_to_translate:    
        return
    
    text = ' '.join(arguments.input_text_to_translate).strip()
    
    logger.debug(f"Translating input: {text}")
    
    try:
        translated_text = translate_text(text)
    except TranslationError as e:
        print(f"Error: {e.message}")
        return
    
    print(f"{translated_text}")
    
if __name__ == "__main__":
    main()
