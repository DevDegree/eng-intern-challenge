from sys import argv
from enum import Enum

class CharacterType(Enum):
    CAPITAL = '.....O'
    NUMBER = '.O.OOO' 
    SPACE = '......'

class Translator:
    def __init__(self) -> None:
        pass

class BrailleTranslator(Translator):
    def __init__(self) -> None:
        super().__init__()
        
        self.__latin_alphabet = {'A': 'O.....', 'B': 'O.O...', 'C': 'OO....',
                                'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...',
                                'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...',
                                'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.',
                                'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
                                'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.',
                                'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
                                'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
                                'Y': 'OO.OOO', 'Z': 'O..OOO'}
        
        self.__latin_numbers = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', 
                              '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
                              '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
                              '0': '.OOO..'}
        
        self.__braille_alphabet = {value: key for key, value in self.__latin_alphabet.items()}
        self.___braille_numbers = {value: key for key, value in self.__latin_numbers.items()}
        
        self.__actions = [CharacterType.CAPITAL.value, CharacterType.NUMBER.value, CharacterType.SPACE.value]
    
    def _translate_to_braille(self, latin_text: str) -> str:
        converted_text = ''
        first_number = False
        for charac in latin_text:
            if charac.isalpha():
                if charac.isupper():
                    converted_text += CharacterType.CAPITAL.value
                converted_text += self.__latin_alphabet.get(charac.upper())
                continue
            if charac.isnumeric():
                if not first_number:
                    converted_text += CharacterType.NUMBER.value
                    first_number = True
                converted_text += self.__latin_numbers.get(charac)
                continue
            if charac == ' ':
                if first_number:
                    first_number = False
                converted_text += CharacterType.SPACE.value
                continue
        return converted_text
    
    def _translate_to_latin(self, braille_text: str) -> str:
        converted_text = ''
        next_capital = False
        next_number = False

        for charac in braille_text:
            if charac in self.__actions:
                action = self.__actions[self.__actions.index(charac)]
        
                if action == CharacterType.CAPITAL.value:
                    next_capital = True
                elif action == CharacterType.NUMBER.value:
                    next_number = True
                elif action == CharacterType.SPACE.value:
                    if next_number:
                        next_number = False
                    converted_text += ' '
                else:
                    converted_text += action
                continue
                
            if next_capital:
                next_capital = False
                converted_text += self.__braille_alphabet.get(charac).upper()
                continue
            if next_number:
                converted_text += self.___braille_numbers.get(charac)
                continue
            
            converted_text += self.__braille_alphabet.get(charac).lower()
                    
        return converted_text
   
    def _is_braille(self, text) -> bool:
        if len(text) % 6 == 0:
            for charac in text:
                if charac != 'O' and charac != '.':
                    return False
            return True
        return False
    
    def _split_braille_characters(self, text: str) -> list:
        return [text[i:i+6] for i in range(0, len(text), 6)]
   
    def translate(self, text: str) -> str:
        characs = []
        if self._is_braille(text):
            characs = self._split_braille_characters(text)
            # print(self._translate_to_latin(characs))
            return self._translate_to_latin(characs)
        else:
            characs = list(text)
            # print(self._translate_to_braille(characs))
            return self._translate_to_braille(characs)

def process_argv(argv: list[str]) -> str:
    return ' '.join(argv[1:])

def main():
    if len(argv) > 1:
        translator = BrailleTranslator()
        translator.translate(process_argv(argv))
        return 0
    return 1
    
if __name__ == '__main__':
    main()