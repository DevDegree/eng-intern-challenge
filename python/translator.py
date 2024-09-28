import sys

class BrailleTranslator:
    # Length of a Braille character
    braille_input_length = 6  # Braille consists of 6 characters

    def __init__(self, is_braille_input: bool = False):
        """
        Initialize the BrailleTranslator with a flag indicating if the input is Braille or English.

        Args:
            is_braille_input (bool): A flag indicating if the input is Braille (True) or English (False).
        """
        # self.input_text = input_text
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

        # Capitalization and number markers
        self.capitalization_marker = '.....O'  # Prefix for capital letters
        self.number_marker = '.O.OOO'          # Prefix for numbers
        
        # Initialize state attributes
        self.is_capital = False # Flag to keep track if the next letter should be capitalized
        self.is_number = False  # Flag to keep track of when in a number sequence 
    
    def reset_state(self):
        """Reset the internal state for capitalization and number mode."""
        self.is_capital = False
        self.is_number = False

    def toggle_capital(self):
        """Toggle the capitalization state."""
        self.is_capital = not self.is_capital

    def set_number_mode(self):
        """Enable number mode."""
        self.is_number = True

    def unset_number_mode(self):
        """Disable number mode."""
        self.is_number = False

    def translate(self, input_text: str) -> str:
        """
        Translate the input text based on its type (English or Braille).
        
        Args:
            input_text (str): The text to be translated.
        
        Returns:
            str: The translated text.
        """
        if self.is_braille_input:
            return self.braille_to_english(input_text)
        else:
            return self.english_to_braille(input_text) 

    def braille_to_english(self, braille_text: str) -> str:
        """Convert Braille text to English."""
        english = []        # List to store the English result
        self.reset_state()  # Reset the state before starting translation

        for i in range(0, len(braille_text), self.braille_input_length):
            braille_char = braille_text[i:i+self.braille_input_length] # get a chunk of 6 chars

            if braille_char == self.capitalization_marker:
                self.toggle_capital()
                continue    #skip further processing for this interation

            if braille_char == self.number_marker:
                self.set_number_mode()
                continue
            
            english_char = self.braille_to_english_map.get(braille_char, ' ')

            # Convert letter to digit if in 'number mode'
            if self.is_number:
                english_char = self.letter_to_digit.get(english_char, english_char)

            # Apply capitalization if needed
            if self.is_capital:
                english_char = english_char.upper()
                self.toggle_capital()
            
            # Reset 'number mode' when encountering a space in Braille
            if braille_char == '......':
                self.unset_number_mode()

            english.append(english_char)

        return ''.join(english)
    

    def english_to_braille(self, text: str) -> str:
        """Convert English text to Braille."""
        braille = []        # List to store the Braille result
        self.reset_state()  # Reset the state before starting translation

        for char in text:    
            # Handle capitalization
            if char.isupper():
                braille.append(self.capitalization_marker)
                char = char.lower()
            
            # Handle digits
            if char.isdigit():
                if not self.is_number:
                    braille.append(self.number_marker)
                    self.set_number_mode()
                # Use the digit_to_braille map to get the corresponding Braille pattern
                braille_char = self.digit_to_braille.get(char, '......')
                braille.append(braille_char)
                continue  # Skip to the next character

            # Reset 'number mode' after a space or non-digit character
            if char == ' ':
                self.unset_number_mode()
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

    translator = BrailleTranslator(is_braille_input)
    result = translator.translate(input_string)

    print(result)

if __name__ == "__main__":
    main()
