import sys
import re


class Translator:

    def __init__(self) -> None:
        self.braille_to_english = {
            'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
            'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
            '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
            'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
            'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
            'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
            'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ',
            '.....O': 'CAP', '.O.OOO': 'NUM',

        }

        self.braille_to_english_numbers = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
                                           'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
                                           '.OO...': '9', '.OOO..': '0'}
        self.english_to_braille = dict(
            map(lambda x: (x[1], x[0]), list(self.braille_to_english.items())))
        self.english_to_braille_numbers = dict(
            map(lambda x: (x[1], x[0]), list(self.braille_to_english_numbers.items())))

    def translate(self, input):
        return self.braille_to_english_translation(input) if self.is_braille(input) else self.english_to_braille_translation(input)

    def is_braille(self, input):
        pattern = re.compile('^[\\.O]+$')
        return bool(pattern.match(input))

    def english_to_braille_translation(self, input):
        output = ""
        is_number = False
        for char in input:
            if char.isnumeric():
                if not is_number:
                    output += self.english_to_braille['NUM']
                    is_number = True
                output += self.english_to_braille_numbers[char]
            elif char == ' ':
                output += self.english_to_braille[' ']
                is_number = False
            elif char.isupper():
                output += self.english_to_braille['CAP']
                output += self.english_to_braille[char.lower()]
            else:
                output += self.english_to_braille[char]
        return output

    def braille_to_english_translation(self, input):
        output = ""
        is_number = False
        i = 0
        while i < len(input):
            # read input in 6 char segments
            char = self.braille_to_english.get(input[i:i+6])
            if is_number:
                output += self.braille_to_english_numbers.get(input[i:i+6])
            elif char == "NUM":
                i += 6
                is_number = True
                output += self.braille_to_english_numbers.get(input[i:i+6])
            elif char == " ":
                is_number = False
                output += " "
            elif char == "CAP":
                i += 6
                output += self.braille_to_english.get(input[i:i+6]).upper()
            else:
                output += char
            i += 6
        return output


input = sys.argv[1:]

if (len(input) == 0):
    print("No input given")
else:
    input = " ".join(input)
    translator = Translator()
    print(translator.translate(input))
