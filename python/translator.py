import sys


class Translator:
    def __init__(self):
        self.en_to_braille = {
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
            'Capital': '.....O',
            'Decimal': '.O...O',
            'Number': '.O.OOO',
            '.': '..OO.O',
            ',': '..O...',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '<': '.OO...O',
            '>': 'O..OO.',
            '(': 'O.O..O',
            ')': '.O.OO.',
            ' ': '......'
        }
        self.braille_to_en = {value: key for key, value in self.en_to_braille.items()}
        self.braille_to_en['O..OO.'] = 'o'

    def check_braille(self, sentence):
        return all(ch in '.O' for ch in sentence)
    
    def _translate_braille2en(self, sentence):
        res = []
        read_number = False
        capitalize = False
        for i in range(0, len(sentence), 6):
            action = self.braille_to_en[sentence[i:i+6]]
            if action == 'Capital':
                capitalize = True
                continue
            if action == 'Number':
                read_number = True
                continue
            if read_number:
                if action != ' ':
                    res.append('0' if action == 'j' else chr(ord('1') + ord(action) - ord('a')))
                else:
                    res.append(action)
                    read_number = False
                continue
            if capitalize:
                res.append(action.upper())
                capitalize = False
                continue
            res.append(action)

        return ''.join(res)
    
    def _translate_en2braille(self, sentence):
        res = []
        reading_number = False
        for ch in sentence:
            if ch.isdigit():
                if not reading_number:
                    res.append(self.en_to_braille['Number'])
                    reading_number = True
                ch = 'j' if ch == '0' else chr(ord('a') + ord(ch) - ord('1'))
            else:
                reading_number = False
            
            if ch.isupper():
                res.append(self.en_to_braille['Capital'])
                ch = ch.lower()
            
            res.append(self.en_to_braille[ch])
        return ''.join(res)

    def translate(self, sentence):
        is_braille = self.check_braille(sentence)
        if is_braille:
            return self._translate_braille2en(sentence)
        return self._translate_en2braille(sentence)


def main():
    sentence = ' '.join(sys.argv[1:])
    translator = Translator()
    print(translator.translate(sentence))

if __name__ == "__main__":
    main()
