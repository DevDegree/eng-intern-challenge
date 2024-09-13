import argparse
from typing import Dict

class Translator:
    
    def __init__(self):
        self.alphabet_to_braille = self.default_alphabet_to_braille()
        self.number_to_braille = self.default_number_to_braille()
        self.braille_to_alphabet = {v: k for k, v in self.alphabet_to_braille.items()} 
        self.braille_to_number = {v: k for k, v in self.number_to_braille.items()}
        self.flag = None
        self.number_mode = False
    
    def default_alphabet_to_braille(self) -> Dict[str, str]:
        """Braille dot patterns for lowercase letters and special characters as 6-character strings."""
        return {
            # base letters a-j
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            
            # k-t (second decade)
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            
            # u-z (third decade)
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

            # Special characters
            '.': '..OO.O', 
            ',': '..O...', 
            '?': '..0.00',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '(': 'O.O..O',
            ')': '.O.OO.',
            '>': 'O..OO.',
            '<': '.OO..O',
            ' ': '......',
            
            
            # Flags
            'capital': '.....O',   # Capital follows
            'number': '.O.OOO',    # Number follows
        }

    def default_number_to_braille(self) -> Dict[str, str]:
        """Braille dot patterns for numbers."""
        return {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        }

    def detect_mode(self, input_str: str) -> str:
        """Detect whether the input is Braille or ASCII."""
        if all(c in 'O. ' for c in input_str):
            return 'braille_to_ascii'
        return 'ascii_to_braille'
    
    def ascii_to_braille(self, input_text: str) -> str:
        """Convert ASCII text to Braille representation."""
        result = []
        self.number_mode = False

        for char in input_text:
            if char.isupper():
                result.append(self.alphabet_to_braille['capital'])  # Add capital flag
                char = char.lower()  # Convert to lowercase after adding flag

            if char.isdigit():
                if not self.number_mode:
                    result.append(self.alphabet_to_braille['number'])  # Add number flag
                    self.number_mode = True
                result.append(self.number_to_braille.get(char, ''))
            elif char == ' ':
                self.number_mode = False  # Exit number mode on space
                result.append(self.alphabet_to_braille.get(char, ''))
            else:
                result.append(self.alphabet_to_braille.get(char, ''))

        return ''.join(result)

    def braille_to_ascii(self, braille_text: str) -> str:
        """Convert Braille representation to ASCII text."""
        result = []
        self.number_mode = False
        self.flag = None

        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i+6]

            if braille_char == '......':  # Handle space
                result.append(' ')
                self.number_mode = False  # Reset number mode on space
                continue

            # Check for flags (capital or number)
            if braille_char == self.alphabet_to_braille['capital']:
                self.flag = 'capital'
                continue
            elif braille_char == self.alphabet_to_braille['number']:
                self.number_mode = True
                continue

            # Determine whether to use number or alphabet mode
            if self.number_mode:
                ascii_char = self.braille_to_number.get(braille_char, '')
            else:
                ascii_char = self.braille_to_alphabet.get(braille_char, '')

            # Apply capitalization if the flag is set
            if self.flag == 'capital':
                result.append(ascii_char.upper())
                self.flag = None  # Reset flag after use
            else:
                result.append(ascii_char)

        return ''.join(result)

def main():
    parser = argparse.ArgumentParser(description="Bidirectional ASCII-Braille Translator with auto-detection")
    parser.add_argument('input', nargs='+', help="Input string (ASCII or Braille)")
    args = parser.parse_args()

    input_text = ' '.join(args.input)
    translator = Translator()

    mode = translator.detect_mode(input_text)
    if mode == 'ascii_to_braille':
        result = translator.ascii_to_braille(input_text)
    else:
        result = translator.braille_to_ascii(input_text)
    
    print(result)

if __name__ == "__main__":
    main()
