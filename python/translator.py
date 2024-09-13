import sys

class BrailleTranslator:
    # Braille alphabet and numbers mapping including punctuation and special symbols
    BRAILLE_ALPHABET = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......',
        'capital': '.....O', 'number': '.O.OOO',
        '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
        '.': '......', ',': '..O...', '?': '..OO.O', '!': '..OOOO', ';': '..O.O.',
        ':': '..O.OO', '-': '....O.', '/': '.O.O..', '<': '....OO', '>': '...O.O',
        '(': '...OO.', ')': '...OOO', 
    }

    # Reverse mapping for Braille to English translation
    ENGLISH_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}

    def __init__(self):
        """Initialize the Braille Translator with default settings."""
        self.capitalize_next = False
        self.number_mode = False

    def translate_to_braille(self, text: str) -> str:
        """Translate English text to Braille."""
        braille_output = []
        for char in text:
            if char.isupper():
                braille_output.append(self.BRAILLE_ALPHABET['capital'])
                braille_output.append(self.BRAILLE_ALPHABET[char.lower()])
            elif char.isdigit():
                braille_output.append(self.BRAILLE_ALPHABET['number'])
                braille_output.append(self.BRAILLE_ALPHABET[char])
            else:
                braille_output.append(self.BRAILLE_ALPHABET.get(char, ''))
        return ''.join(braille_output)

    def translate_to_english(self, braille: str) -> str:
        """Translate Braille to English text."""
        self.capitalize_next = False
        self.number_mode = False

        english_output = []

        # Split braille string into 6-character symbols
        symbols = [braille[i:i+6] for i in range(0, len(braille), 6)]

        for symbol in symbols:
            char = self._translate_symbol(symbol)
            if char:
                english_output.append(char)

        return ''.join(english_output)

    def _translate_symbol(self, symbol: str) -> str:
        """Helper method to translate individual Braille symbols to English."""
        if symbol == self.BRAILLE_ALPHABET['capital']:
            self.capitalize_next = True
            return ''
        elif symbol == self.BRAILLE_ALPHABET['number']:
            self.number_mode = True
            return ''
        elif symbol == self.BRAILLE_ALPHABET[' ']:
            self.number_mode = False  # Reset number mode after space
            return ' '

        char = self.ENGLISH_ALPHABET.get(symbol, '')
        if self.number_mode and char.isalpha():
            # Convert a-j to 1-9 and 0 respectively
            number = str(ord(char) - ord('a'))
            return '0' if number == '-1' else number

        if self.capitalize_next:
            char = char.upper()
            self.capitalize_next = False

        return char

def main():
    """Main function to handle input and initiate translation."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_or_braille>")
        return

    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()

    # Determine if the input is Braille or English by checking for valid Braille characters
    if is_braille(input_text):
        translated_text = translator.translate_to_english(input_text)
    else:
        translated_text = translator.translate_to_braille(input_text)

    print(translated_text)

def is_braille(text: str) -> bool:
    """Check if the given input is in Braille format."""
    return all(c in 'O.' for c in text.replace(' ', ''))

if __name__ == "__main__":
    main()
