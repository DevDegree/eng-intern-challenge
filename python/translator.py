import sys

class BrailleConverter:

    # English Dictionary Mapping
    english_letters_dict = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
        "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO"
    }

    english_numbers_dict = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
        "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }

    # Braille Dictionary Mapping
    braille_letters_dict = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
        "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
        "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
        ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
        "OO.OOO": "y", "O..OOO": "z"
    }

    braille_numbers_dict = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
        "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
    }

    # Helper Methods

    def is_braille(self, string):
        for char in string:
            if char != 'O' and char != '.':
                return False
        return True

    def convert_to_english(self, string):
        capital_follows = number_follows = False
        english = []

        for symbol in [string[i:i+6] for i in range(0, len(string), 6)]:
            if symbol == ".....O":
                capital_follows = True
            elif symbol == ".O.OOO":
                number_follows = True
            elif symbol == "......":
                english.append(" ")
                number_follows = False
            else:
                if number_follows:
                    char = self.braille_numbers_dict[symbol]
                elif capital_follows:
                    char = self.braille_letters_dict[symbol].upper()
                else:
                    char = self.braille_letters_dict[symbol]
                english.append(char)
                capital_follows = False

        return ''.join(english)

    def convert_to_braille(self, string):
        braille = []
        number_mode = False

        for letter in string:
            if letter.isdigit():
                if not number_mode:
                    braille.append(".O.OOO")
                    number_mode = True
                braille.append(self.english_numbers_dict[letter])
            else:
                number_mode = False
                if letter.isupper():
                    braille.append(".....O")
                    letter = letter.lower()
                braille.append(self.english_letters_dict[letter])

        return ''.join(braille)


if __name__ == "__main__":
    converter = BrailleConverter()
    inputs = sys.argv[1:]

    if len(inputs) > 1:
        result = "......".join(converter.convert_to_braille(word) for word in inputs)
    else:
        input_text = inputs[0]
        result = (converter.convert_to_english(input_text) 
                  if converter.is_braille(input_text) 
                  else converter.convert_to_braille(input_text))

    print(result)