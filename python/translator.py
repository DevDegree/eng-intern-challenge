import sys

english_to_braille_letters = {
    'a': 'O.....',  
    'b': 'O.O...',  
    'c': 'OO....', 
    'd': 'OO.O..',  
    'e': 'O..O..',  
    'f': 'OOO...',  
    'g': 'OOOO..', 
    'h': 'O.OO..',  
    'i': '.OO...', 
    'j': '.OOO..',  
    'k': 'O...O.',  
    'l': 'O.O.O.',  
    'm': 'OO..O.',  
    'n': 'OO.OO.', 
    'o': 'O..OO.',  
    'p': 'OOO.O.',  
    'q': 'OOOOO.',  
    'r': 'O.OOO.',  
    's': '.OO.O.',  
    't': '.OOOO.',  
    'u': 'O...OO',  
    'v': 'O.O.OO',  
    'w': '.OOO.O',  
    'x': 'OO..OO',  
    'y': 'OO.OOO',  
    'z': 'O..OOO'
}

english_to_braille_digits = {
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

# invert the dictionaries
braille_to_english_letters = {v: k for k, v in english_to_braille_letters.items()}
braille_to_english_digits = {v: k for k, v in english_to_braille_digits.items()}


CAPITAL_FLAG_BRAILLE = '.....O'
NUMBER_FLAG_BRAILLE = '.O.OOO'
SPACE_BRAILLE = '......'

def main():

    is_braille = False

    if len(sys.argv) == 2 and braille_check(sys.argv[1]):
        is_braille = True
    else:
        is_braille = False
    

    if is_braille:
        english = braille_to_english(sys.argv[1])
        print(english)

    else: 

        # concatenate arguments into one string
        sentence = ""
        for arg in sys.argv[1:]:
            sentence += arg + " "
        sentence = sentence[:-1] # remove last space
        
        braille = english_to_braille(sentence)
        print(braille)

    
def braille_check(text):
    # braille text must be a multiple of 6 characters long and only contain 0 and .
    return all(char in 'O.' for char in text) and len(text) % 6 == 0
    
def english_to_braille(text):
    braille = ""
    num_flag = False
    for char in text:
        if char.isupper():
            braille += CAPITAL_FLAG_BRAILLE
            char = char.lower()
        if char.isdigit():
            if not num_flag:
                num_flag = True
                braille += NUMBER_FLAG_BRAILLE
            braille += english_to_braille_digits[char]
        elif char.isalpha():
            braille += english_to_braille_letters[char]
        elif char == ' ':
            num_flag = False
            braille += SPACE_BRAILLE
    return braille

def braille_to_english(text):
    english = ""
    num_flag = False
    cap_flag = False
    for i in range(0, len(text), 6):
        char = text[i:i+6]
        if char == CAPITAL_FLAG_BRAILLE:
            cap_flag = True
        elif char == NUMBER_FLAG_BRAILLE:
            num_flag = True
        elif char == SPACE_BRAILLE:
            english += ' '
            num_flag = False
        else:
            if num_flag:
                english += braille_to_english_digits[char]
            elif cap_flag:
                english += braille_to_english_letters[char].upper()
                cap_flag = False
            else:
                english += braille_to_english_letters[char]
    return english

if __name__ == '__main__':
    main()

