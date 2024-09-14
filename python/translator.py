
from dataclasses import dataclass
from abc import ABC, abstractmethod
import sys
from collections import defaultdict

@dataclass
class BraileSymbol:
    '''
    BraileSymbol symbol representation
    '''
    letter: str = None 
    number: str = None
    special: str = None
    rule: str = None # capital follows, number follows, decimal follows, default

class Translator(ABC):
    '''
    Translator abstract class
    '''
    # one-to-one mapping is easy for further translation
    eng_letters_to_braile = { 'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO'}
    
    eng_numbers_to_braile = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}
    
    eng_special_to_braile = {' ': '......', '.': '..OO.O',',': '..O...', '?': '..O.OO',
        '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
        '/': '.O..O.', '<': '.OO...O', '>': 'O..OO.', '(': 'O.O..O',
        ')': '.O.OO.'}
    
    CAPITAL_FOLLOWS = '.....O'

    NUMBER_FOLLOWS = '.O.OOO'

    DECIMAL_FOLLOWS = '.O...O'

    @abstractmethod
    def run(self, input_str: str) -> str:
        '''
        Run the translation
        '''
        pass

    @abstractmethod
    def translate_by_rules(self, symbol) -> str:
        '''
        Translate the alphabet symbol, or keys in the hashtable, by corresponding rules
        '''
        pass


class BraileTranslator(Translator):
    def __init__(self) -> None:
        self.braile_to_eng = defaultdict(BraileSymbol)

        for letter, braile in self.eng_letters_to_braile.items():
            self.braile_to_eng[braile].letter = letter
        
        for number, braile in self.eng_numbers_to_braile.items():
            self.braile_to_eng[braile].number = number

        for special, braile in self.eng_special_to_braile.items():
            self.braile_to_eng[braile].special = special

        self.braile_to_eng[self.CAPITAL_FOLLOWS] = BraileSymbol(rule='capital follows')
        self.braile_to_eng[self.NUMBER_FOLLOWS] = BraileSymbol(rule = 'number follows')
        self.braile_to_eng[self.DECIMAL_FOLLOWS] = BraileSymbol(rule = 'decimal follows')

        self.mark = ''

    def reset_mark(self) -> None:
        self.mark = 'default'
    
    def update_mark(self, mark: str) -> None:
        self.mark = mark
        
    def translate_by_rules(self, symbol: str) -> str:

        output = self.braile_to_eng[symbol]

        if output.rule:
            self.update_mark(output.rule)
            return '.' if output.rule == 'decimal follows' else ''
        
        if self.mark == 'default':
            return output.letter or output.special or output.number
        
        if self.mark == 'capital follows':
            self.reset_mark()
            return output.letter.upper()
        
        if output.special == ' ':
            self.reset_mark() # reset mark for number
            return output.special
        
        return output.number

    def run(self, input_str: str) -> str:
        output = ''
        for i in range(0, len(input_str), 6):
            chunk = input_str[i:i+6]
            if chunk in self.braile_to_eng:
                output += self.translate_by_rules(chunk)
            else:
                raise ValueError(f"Invalid Braille chunk: {chunk}")
            
        return output
    
class EnglishTranslator(Translator):
    def __init__(self) -> None:
        self.eng_to_braile = {**self.eng_letters_to_braile, **self.eng_numbers_to_braile, **self.eng_special_to_braile}
        self.is_number = False

    def run(self, input_str: str) -> str:
        output = ''
        for char in input_str:
            output += self.translate_by_rules(char)
        return output
    
    def translate_by_rules(self, symbol: str) -> str:
        if symbol.isupper():
            return self.CAPITAL_FOLLOWS + self.eng_to_braile[symbol.lower()]
        elif symbol.isdigit():
            digit_braile = self.eng_to_braile[symbol]
            if self.is_number:
                return digit_braile
            else:
                self.is_number = True
                return self.NUMBER_FOLLOWS + digit_braile
        elif symbol == '.':
            if self.is_number:
                return self.DECIMAL_FOLLOWS
            else:    
                return self.eng_to_braile[symbol]
        elif symbol == ' ':
            if self.is_number:
                self.is_number = False
            return self.eng_to_braile[symbol]
        else:
            return self.eng_to_braile[symbol]
        

class TranslatorFactory:
    @staticmethod
    def get_translator(inputs: str) -> Translator:
        lang = 'braile'
        for c in inputs:
            if c not in ['O', '.']:
                lang = 'english'
                break
        if lang == 'braile':
            return BraileTranslator()
        elif lang == 'english':
            return EnglishTranslator()
        
def main():
    input_str = ' '.join(sys.argv[1:])
    if not input_str:
        print("Please provide an input string to translate.")
        sys.exit(1)

    translator = TranslatorFactory.get_translator(input_str)
    print(translator.run(input_str), end='')

if __name__ == '__main__':
    main()