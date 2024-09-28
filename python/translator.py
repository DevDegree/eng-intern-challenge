import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO', ' ': '......',
}

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
}

BRAILLE_DIGITS = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


class BrailleTranslator:
    def __init__(self, text: str):
        self.text: str = text
        self.language = self.detectLang()
        
    
    def detectLang(self)-> str:
        multiple_of_six = len(self.text) % 6 == 0
        lang = "bra"
        for i in self.text:
            if not (i == 'O' or i == '.'):
                lang = "eng"        
        if not multiple_of_six:
            lang = "eng" 
            
        return lang
    
    def translate(self):
        translated = ""
        if self.language == "bra":
            translated = self.bra_to_eng()
        elif self.language == "eng":
            translated = self.eng_to_bra()
        
        return translated
    
    def eng_to_bra(self):
        translated = ""
        
        for char in self.text:    
            if char.isdigit():
                translated = translated +ENGLISH_TO_BRAILLE['number']
                
            elif char.isupper():
                translated = translated +ENGLISH_TO_BRAILLE['capital']

            translated = translated + ENGLISH_TO_BRAILLE[char.lower()]
        return translated
    
    def bra_to_eng(self):
        bra_char = []
        translated = ""
        is_digit = False
        is_capital = False
        for i in range(0, len(self.text), 6):
            bra_char.append(self.text[i:i + 6])
        
        for i in bra_char:
            if i == ENGLISH_TO_BRAILLE['number']:
                is_digit = True
            elif is_digit:
                translated = translated +BRAILLE_DIGITS[i]
                is_digit = False
            elif i == ENGLISH_TO_BRAILLE['capital']:
                is_capital = True
            elif is_capital:
                translated = translated + BRAILLE_DIGITS[i].upper()
                is_capital = False
            
        return translated

if __name__ == '__main__':
    
    text = ''.join(sys.argv[1:])
    translator = BrailleTranslator(text)
    result = translator.translate()
    print(result)

    
    
    

