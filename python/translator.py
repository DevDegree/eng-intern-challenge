import sys

# Braille Dictionaries
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "num", ".O...O": "."
}

braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "......": " "
}

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", ".": ".O...O", "1": "O.....", "2": "O.O...",
    "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

class BrailleTranslator:
    def __init__(self, input_str):
        self.input_str = input_str
        self.braille_mode = False
        self.capital_mode = False
    # to check if the input string is braille or not
    def is_braille(self):
        return all(c in 'O.' for c in self.input_str.replace(' ', ''))
    # translate from braille to english
    def translate_to_english(self):
        result = []
        i = 0
        while i < len(self.input_str):
            symbol = self.input_str[i:i + 6]
            i += 6

            if symbol == ".....O":
                self.capital_mode = True
                continue
            elif symbol == ".O.OOO":
                self.braille_mode = True
                continue
            
            if symbol in braille_to_english:
                char = braille_to_english[symbol]
                if self.braille_mode:
                    if char == " ":
                        self.braille_mode = False
                    else:
                        result.append(braille_to_number.get(symbol, char))
                elif self.capital_mode:
                    result.append(char.upper())
                    self.capital_mode = False
                else:
                    result.append(char)
            elif symbol == "......":
                result.append(" ")

        return ''.join(result)
    # translates from english to braille
    def translate_to_braille(self):
        result = []
        number_mode = False

        for char in self.input_str:
            if char == " ":
                result.append(english_to_braille[" "])
                number_mode = False
            elif char.isdigit():
                if not number_mode:
                    result.append(".O.OOO")
                    number_mode = True
                result.append(english_to_braille[char])
            elif char.isupper():
                result.append(".....O")
                result.append(english_to_braille[char.lower()])
                number_mode = False
            else:
                if char.isnumeric():
                    result.append(".O.OOO")
                result.append(english_to_braille[char])
                number_mode = False

        return ''.join(result)
#main
if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(input_text)

    if translator.is_braille():
        print(translator.translate_to_english())
    else:
        print(translator.translate_to_braille())
# please hire me 
