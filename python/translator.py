import sys

# Object responsible for managing the alphabets
class EnglishBrailleAlphabet:
    def __init__(self):
        self._english_to_braille = {
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

        self._numbers_to_braille = {
            '1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            'O': '.OOO..',
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

        self._numbers_and_english_to_braille = {**self._numbers_to_braille, **self._english_to_braille}

        self._braille_to_english = {v: k for k, v in self._english_to_braille.items()}
        self._braille_to_numbers = {v: k for k, v in self._numbers_to_braille.items()}

    # translates an english character to braille
    def to_braille(self, english, number_follows):
        braille = ''

        if english.isupper():
            braille += self._capital_follows()
        elif english == '.':
            braille += self._decimal_follows()
        elif number_follows:
            braille += self._number_follows()

        braille += self._numbers_and_english_to_braille[english.lower()]

        return braille

    # translates a braille character to english
    def to_english(self, braille, upper=False, decimal=False, number=False):
        if (number and self._braille_to_english[braille] == ''):
            number = False

        if upper: return self._braille_to_english[braille].upper()
        if number or decimal: return self._braille_to_numbers[braille]

        return self._braille_to_english[braille]

    # checks if the braille character signals a coming capital
    def does_capital_follow(self, braille):
        return braille == self._capital_follows()

    def _capital_follows(self):
        return '.....O'
    
    # checks if the braille character signals a coming decimal
    def does_decimal_follow(self, braille):
        return braille == self._decimal_follows()

    def _decimal_follows(self):
        return '.O...O'
    
    # checks if the braille character signals a coming number
    def does_number_follow(self, braille):
        return braille == self._number_follows()
    
    def _number_follows(self):
        return '.O.OOO'

# Class for managing the translations
class Translator:
    def __init__(self, target, alphabet):
        self._target = target # what is being translated
        self._alphabet = alphabet # the alphabet we are using

    def __call__(self):
        if self._should_translate_to_english():
            return self._translate_to_english()
        else:
            return self._translate_to_braille()
        
    def _should_translate_to_english(self):
        joined = ''.join(self._target)
        return len(set(joined)) == 2 and 'O' in set(joined) and '.' in set(joined) and len(joined) % 6 == 0

    def _translate_to_english(self):
        spliced_braille = self._splice_braille()
        number_follows, is_number = False, False
        decimal_follows, is_decimal = False, False
        capital_follows, is_capital = False, False
        translated = ''

        for element in spliced_braille:
            number_follows = self._alphabet.does_number_follow(element)
            decimal_follows = self._alphabet.does_decimal_follow(element)
            capital_follows = self._alphabet.does_capital_follow(element)

            if number_follows:
                is_number = True
                number_follows = False
                continue

            if capital_follows:
                is_capital = True
                capital_follows = False
                continue

            if decimal_follows:
                is_decimal = True
                decimal_follows = False
                continue

            translated += self._alphabet.to_english(element, is_capital, is_decimal, is_number)

            is_capital = False
            is_decimal = False
            is_number = False

        return translated

    # turn the braille into distinct characters
    def _splice_braille(self):
        joined = ''.join(self._target)
        return [joined[i:i+6] for i in range(0, len(joined), 6)]

    def _translate_to_braille(self):
        translated = ''
        for i, letter in enumerate(' '.join(self._target)):
            if letter.isnumeric() and not ' '.join(self._target)[i-1].isnumeric():
                translated += self._alphabet.to_braille(letter, number_follows=True)
            else:
                translated += self._alphabet.to_braille(letter, number_follows=False)

        return translated


if __name__ == '__main__':
    t = Translator(sys.argv[1:], EnglishBrailleAlphabet())
    print(t())