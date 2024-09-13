import sys 
import re
from enum import Enum


class SpecialCharacters(Enum):
    """
    Enum class to represent the special characters in braille
    """
    CAPITAL = 1
    NUMBER = 2


class BrailleToEnglishMap:
    """
    Class to map braille blocks to english characters.
    """
    def __init__(self, is_number=False, is_capital=False):
        self.is_number = is_number
        self.is_capital = is_capital

    def map_braille_block(self, braille_block: str) -> str:
        """Maps a braille block to an english character. 
        Assumes that all braille blocks preceding this one and including this one are valid.
        """
        global BRAILLE_SPACE
        global BRAILLE_TO_ENGLISH
        global BRAILLE_TO_NUMBER
        global BRAILLE_TO_SPECIAL_CHARACTERS

        if self.is_number:
            # Case where it is a digit of a number
            if braille_block in BRAILLE_TO_NUMBER:
                return BRAILLE_TO_NUMBER[braille_block]
            # Case where it is the space following the number
            else:
                self.is_number = False
                return BRAILLE_TO_ENGLISH[braille_block]
        elif braille_block in BRAILLE_TO_SPECIAL_CHARACTERS:
            # Special character capital
            if BRAILLE_TO_SPECIAL_CHARACTERS[braille_block] == SpecialCharacters.CAPITAL:
                self.is_capital = True
            # Special character number
            else:
                self.is_number = True
            return ""
        else:
            # The previous character was the capital special character
            if self.is_capital:
                self.is_capital = False
                return BRAILLE_TO_ENGLISH[braille_block].upper()
            return BRAILLE_TO_ENGLISH[braille_block]


class EnglishToBrailleMap:
    """
    Class to map english characters to braille blocks
    """
    def __init__(self, is_number=False):
        self.is_number = is_number

    def map_character(self, character: str) -> str:
        """Maps an english character to a braille block.
        Assumes that all characters preceding the current one alongside the current one are valid.
        """
        global ENGLISH_TO_BRAILLE
        global NUMBER_TO_BRAILLE
        global SPECIAL_CHARACTERS_TO_BRAILLE

        # Where the character is an alphabetical character or a space
        if character.lower() in ENGLISH_TO_BRAILLE:
            # The character is a capital letter
            if character.isalpha() and character.isupper():
                return SPECIAL_CHARACTERS_TO_BRAILLE[SpecialCharacters.CAPITAL] + ENGLISH_TO_BRAILLE[character.lower()]
            return ENGLISH_TO_BRAILLE[character]
        # Where the character is a number
        else:
            # If the previous character was a number
            if self.is_number:
                return NUMBER_TO_BRAILLE[character]
            # Setting the is_number flag to True so for the next digit we do not also attach the number special character
            else:
                self.is_number = True
                return SPECIAL_CHARACTERS_TO_BRAILLE[SpecialCharacters.NUMBER] + NUMBER_TO_BRAILLE[character]


# Constants for mapping English to Braille 
BRAILLE_SPACE = '......'
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': BRAILLE_SPACE
}
NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
SPECIAL_CHARACTERS_TO_BRAILLE = {
    SpecialCharacters.CAPITAL: '.....O',
    SpecialCharacters.NUMBER: '.O.OOO'
}

# Constant for mapping Braille to English
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_SPECIAL_CHARACTERS = {v: k for k, v in SPECIAL_CHARACTERS_TO_BRAILLE.items()}

def is_braille(text: str) -> bool:
    """Check if the input text is in braille format
    
        Parameters:
            text (str): The input text that needs to be checked
        
        Returns:
            output (bool): True if the input text is in braille format, False otherwise
    """
    if len(text) % 6 == 0 and re.fullmatch(r'[O.]+', text):
        return True
    return False

def translate_english_to_braille(text: str) -> str:
    """Translates english text to braille. 
    Assumes that the input english text is valid and follows the guidelines provided in the problem statement.
    
        Parameters:
            text (str): The text in english that needs to be translated to braille

        Returns:
            output (str): The braille representation of the input english text
    """
    ENGLISH_TO_BRAILLE = EnglishToBrailleMap()
    final_braille_text = []
    for ch in text:
        final_braille_text.append(ENGLISH_TO_BRAILLE.map_character(ch))
    return "".join(final_braille_text)
    
def translate_braille_to_english(text: str) -> str:
    """Translates braille text to english
    Assumes that the input braille text is valid and follows the guidelines provided in the problem statement.

        Parameters:
            text (str): The text in braille that needs to be translated to english

        Returns:
            output (str): The english representation of the input braille text
    """
    BRAILLE_TO_ENGLISH = BrailleToEnglishMap()
    final_english_text = []
    text_index = 0
    while text_index < len(text):
        curr_braille_block = text[text_index:text_index+6]
        final_english_text.append(BRAILLE_TO_ENGLISH.map_braille_block(curr_braille_block))
        text_index += 6
    return "".join(final_english_text)

if __name__ == "__main__":
    # Checking if we have received program arguments for the translator
    if len(sys.argv) <= 1:
        raise Exception("Improper input detected")
    
    # Appending all of the program arguments to form a single string
    text = " ".join(sys.argv[1:])

    # Checking if the input text is in braille format
    if is_braille(text):
        # Translating the braille text to english
        print(translate_braille_to_english(text))
    else:
        # Translating the english text to braille
        print(translate_english_to_braille(text))
