from language import english_to_braille, special_char_to_braille, indicator_to_braille, number_to_braille
import sys 


class Translator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.english_to_braille = english_to_braille
        self.special_char_to_braille =special_char_to_braille
        self.indicator_to_braille = indicator_to_braille
        self.number_to_braille = number_to_braille
    
    def is_braille(self):
        '''
        Function to check if the given input is in braille or not
        
        '''
        if len(self.input_string) == 6 and all(char in '0.' for char in self.input_string):
            return True
        else:
            return False
        
    def translate_english_to_braille(self):
        braille = []
        is_digit=False
        for character in self.input_string:
          
            if character.isnumeric():
                if not is_digit:
                    is_digit=True
                    braille.append(self.indicator_to_braille['Number'])
                braille.append(self.number_to_braille[character])
            
            elif character ==' ': 
            #can be generalized to in operator incase of multiple special character
                is_digit=False
                braille.append(self.special_char_to_braille[character])
                
           
            elif character.isupper():
                braille.append(self.indicator_to_braille['Capital'])
                braille.append(self.english_to_braille[character.lower()])
            else:
                braille.append(self.english_to_braille[character])
        
        return "".join(braille)

def main():
    input_string = " ".join(sys.argv[1:])
    translator = Translator(input_string)
    result = translator.translate_english_to_braille()
    print(result)
if __name__ == "__main__":
    main()