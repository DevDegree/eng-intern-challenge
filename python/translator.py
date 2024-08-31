class BrailleMappings:
    def __init__(self):
        # Alphabet Braille to English
        self.braille_to_eng_alphabets = {
            "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
            "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
            ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
            "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
            "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
            "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
            "OO.OOO": "y", "O..OOO": "z"
        }

        # Numbers Braille to English
        self.braille_to_eng_number = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
            "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
            ".OO...": "9", ".OOO..": "0", ".O...O": "."
        }

        # Special symbols
        self.num = ".O.OOO"
        self.cap = ".....O"
        self.space = "......"

         # Invert dictionaries for English to Braille mappings
        self.eng_to_braille_alphabets = {v: k for k, v in self.braille_to_eng_alphabets.items()}
        self.eng_to_braille_numbers = {v: k for k, v in self.braille_to_eng_number.items()}

    def get_alphabet_mapping(self, char):
        return self.eng_to_braille_alphabets.get(char)

    def get_number_mapping(self, char):
        return self.eng_to_braille_numbers.get(char)

    def get_braille_alphabet(self, symbol):
        return self.braille_to_eng_alphabets.get(symbol)

    def get_braille_number(self, symbol):
        return self.braille_to_eng_number.get(symbol)

class BrailleTranslator:
    def __init__(self):
        self.mappings = BrailleMappings()

def main():
    import sys
    translator = BrailleTranslator()
    input_text = " ".join(sys.argv[1:])

    if all(c in ['O', '.', ' '] for c in input_text):
        print(translator.translate_to_english(input_text))
    else:
        print(translator.translate_to_braille(input_text))


if __name__ == "__main__":
    main()
