class BrailleTranslator:
    #from Braille to English letters
    BRAILLE_TO_LETTER = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
        "O..OOO": "z", "......": " "
    }

    # from English letters to Braille
    LETTER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_LETTER.items()}

    # from Braille to English numbers
    BRAILLE_TO_NUMBER = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
    }

    # from numbers to Braille
    NUMBER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBER.items()}

    # special modes
    CAPITAL_SIGN = ".....O"
    NUMBER_SIGN = ".O.OOO"
    SPACE = "......"

    def is_braille(cls, text):
        """Determine if the given text is in Braille format."""
        return all(char in 'O.' for char in text) and len(text) % 6 == 0

    def translate(cls, input_text):
        """Translate input text to Braille or vice versa."""
        if cls.is_braille(input_text):
            return cls.braille_to_text(input_text)
        else:
            return cls.text_to_braille(input_text)

    def braille_to_text(cls, braille_text):
        """Convert Braille to English text."""
        result = []
        capitalize_next = False
        number_mode = False

        # Process by 6
        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i + 6]

            if braille_char == cls.CAPITAL_SIGN:
                capitalize_next = True
            elif braille_char == cls.NUMBER_SIGN:
                number_mode = True
            elif braille_char == cls.SPACE:  # Handle spaces
                result.append(" ")
                number_mode = False  # Reset
            else:
                char = cls._get_char_from_braille(braille_char, capitalize_next, number_mode)
                result.append(char)
                capitalize_next = False  # Reset

        return ''.join(result)

    def _get_char_from_braille(cls, braille_char, capitalize_next, number_mode):
        """Helper method to get a character from Braille."""
        if number_mode:
            char = cls.BRAILLE_TO_NUMBER.get(braille_char, '?')  # Fallback to '?' for unknown
        else:
            char = cls.BRAILLE_TO_LETTER.get(braille_char, '?')  # Fallback to '?' for unknown
            if capitalize_next and char.isalpha():
                char = char.upper()
        return char

    def text_to_braille(cls, text):
        result = []
        number_mode = False

        for char in text:
            if char.isalpha():
                if number_mode:
                    result.append(cls.SPACE)
                    number_mode = False
                if char.isupper():
                    result.append(cls.CAPITAL_SIGN)
                    char = char.lower()
                result.append(cls.LETTER_TO_BRAILLE[char])
            elif char.isdigit():
                if not number_mode:
                    result.append(cls.NUMBER_SIGN)
                    number_mode = True
                result.append(cls.NUMBER_TO_BRAILLE[char])
            elif char == ' ':
                result.append(cls.SPACE)
                number_mode = False  
            else:
                result.append(cls.SPACE)

        return ''.join(result)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text to translate>")
        sys.exit(1)

    # Join all arguments into a single string
    input_text = ' '.join(sys.argv[1:])

    translator = BrailleTranslator()
    result = translator.translate(input_text)
    print(result)

if __name__ == "__main__":
    main()
