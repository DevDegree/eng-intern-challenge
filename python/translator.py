import sys

class Translator:
    _BRAILLE_TO_LETTER = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
        "O..OOO": "z", "......": " "
    }

    _LETTER_TO_BRAILLE = {v: k for k, v in _BRAILLE_TO_LETTER.items()}

    _BRAILLE_TO_NUMBER = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
    }

    _NUMBER_TO_BRAILLE = {v: k for k, v in _BRAILLE_TO_NUMBER.items()}

    _CAPITAL_SIGN = ".....O"
    _NUMBER_SIGN = ".O.OOO"

    @classmethod
    def _is_braille(cls, text):
        return all(char in 'O.' for char in text) and len(text) % 6 == 0

    @classmethod
    def _braille_to_text(cls, braille_text):
        result = []
        capitalize_next = False
        number_mode = False
        i = 0

        while i < len(braille_text):
            braille = braille_text[i:i+6]
            i += 6

            if braille == cls._CAPITAL_SIGN:
                capitalize_next = True
            elif braille == cls._NUMBER_SIGN:
                number_mode = True
            elif braille == "......":  # Space
                result.append(" ")
                number_mode = False
            else:
                if number_mode:
                    char = cls._BRAILLE_TO_NUMBER.get(braille, cls._BRAILLE_TO_LETTER.get(braille, ' '))
                else:
                    char = cls._BRAILLE_TO_LETTER.get(braille, ' ')
                    if capitalize_next and char.isalpha():
                        char = char.upper()
                        capitalize_next = False
                result.append(char)

        return ''.join(result)

    @classmethod
    def _text_to_braille(cls, text):
        result = []
        number_mode = False

        for char in text:
            if char.isalpha():
                if number_mode:
                    result.append(cls._NUMBER_SIGN)
                    number_mode = False
                if char.isupper():
                    result.append(cls._CAPITAL_SIGN)
                    char = char.lower()
                result.append(cls._LETTER_TO_BRAILLE[char])
            elif char.isdigit():
                if not number_mode:
                    result.append(cls._NUMBER_SIGN)
                    number_mode = True
                result.append(cls._NUMBER_TO_BRAILLE[char])
            elif char == ' ':
                result.append(cls._LETTER_TO_BRAILLE[char])
                number_mode = False
            else:
                result.append('......')  # Default to space for unrecognized characters
                number_mode = False

        return ''.join(result)

    @classmethod
    def translate(cls, input_text):
        if cls._is_braille(input_text):
            return cls._braille_to_text(input_text)
        else:
            return cls._text_to_braille(input_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text to translate>")
        sys.exit(1)

    # Join all arguments into a single string
    input_text = ' '.join(sys.argv[1:])

    translator = Translator()
    result = translator.translate(input_text)
    print(result)

if __name__ == "__main__":
    main()

# Example usage
translator = Translator()

# Test translations
# print(translator.translate(".....OO.....O.O...OO.....O.OOOO.....O.O...OO..........O.....")) #Abc 123
# print(translator.translate("Hello world"))
# print(translator.translate("42"))