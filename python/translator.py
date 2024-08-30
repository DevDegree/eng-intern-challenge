import sys

braille_dict = {
  
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',

    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',

    ',': '..O...',
    ';': '..O.O.',  
    ':': '..OO..',  
    '.': '..OO.O',  
    '!': '..OOO.',
    '(': 'O..OO.',
    ')': 'O..OO.',
    '?': '..O.OO',  
    '-': '....OO',
    '/': '.O..O.',  
    '<': '.OO..O',
    '>': 'O..OO.',
    ' ': '......',      
    'capital': '.....O',  
    'number': '.O.OOO',   
    'decimal': '.O...O'  
}





def english_to_braille(text):
    braille_text = ''
    number_mode = False
    
    for char in text:
        if char.isupper():
            braille_text += braille_dict['capital'] + braille_dict[char.lower()]
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                braille_text += braille_dict['number'] + braille_dict[char]
                number_mode = True 
            else:
                braille_text += braille_dict[char]
        elif char == '.':
            if number_mode:
                braille_text += braille_dict['decimal']  
            else:
                braille_text += braille_dict[char]
            number_mode = False  
        else:
            braille_text += braille_dict[char]
            number_mode = False  
    
    return braille_text



def braille_to_english(braille_string):
    english_text = ''
    capitalize = False
    number_mode = False
    decimal_mode = False

    inverted_dict = {}
    for key, value in braille_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]  
        else:
            inverted_dict[value].append(key)

    for i in range(0, len(braille_string), 6):
        symbol = braille_string[i:i + 6]   
        if symbol in inverted_dict and inverted_dict[symbol] == ['capital']:
            capitalize = True
            continue  
        elif symbol in inverted_dict and inverted_dict[symbol] == ['number']:
            number_mode = True
            continue 
        elif symbol in inverted_dict and inverted_dict[symbol] == ['decimal']:
            decimal_mode = True
            continue  
        char_list = inverted_dict.get(symbol)
        if not char_list:
            continue  
        char = char_list[0]  
        if number_mode and len(char_list) > 1:
            char = char_list[1]         
        if char:
            if capitalize:
                char = char.upper()  
                capitalize = False
            if number_mode:
                if char.isdigit():
                    english_text += char
                else:                  
                    number_mode = False
                    english_text += char
            elif decimal_mode:
                if char.isdigit() or char == '.':
                    english_text += char
                else:
                    decimal_mode = False
                    english_text += char  
            else:
                english_text += char  

    return english_text




def is_braille(text):
    braille_patterns = ['O.', '.O', 'OO', 'O..', '..O', '.OO', 'O.O', 'O..O', 'OO..', 'OOO', 'O.OO', '......']
 
    return any(pattern in text for pattern in braille_patterns)


if __name__ == "__main__":
    inputs = sys.argv[1:]  # Get input arguments
    combined_inputs = ' '.join(inputs)  
    if(is_braille(str(combined_inputs))):
        print(braille_to_english(combined_inputs))
    else:
        print(english_to_braille(combined_inputs))




