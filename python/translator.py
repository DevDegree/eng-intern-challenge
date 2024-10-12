import sys
import re

class BrailleTranslator:
    # Define the Braille representations for the alphabet (lowercase letters)
    BRAILLE_ALPHABET = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    }

    # Define the Braille representations for numbers
    BRAILLE_NUMBERS = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    # Special Braille symbols
    CAPITAL_SYMBOL = '.....O'  # Indicates that the next letter is capitalized
    NUMBER_SYMBOL = '.O.OOO'   # Indicates that the following symbols are numbers
    SPACE = '......'           # Represents a space between words

    def __init__(self):
        # Create reverse mappings from Braille to letters and numbers for decoding
        self.braille_to_letter = {v: k for k, v in self.BRAILLE_ALPHABET.items()}
        self.braille_to_number = {v: k for k, v in self.BRAILLE_NUMBERS.items()}

    def is_valid_braille(self, input_string):
        """
        Check if the input string is valid Braille.

        A valid Braille string:
        - Consists only of 'O' (capital letter O) and '.' (period)
        - Has a length that is a multiple of 6, as each Braille character is 6 dots
        """
        return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0

    def is_valid_english(self, input_string):
        """
        Check if the input string is valid English text.

        Valid English text:
        - Consists of letters (uppercase or lowercase), digits, and spaces
        """
        return bool(re.match(r'^[a-zA-Z0-9 ]+$', input_string))

    def translate(self, input_string):
        """
        Determine the type of input and translate accordingly.

        If the input is valid Braille, translate to English text.
        If the input is valid English text, translate to Braille.
        """
        if self.is_valid_braille(input_string):
            # Input is Braille; translate to text
            return self.braille_to_text_translate(input_string)
        elif self.is_valid_english(input_string):
            # Input is English text; translate to Braille
            return self.text_to_braille_translate(input_string)
        else:
            # Input is invalid
            raise ValueError("Invalid input: must be either valid Braille or English text.")

    def text_to_braille_translate(self, text):
        """
        Translate English text to Braille.

        Handles capitalization, numbers, and spaces.
        """
        result = []           # List to hold Braille symbols
        is_number_mode = False  # Flag to indicate if we're in number mode

        for char in text:
            if char.isupper():
                # If the character is uppercase, add the capital symbol
                result.append(self.CAPITAL_SYMBOL)
                char = char.lower()  # Convert to lowercase for mapping

            if char.isdigit():
                if not is_number_mode:
                    # If entering number mode, add the number symbol
                    result.append(self.NUMBER_SYMBOL)
                    is_number_mode = True
                # Append the Braille representation of the digit
                result.append(self.BRAILLE_NUMBERS[char])
            else:
                if is_number_mode:
                    # Exit number mode when encountering a non-digit character
                    is_number_mode = False
                if char == ' ':
                    # Append the space symbol
                    result.append(self.SPACE)
                    is_number_mode = False  # Reset number mode after space
                elif char in self.BRAILLE_ALPHABET:
                    # Append the Braille representation of the letter
                    result.append(self.BRAILLE_ALPHABET[char])
                else:
                    # Character is unsupported
                    raise ValueError(f"Unsupported character: {char}")

        # Combine all Braille symbols into a single string
        return ''.join(result)

    def braille_to_text_translate(self, braille):
        """
        Translate Braille to English text.

        Handles capitalization, numbers, and spaces.
        """
        result = []  # List to hold decoded characters
        # Split the Braille string into chunks of 6 characters (each Braille symbol)
        braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
        is_capital = False     # Flag to indicate if the next letter should be capitalized
        is_number_mode = False  # Flag to indicate if we're in number mode

        for braille_char in braille_chars:
            if braille_char == self.CAPITAL_SYMBOL:
                # Next letter should be capitalized
                is_capital = True
            elif braille_char == self.NUMBER_SYMBOL:
                # Enter number mode
                is_number_mode = True
            elif braille_char == self.SPACE:
                # Append a space and reset number mode
                result.append(' ')
                is_number_mode = False
            elif is_number_mode:
                # In number mode; translate using the number mapping
                if braille_char in self.braille_to_number:
                    char = self.braille_to_number[braille_char]
                    result.append(char)
                else:
                    # Braille symbol is not a valid number
                    raise ValueError(f"Invalid number Braille symbol: {braille_char}")
            else:
                # Not in number mode; translate using the letter mapping
                if braille_char in self.braille_to_letter:
                    char = self.braille_to_letter[braille_char]
                    if is_capital:
                        # Capitalize the letter
                        char = char.upper()
                        is_capital = False  # Reset capitalization flag
                    result.append(char)
                else:
                    # Braille symbol is not a valid letter
                    raise ValueError(f"Invalid letter Braille symbol: {braille_char}")

        # Combine all characters into a single string
        return ''.join(result)

def main():
    if len(sys.argv) < 2:
        # No input provided; print usage message
        print("Please provide an input string.")
        sys.exit(1)

    # Combine all command-line arguments into a single string
    input_string = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()

    try:
        # Attempt to translate the input
        result = translator.translate(input_string)
        # Print the translation result without an extra newline
        print(result, end='')
    except ValueError as e:
        # An error occurred; print the error message to stderr
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
