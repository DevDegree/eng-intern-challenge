import sys

ENG_TO_BRL = {
    # Following Codes
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',
    'decimal_follows': '.O...O',

    # a-z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    # Special symbols
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......',
}

ENG_TO_BRL_NUM = {
    # 0-9
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRL_TO_ENG = {k: v for v, k in ENG_TO_BRL.items()}
BRL_TO_ENG_NUM = {k: v for v, k in ENG_TO_BRL_NUM.items()}

class Translator:
    def __init__(self, texts):
        self.texts = texts
    
    # If texts are braille or english
    # It is assumed that English contains A-Z, a-z, 0-9, spaces but NOT .
    def is_braille(self):
        for text in self.texts:
            if text != '.' and text != 'O':
                return False
        return True
    
    def eng_to_brl(self):
        translation = ""
        writing_nums = False
        for text in self.texts:
            if text == ' ':
                writing_nums = False
            if text.isupper():
                translation += ENG_TO_BRL['capital_follows'] + ENG_TO_BRL[text.lower()]
            elif text == '.' and writing_nums:
                translation += ENG_TO_BRL['decimal_follows'] + ENG_TO_BRL[text]
            elif text.isnumeric():
                if not writing_nums:
                    writing_nums = True
                    translation += ENG_TO_BRL['number_follows']
                translation += ENG_TO_BRL_NUM[text]
            else:
                translation += ENG_TO_BRL[text]
        return translation

    def brl_to_eng(self):
        if len(self.texts) % 6 != 0:
            raise Exception("Attempted to translate improperly formatted Braille text!")
        translation = ""
        code = self.texts[0:6]

        next_upper = False
        next_numbers = False
        next_decimal = False
        for i in range(int(len(self.texts) / 6)):
            code = self.texts[i * 6:(i * 6 + 6)]
            next = BRL_TO_ENG[code]
            if next == ' ': # reset next numbers
                next_numbers = False

            if next == 'capital_follows':
                next_upper = True
                continue
            if next == 'number_follows':
                next_numbers = True
                continue
            if next == 'decimal_follows':
                next_decimal = True
                continue
            
            if next_upper: # we may assume that a letter follows the 'capital_follows'
                next_upper = False
                translation += BRL_TO_ENG[code].upper()
            else:
                if next_decimal: # we may assume that a decimal follows the 'decimal_follows'
                    translation += BRL_TO_ENG[code]
                    next_decimal = False
                elif next_numbers:
                    translation += BRL_TO_ENG_NUM[code]
                else:
                    translation += BRL_TO_ENG[code]

        return translation

    def translate(self):
        if self.is_braille():
            return self.brl_to_eng()
        else:
            return self.eng_to_brl()
        
    def output(self):
        print(self.translate())

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:])
    translator = Translator(msg)
    translator.output()