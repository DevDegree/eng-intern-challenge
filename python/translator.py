import sys
braille_alphabets = {
    'A': 'O.....',  
    'B': 'O.O...',  
    'C': 'OO....',  
    'D': 'OO.O..',  
    'E': 'O..O..',  
    'F': 'OOO...',  
    'G': 'OOOO..',  
    'H': 'O.OO..',  
    'I': '.OO...',  
    'J': '.OOO..',  
    'K': 'O...O.',  
    'L': 'O.O.O.',  
    'M': 'OO..O.',  
    'N': 'OO.OO.', 
    'O': 'O..OO.',  
    'P': 'OOO.O.',  
    'Q': 'OOOOO.',  
    'R': 'O.OOO.',  
    'S': '.OO.O.', 
    'T': '.OOOO.',  
    'U': 'O...OO',  
    'V': 'O.O.OO',  
    'W': '.OOO.O', 
    'X': 'OO..OO',  
    'Y': 'OO.OOO',  
    'Z': 'O..OOO',  
}

braille_digits = {
    '1': 'O.....',  
    '2': 'O.O...',  
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..', 
}

capital_follows = '.....O'

decimal_follows = '.O...O'

number_follows = '.O.OOO'

braille_special_characters = {
    '.': '..OO.O',     
    ',': '..O...',        
    '?': '..O.OO', 
    '!': '..OOO.',
    ':': '..OO..',        
    ';': '..O.O.',   
    '-': '....OO',       
    '/': '.O..O.', 
    '<': '.OO..O',    
    '>': 'O..OO.', 
    '(': 'O.O..O', 
    ')': '.O.OO.',
    ' ': '......',  
}

def identify_braille(input):
    if (len(input) % 6 != 0):
        return False
    else:
        for i in input:
            if i != 'O' and i != '.':
                return False
    return True

def english_to_braille(input):
    braille_string = ''
    length = len(input)
    cnt = 0
    num_cnt = 0  
    
    for i in input:
        if i.isupper():
            braille_string += capital_follows
            braille_string += braille_alphabets[i]
        elif i.islower():
            i = i.upper()
            braille_string += braille_alphabets[i]
        elif i.isdigit():
            if num_cnt == 0:
                braille_string += number_follows
            num_cnt += 1  
            braille_string += braille_digits[i]
            
            if cnt != length - 1 and not input[cnt + 1].isdigit() and input[cnt + 1] != ' ':
                braille_string += '......' 
                num_cnt = 0  
        elif i == '.' and cnt != length - 1 and input[cnt + 1].isdigit():
            braille_string += decimal_follows
        elif i in braille_special_characters:
            if i == ' ':
                num_cnt = 0  
            braille_string += braille_special_characters[i]
        else:
            braille_string += '......'
        
        cnt += 1  
    
    return braille_string


def braille_to_english(input):
    braille = ''
    eng = ''
    i = 0
    while i < len(input):
        braille = input[i: i+6]
        
        if (braille == '.....O'):
            i = i + 6
            braille = input[i: i+6]
            char = convert_other_braille(braille)
            eng += char
        elif (braille == number_follows):
            i = i + 6
            while i < len(input) and input[i: i + 6] != '......':
                braille = input[i: i+6]
                char = convert_num_braille(braille)
                eng += char
                i = i + 6
            continue
        else:
            char = convert_other_braille(braille)
            if (char.isalpha()):
                char = char.lower()
            eng += char
        i = i + 6

    return eng

def convert_num_braille(braille_value):
    for key, value in braille_digits.items():
            if value == braille_value:
                return key

def convert_other_braille(braille_value):
    for key, value in braille_alphabets.items():
            if value == braille_value:
                return key
    for key, value in braille_special_characters.items():
            if value == braille_value:
                return key

def main():
    input_text = ' '.join(sys.argv[1:])
    flag = identify_braille(input_text)
    if (flag):
      print(braille_to_english(input_text))
    else:
      print(english_to_braille(input_text))

if __name__ == "__main__":
    main() 
