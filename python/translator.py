
# dharmilgandhi6293@gmail.com
import sys

class Translator:
    # Define translation dictionaries for English to Braille
    ENGLISH_TO_BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
        ' ': '......',  # Space
    }

    NUMBERS_TO_BRAILLE = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    }

    # Create reverse mappings from Braille to English
    BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBERS = {value: key for key, value in NUMBERS_TO_BRAILLE.items()}

    # Braille representations for special symbols
    CAPITAL_FOLLOWS = '.....O'  # Indicates that the following letter is capitalized
    NUMBER_FOLLOWS = '.O.OOO'   # Indicates that the following characters are numbers

    @staticmethod
    def translate_english_to_braille(english):
        braille = ''
        is_number = False   # Flag to indicate if following characters are numbers

        for char in english:
            if char.isdigit() and not is_number:
                # Set flag if the current character is a digit and it is not set
                braille += Translator.NUMBER_FOLLOWS
                is_number = True
            elif char == ' ' and is_number:
                # Reset flag at end of number sequence
                is_number = False
            elif char.isalpha() and is_number:
                # Reset flag at end of number sequence
                is_number = False

            # Convert alphabetic character to Braille
            if char.isalpha():
                if char.isupper():
                    braille += Translator.CAPITAL_FOLLOWS
                    char = char.lower()
                braille += Translator.ENGLISH_TO_BRAILLE.get(char, '?')
            # Convert numeric character to Braille
            elif is_number:
                braille += Translator.NUMBERS_TO_BRAILLE.get(char, '?')
            # Convert punctuation or other available characters to Braille
            elif char in Translator.ENGLISH_TO_BRAILLE:
                braille += Translator.ENGLISH_TO_BRAILLE.get(char, '?')

        return braille

    @staticmethod
    def translate_braille_to_english(braille):
        english = ''
        is_capital = False  # Flag to indicate if next letter should be capitalized
        is_number = False   # Flag to indicate if following characters are numbers

        # Split the Braille text into individual Braille characters (each represented by 6 dots)
        braille_chars = [braille[i: i + 6] for i in range(0, len(braille), 6)]

        for char in braille_chars:
            if char == Translator.CAPITAL_FOLLOWS:
                # Set flag to capitalize the next letter
                is_capital = True
                continue
            elif char == Translator.NUMBER_FOLLOWS:
                # Set flag to indicate that the following characters are numbers
                is_number = True
                continue
            elif char == '......':  # Braille space
                # Reset number flag at space
                english += ' '
                is_number = False
                continue

            if is_number:
                # Translate Braille number to English digit
                english += Translator.BRAILLE_TO_NUMBERS.get(char, '?')
            else:
                # Translate Braille character to English letter
                letter = Translator.BRAILLE_TO_ENGLISH.get(char, '?')
                if is_capital:
                    english += letter.upper()
                    is_capital = False
                else:
                    english += letter

        return english

    @staticmethod
    def is_braille(text):
        # Check if given text contains only Braille characters
        return all(char in 'O.' for char in text.replace(' ', ''))

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    translator = Translator()

    if translator.is_braille(text):
        translated_text = translator.translate_braille_to_english(text)
    else:
        translated_text = translator.translate_english_to_braille(text)

    print(translated_text)

if __name__ == '__main__':
    main()