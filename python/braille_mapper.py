"""Mapping class between braille and english characters."""
class BrailleMapper:
    def __init__(self):

        # Maps the braille representation to english alphabetic characters
        self.braille_to_letter = {
            "O.....": "a",
            "O.O...": "b",
            "OO....": "c",
            "OO.O..": "d",
            "O..O..": "e",
            "OOO...": "f",
            "OOOO..": "g",
            "O.OO..": "h",
            ".OO...": "i",
            ".OOO..": "j",
            "O...O.": "k",
            "O.O.O.": "l",
            "OO..O.": "m",
            "OO.OO.": "n",
            "O..OO.": "o",
            "OOO.O.": "p",
            "OOOOO.": "q",
            "O.OOO.": "r",
            ".OO.O.": "s",
            ".OOOO.": "t",
            "O...OO": "u",
            "O.O.OO": "v",
            ".OOO.O": "w",
            "OO..OO": "x",
            "OO.OOO": "y",
            "O..OOO": "z",
            "..OO.O": ".",
            "..O...": ",",
            "..O.OO": "?",
            "..OOO.": "!",
            "..OO..": ":",
            "..O.O.": ";",
            "....OO": "-",
            ".O..O.": "/",
            ".OO..O": "<",
            "O.O..O": "(",
            ".O.OO.": ")",
            "......": " "
        }
        
        # Maps the braille representation to numeric characters
        self.braille_to_number = {
            "O.....": "1",
            "O.O...": "2",
            "OO....": "3",
            "OO.O..": "4",
            "O..O..": "5",
            "OOO...": "6",
            "OOOO..": "7",
            "O.OO..": "8",
            ".OO...": "9",
            ".OOO..": "0"
        }

        # Reverse the mappings to translate in both directions   
        self.letter_to_braille = {v: k for k, v in self.braille_to_letter.items()}
        self.number_to_braille = {v: k for k, v in self.braille_to_number.items()}

    # Gets the English character of a given braille representation
    def get_english(self, braille, is_number):
        return self.braille_to_number.get(braille, None) if is_number else self.braille_to_letter.get(braille, None)

    # Gets the braille representation of a given English character
    def get_braille(self, character, is_number):
        return self.number_to_braille.get(character, None) if is_number else self.letter_to_braille.get(character, None)