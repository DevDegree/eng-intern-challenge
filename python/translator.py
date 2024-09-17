import sys

class translator:
    english_to_braille = {}
    braille_to_english_chars = {}
    braille_to_repeated_chars = {}
    braille_to_english_numbers = {}
    capital_follows = ".....O"
    number_follows = ".O.OOO"
    space = "......"

    @classmethod
    def main(cls, input):
        cls.initialize_maps()
        output = cls.translate_braille(input) if cls.is_braille(input) else cls.translate_english(input)
        print(output)

    @classmethod
    def translate_english(cls, string):
        braille_string = []
        append_number = True
        for char in string:
            # if character is digit and not already appended with digit follows then append
            if char.isdigit() and append_number:
                braille_string.append(cls.number_follows)
                append_number = False
            # if space then reset append number
            if char == ' ':
                append_number = True
            # if character is uppercase the append capital follows
            if char.isupper():
                braille_string.append(cls.capital_follows)
                char = char.lower()
            braille = cls.english_to_braille.get(char, '')
            braille_string.append(braille)
        return ''.join(braille_string)

    @classmethod
    def translate_braille(cls, string):
        english_string = []
        capitalise_word = False
        is_number = False
      # increment by 6 for braille
        for i in range(0, len(string) - 1, 6):
            substring = string[i:i+6]
            if substring == cls.capital_follows:
                capitalise_word = True
                continue
            if substring == cls.number_follows:
                is_number = True
                continue
            if substring == cls.space:
                is_number = False

            english_char = cls.braille_to_english_chars.get(substring)
            if english_char is None: # for repeated character
                english_char = cls.braille_to_repeated_chars.get(substring)
            
            if capitalise_word:
                english_string.append(english_char.upper())
                capitalise_word = False # resetting
                continue
            if is_number:
                english_string.append(cls.braille_to_english_numbers.get(substring))
                continue
            english_string.append(english_char)
        return ''.join(english_string)

    @staticmethod
    def is_braille(string):
        return string.startswith('O') or string.startswith('.')

    @classmethod
    def initialize_maps(cls):
        #alphabets and special characters
        cls.braille_to_english_chars = {
            "O.....": 'a',
            "O.O...": 'b',
            "OO....": 'c',
            "OO.O..": 'd',
            "O..O..": 'e',
            "OOO...": 'f',
            "OOOO..": 'g', 
            "O.OO..": 'h', 
            ".OO...": 'i', 
            ".OOO..": 'j',
            "O...O.": 'k', 
            "O.O.O.": 'l', 
            "OO..O.": 'm', 
            "OO.OO.": 'n', 
            "O..OO.": 'o',
            "OOO.O.": 'p',
            "OOOOO.": 'q', 
            "O.OOO.": 'r', 
            ".OO.O.": 's', 
            ".OOOO.": 't',
            "O...OO": 'u', 
            "O.O.OO": 'v', 
            ".OOO.O": 'w', 
            "OO..OO": 'x', 
            "OO.OOO": 'y',
            "O..OOO": 'z', 
            "......": ' ', 
            "..OO.O": '.', 
            "..O...": ',', 
            "..O.OO": '?',
            "..OOO.": '!', 
            "..OO..": ':', 
            "..O.O.": ';', 
            "....OO": '-', 
            ".O..O.": '/',
            ".OO..O": '<', 
            "O.O..O": '(', 
            ".O.OO.": ')'
        }

        #numbers
        cls.braille_to_english_numbers = {
            "O.....": '1', 
            "O.O...": '2', 
            "OO....": '3', 
            "OO.O..": '4', 
            "O..O..": '5',
            "OOO...": '6', 
            "OOOO..": '7', 
            "O.OO..": '8', 
            ".OO...": '9', 
            ".OOO..": '0'
        }

        #repeated chars
        cls.braille_to_repeated_chars = {"O..OO.": '>'}

        # intiliazing english to braille map
        cls.english_to_braille = {v: k for k, v in cls.braille_to_english_chars.items()}
        cls.english_to_braille.update({v: k for k, v in cls.braille_to_english_numbers.items()})
        cls.english_to_braille.update({v: k for k, v in cls.braille_to_repeated_chars.items()})

if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    translator.main(input)
