from string import ascii_lowercase, digits, ascii_uppercase
class Translate:
    def __init__(self) -> None:
        self.ascii_to_braille = {
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
            'z':  'O..OOO',
            '1':  'O.....',
            '2':  'O.O...',
            '3':  'OO....',
            '4':  'OO.O..',
            '5':  'O..O..',
            '6':  'OOO...',
            '7':  'OOOO..',
            '8':  'O.OO..',
            '9':  '.OO...',
            '0':  '.OOO..',
            ' ': '......',
            '.': '..OO.O',
            ',': '..O...',
            '?': '..O.OO',
            '!': '..OOO.',
            ':': '..OO..',
            ';': '..O.O.',
            '-': '....OO',
            '/': '.O..O.',
            '<': '.OO..O',
            '>': 'O..OO.',
            '(': 'O.O..O',
            ')': '.O.OO.',
        }
        self.CAPS = '.....O'
        self.NUM = '.O.OOO'
        self.SPACE = '......'
        self.braille_to_letter = {}
        self.braille_to_number = {}
        for c in ascii_lowercase:
            b = self.ascii_to_braille[c]
            self.braille_to_letter[b] = c
        for d in digits:
            b = self.ascii_to_braille[d]
            self.braille_to_number[b] = d

    def is_braillie(self, s):
        return all(c == '.' or c == 'O' for c in s)

    def translate(self, s):
        if self.is_braillie(s):
            return self._translate_braillie(s)
        else:
            return self._translate_english(s)


    def to_english(self, b, caps=False, num=False):
        if num:
            return self.braille_to_number[b]
        c = self.braille_to_letter[b]
        if caps:
            c = c.upper()
        return c

    def _translate_braillie(self, s):
        res = []
        chunks = [s[i:i+6] for i in range(0, len(s), 6)]
        caps = False
        num = False
        for c in chunks:
            if c == self.CAPS:
                caps = True
            elif c == self.NUM:
                num = True
            elif c == self.ascii_to_braille[' ']:
                res.append(' ')
                num = False
            else:
                res.append(self.to_english(c, caps, num))
                caps = False
        return ''.join(res)

    def _translate_english(self, s):
        res = []
        num = False
        for c in s:
            if c in digits:
                if not num:
                    num = True
                    res.append(self.NUM)
            if c == ' ':
                num = False
            elif c in ascii_uppercase:
                res.append(self.CAPS)
                c = c.lower()
            res.append(self.ascii_to_braille[c])
        return ''.join(res)


