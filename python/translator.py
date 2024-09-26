import sys

#Mapping from English letters to Braille
ENGLISH_TO_BRAILLE = {
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
    'z': 'O..OOO',
    ' ': '......',
}

# Braille prefixes
CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'  #Corrected Numb Prefix

# Mapping digits to Braille 
DIGIT_TO_BRAILLE = {
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

# Reverse mapping for letters
BRAILLE_TO_ENGLISH_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Reverse mapping for digits
BRAILLE_TO_ENGLISH_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()} 

def is_braille(input_str):
  
    return all(c in {'O', '.'} for c in input_str)

def english_to_braille(text):
    
    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit():

            if not number_mode:
                braille_output.append(NUMBER_PREFIX)
                number_mode = True
            braille_output.append(DIGIT_TO_BRAILLE.get(char, '......'))

        else:
            if number_mode:
              
                number_mode = False
            if char.isupper():
                braille_output.append(CAPITAL_PREFIX)
                braille_output.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......')) 
            else:
                braille_output.append(ENGLISH_TO_BRAILLE.get(char, '......')) 

  
    if number_mode:
        number_mode = False 

    return ''.join(braille_output)


def braille_to_english(braille_text):
  
    english_output = []
    i = 0
    number_mode = False
    capitalize_next = False 

    while i < len(braille_text):
        #Each Braille character is 6 characters 
        chunk = braille_text[i:i+6]
        if len(chunk) < 6:
            
            break

        if chunk == CAPITAL_PREFIX:
            capitalize_next = True
            i += 6
            continue

        elif chunk == NUMBER_PREFIX:
            number_mode = True
            i += 6
            continue

        elif chunk == ENGLISH_TO_BRAILLE[' ']: 
            if number_mode:
               
                number_mode = False
            else:
                # Actual space in input
                english_output.append(' ')
            i += 6
            continue
        else:
            if number_mode:
             
                char = BRAILLE_TO_ENGLISH_DIGIT.get(chunk, '?')
                if char != '?':
                    english_output.append(char) 
                else:
                 
                    number_mode = False
                 
                    char = BRAILLE_TO_ENGLISH_LETTER.get(chunk, '?')

                    if capitalize_next and char.isalpha():
                        char = char.upper()
                        capitalize_next = False
                    english_output.append(char) 

            else:
               
                char = BRAILLE_TO_ENGLISH_LETTER.get(chunk, '?')

                if char != '?':

                    if capitalize_next and char.isalpha(): 

                        char = char.upper()
                        capitalize_next = False
                    english_output.append(char) 

                else:
                  
                    english_output.append('?') 
        i += 6

    return ''.join(english_output) 

def main():

    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
    else:
      
        input_str = input("Enter the string to translate: ").strip()        
        
    if is_braille(input_str):
        translated = braille_to_english(input_str) 

    else:
        translated = english_to_braille(input_str)  
    print(translated)

if __name__ == "__main__":
    main()
