import sys

class BrailleTranslator:
    def __init__(self, input_text: str, is_braille_input: bool):
        """
        Initialize the BrailleTranslator with the input text and determine if it is Braille or English.

        Args:
            input_text (str): The text to be translated.
            is_braille_input (bool): A flag indicating if the input is Braille (True) or English (False).
        """
        self.input_text = input_text
        self.is_braille_input = is_braille_input

        # English -> Braille (raised dots represented as O, unraised dots as .)
        self.english_to_braille_map = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
            'z': 'O..OOO', ' ': '......',  # Space
            '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
            ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
            '<': '.OO..O', '>': 'O..OO.'
        }

        # Braille -> English
        self.braille_to_english_map = {v: k for k, v in self.english_to_braille_map.items()}

        # Letter -> Digit
        self.letter_to_digit = {
            'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
            'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
        }

        # Digit -> Braille
        self.digit_to_braille = {
            '1': self.english_to_braille_map['a'],
            '2': self.english_to_braille_map['b'],
            '3': self.english_to_braille_map['c'],
            '4': self.english_to_braille_map['d'],
            '5': self.english_to_braille_map['e'],
            '6': self.english_to_braille_map['f'],
            '7': self.english_to_braille_map['g'],
            '8': self.english_to_braille_map['h'],
            '9': self.english_to_braille_map['i'],
            '0': self.english_to_braille_map['j'],
        }

        # Add capitalization and number markers
        self.capitalization_marker = '.....O'  # Prefix for capital letters
        self.number_marker = '.O.OOO'          # Prefix for numbers

    def translate(self) -> str:
        """Translate the input text based on its type (English or Braille)."""
        if self.is_braille_input:
            return self.braille_to_english(self.input_text)
        else:
            return self.english_to_braille(self.input_text) 

    def braille_to_english(self, braille_text: str) -> str:
        """Convert Braille text to English."""
        english = []        # List to store the English result
        is_capital = False  # Flag to keep track if the next letter should be capitalized
        is_number = False   # Flag to keep track of when in a number sequence 

        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i+6] # get a chunk of 6 chars

            if braille_char == self.capitalization_marker:
                is_capital = True
                continue    #skip further processing for this interation

            if braille_char == self.number_marker:
                is_number = True  # Enter number mode
                continue
            
            english_char = self.braille_to_english_map.get(braille_char, ' ')

            # Convert letter to digit if in 'number mode'
            if is_number:
                english_char = self.letter_to_digit.get(english_char, english_char)

            # Apply capitalization if needed
            if is_capital:
                english_char = english_char.upper()
                is_capital = False
            
            # Reset 'number mode' when encountering a space in Braille
            if braille_char == '......':
                is_number = False

            english.append(english_char)

        return ''.join(english)
    

    def english_to_braille(self, text: str) -> str:
        """Convert English text to Braille."""
        braille = []        # list to store the Braille result
        is_number = False   # Flag to keep track of when we are in a number sequence 

        for char in text:    
            # Handle capitalization
            if char.isupper():
                braille.append(self.capitalization_marker)
                char = char.lower()
            
            # Handle digits
            if char.isdigit():
                if not is_number:
                    braille.append(self.number_marker)
                    is_number = True
                # Use the digit_to_braille map to get the corresponding Braille pattern
                braille_char = self.digit_to_braille.get(char, '......')
                braille.append(braille_char)
                continue  # Skip to the next character

            # Reset 'number mode' after a space or non-digit character
            if char == ' ':
                is_number = False 
                braille.append('......')
                continue
            
            # Append the corresponding Braille character
            braille_char = self.english_to_braille_map.get(char, '......')
            braille.append(braille_char)

        return ''.join(braille) # joint list into final Braille string

    @staticmethod
    def is_braille(input_string: str) -> bool:
        """Detect if the input string is Braille"""
        for char in input_string:
            if char not in 'O. ': # check to see if there are any char's other than '0' '.' or 'space'
                return False
        return True

def main():
    if len(sys.argv) < 2:
        return
    
    # Join all arguments (after script name) into a single string
    input_string = ' '.join(sys.argv[1:])

    is_braille_input = BrailleTranslator.is_braille(input_string)

    translator = BrailleTranslator(input_string, is_braille_input)
    if is_braille_input:
        result = translator.braille_to_english(input_string)
    else:
        result = translator.english_to_braille(input_string)
    
    print(result)

if __name__ == "__main__":
    main()
