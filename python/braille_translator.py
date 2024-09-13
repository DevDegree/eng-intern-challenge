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

class BrailleTranslator:
    """A translator class for converting between English and Braille"""
    def __init__(self):
        self.english_to_braille_dict = english_to_braille
        self.braille_to_letter = {v: k for k, v in english_to_braille.items() if k.isalpha()}
        self.braille_to_digit = {v: k for k, v in english_to_braille.items() if k.isdigit()}
        self.capital_sign = self.english_to_braille_dict['CAPITAL']
        self.number_sign = self.english_to_braille_dict['NUMBER']
        self.space_sign = self.english_to_braille_dict[' ']

    def translate_to_braille(self, english_text: str) -> str:
        """
        translates English text to Braille
        args:
            english_text (str): The English text to translate
        returns:
            str: The translated Braille text
        """
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

    def translate_to_english(self, braille_text: str) -> str:
        """
        translates Braille text to English.
        args:
            braille_text (str): The Braille text to translate.
        returns:
            str: The translated English text.
        """
        english_output = []
        index = 0
        capital_mode = False
        number_mode = False
        while index < len(braille_text):
            braille_char = braille_text[index:index+6]
            index += 6

            if braille_char == self.space_sign:
                english_output.append(' ')
                number_mode = False
                capital_mode = False
                continue

            elif braille_char == self.capital_sign:
                capital_mode = True
                continue

            elif braille_char == self.number_sign:
                number_mode = True
                continue

            else:
                if number_mode:
                    char = self.braille_to_digit.get(braille_char, '')
                    if char:
                        english_output.append(char)
                    else:
                        pass
                else:
                    char = self.braille_to_letter.get(braille_char, '')
                    if char:
                        if capital_mode:
                            english_output.append(char.upper())
                            capital_mode = False
                        else:
                            english_output.append(char)
                    else:
                        pass

        return ''.join(english_output)
