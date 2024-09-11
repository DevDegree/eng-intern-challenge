import sys

# Braille encoding for English Characters
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Braille encoding for numeric characters.
NUMS_TO_BRAILLE = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Symbols in Braille, such as space, capitalization, and numbers.
SYMBOLS_BRAILLE = {
    'CAPITAL_FOLLOW': '.....O', 
    'SPACE': '......',        
    'NUMBER_FOLLOW': '.O.OOO'    
}

# Reverse mapping 
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()} 
BRAILLE_TO_NUMS = {v: k for k, v in NUMS_TO_BRAILLE.items()}        


# To determine whether the input is Braille or not
def is_braille(i):
    return all(char in "O." for char in i)

def translate_to_braille(text):
    output = ""
    is_number = False
    for char in text:
        if char == " ":
            output += SYMBOLS_BRAILLE['SPACE'] 
            is_number = False  
        elif char.isdigit():
            if not is_number:
                output += SYMBOLS_BRAILLE['NUMBER_FOLLOW'] 
                is_number = True 
            output += NUMS_TO_BRAILLE[char]
        elif char.isupper():
            output += SYMBOLS_BRAILLE['CAPITAL_FOLLOW'] + ENGLISH_TO_BRAILLE[char.lower()]
            is_number = False 
        else:
            output += ENGLISH_TO_BRAILLE.get(char, "")  
            is_number = False 
    return output

# Translate to Braille from English
def translate_to_english(text):
    output = ""
    i = 0
    is_number = False  
    is_cap = False    
    
    while i < len(text):
        braille_char = text[i:i+6] 
        
        if braille_char == SYMBOLS_BRAILLE['SPACE']:
            output += " " 
            i += 6
        elif braille_char == SYMBOLS_BRAILLE['CAPITAL_FOLLOW']:
            is_cap = True 
            i += 6
        elif braille_char == SYMBOLS_BRAILLE['NUMBER_FOLLOW']:
            is_number = True 
            i += 6
        elif is_number:
            output += BRAILLE_TO_NUMS.get(braille_char, "")
            i += 6
            is_number = False 
        else:
        
            letter = BRAILLE_TO_ENGLISH.get(braille_char, "")
            if is_cap:
                output += letter.upper()
                is_cap = False
            else:
                output += letter
            i += 6
            
    return output


if __name__ == "__main__":

    input = " ".join(sys.argv[1:])
    
    if is_braille(input):
        print(translate_to_english(input))
    else:
        print(translate_to_braille(input))

