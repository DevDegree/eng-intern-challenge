import sys
from braille_mapping import BRAILLE_MAPPING as braille_map, REVERSE_MAPPING as reverse_map

class BrailleTranslator:
    def __init__(self):
        self.braille_map = braille_map
        self.reverse_map = reverse_map

    def handle_capitalization(self, char: str, result: list):
        """Handle capitalization mode"""
        result.append(self.braille_map['CAPITAL'])
        result.append(self.braille_map[char.lower()])

    def handle_number_mode(self, char: str, result: list, number_mode_active: bool):
        """Handle number mode"""
        if not number_mode_active:
            result.append(self.braille_map['NUMBER'])
        result.append(self.braille_map[char])
        return True  # Number mode remains active

    def translate_to_braille(self, text: str) -> str:
        text = text.strip()  # Strip any leading/trailing whitespace
        result = []
        number_mode_active = False

        for char in text:
            if char.isupper():
                self.handle_capitalization(char, result)
            elif char.isdigit():
                number_mode_active = self.handle_number_mode(char, result, number_mode_active)
            elif char == ' ':
                result.append(self.braille_map['SPACE'])
                number_mode_active = False  # Reset number mode on space
            else:
                result.append(self.braille_map[char.lower()])

        return ''.join(result)

    def translate_to_english(self, braille: str) -> str:
        braille = braille.strip()  # Strip any leading/trailing whitespace
        result = []
        i = 0
        capitalize_next = False
        number_mode_active = False

        while i < len(braille):
            symbol = braille[i:i+6]
            i += 6

            if symbol == self.braille_map['CAPITAL']:
                capitalize_next = True
            elif symbol == self.braille_map['NUMBER']:
                number_mode_active = True
            elif symbol == self.braille_map['SPACE']:
                result.append(' ')
                number_mode_active = False  # Reset number mode on space
            else:
                char = self.reverse_map.get(symbol)
                if not char:
                    raise ValueError(f"Invalid Braille symbol: {symbol}")

                if number_mode_active:
                    result.append(char)  # Treat as a number
                elif capitalize_next:
                    result.append(char.upper())
                    capitalize_next = False
                else:
                    result.append(char)

        return ''.join(result)

def main():
    translator = BrailleTranslator()

    if len(sys.argv) < 2:
        sys.exit(0)

    input_text = ' '.join(sys.argv[1:]).strip()  # Strip any leading/trailing whitespace

    if all(c in 'O.' for c in input_text):
        output = translator.translate_to_english(input_text)
    else:
        output = translator.translate_to_braille(input_text)

    sys.stdout.write(output.strip())  # Ensure no trailing newline or spaces in output

if __name__ == "__main__":
    main()