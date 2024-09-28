import sys

# English : Braille dictionary mapping
braille_dict = {
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
    'capital': '.....O',
    'number': '.O.OOO'
}

# Braille : English Dictionary Mapping
reverse_braille_sym_dict = {v: k for k, v in braille_dict.items()}

# Number : Braille Dictionary Mapping
braille_numbers = {
    '1': braille_dict['a'],
    '2': braille_dict['b'],
    '3': braille_dict['c'],
    '4': braille_dict['d'],
    '5': braille_dict['e'],
    '6': braille_dict['f'],
    '7': braille_dict['g'],
    '8': braille_dict['h'],
    '9': braille_dict['i'],
    '0': braille_dict['j']
}

# Braille : Number Dictionary Mapping
reverse_braille_num_dict = {v: k for k, v in braille_numbers.items()}

# To check if the text is Braille or English
def checkbraille(text):
    if len(text) % 6 != 0:
        return False
    return all(c in "O." for c in text)

# Converting English to Braille
def english_to_braille(text):
    output_text = []
    is_number = False # Flag for checking number till space is encountered

    for char in text:

        # Checking if character is upper      
        if char.isupper():
            output_text.append(braille_dict['capital'])  
            char = char.lower()  
            
        # Checking if character is number
        if char.isdigit():
            if not is_number:
                output_text.append(braille_dict['number'])  
                is_number = True  
            output_text.append(braille_numbers[char])  
            

        # Space and Alphabets
        else:
            is_number = False  
            output_text.append(braille_dict.get(char, '......'))  # Converting letter or space to Braille
        


    return ''.join(output_text)

# Converting Braille to English
def braille_to_english(text):
    output_text = []
    is_capital = False # Flag for only capitalizing the next character
    is_number = False # Flag for checking number till space is encountered
    
    
    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]
       
        if braille_char == braille_dict['capital']:
            is_capital = True
            continue
        if braille_char == braille_dict['number']:
            is_number = True
            continue
        
        
        if braille_char == '......':  
            output_text.append(' ')
            is_number = False  
        
        else:
            if is_number:
                # Convert to a number if it is number
                char = reverse_braille_num_dict.get(braille_char, '')
                output_text.append(char)
                continue
            else:
                # Convert Braille to English using Braille : Number Dictionary
                char = reverse_braille_sym_dict.get(braille_char, '')
                if is_capital:
                    output_text.append(char.upper())
                    is_capital = False  
                else:
                    output_text.append(char)
            is_number = False  
    
    return ''.join(output_text)

#Main
if __name__ == "__main__":

    input_text = ' '.join(sys.argv[1:])
    
    if checkbraille(input_text):
        
        print(braille_to_english(input_text))
    else:
        
        print(english_to_braille(input_text))

