from sys import argv
from enum import Enum

class CharacterType(Enum):
    CAPITAL = '.....O'
    DECIMAL = '.O...O'
    NUMBER = '.O.OOO' 
    SPACE = '......'

class Translator:
    def __init__(self):
        self.next_capital = False
        self.next_number = False
        self.next_decimal = False

class BrailleTranslator(Translator):
    def __init__(self):
        super().__init__()
        
        self.latin_alphabet = { 'A': 'O.....', 'B': 'O.O...', 'C': 'OO....',
                                'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...',
                                'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...',
                                'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.',
                                'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
                                'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.',
                                'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
                                'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
                                'Y': 'OO.OOO', 'Z': 'O..OOO', 
                                }
        
        self.latin_symbols = {  '.': '..OO.O', ',': '..O...', '?': '..O.OO',
                                '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
                                '-': '....OO', '/': '.O..O.', '<': '.OO..O',
                                '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'}
        
        self.latin_numbers = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', 
                              '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                              '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
                              '0': '.OOO..'}
        
        self.braille_alphabet = {}
        self.braille_numbers = {}
        
        for key, value in self.latin_alphabet.items():
            self.braille_alphabet[value] = key
        
        for key, value in self.latin_numbers.items():
            self.braille_numbers[value] = key
            
    def is_braille(self, text) -> bool:
        if len(text) % 6 == 0:
            for charac in text:
                if charac != 'O' and charac != '.':
                    return False
            return True
        return False
    
    def __translate_to_braille(self, latin_text: str) -> str:
        converted_text = ''
        for charac in latin_text:
            if charac.isupper():
                converted_text += CharacterType.CAPITAL.value
            elif charac.isnumeric():
                converted_text += (CharacterType.NUMBER.value + self.latin_numbers.get(charac))
            elif charac in self.latin_symbols:
                converted_text += self.latin_symbols.get(charac) # TODO: check for decimal
            elif charac == ' ':
                converted_text += CharacterType.SPACE.value
            else:
                converted_text += self.latin_alphabet.get(charac.upper())
        return converted_text
    
    def __translate_to_latin(self, braille_text: str) -> str:
        converted_text = ''
        for charac in braille_text:
            if charac == CharacterType.CAPITAL.value:
                self.next_capital = True
                continue
            if self.next_capital:
                self.next_capital = False
                converted_text += self.braille_alphabet.get(charac).upper()
                continue
            if charac == CharacterType.NUMBER.value:
                self.next_number = True
                continue
            if self.next_number:
                self.next_number = False
                converted_text += self.braille_numbers.get(charac)
                continue
            if charac == CharacterType.SPACE.value:
                converted_text += ' '
                continue
            if charac == CharacterType.DECIMAL.value:
                self.next_decimal = True
                continue
            if self.next_decimal:
                self.next_decimal = False
                converted_text += self.latin_symbols.get(charac)
                continue
            if charac in self.latin_symbols:
                converted_text += self.latin_symbols.get(charac)
            else:
                converted_text += self.braille_alphabet.get(charac).lower()
        return converted_text
   
    def translate(self, text: str) -> str:
        characs = []
        if self.is_braille(text):
            for i in range(0, len(text), 6):
                characs.append(text[i:i+6])
            print(self.__translate_to_latin(characs))
        else:
            characs = list(text)
            print(self.__translate_to_braille(text))

def main():
    if len(argv) > 1:
        translator = BrailleTranslator()
        text = ' '.join(argv[1:])
        translator.translate(text)
    else:
        pass
    
if __name__ == '__main__':
    main()