VALID_ENGLISH_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
VALID_BRAILLE_CHARS = set(".O")
LETTER_BRAILLE_MAP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}
NUMBER_BRAILLE_MAP = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
CAPITAL_BRAILLE_CODE = '.....O'
NUMBER_BRAILLE_CODE = '.O.OOO'
SPACE_BRAILLE_CODE = '......'
REVERSE_BRAILLE_MAP = {**{v: k for k, v in LETTER_BRAILLE_MAP.items()}, **{v: k for k, v in NUMBER_BRAILLE_MAP.items()}}
REVERSE_BRAILLE_MAP[' '] = SPACE_BRAILLE_CODE

class BrailleTranslator:
    def __init__(self, input_str):
        self.input_str = input_str

    def translate(self):
        if self.is_braille(self.input_str):
            return self.braille_to_english(self.input_str)
        return self.english_to_braille(self.input_str)

    def is_braille(self, input_str):
        """Determine if the input string is in Braille (contains only 'O' and '.')"""
        return all(char in VALID_BRAILLE_CHARS for char in input_str)

    def english_to_braille(self, english_str):
        """Translate English text to Braille"""
        output = []
        number_mode = False
        for char in english_str:
            if char.isdigit() and not number_mode:
                output.append(NUMBER_BRAILLE_CODE)
                number_mode = True
            elif not char.isdigit() and number_mode:
                number_mode = False

            if char.isupper():
                output.append(CAPITAL_BRAILLE_CODE)
                char = char.lower()

            output.append(REVERSE_BRAILLE_MAP.get(char, SPACE_BRAILLE_CODE))
        return ''.join(output)

    def braille_to_english(self, braille_str):
        """Translate Braille to English"""
        output = []
        chars = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]
        capitalize_next = False
        number_mode = False

        for char in chars:
            if char == CAPITAL_BRAILLE_CODE:
                capitalize_next = True
                continue
            if char == NUMBER_BRAILLE_CODE:
                number_mode = True
                continue
            if char == SPACE_BRAILLE_CODE:
                output.append(' ')
                number_mode = False
                continue

            translated_char = LETTER_BRAILLE_MAP.get(char, ' ')
            if number_mode:
                translated_char = NUMBER_BRAILLE_MAP.get(char, '')
            elif capitalize_next:
                translated_char = translated_char.upper()
                capitalize_next = False

            output.append(translated_char)

        return ''.join(output)


def get_input_from_args() -> str:
    import sys
    """
    Retrieves the input code from command-line arguments.
    """
    if len(sys.argv) < 2:
        raise ValueError("Usage: python translator.py <text to translate>")
    return " ".join(sys.argv[1:])


def main():
    input_str = get_input_from_args()
    translator = BrailleTranslator(input_str)
    print(translator.translate())


if __name__ == "__main__":
    main()
