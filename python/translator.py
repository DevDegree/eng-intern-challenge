import sys
class Translator: 
    #hash table of braille to english translation 
    translation = {
        'a' : "O.....",
        'b' : "O.O...",
        'c' : "OO....",
        'd' : "OO.O..",
        'e' : "O..O..",
        'f' : "OOO...",
        'g' : "OOOO..",
        'h' : "O.OO..",
        'i' : ".OO...",
        'j' : ".OOO..",
        'k' : "O...O.",
        'l' : "O.O.O.",
        "m" : "OO..O.",
        "m" : "OO.OO.",
        "o" : "O..OO.",
        'p' : "OOO.O.",
        'q' : "OOOOO.",
        'r' : "O.OOO.",
        's' : ".OO.O.",
        't' : ".OOOO.",
        'u' : "O...OO",
        'v' : "O.O.OO",
        'w' : ".OOO.O",
        'x' : "OO..OO",
        'y' : "OO.OOO",
        'z' : "O..OOO",
        'captial' : ".....O",
        'number' : ".O.OOO",
        " " : "......",
    }

    # def evaluate_arg(self, input : []) -> str:

    def value_to_key(self, value: str) -> str:
        for key, val in self.translation.items():
            if val == value:
                return key
            
    def translator(self) -> str:
        input = ""
        for arg in sys.argv[1:]:
            #concatenate arguments into one string
            if arg == (sys.argv[len(sys.argv) -1]): 
                input += arg
            else: 
                input += arg + " "
          
        if "." in input: 
            #braille input recieved
            translated_string = ""
            to_capitaize = False; 
            to_num = False
            for i in range (0, len(input), 6): 
                char = input[i:i+6]
                key = self.value_to_key(char)

                if key == 'captial':
                    to_capitaize = True; 
                    continue

                if key == 'number':
                    to_num = True; 
                    continue

                if key ==' ':                  
                    #append space
                    translated_string += " "
                    continue

                if to_num == True : 
                    num = ord(key) - 96
                    #append num
                    translated_string += str(num)
                    to_num == False
                    continue

                if to_capitaize == True : 
                    #append capitalized letter
                    translated_string += key.upper()
                    to_capitaize = False

                else:
                    #append lowercase letter
                    translated_string += str(key)

            return translated_string   
             
        else: 
            #english recieved --> translate to braille
            translated_string = ""
            is_num = False
            for char in input: 
                if char.isnumeric() == True:
                    if is_num == False :
                        translated_string += self.translation['number']
                        is_num = True
                    #translate number to correct letter equivalent
                    key = chr(int(char) + 96)
                    translated_string += self.translation[key]
                 
                else:    
                    is_num = False     
                    if char.isupper() == True:
                        translated_string += self.translation['captial']
                        translated_string += self.translation[str(char.lower())] 
                    else:
                        translated_string += self.translation[char] 

            return translated_string


obj = Translator()
print (obj.translator())
