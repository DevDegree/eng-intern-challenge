from textwrap import wrap

#make alphabet dictionary
alphabet_to_brail = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..',
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000',
    'z': '0..000', 
    #'1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', '5': '0..0..',
    #'6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', '0': '.000..', 
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

#make brail dictionary
brail_to_alphabet={
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

#make function to translate english to brail
def english_to_brail(text):
    #need to add capital,decimal and numbers
    brail = ''
    for letter in text.lower(): 
        brail += alphabet_to_brail[letter]
    return brail


#make function to translate brail to english
def brail_to_english(input):
    #need to add capital,decimal and numbers
    text = ''
    character = wrap(input, 6) #separate input into sections of 6
    capitalize_next = False


    for i in character:
        if capitalize_next:
            text += brail_to_alphabet[i].upper()  # Capitalize next character
            capitalize_next = False
        elif i == '.....0':  # Assuming this is your capitalization marker
            capitalize_next = True
        else:
            text += brail_to_alphabet[i]
    return text

#make function to choose how to translate
def translate(input):
    if all(char in '0.' for char in input):
        return brail_to_english(input)
    else:
        return english_to_brail(input)


print(translate('.....000....0......0000.'))
