import sys
from enum import Enum

# translator class
class Translator:
    # language type class
    class Type(Enum):
        BRAILLE = 1
        ENGLISH = 2
        
    # mappings
    english_map = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
        "capital follows": ".....O",
        "number follows": ".O.OOO",
        " ": "......",
    }
    braille_map = {value: key for key, value in english_map.items()}
    num_map = {
        "0": "j",
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
    }
    num_map.update({v: k for k, v in num_map.items()})
    
    # initialization function
    def __init__(self, input):
        self.input = input
        self.type = self.check_type()
        
    # determine type of language
    def check_type(self):
        # alternative: can check for text contains '.'
        
        if len(self.input) > 1: # braille input should have no spaces
            return Translator.Type.ENGLISH
        
        s = self.input[0]
        number = False
        
        if len(s) % 6 != 0: # braille input must be multiple of 6 length
            return Translator.Type.ENGLISH
        
        for i in range(0, len(s), 6): 
            val = s[i:i+6]
            
            # braille input must be in mappable values
            if val not in Translator.braille_map.keys(): 
                return Translator.Type.ENGLISH
            
            english = self.braille_map[val]
            
            # check for correct translation of number follows
            if english == "number follows": 
                number = True
            elif number and english not in "abcdefghij" and english != "capital follows" and english != " ":
                return Translator.Type.ENGLISH
            
            # reset number follows on space
            if english == " ":
                number = False
        return Translator.Type.BRAILLE # all braille checks passed    
    
    # translate braille to english
    def braille_to_english(self):
        s = self.input[0]
        translated = ""
        capital = False
        number = False
        
        # iterate over braille words
        for i in range(0, len(s), 6): 
            val = s[i:i+6] 
            english_val = self.braille_map[val]
            
            # check for number follows and capital follows
            if english_val == "capital follows":
                capital = True
            elif english_val == "number follows":
                number = True
                capital = False
            elif english_val == " ":
                number = False # disable number follows on space
                capital = False
                translated += " "
            else:
                if number: # translate number follows
                    english_val = self.num_map[english_val]
                elif capital: # translate capital follows
                    english_val = english_val.upper()
                    capital = False # disable capital follows after one character
                translated += english_val     
        return translated
    
    # translate english to braille
    def english_to_braille(self):
        translated = ""
        
        # iterate over all words
        for j, s in enumerate(self.input):
            number = False
            # iterate over all characters
            for val in s: 
                # translate number 
                if val >= '0' and val <= '9': 
                    if not number: # print number follows if not yet
                        translated += self.english_map["number follows"]
                        number = True
                    translated += self.english_map[self.num_map[val]]
                else:
                    if val.isupper():
                        translated += self.english_map["capital follows"]
                        val = val.lower()
                    translated += self.english_map[val]
        
            # add space if not last word  
            if j != len(self.input) - 1:
                translated += self.english_map[" "]
        return translated
        
    # translate based on input type
    def translate(self):
        if self.type == Translator.Type.BRAILLE:
            return self.braille_to_english()
        else:
            return self.english_to_braille()
        
# main function
def main():
    input = sys.argv[1:]
    translator = Translator(input)
    print(translator.translate())

if __name__ == "__main__":
    main()