#All alphabets mapped to Braille
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

NUM_PREFIX = '..OOOO'

#Prefix for capital letters
CAP_PREFIX = '.....O'

#Mapping for digits 
DIGIT_TO_BRAILLE = {
    '1': ENGLISH_TO_BRAILLE['a'],
    '2': ENGLISH_TO_BRAILLE['b'],
    '3': ENGLISH_TO_BRAILLE['c'],
    '4': ENGLISH_TO_BRAILLE['d'],
    '5': ENGLISH_TO_BRAILLE['e'],
    '6': ENGLISH_TO_BRAILLE['f'],
    '7': ENGLISH_TO_BRAILLE['g'],
    '8': ENGLISH_TO_BRAILLE['h'],
    '9': ENGLISH_TO_BRAILLE['i'],
    '0': ENGLISH_TO_BRAILLE['j'],
}

#Mappings for letters and digits
BRAILLE_TO_ENGLISH_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_ENGLISH_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}

#Prefixes added to mapping
PREFIXES = { 
    CAP_PREFIX: 'CAPITAL',  
    NUM_PREFIX: 'NUMBER',    
}

def is_braille(input_str):   
  
    return all(c in {'O', '.'} for c in input_str)           

def english_to_braille(text):
 
    braille = []
    is_number = False
    for char in text:

        if char.isupper():
            if is_number:
                
                braille.append(ENGLISH_TO_BRAILLE[' ']) 
                is_number = False
            braille.append(CAP_PREFIX)
            braille.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))

        elif char.isdigit():

            if not is_number:   
                braille.append(NUM_PREFIX) 
                is_number = True
            braille.append(DIGIT_TO_BRAILLE.get(char, '......'))  

        else:  


            if is_number:
                
                braille.append(ENGLISH_TO_BRAILLE[' '])  
                is_number = False
            braille.append(ENGLISH_TO_BRAILLE.get(char, '......'))


    return ''.join(braille)



def braille_to_english(braille_str):
   
    result = []
    i = 0
    is_number = False
    capitalize_next = False

    while i < len(braille_str):
        
        #Braille character is 6 characters long
        braille_char = braille_str[i:i+6]
        if len(braille_char) < 6:
           
            break

        if braille_char in PREFIXES:
            if PREFIXES[braille_char] == 'CAPITAL':
                capitalize_next = True
            elif PREFIXES[braille_char] == 'NUMBER':
                is_number = True
            i += 6
            continue

        if braille_char == ENGLISH_TO_BRAILLE[' ']:  
            if is_number:
                is_number = False
              
            else:
                result.append(' ')
            i += 6
            continue

        if is_number:
            if braille_char in BRAILLE_TO_ENGLISH_DIGIT:
                result.append(BRAILLE_TO_ENGLISH_DIGIT[braille_char])
            else:
                
                is_number = False
                char = BRAILLE_TO_ENGLISH_LETTER.get(braille_char, '?')  

                if capitalize_next and char.isalpha():
                    char = char.upper()
                    capitalize_next= False

                result.append(char)
                
        else:

            char = BRAILLE_TO_ENGLISH_LETTER.get(braille_char, '?') 
            if char:

                if capitalize_next and char.isalpha():
                    char = char.upper()
                    capitalize_next = False
                result.append(char)

            else:
                result.append('?')
        i += 6

    return ''.join(result)




def main():

    input_str = input("Enter the string to translate: ").strip()

    if is_braille(input_str):
        translated = braille_to_english(input_str)

    else:
        translated = english_to_braille(input_str)
    print(translated)

if __name__ == "__main__":
    main()
