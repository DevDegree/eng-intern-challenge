from textwrap import wrap

#make alphabet dictionary
alphabet_to_braille = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..',
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000',
    'z': '0..000', 
    'capital_follows': '.....0', 
    'decimal_follows': '.0...0', 
    'number_follows': '.0.000',
    '.': '..00.0',
    ',': '..0...',
    '?': '..0.00',
    '!': '..000.',
    ':': '..00..',
    ';': '..0.0.',
    '-': '....00',
    '/': '.0..0.',
    '<': '.00..0',
    '>': '0..00.',
    '(': '0.0..0',
    ')': '.0.00.',
    ' ': '......', 
}

#make braille dictionary
braille_to_alphabet={
    '0.....': 'a', '0.0...': 'b', '00....': 'c', '00.0..': 'd', '0..0..': 'e',
    '000...': 'f', '0000..': 'g', '0.00..': 'h', '.00...': 'i', '.000..': 'j',
    '0...0.': 'k', '0.0.0.': 'l', '00..0.': 'm', '00.00.': 'n', '0..00.': 'o',
    '000.0.': 'p', '00000.': 'q', '0.000.': 'r', '.00.0.': 's', '.0000.': 't',
    '0...00': 'u', '0.0.00': 'v', '.000.0': 'w', '00..00': 'x', '00.000': 'y',
    '0..000': 'z',  
    #'0.....': '1', '0.0...': '2', '00....': '3', '00.0..': '4', '0..0..': '5',
    #'000...': '6', '0000..': '7', '0.00..': '8', '.00...': '9', '.000..': '0',
    '.....0': 'capital_follows', 
    '.0...0': 'decimal_follows', 
    '.0.000': 'number_follows',
    '..00.0': '.', 
    '..0...': ',', 
    '..0.00': '?', 
    '..000.': '!', 
    '..00..': ':',
    '..0.0.': ';', 
    '....00': '-', 
    '.0..0.': '/', 
    '.00..0': '<', 
    '0..00.': '>',
    '0.0..0': '(', 
    '.0.00.': ')', 
    '......': ' ',
}

braille_to_numbers = {
    '0.....': '1',
    '0.0...': '2',
    '00....': '3',
    '00.0..': '4',
    '0..0..': '5',
    '000...': '6',
    '0000..': '7',
    '0.00..': '8',
    '.00...': '9',
    '.000..': '0',
}

#make function to translate english to braille
def english_to_braille(text):
    #need to add capital,decimal and numbers
    braille = ''
    for letter in text.lower(): 
        braille += alphabet_to_braille[letter]
    return braille

#make function to translate braille to english
def braille_to_english(input):
    #need to add decimal
    text = ''
    character = wrap(input, 6) #separate input into sections of 6
    capitalize_next = False
    is_number = False

    #build translation text
    for i in character:
        if is_number:
            if i in braille_to_numbers: #if i is in braille_to_numbers add number
                text += braille_to_numbers[i]
            is_number = False  # reset is_number too False            
        elif i == '.0.000':  
            is_number = True
        elif capitalize_next:
            text += braille_to_alphabet[i].upper()  # capitalize letter and add to text
            capitalize_next = False  # reset capitalize_next to false
        elif i == '.....0':  
            capitalize_next = True
        else:
            text += braille_to_alphabet[i]
    
    return text

#make function to choose how to translate
def translate(input):
    if all(char in '0.' for char in input):
        return braille_to_english(input)
    else:
        return english_to_braille(input)



#test code
print(translate('00..0.00.000......00....0.....0.000.'))
