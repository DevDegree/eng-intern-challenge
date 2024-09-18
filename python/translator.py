import sys

#Mappings
CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'

BRAILLE_TO_ENG = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

# Braille uses a-j to map numbers 1-0
NUMBER_TO_BRAILLE = {
    '1': 'O.....',  
    '2': 'O.O...', 
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..'   
}

ENG_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ENG.items()}
BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}



# Functions
def is_braille(string: str) -> bool:
    valid_chars = {'O', '.', ' '}
    return all(letter in valid_chars for letter in string)

def english_to_braille(english_text: str)->str :
    braille_output =''
    is_number_mode = False

    for char in english_text:
        if char.isupper():
            braille_output += CAPITAL_PREFIX
            char = char.lower()
        
        if char.isdigit():
            if not is_number_mode:
                braille_output += NUMBER_PREFIX
                is_number_mode = True

            braille_output += NUMBER_TO_BRAILLE[char]
        else:
            if is_number_mode:
                is_number_mode = False
            braille_output  += ENG_TO_BRAILLE.get(char, '')
        
    return braille_output 


def braille_to_english(braille_text: str) -> str:
    english_output = ''
    i = 0
    length = len(braille_text)
    is_number_mode = False
    is_capital = False

    
    while i < length:
        braille_char = braille_text[i:i+6]

        if braille_char == CAPITAL_PREFIX:
            is_capital = True 
            i += 6
            continue
        elif braille_char == NUMBER_PREFIX:
            is_number_mode = True
            i += 6
            continue
        elif braille_char == '......':
            english_output += ' '
            is_number_mode = False
            is_capital = False
        else:
            if is_number_mode:
                char = BRAILLE_TO_NUMBER.get(braille_char,'')
            else:
                char = BRAILLE_TO_ENG.get(braille_char,'')
            
            if is_capital:
                char = char.upper()
                is_capital = False
            english_output += char

        i += 6
    
    return english_output
    
            
            


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python translator.py <input-string>")
        sys.exit(1)

    input_string = sys.argv[1]

    if is_braille(input_string):
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)


    
        





        






    







