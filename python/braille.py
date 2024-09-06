from dictionary import Dictionary
from word import Word

class Braille(Word): 
    def execute(self): 
        translated = ''
        idx = 0

        while idx < len(self.input_list):
            if self.input_list[idx] == Dictionary.BRAILLE['number']:
                idx += 1
                while self.input_list[idx] != Dictionary.BRAILLE[' '] and (idx+1) != len(self.input_list):
                    translated += Dictionary.NUMBER_REVERSE[self.input_list[idx]]
                    idx += 1
                if self.input_list[idx] == Dictionary.BRAILLE[' ']:
                    translated += Dictionary.BRAILLE_REVERSE[self.input_list[idx]]
                if (idx+1) == len(self.input_list):
                    translated += Dictionary.NUMBER_REVERSE[self.input_list[idx]]
            elif self.input_list[idx] == Dictionary.BRAILLE['capital']:
                idx += 1
                translated += Dictionary.BRAILLE_REVERSE[self.input_list[idx]].upper()
            else:
                translated += Dictionary.BRAILLE_REVERSE[self.input_list[idx]]
            idx += 1
        
        return translated
    
    
