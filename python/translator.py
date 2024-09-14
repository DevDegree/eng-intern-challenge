import sys

class BrailleTranslator:
    BRAILLE_TO_LETTER = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '......': ' '
    }
    LETTER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_LETTER.items()}
    CAPITAL_SIGN = '.....O'
    NUMBER_SIGN = '.O.OOO'
    BRAILLE_TO_DIGIT = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }
    DIGIT_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_DIGIT.items()}

    def __init__(self, input_text):
        self.input_text = input_text

    def translate(self):
        cleaned_input = self.input_text.replace(' ', '')
        if set(cleaned_input).issubset({'O', '.'}) and len(cleaned_input) % 6 == 0:
            return self._braille_to_text()
        else:
            return self._text_to_braille()

    def _text_to_braille(self):
        braille_output = []
        number_mode = False
        for char in self.input_text:
            if char.isalpha():
                if number_mode:
                    number_mode = False
                if char.isupper():
                    braille_output.append(self.CAPITAL_SIGN)
                braille_char = self.LETTER_TO_BRAILLE.get(char.lower(), '......')
                braille_output.append(braille_char)
            elif char.isdigit():
                if not number_mode:
                    braille_output.append(self.NUMBER_SIGN)
                    number_mode = True
                braille_char = self.DIGIT_TO_BRAILLE.get(char, '......')
                braille_output.append(braille_char)
            elif char == ' ':
                braille_output.append('......')
                number_mode = False
            else:
                braille_output.append('......')
                number_mode = False
        return ''.join(braille_output)

    def _braille_to_text(self):
        text_output = []
        index = 0
        input_length = len(self.input_text)
        number_mode = False
        capitalize_next = False

        while index + 6 <= input_length:
            braille_char = self.input_text[index:index+6]

            if braille_char == self.CAPITAL_SIGN:
                capitalize_next = True
            elif braille_char == self.NUMBER_SIGN:
                number_mode = True
            elif braille_char == '......':
                text_output.append(' ')
                number_mode = False
                capitalize_next = False
            else:
                char = None
                if number_mode:
                    char = self.BRAILLE_TO_DIGIT.get(braille_char)
                    if char is None:
                        number_mode = False
                        char = self.BRAILLE_TO_LETTER.get(braille_char)
                else:
                    char = self.BRAILLE_TO_LETTER.get(braille_char)
                if char:
                    if capitalize_next:
                        char = char.upper()
                        capitalize_next = False
                    text_output.append(char)
                else:
                    number_mode = False
            index += 6
        return ''.join(text_output)

def main():
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:]).strip()
    else:
        input_text = input("Enter text or Braille to translate: ").strip()

    if not input_text:
        print("No input provided.")
        sys.exit(1)

    translator = BrailleTranslator(input_text)
    print(translator.translate())

if __name__ == "__main__":
    main()
