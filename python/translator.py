#MohammadHossein Karimian
#mohammadkarimian122@gmail.com
import sys
class BraillTranslator:
    def __init__(self):
        self.dict_letters_to_braille = {
            'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..',
            'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.',
            'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
            'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO', ' ': '......', '.': '..OO.O',
            ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
            '/': '.O..O.', '<': '.OO..O', '(': 'O.O..O', ')': '.O.OO.'
        }
        self.braille_to_letters = {value: key for key, value in self.dict_letters_to_braille.items()} #inverse of the above dictionary

        self.dict_numbers_to_braille = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
                                        '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
                                        '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
                                        }
        self.braille_to_numbers = {value: key for key, value in self.dict_numbers_to_braille.items()} #inverse of the above dictionary

        self.capital_follows = ".....O"
        self.decimal_follows = ".O...O" #Was not mentioned so it was not obvious how to consider it
        self.number_follows = ".O.OOO"

    def Check_Language(self, str):
        if len(str)<6:
            return "English"
        # Check to see that the first 6 letters contains anything other than . or O which are used for Braille
        for i in range(6):
            if str[i] != '.' and str[i] != 'O':
                return "English"
        return "Braille"

    def Translate_To_Braille(self, str):

        translating_numbers = False
        translated = ""
        for chr in str:
            if chr.isdigit():
                if not translating_numbers:
                    translated += self.number_follows
                    translating_numbers = True
                translated += self.dict_numbers_to_braille[chr]
            else:
                if chr == ' ':
                    translating_numbers = False
                if chr.isupper():
                    translated += self.capital_follows
                if chr == '>':
                    translated += 'O..OO.'
                    continue
                translated += self.dict_letters_to_braille[chr.upper()]
        return translated

    def Translate_To_English(self, str):

        translating_numbers = False
        next_is_capital = False
        translated = ""
        for i in range(0, len(str), 6):
            current = str[i:i+6]
            if current == self.capital_follows:
                next_is_capital = True
                continue
            if current == self.number_follows:
                translating_numbers = True
                continue
            if current == "......":
                translated += ' '
                translating_numbers = False
                continue
            if translating_numbers:
                translated += self.braille_to_numbers[current]
                continue
            if next_is_capital:
                translated += self.braille_to_letters[current]
                next_is_capital = False
            else:
                translated += self.braille_to_letters[current].lower()
        return translated


def main():
    result = ""
    translate = BraillTranslator()
    if len(sys.argv) < 2:
        print("Error: No input provided.")
        return
    str = ' '.join(sys.argv[1:])
    if translate.Check_Language(str) == "English":
        result = translate.Translate_To_Braille(str)
    else:
        result = translate.Translate_To_English(str)
    print(result)


if __name__ == "__main__":
    main()
