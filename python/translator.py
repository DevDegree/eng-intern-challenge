import sys
from typing import Literal


BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',

    ' ': '......',  

    'capital': '.....O',
    'number': '.O.OOO',
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

BRAILLE_ALPHABET_TO_ENGLISH = {v: k for k, v in BRAILLE_ALPHABET.items()}
BRAILLE_NUMBERS_TO_DIGITS = {v: k for k, v in BRAILLE_NUMBERS.items()}

class Translator:
    def __init__(self):
        message = self.get_message()
        if self.check_message_type(message) == 'braille':
            print(self.braille_to_english(message))
        else:
            print(self.english_to_braille(message))

    def get_message(self) -> str:
        """
        Returns the message that user entered via CLI
        :return: message
        """
        # Join all arguments into a single string
        message = " ".join(sys.argv[1:])
        return message

    def check_message_type(self, message: str) -> Literal["english", "braille"]:
        """
        Determines whether the message is in English or Braille
        :param message: message that user entered
        :return: 'english' or 'braille'
        """
        char_count_map = {}

        for char in message:
            char_count_map[char] = char_count_map.get(char, 0) + 1

        total_count = char_count_map.get('.', 0) + char_count_map.get('O', 0)
        if total_count == len(message):
            return "braille"

        return "english"
    
    def english_to_braille(self, message: str) -> str:
        """
        Converts English text to Braille.
        :param message: English text
        :return: Braille translation
        """

        translated_message = ""
        number_mode = False

        for char in message:

            if char.isupper():
                translated_message += BRAILLE_ALPHABET['capital']
                translated_message += BRAILLE_ALPHABET[char.lower()]
            
            elif char.isdigit():
                if not number_mode:
                    number_mode = True
                    translated_message += BRAILLE_ALPHABET['number']
                
                translated_message += BRAILLE_NUMBERS[char]
            
            elif char == " ":
                number_mode = False
                translated_message += BRAILLE_ALPHABET[' ']
            
            else:
                translated_message += BRAILLE_ALPHABET[char] 
        
        return translated_message


        

    def braille_to_english(self, message: str) -> str:
        """
        Converts Braille to English text.
        :param message: Braille text
        :return: English translation
        """

        translated_message = ""
        i = 0

        capital_mode = False
        number_mode = False



        while i < len(message):

            skip_turn = False

            symbol = message[i:i+6]
            i += 6
            if symbol == BRAILLE_ALPHABET['capital']:
                capital_mode = True
                skip_turn = True

            elif symbol == BRAILLE_ALPHABET['number']:
                number_mode = True
                skip_turn = True

            elif symbol == BRAILLE_ALPHABET[' ']:
                number_mode = False
        
            
            letter = ''

            if skip_turn:
                letter = ''
            
            elif number_mode:
                letter = BRAILLE_NUMBERS_TO_DIGITS[symbol]

            elif capital_mode: 
                letter = BRAILLE_ALPHABET_TO_ENGLISH[symbol].upper()
                capital_mode = False

            else:
                letter = BRAILLE_ALPHABET_TO_ENGLISH[symbol] 
            
            translated_message += letter

        
        return translated_message

        

if __name__ == "__main__":
    Translator()

