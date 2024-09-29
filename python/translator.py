class EnglishToBrailleTranslator:
    def __init__(self):
        # English to Braille dictionary for letters and punctuation
        self.english_to_braille_letters_and_punctuations = {
            # Letters
            "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..",
            "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
            "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
            "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
            "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO",
            "Z": "O..OOO",

            # Numbers
            "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
            "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
            "9": ".OO...", "0": ".OOO..",

            # Punctuation
            ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
            ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
            "(": "O.O..O", ")": ".O.OO.", " ": "......"
        }

        # English to Braille dictionary for special symbols
        self.english_to_braille_special_symbols = {
            "NF": ".O.OOO",  # Number follows indicator
            "CF": ".....O",  # Capital follows indicator
            "DF": ".O...O"  # Decimal follows indicator
        }




class BrailleToEnglishTranslator:
    def __init__(self):
        # Braille to English dictionary
        self.braille_to_english_letters_and_punctuations = {
            "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
            "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
            "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
            "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
            "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
            "O..OOO": "Z",

            # Punctuation
            "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
            "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
            "O.O..O": "(", ".O.OO.": ")", "......": " "
        }

        self.braille_to_english_special_symbols = {
            ".O.OOO": "NF", ".....O": "CF", ".O...O": "DF"
        }

        self.braille_to_english_numbers = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
            "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
            ".OOO..": "0"
        }


if __name__=='__main__':
    pass