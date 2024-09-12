import sys

class Translator:
    def __init__(self):
        self.eng_braille_map = {
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
        self.braille_eng_map = {val: key for key, val in self.eng_braille_map.items()}
        self.capital = '.....O'
        self.number = '.O.OOO'
        self.valid_braille = set('O.')
    
    def is_braille(self, text):
        return set(text).issubset(self.valid_braille) and len(text) % 6 == 0
    
    def digit_to_braille_letter(self, digit):
        return chr(ord('a') + (int(digit) - 1) % 10)
    
    def braille_letter_to_digit(self, letter):
        return str((ord(letter) - ord('a') + 1) % 10)
    
    def english_to_braille(self, text):
        translated = ''
        number_mode = False
        for c in text:
            if c.isdigit():
                if not number_mode:
                    translated += self.number
                    number_mode = True
                c = self.digit_to_braille_letter(c)
            elif c.isupper():
                translated += self.capital
                c = c.lower()
            elif c == ' ':
                number_mode = False
            translated += self.eng_braille_map[c]

        return translated

    def braille_to_english(self, text):
        translated = ''
        number_mode = False
        capital_mode = False
        for i in range(0, len(text), 6):
            chunk = text[i:i+6]
            
            if chunk == self.number:
                number_mode = True
            elif chunk == self.capital:
                capital_mode = True
            else:
                c = self.braille_eng_map[chunk]
                if c == ' ':
                    number_mode = False
                elif number_mode:
                    c = self.braille_letter_to_digit(c)
                elif capital_mode:
                    capital_mode = False
                    c = c.upper()
                translated += c

        return translated
    
    def translate(self, text):
        if self.is_braille(text):
            return self.braille_to_english(text)
        else:
            return self.english_to_braille(text)

def main():
    if len(sys.argv) < 2:
        return
    
    translator = Translator()
    text = ' '.join(sys.argv[1:])
    print(translator.translate(text))

if __name__ == '__main__':
    main()
