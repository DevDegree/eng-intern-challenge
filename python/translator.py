# Braille mappings (O = raised dot, . = no dot)
braille_alphabet = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    
    # Numbers 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 'O': '.OOO..',

    # Special symbols
    'capital': '.....O',    
    'number': '.O.OOO',    
    ' ': '......',        

    # Punctuation
    '.': '.O..OO',         
    ',': '.O....',         
    ';': '.OO...',         
    ':': '.OO.O.',
    '?': '.OO.OO',        
    '!': '.O.OO.', 
    '(': 'OO.OO.', 
    ')': 'OO.OO.',         
    "'": '.....O',          
    '-': '......O',
    '/': 'O..OO.',        
    '@': 'OOO.O.',         
    '#': '.O.OOO',          
}


def translate_to_braille(text):
    # Translate English to Braille
    result = []
    flag_digit = False
    for char in text:
        if char.isupper():
            result.append(braille_alphabet['capital'])  
            char = char.lower()
        if char.isdigit():
            if flag_digit == False:
                result.append(braille_alphabet['number'])  
                flag_digit = True
            result.append(braille_alphabet[char])      
        else:
            flag_digit = False
            result.append(braille_alphabet.get(char, '......'))  
        
    return ''.join(result)

def translate_to_english(braille):
    # Translate Braille to English
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]  # Get the 6-character Braille symbol
        if symbol == braille_alphabet['capital']:
            capitalize_next = True
        elif symbol == braille_alphabet['number']:
            number_mode = True
        else:
            for letter, braille_code in braille_alphabet.items():
                if braille_code == symbol:
                    if number_mode:
                        result.append(letter)  
                    elif capitalize_next:
                        result.append(letter.upper())  
                        capitalize_next = False
                    else:
                        result.append(letter)
                    number_mode = False
                    break
        i += 6
    return ''.join(result)

def main():
    
    import sys
    n = len(sys.argv)
    input_text = []
    
    for i in range(1, n):
        input_text.append(sys.argv[i])  
    
    input_text = ' '.join(input_text)
    
    if all(c in 'O.' for c in input_text):  
        print(translate_to_english(input_text))
    else:  
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()


