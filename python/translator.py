from constants import BRAILLE_MAP, INVERSE_BRAILLE_MAP
from dataclasses import dataclass
import sys

class Translator:
    BRAILLE_MAP = BRAILLE_MAP
    INVERSE_BRAILLE_MAP = INVERSE_BRAILLE_MAP

    def encode_braille(self, input):
        # Translates English to braille language. Map each element to it's 
        # corresponding braille counterpart. For every capital element, capitalize
        # the following letter. For every number element, expect following to be numbers
        # until a space match.
        output = ""
        is_number = False 
        for element in input:
            if element == " ":
                is_number = False
            elif is_number == True:
                pass
            elif element.isupper():
                output += self.BRAILLE_MAP['CAPITAL']
                element=element.lower()
            elif element.isnumeric():
                is_number = True
                output += self.BRAILLE_MAP['NUMBER']
            

            output += self.BRAILLE_MAP[element]
        return output
    
    def decode_braille(self, input):
        # Translates braille leanguage to English. Loop through every 6,
        # elements and match them to the corresponding English counterpart.
        # For every capital match, capitalize the following letter. For every
        # number match, expect following to be numbers until a space match.
        output = ""
        is_num = False
        is_cap = False

        for i in range(0, len(input), 6):
            braille_char = input[i:i+6]
            char = self.INVERSE_BRAILLE_MAP[braille_char]

            if (char == " "):
                is_num = False
            elif char == "CAPITAL":
                is_cap = True
                continue
            elif char == "NUMBER":
                is_num = True
                continue
            
            if is_cap:
                output += char.upper()
                is_cap = False
            elif is_num:
                output += str(ord(char) - 96)
            else:
                output += char

        return output

if __name__ == "__main__":

    # Parse user inputs and check for alphanumerics
    input = " ".join(sys.argv[1:])
    is_plaintext = input.replace(" ", "").isalnum()

    translator = Translator()
    
    if is_plaintext:
        print(translator.encode_braille(input))
    else:
        print(translator.decode_braille(input))
