"""

-> the input is a string
requirements: 

 - Translator
  - Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.
  - For Braille, each character is stored as a series of `O` (the letter O) or `.` (a period).
  - Store Braille symbols as a 6 character string reading left to right, line by line, starting at the top left. See examples below.
  - When a Braille `capital follows` symbol is read, assume only the next symbol should be capitalized. 
  - When a Braille `number follows` symbol is read, assume all following symbols are numbers until the next `space` symbol.
- Braille Alphabet
  - Letters `a` through `z`
    - The ability to capitalize letters
  - Numbers `0` through `9`
  - The ability to include `spaces` ie: multiple words


--> we have to define multiple functions: 
        1) Language detection 
            -> in this case if there are no "." then it cannot be Braille, therefore it will be classified as english 
            -> similarly, if the character "O" does not exist in the string it will be classified as english (this is not a strong check argument however it can be used)
        2) English to Braille conversion function
        3) Braille to English conversion function 


in the version from english to braille need to make sure of the following: 

-> check if its a capital letter 
-> check if its a number, if it is then all the next symbols are numbers 
-> also differentiate between numbers and letters using .isalpha() and .isdigit()
-> need to handle decimal points 
-> only need to look through the keys this time and insert the value of that key from the dict


        
"""
import argparse
BRAILLE_MAP_CHAR = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}

BRAILLE_MAP_NUM = {
   '0': 'O.OOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}


cap_follow = '.....O'
dec_follow = '.O...O' # this is our "special" case no need of an array here 
num_follow = '.O.OOO'


def check_language(input_string: str): 
    if (len(input_string) % 6) != 0: # A Braille-represented string must be a multiple of 6 because of the 3x2 matrix
        translated_etob = english_to_braille(input_string)
        return translated_etob
    else: 
        translated_btoe = braille_to_english(input_string)
        return translated_btoe


def braille_to_english(braille_string: str):
    translate_text = [] #storage for final text 
    cap_next = False #init for checking capital letters and numbers 
    num_next = False 
    for i in range(0, len(braille_string), 6):
        chunk = braille_string[i:i + 6] # slice the string every 6 characters 

        if cap_next:
            for key in BRAILLE_MAP_CHAR: 
                if chunk == BRAILLE_MAP_CHAR[key]: 
                    translate_text.append(key.upper()) # making the key upper case 
                    break
                
            cap_next = False #reset since only 1 character is uppercase as per instructions  

        elif num_next: 
            for key in BRAILLE_MAP_NUM:
                if chunk == BRAILLE_MAP_NUM[key]: # look through the numbers mapping 
                    translate_text.append(key)
                    break
            num_next = True 

        elif chunk == cap_follow: # check for capital 
            cap_next = True  

        elif chunk == dec_follow: #check for decimal 
            translate_text.append('.')

        elif chunk == num_follow:
            num_next = True  

        else:  # "base" case 
            for key in BRAILLE_MAP_CHAR: 
                if chunk == BRAILLE_MAP_CHAR[key]:
                    translate_text.append(key)

    return ''.join(translate_text)

def english_to_braille(english_string: str) -> str:
    translate_text = [] # storage for final result 
    is_number_mode = False # init for digit 

    for char in english_string:
        if char.isalpha(): #check if its a letter 
            if char.isupper(): # checking for uppercase 
                translate_text.append(cap_follow)
                char = char.lower()  # Convert to lowercase for lookup
            # Add Braille representation for the character
            translate_text.append(BRAILLE_MAP_CHAR.get(char, ''))
            is_number_mode = False

        elif char.isdigit(): #check if its a number
            if not is_number_mode:
                translate_text.append(num_follow)
                is_number_mode = True
            translate_text.append(BRAILLE_MAP_NUM.get(char, ''))

        elif char == ' ': # handling empty spaces 
            translate_text.append(BRAILLE_MAP_CHAR.get(' ', ''))

        else:
            translate_text.append('......')  # Default to empty Braille representation

    return ''.join(translate_text)
    


def main():
    parser = argparse.ArgumentParser(description='Translate between English and Braille.')
    parser.add_argument('input_string', type=str, help='The input string to translate.')
    args = parser.parse_args()
    
    result = check_language(args.input_string)
    print(result)

if __name__ == "__main__":
    main()
    





    


