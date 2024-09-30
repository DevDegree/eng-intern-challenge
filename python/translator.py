# Braille mappings (0 = raised dot, . = no dot)
braille_alphabet = {
    # Letters
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..', 
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000',
    'z': '0..000',
    
    # Numbers 
    '1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', '5': '0..0..',
    '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', '0': '.000..',

    # Special symbols
    'capital': '.....0',    
    'number': '.0.000',    
    ' ': '......',        

    # Punctuation
    '.': '.0..00',         
    ',': '.0....',         
    ';': '.00...',         
    ':': '.00.0.',
    '?': '.00.00',        
    '!': '.0.00.', 
    '(': '00.00.', 
    ')': '00.00.',         
    "'": '.....0',          
    '-': '......0',
    '/': '0..00.',        
    '@': '000.0.',         
    '#': '.0.000',          
}


def translate_to_braille(text):
    # Translate English to Braille
    result = []
    for char in text:
        if char.isupper():
            result.append(braille_alphabet['capital'])  
            char = char.lower()
        if char.isdigit():
            result.append(braille_alphabet['number'])  
            result.append(braille_alphabet[char])      
        else:
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
    input_text = sys.argv[1]
   
    if all(c in '0.' for c in input_text):  
        print(translate_to_english(input_text))
    else:  
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()


