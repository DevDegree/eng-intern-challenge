import sys

class Translator:
    # English to braille mapping for letters
    ENGLISH_TO_BRAILLE_LETTERS = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        ' ': '......'
    }

    # English to brail mapping for numbers
    ENGLISH_TO_BRAILLE_NUMS = {
        '0': '.OOO..',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
    }

    CAPITAL = '.....O'
    NUMBER = '.O.OOO'
    BRAILLE_SPACE = '......'

    # Braille to english mappings, computed by reversing the english-to-braille dictionaries
    BRAILLE_TO_ENGLISH_LETTERS = {b: e for e, b in ENGLISH_TO_BRAILLE_LETTERS.items()}
    BRAILLE_TO_ENGLISH_NUMS = {b: e for e, b in ENGLISH_TO_BRAILLE_NUMS.items()}

    def english_to_braille(self, text):
        """
        Converts an English text to Braille representation.

        Args:
            text (str): The input English text.

        Returns:
            str: The corresponding Braille translation.
        """

        result = ""
        num_mode = False

        for char in text:
            # Handle digits and number mode
            if char.isdigit():
                if not num_mode:
                    num_mode = True
                    result += self.NUMBER
                # Return the char from the dictionary, return an empty char as default if char is not unexpected
                result += self.ENGLISH_TO_BRAILLE_NUMS.get(char, '')
            else:
                # Reset number mode when switching to letters
                if num_mode:
                    num_mode = False
                # Handle capital letters
                if char.isupper():
                    result += self.CAPITAL
                    char = char.lower()
                result += self.ENGLISH_TO_BRAILLE_LETTERS.get(char, '')

        return result

    def braille_to_english(self, braille):
        """
        Converts Braille text to English.

        Args:
            braille (str): The Braille text (O and . notation).

        Returns:
            str: The corresponding English translation.
        """

        result = ""
        num_mode = False
        capital = False
        for i in range(0, len(braille), 6):
            char = braille[i:i+6]

            # Checking for numbers
            if char == self.NUMBER:
                num_mode = True
            
            # Handle spaces
            elif char == self.BRAILLE_SPACE:
                if num_mode:
                    num_mode = False
                result += ' '

            # Handle number translations
            elif num_mode:
                result += self.BRAILLE_TO_ENGLISH_NUMS.get(char, '')

            # Handle capital letters
            else:
                if char == self.CAPITAL:
                    capital = True
                elif capital:
                    result += self.BRAILLE_TO_ENGLISH_LETTERS.get(char, '').upper()
                    capital = False
                else:
                    result += self.BRAILLE_TO_ENGLISH_LETTERS.get(char, '')

        return result

    def translate(self, input):
        """
        Automatically determines if the input is Braille or English and translates it accordingly.

        Args:
            input_text (str): The input text in either Braille or English.

        Returns:
            str: The translated text.
        """

        # Check if the input is Braille (all chars are either '.' or '0')
        if all(char in 'O.' for char in input):
            if len(input) % 6 == 0:
                return self.braille_to_english(input)
            # Raise an error if the braille isn't valid - if the length is not a multiple of 6
            else:
                raise ValueError("Invalid Braille Input: Length must be a multiple of 6.")
        # Otherwise, the text is english
        else:
            return self.english_to_braille(input)

def main():
    """
    Main function to run the Braille translator. Collects input from the command line and prints the translation.
    """

    # Error if there is no input
    if len(sys.argv) < 2:
            raise ValueError("No input provided. Please pass a string to translate.")

    input_text = " ".join(sys.argv[1:])
    translator = Translator()

    try:
        result = translator.translate(input_text)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

