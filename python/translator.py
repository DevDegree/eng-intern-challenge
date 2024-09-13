from language import english_to_braille, special_char_to_braille, indicator_to_braille, number_to_braille
import sys 


class Translator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.english_to_braille = english_to_braille
        self.special_char_to_braille =special_char_to_braille
        self.indicator_to_braille = indicator_to_braille
        self.number_to_braille = number_to_braille


        self.braille_to_english = {br:char for char, br in english_to_braille.items()}
        self.braille_to_number = {br:num for num, br in number_to_braille.items()}
        self.braille_to_indicator = {br:ind for ind, br in indicator_to_braille.items()}
        self.braille_to_special_char = {br:spec for spec, br in special_char_to_braille.items()}
    
    
    def is_braille(self):
        '''
        Function to check if the given input is in braille or not
        
        '''
        if len(self.input_string) % 6==0 and all(char in 'O.' for char in self.input_string):
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
    
    def transalte_braille_to_english(self):
        english = []
        index=0
        combined_dict = {**self.braille_to_english,**self.braille_to_special_char}
        
        while index <= len(self.input_string)-6:
            current_br_str = self.input_string[index:index+6]
          
            
            
            if current_br_str in self.braille_to_indicator.keys():

                current_braille_to_eng = self.braille_to_indicator[current_br_str]
                if current_braille_to_eng == 'Capital':
                    index+=6
                    next_br_str  =  self.input_string[index:index+6]
                    next_braille_to_eng = self.braille_to_english[next_br_str]
                    english.append(next_braille_to_eng.upper())
                
                elif current_braille_to_eng == 'Number':
                    index+=6

                    while index <= len(self.input_string)-6 :
                        next_br_str = self.input_string[index:index+6]
                        
                        if next_br_str in self.braille_to_number.keys():
                            english.append(self.braille_to_number[next_br_str])
                        elif next_br_str in self.braille_to_special_char.keys():
                            english.append(self.braille_to_special_char[next_br_str])
                            break
                        else:
                            pass
                        index+=6
                elif  current_braille_to_eng == 'Decimal':
                    index+=6
                    english.append(self.braille_to_special_char[next_br_str])
                else:
                    pass
                         

            else:
                if current_br_str in self.braille_to_english:
                    english.append(self.braille_to_english[current_br_str])
                else:
                    english.append(self.braille_to_special_char[current_br_str])
                  
            index+=6
        return "".join(english)
  
def main():
    input_string = " ".join(sys.argv[1:])
    translator = Translator(input_string)
    if translator.is_braille():
        result = translator.transalte_braille_to_english()
    else:
        result = translator.translate_english_to_braille()
    print(result)
if __name__ == "__main__":
    main()