import sys

eng_to_braille = {
    # Letters A-Z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 

    # Numbers 0-9 (with number follows prefix)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Special symbols
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '..O..O', '/': '..O..O', 
    '<': '..O.O.', '>': '..OO.O', '(': '..OO..', ')': '..OO..', ' ': '......',

    # Prefixes
    'capital': '.....O',  # Capital follows
    'number': '.O.OOO',   # Number follows
    'decimal': '.O..OO',  # Decimal follows
}

braille_to_eng = {v: k for k, v in eng_to_braille.items() if not k.isdigit()}
braille_to_number = {v: k for k, v in eng_to_braille.items() if k.isdigit()}

class Translator:
    def __init__(self, text):
        self.text = text

    def is_english(self):
        for text in self.text:
            if text == ".":
                return False
            if text == "O":
                continue

            return True
    
    def print_translation(self):
        if self.is_english():
            print(self.translate_to_braille())
        else:
            print(self.translate_to_english())

    def translate_to_braille(self):
        translation = ""
        is_number = False
        for text in self.text:
            if text.isupper():
                translation += eng_to_braille["capital"]
                text = text.lower()
            if text.isdigit():
                if not is_number:
                    translation += eng_to_braille["number"]
                    is_number = True
                translation += eng_to_braille[text]
            elif text in eng_to_braille:
                translation += eng_to_braille[text]

            if text == " ":
                is_number = False
        return translation
    
    def translate_to_english(self):
        translation = ""
        i = 0
        is_number = False
        while i < len(self.text):
            if is_number:
                letter_translation = braille_to_number[self.text[i:i+6]]
            else:
                letter_translation = braille_to_eng[self.text[i:i+6]]
            i += 6
            if letter_translation == "capital":
                letter_translation = braille_to_eng[self.text[i:i+6]].upper()
                i += 6
            if letter_translation == "number":
                is_number = True
                continue
            if letter_translation == " ":
                is_number = False

            translation += letter_translation

        return translation


if __name__ == "__main__":
    translator = Translator(" ".join(sys.argv[1:]))
    translator.print_translation()