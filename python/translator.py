class BrailleTranslator:
    BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.','u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO','z': 'O..OOO',
        '0': '.O.OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
        ' ': '......', 'cap': '.....O','num': '.O.OOO'
    }

    ENGLISH = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
        '......': ' ', '.....O': 'cap', '.O.OOO': 'num'
    }
    
    NUMBERS = {
        '.O.OOO': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'
    }

    def __init__(self, text):
        self.text = text

    def is_braille(self):
        args = self.text.replace(" ", "")
        for char in args:
            if char not in "O.":
                return False
        return True

    def translate_to_braille(self):
        braille_text = ""
        number_mode = False 

        for char in self.text:
            if char.isupper():
                braille_text += self.BRAILLE['cap']
                braille_text += self.BRAILLE[char.lower()]
                number_mode = False 
            elif char.isdigit():
                if not number_mode:
                    braille_text += self.BRAILLE['num']
                    number_mode = True
                braille_text += self.BRAILLE[char]
            elif char in self.BRAILLE:
                braille_text += self.BRAILLE[char]
                number_mode = False 
            else:
                braille_text += "......" 
                number_mode = False 
        return braille_text

    def translate_to_english(self):
        english_text = ""
        i = 0
        capital_mode = False
        number_mode = False 

        while i < len(self.text):
            braille_char = self.text[i:i+6]

            if braille_char == self.BRAILLE['cap']:
                capital_mode = True
                number_mode = False
            elif braille_char == self.BRAILLE['num']:
                number_mode = True
            elif braille_char == '......': 
                english_text += ' '
                number_mode = False
                capital_mode = False
            else:
                if number_mode:
                    english_text += self.NUMBERS[braille_char]
                else:
                    letter = self.ENGLISH[braille_char]
                    if capital_mode:
                        english_text += letter.upper()
                    else:
                        english_text += letter
                capital_mode = False
            i += 6
        return english_text

    def translate(self):
        if self.is_braille():
            return self.translate_to_english()
        else:
            return self.translate_to_braille()

if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    translator = BrailleTranslator(input_text)
    print(translator.translate())

