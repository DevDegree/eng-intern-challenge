import json
import os
import sys

class BrailleTranslator:
    def __init__(self, file_path='braille_mapping.json'):
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        file_path = os.path.join(script_dir, file_path) 
        self.braille_dict = self.read_braille_dictionary(file_path)
        self.letters_dict = self.braille_dict['alphabets']
        self.numbers_dict = self.braille_dict['numbers']
        self.other_dict = self.braille_dict['other']
        self.inverse_letters_dict = {v: k for k, v in self.letters_dict.items()}
        self.inverse_numbers_dict = {v: k for k, v in self.numbers_dict.items()}

    def english_to_braille(self, input):
        braille_output = []
        isNumber = False
        for char in input:
            
            if char.isupper():
                braille_output.append(self.other_dict.get('capital', '......')) 
                char = char.lower()
                isNumber=False
        
            if char.isdigit(): 
                if not isNumber:
                    isNumber=True
                    braille_output.append(self.other_dict.get('number', '......'))  
                braille_output.append(self.numbers_dict.get(char, '......'))  
            elif char == ' ':
                braille_output.append(self.other_dict.get('space', '......'))  
                isNumber=False
            elif char in self.other_dict:
                braille_output.append(self.other_dict.get(char, '......'))  
                isNumber=False
            else:
                braille_output.append(self.letters_dict.get(char, '......'))  
                isNumber=False
    
        return ''.join(braille_output)

    def braille_to_english(self, braille_input):
        english_output = []
        isCapital=False
        isNum=False
        i = 0
        while i < len(braille_input):
            char = braille_input[i:i+6]
            if char == self.other_dict.get('capital'):
                i += 6
                isCapital=True
                continue
            elif char == self.other_dict.get('number'):
                i += 6
                isNum=True
                continue
            elif char==self.other_dict.get('space'):
                english_output.append(' ')
            elif isNum and char in self.inverse_numbers_dict:
                english_output.append(self.inverse_numbers_dict.get(char))
            elif char in self.inverse_letters_dict:
                letter=self.inverse_letters_dict.get(char)
                if(isCapital):
                    letter=letter.upper()
                    isCapital=False
                english_output.append(letter)
                isNum=False
            i += 6
        return ''.join(english_output)


    def read_braille_dictionary(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
        
    def detect_text(self,input_text):
        if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
            return self.braille_to_english(input_text)
        else:
            return self.english_to_braille(input_text)    

def main():
    translator = BrailleTranslator(file_path='braille_mapping.json')
    if len(sys.argv) > 1:
        input = " ".join(sys.argv[1:]) 
        output=translator.detect_text(input) 
        print(output)
    else:
        print("Please provide an input string to translate.")    
    

if __name__ == "__main__":
    main()
