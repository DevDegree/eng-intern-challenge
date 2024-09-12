import sys

class BrailleTranslator:
    braille_map = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
        'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
        'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
        'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
        'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
        'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', 
        '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
        '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
        'capital_follows': '.....O', 'decimal_follows': '.O...O', 'number_follows': '.O.OOO',
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
        '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
    }

    reverse_map = {v: k for k, v in braille_map.items()}

    def __init__(self, input_str):
        self.input_str = input_str

    def is_braille(self):
        return all(c in 'O.' for c in self.input_str) and len(self.input_str) % 6 == 0

    def translate_to_braille(self):
        result = []
        number_mode = False

        for char in self.input_str:
            if char.isdigit() and not number_mode:
                result.append(self.braille_map['number_follows'])
                number_mode = True
            elif not char.isdigit():
                number_mode = False

            if char.isupper():
                result.append(self.braille_map['capital_follows'])
                char = char.lower()

            result.append(self.braille_map.get(char, ''))

        return ''.join(result)

    def translate_to_english(self):
        result = []
        number_mode = False
        capitalize_next = False

        for i in range(0, len(self.input_str), 6):
            braille_char = self.input_str[i:i + 6]

            if braille_char == self.braille_map['number_follows']:
                number_mode = True
                continue
            elif braille_char == self.braille_map['capital_follows']:
                capitalize_next = True
                continue

            letter = self.reverse_map.get(braille_char, '')
            if number_mode:
                if letter.isdigit():
                    result.append(letter)
                number_mode = False
            elif capitalize_next:
                result.append(letter.upper())
                capitalize_next = False
            else:
                result.append(letter)

        return ''.join(result)

    def translate(self):
        if self.is_braille():
            return self.translate_to_english()
        else:
            return self.translate_to_braille()


def main():
    input_str = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(input_str)
    print(translator.translate(), end='')


if __name__ == "__main__":
    main()

