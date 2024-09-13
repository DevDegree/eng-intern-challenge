from language import english_to_braille, special_char_to_braille, indicator_to_braille, number_to_braille
import sys 


class Translator:

    '''
    Checks the given input string language and translated to other language. 
    current language support is braille and english. 
    
    Language is defined in language.py
    Another layer of abstraction can be created to just run the translation.
    '''
    def __init__(self, input_string: str):
        '''
        Paramters
        input_string: (braille or english)
        
        '''
        self.input_string = input_string

        #Declaring variables for english to braille translation
        self.english_to_braille = english_to_braille
        self.special_char_to_braille =special_char_to_braille
        self.indicator_to_braille = indicator_to_braille
        self.number_to_braille = number_to_braille

        #Declaring variables for braille to english translation
        self.braille_to_english = {br:char for char, br in english_to_braille.items()}
        self.braille_to_number = {br:num for num, br in number_to_braille.items()}
        self.braille_to_indicator = {br:ind for ind, br in indicator_to_braille.items()}
        self.braille_to_special_char = {br:spec for spec, br in special_char_to_braille.items()}
    
    
    def is_braille(self):
        '''
        Function to check if the given input is in braille or not
        Given logic is each braille term contains either 0 or . and is of length 6
        
        '''
        if len(self.input_string) % 6==0 and all(char in 'O.' for char in self.input_string):
            return True
        else:
            return False
        
    def translate_english_to_braille(self):
        '''
        Function converts english sentence to braille 
        Supports capital letters, numbers and punctuation. 

        input: Abc 123
        
        Returns 
        output .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
        
        '''
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
                
           
            elif character.isupper(): #checks for capitalization
                braille.append(self.indicator_to_braille['Capital'])
                braille.append(self.english_to_braille[character.lower()]) #since the language dict is in lowercase
            else:
                braille.append(self.english_to_braille[character]) # default case
        
        return "".join(braille)
    
    def transalte_braille_to_english(self):
        '''
        Converts a given braille string to english
        Note: A punctuation follows rule might help to distinguish symbols like > with the letter, or a context variable can be defined
        
        '''
        english = []
        index=0
        combined_dict = {**self.braille_to_english,**self.braille_to_special_char}
        
        while index <= len(self.input_string)-6: # loop till the last segment of length 6
            current_br_str = self.input_string[index:index+6]
          
            
            
            if current_br_str in self.braille_to_indicator.keys():  #Check for indicator

                current_braille_to_eng = self.braille_to_indicator[current_br_str]
                #Logic for capitalization
                if current_braille_to_eng == 'Capital':
                    index+=6
                    next_br_str  =  self.input_string[index:index+6]
                    next_braille_to_eng = self.braille_to_english[next_br_str]
                    english.append(next_braille_to_eng.upper())
                
                #Logic if a number indicator is followed, would run until a space is found 
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
                
                #For Decimal encounter 
                #TO do for future usecase since there is ambiguity for test cases on how decimal will be evaluated. 
                elif  current_braille_to_eng == 'Decimal':
                    index+=6
                    english.append(self.braille_to_number[self.input_string[index:index+6]])
                else:
                    pass
                         
            #default case. 
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