from sys import argv
from enum import Enum

class CharacterType(Enum):
    CAPITAL = '.....O'
    DECIMAL = '.O...O'
    NUMBER = '.O.OOO' 
    SPACE = '......'

class Translator:
    def __init__(self):
        pass

class BrailleTranslator(Translator):
    def __init__(self):
        super().__init__()
        self.__next_capital = False
        self.__next_number = False
        
        self.__latin_alphabet = {'A': 'O.....', 'B': 'O.O...', 'C': 'OO....',
                                'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...',
                                'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...',
                                'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.',
                                'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
                                'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.',
                                'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
                                'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
                                'Y': 'OO.OOO', 'Z': 'O..OOO'}
        
        self.__latin_symbols = {'.': '..OO.O', ',': '..O...', '?': '..O.OO',
                                '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
                                '-': '....OO', '/': '.O..O.', '<': '.OO..O',
                                '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'}
        
        self.__latin_numbers = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', 
                              '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                              '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
                              '0': '.OOO..'}
        
        self.__braille_alphabet = {value: key for key, value in self.__latin_alphabet.items()}
        self.__braille_numbers = {value: key for key, value in self.__latin_numbers.items()}
            
    def __is_braille(self, text) -> bool:
        if len(text) % 6 == 0:
            for charac in text:
                if charac != 'O' and charac != '.':
                    return False
            return True
        return False
    
    def __translate_to_braille(self, latin_text: str) -> str:
        converted_text = ''
        first_number = False
        for charac in latin_text:
            if charac.isalpha():
                if charac.isupper():
                    converted_text += CharacterType.CAPITAL.value
                converted_text += self.__latin_alphabet.get(charac.upper())
            elif charac.isnumeric():
                if not first_number:
                    converted_text += CharacterType.NUMBER.value
                    first_number = True
                converted_text += self.__latin_numbers.get(charac)
            elif charac in self.__latin_symbols.keys():
                if charac == '.':
                    if first_number:
                        converted_text += CharacterType.DECIMAL.value
                    else:
                        converted_text += self.__latin_symbols.get(charac)
            elif charac == ' ':
                if first_number:
                    first_number = False
                converted_text += CharacterType.SPACE.value
        return converted_text
    
    def __translate_to_latin(self, braille_text: str) -> str:
        converted_text = ''
        for charac in braille_text:
            if charac == CharacterType.CAPITAL.value:
                self.__next_capital = True
                continue
            if self.__next_capital:
                self.__next_capital = False
                converted_text += self.__braille_alphabet.get(charac).upper()
                continue
            if charac == CharacterType.NUMBER.value:
                self.__next_number = True
                continue
            if self.__next_number:
                self.__next_number = False
                converted_text += self.__braille_numbers.get(charac)
                continue
            if charac == CharacterType.SPACE.value:
                converted_text += ' '
                continue
            if charac == CharacterType.DECIMAL.value:
                converted_text += '.'
                continue
            if charac in self.__latin_symbols:
                converted_text += self.__latin_symbols.get(charac)
            else:
                converted_text += self.__braille_alphabet.get(charac).lower()
        return converted_text
   
    def translate(self, text: str) -> str:
        characs = []
        if self.__is_braille(text):
            for i in range(0, len(text), 6):
                characs.append(text[i:i+6])
            print(self.__translate_to_latin(characs))
        else:
            characs = list(text)
            print(self.__translate_to_braille(characs))

def main():
    if len(argv) > 1:
        translator = BrailleTranslator()
        text = ' '.join(argv[1:])
        translator.translate(text)
        return 0
    return 1
    
if __name__ == '__main__':
    main()