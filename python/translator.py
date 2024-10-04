
import sys

CAPITAL = '.....O'
NUMBER = '.O.OOO'
DECIMAL = '.O...O'
CHAR_SIZE_BRAILLE = 6
SPACE= '......'

eng_to_braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
        'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
        'g': 'OOOO..', 'h': 'O.OO..', 'I': '.OO...', 
        'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
        'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
        'y': 'OO.OOO', 'z': 'O..OOO', 
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
        '!': '..OOO.', ':': '..OO..', ';': '..O.O.', 
        '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
        '(': 'O.O..O', ')': '.O.OO.',
}

eng_to_braille_num_dict = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..', 
}

braille_to_eng_dict = {v: k for k,v in eng_to_braille_dict.items()}
braille_to_eng_num_dict = {v: k for k,v in eng_to_braille_num_dict.items()}

def eng_to_braille(text):
    braille = ""
    num_follow_flag = False
    for char in text:
        if char.isalpha():
            if char.isupper():
                braille += CAPITAL
            braille += eng_to_braille_dict[char.lower()]
    
        elif char.isalnum():
            if not num_follow_flag:
                num_follow_flag = True
                braille += NUMBER
            
            braille += eng_to_braille_num_dict[char]
        
        elif char == ".":
            if not num_follow_flag:
                num_follow_flag = True
                braille += NUMBER
            braille += DECIMAL
        
        elif char.isspace():
            braille += SPACE
            num_follow_flag = False
            
        else:
            braille += eng_to_braille_dict[char]
            
  
    return braille
            

def braille_to_eng(text):
    eng = ""
    num_follow_flag = False
    capital_flag = False
    for idx in range(0, len(text), CHAR_SIZE_BRAILLE):
        braille_char = text[idx:idx+CHAR_SIZE_BRAILLE]
        if braille_char == SPACE:
            eng += " "
            num_follow_flag = False
            
        elif braille_char == NUMBER:
            num_follow_flag = True
        
        elif braille_char == DECIMAL:
            eng += "."
            
        elif braille_char == CAPITAL:
            capital_flag = True    
        
        elif num_follow_flag:
            eng += braille_to_eng_num_dict[braille_char]
            
        else:     
            if capital_flag:
                eng += braille_to_eng_dict[braille_char].upper()
                capital_flag = False
            else:
                eng += braille_to_eng_dict[braille_char]

    return eng
            


def main():
    input = ' '.join(sys.argv[1:])
    if set(input) <= {'.', 'O'}:
        print(braille_to_eng(input))
    else:
        print(eng_to_braille(input))
    
if __name__ == "__main__":
    main()

