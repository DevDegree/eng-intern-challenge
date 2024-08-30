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
