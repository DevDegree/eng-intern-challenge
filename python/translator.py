
import sys


class Translator():
    orgText = ''

    def __init__(self, orgText):
        self.orgText = orgText

    number_follows = 'number_follows'
    capital_follows = 'capital_follows'
    space = " "
    dic = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': 'O.O...',
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
        't': 'O...OO',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        'capital_follows': '.....O',
        'decimal_follows': '.O...O',
        number_follows: '.O.OOO',
        space: '......'
    }
    numbers = {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O..OO..',
        '9': '.OO...',
        'O': '.OOO..',
        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ',': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
    }

    def numberFollows(
        self, letter): letter == self.dic.get(
        self.number_follows, '')

    def capitalFollows(
        self, letter): letter == self.dic.get(
        self.capital_follows, '')

    def spaceFollows(self, letter): letter == self.dic.get(self.space, '')

    def eng_to_b(self, text):
        result = ''
        isNumber = False
        for letter in text:
            if letter.isdigit() and not isNumber:
                isNumber = True
                result += self.dic.get(self.number_follows, '')
            if isNumber and self.spaceFollows(letter):
                isNumber = False
            if letter.isalpha() and letter.isupper():
                result += self.dic.get(self.capital_follows, '')
            result += self.numbers.get(
                letter, '') if letter.isdigit() else self.dic.get(
                letter.lower(), '')
        return result

    def b_to_eng(self, value):
        result = ''
        isNumber = False
        isUpper = False
        for i in range(0, len(value), 6):
            letter = value[i:i + 6]
            if self.numberFollows(letter):
                isNumber = True
            if self.capital_follows(letter):
                isUpper = True
                continue
            elif isUpper:
                result += self.get_key(letter, isNumber, isUpper)
                isUpper = False
                continue
            if self.spaceFollows(letter):
                isNumber = False
            result += self.get_key(letter, isNumber, isUpper)
        return result

    def get_key(self, val, isNumber, isUpper):
        for key, value in self.numbers.items() if isNumber else self.dic.items():
            if val == value:
                return key.upper() if isUpper and not isNumber else key

        return ""

    def is_alpha_or_space_or_digit(self):
        for char in self.orgText:
            if not (char.isalpha() or char.isspace() or char.isdigit()):
                return False
        return True

    def translate(self):
        if self.is_alpha_or_space_or_digit():
            return self.eng_to_b(self.orgText)
        else:
            return self.b_to_eng(self.orgText)

    def __str__(self):
        return self.translate()


if __name__ == '__main__':
    text = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else sys.argv[1]
    tr = Translator(text)
    print(tr)
