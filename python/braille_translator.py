english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
    "(": "O.O..O", ")": ".O.OO.", " ": "......",
    "DECIMAL": ".O...O",
    "CAPITAL": ".....O",  
    "NUMBER": ".O.OOO" 
}

braille_to_english = {v: k for k, v in english_to_braille.items()}

class BrailleTranslator:
    def __init__(self):
        self.english_to_braille_dict = english_to_braille
        self.braille_to_english_dict = braille_to_english

    def translate_to_braille(self, english_text):
        braille_output = []
        number_mode = False
        for c in english_text:
            if c == ' ':
                braille_output.append(self.english_to_braille_dict[' '])
                number_mode = False 
                continue
            if c.isdigit():
                if not number_mode:
                    braille_output.append(self.english_to_braille_dict['NUMBER'])
                    number_mode = True
                braille_char = self.english_to_braille_dict[c]
                braille_output.append(braille_char)
            else:
                if number_mode:
                    number_mode = False
                if c.isupper():
                    braille_output.append(self.english_to_braille_dict['CAPITAL'])
                    c = c.lower()
                braille_char = self.english_to_braille_dict.get(c)
                if braille_char:
                    braille_output.append(braille_char)
        return ''.join(braille_output)

