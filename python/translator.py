'''
steps: 
1. read input from CLA.
2. determine whether input is english or braille (exclusively O and .)
3. convert from one to the other
'''

import sys

BRAILLE_DICT = {
    # letters
    "A":"O.....",
    "B":"O.O...",
    "C":"OO....",
    "D":"OO.O..",
    "E":"O..O..",
    "F":"OOO...",
    "G":"OOOO..",
    "H":"O.OO..",
    "I":".O.O..",
    "J":".OOO..",
    "K":"O...O.",
    "L":"O.O.O.",
    "M":"OO..O.",
    "N":"OO.OO.",
    "O":"O..OO.",
    "P":"OOO.O.",
    "Q":"OOOOO.",
    "R":"O.OOO.",
    "S":".OO.O.",
    "T":".OOOO.",
    "U":"O...OO",
    "V":"O.O.OO",
    "W":".OOO.O",
    "X":"OO..OO",
    "Y":"OO.OOO",
    "Z":"O..OOO",
    
    # numbers
    "0":".OOO..",
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    
    # others
    "space":"......",
    "capital":".....O",
    "number":".O.OOO"}

def translator(user_input: str) -> str:
    
    # taking advantage of no duplicates rule for sets
    unique_chars = set(user_input)
    braille_chars = {"O", "."}
    
    # if all unique characters in user input are braille characters then input is braille
    if unique_chars.issubset(braille_chars):
        return brailleToEnglish(user_input)
    else:
        return englishToBraille(user_input)

# convert from english to braille
def englishToBraille(user_input: str) -> str:
    output = ""
    number_flag = False
    
    for char in user_input:
        if char.islower():
            output += BRAILLE_DICT.get(char.upper())
            
        elif char.isupper():
            output += (BRAILLE_DICT.get("capital") + BRAILLE_DICT.get(char))
        
        elif char.isnumeric():
            
            if number_flag:
                output += BRAILLE_DICT.get(char)
            else:
                output += (BRAILLE_DICT.get("number") + BRAILLE_DICT.get(char))
                number_flag = True
        
        else:
            output += BRAILLE_DICT.get("space")
            number_flag = False
        
    return output

# convert from braille into english
def brailleToEnglish(user_input: str) -> str:
    number_flag = False # true if interpreting numbers
    capital_flag = False # true if next is interpreted as capital
    
    output = ""
    
    s_length = len(user_input)
    chunk = 6
        
    for i in range(0, s_length, chunk):

        letter = user_input[i:i+chunk]
        
        if letter == BRAILLE_DICT.get("capital"):
            capital_flag = True
        
        elif letter == BRAILLE_DICT.get("number"):
            number_flag = True
        
        elif letter == BRAILLE_DICT.get("space"):
            output += " "
            number_flag = False
        
        else:
            
            if number_flag:
                
                for key in find_key(BRAILLE_DICT, letter):
                    if key.isnumeric():
                        output += key
                        break
                
            else:
                temp = ""
                
                for key in find_key(BRAILLE_DICT, letter):
                    if key.isalpha():
                        temp = key
                        break
                if capital_flag:
                    output += temp
                    capital_flag = False
                else:
                    output += temp.lower()
    
    return output

def find_key(dictionary: dict, value: str) -> list:
    return [key for key, val in dictionary.items() if val == value]

if __name__=="__main__":
    user_input = " ".join(sys.argv[1:])
    print(translator(user_input))
