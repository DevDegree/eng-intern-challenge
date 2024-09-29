import sys

class BrailleTranslator:
    def __init__(self, text) -> None:
        self.english_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
            'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
            '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
            '<': '.OO...O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 'Capital': '.....O', 
            'Decimal': '.O...O', 'Number': '.O.OOO',
        }
        self.digit_to_braille = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        }
        self.text = text

    def is_braille_format(self):
        return all(char in '.O' for char in self.text)

    def convert_braille_to_english(self):
        braille_text = self.text
        braille_to_english = {v: k for k, v in self.english_to_braille.items()}
        braille_to_digit = {v: k for k, v in self.digit_to_braille.items()}
        english_translation = []
        index = 0
        
        while index < len(braille_text):
            braille_char = braille_text[index:index+6]
            english_char = braille_to_english.get(braille_char, '')
            
            if english_char == 'Capital':
                index += 6
                braille_char = braille_text[index:index+6]
                english_translation.append(braille_to_english.get(braille_char, '').upper())
            elif english_char == 'Number':
                index += 6
                while index < len(braille_text) and braille_text[index:index+6] in braille_to_digit:
                    braille_char = braille_text[index:index+6]
                    english_translation.append(braille_to_digit.get(braille_char, ''))
                    index += 6
            else:
                english_translation.append(english_char)
            index += 6
        
        return ''.join(english_translation)

    def convert_english_to_braille(self):
        braille_translation = []
        is_digit_mode = False
        english_text = self.text
        
        for char in english_text:
            if char.isdigit():
                if not is_digit_mode:
                    is_digit_mode = True
                    braille_translation.append(self.english_to_braille['Number'])
                braille_translation.append(self.digit_to_braille[char])
            else:
                is_digit_mode = False
                if char.isupper():
                    braille_translation.append(self.english_to_braille['Capital'])
                    char = char.lower()
                braille_translation.append(self.english_to_braille.get(char, ''))
        
        return ''.join(braille_translation)

    def translate(self):
        if self.is_braille_format():
            return self.convert_braille_to_english()
        else:
            return self.convert_english_to_braille()

def main():
    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(text=input_text)
    print(translator.translate())

if __name__ == "__main__":
    main()