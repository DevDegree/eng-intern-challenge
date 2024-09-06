from dictionary import Dictionary
from word import Word

class English(Word): 
    def execute(self): 
        translated = ''
       
        for idx,val in enumerate(self.word):
            if val.isdigit():
                if (idx == 0) or not self.word[idx-1].isdigit():
                    translated += Dictionary.BRAILLE['number'] 
                translated += Dictionary.NUMBER[val]
            else:
                if val.isupper():
                    translated += Dictionary.BRAILLE['capital']
                    translated += Dictionary.BRAILLE[val.lower()]
                elif val in Dictionary.BRAILLE.keys():
                    translated += Dictionary.BRAILLE[val]
        
        return translated

