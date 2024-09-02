
import sys
#LETS CREATE A DICTIONARY FOR BRAILE TO ENGLISH

braille_dict = {
    '0.....': 'a',
    '0.0...': 'b',
    '00....': 'c',
    '00.0..': 'd',
    '0..0..': 'e',
    '000...': 'f',
    '0000..': 'g',
    '0.00..': 'h',
    '.00...': 'i',
    '.000..': 'j',
    '0...0.': 'k',
    '0.0.0.': 'l',
    '00..0.': 'm',
    '00.00.': 'n',
    '0..00.': 'o',
    '000.0.': 'p',
    '00000.': 'q',
    '0.000.': 'r',
    '.00.0.': 's',
    '.0000.': 't',
    '0...00': 'u',
    '0.0.00': 'v',
    '.000.0': 'w',
    '00..00': 'x',
    '00.000': 'y',
    '0..000': 'z',
    '......': ' ',
    '.....0_act': 'capital',
    '.0...0_act': 'decimal',
    '.0.000_act': 'number',
    '..0..._punct': ',',
    '..00.0_punct': '.',
    '..0.00_punct': '?',
    '..00.._punct': ':',
    '..0.0._punct': ';',
    '....00_punct': '-',
    '.0..0._punct': '/',
    '.00..0_punct': '<',
    '0..00._punct': '>',
    '0.0..0_punct': '(',
    '.0.00._punct': ')',

}

#act = action

braille_dict_num = {
    '0.....': '1',
    '0.0...': '2',
    '00....': '3',
    '00.0..': '4',
    '0..0..': '5',
    '000...': '6',
    '0000..': '7',
    '0.00..': '8',
    '.00...': '9',
    '.000..': '0'
}


eng_to_braille = {}
for braille, char in braille_dict.items():
    eng_to_braille[char] = braille

eng_to_braille_num = {}
for braille, char in braille_dict_num.items():
    eng_to_braille_num[char] = braille

pun = ['.', ',', '?', ':', ';', '-', '/', '<', '>', '(', ')']
action=[]


def trans_eng_to_braille(text):
    braille = ""
    boolean_num = False
    for char in text:
        if char.isupper():
            braille += eng_to_braille['capital'].split('_')[0]
            char = char.lower()
            braille += eng_to_braille[char]
            boolean_num = False
        elif char.isdigit():
            if not boolean_num:
                braille += eng_to_braille['number'].split('_')[0]
                boolean_num = True
            braille += eng_to_braille_num[char]
        elif char in pun:
            braille += eng_to_braille[char + '_punct']
            boolean_num = False
        elif char == ".":
            braille += eng_to_braille['decimal'].split('_')[0]
        else:
            braille += eng_to_braille[char]
            boolean_num = False  

    return braille

def trans_brail_to_eng(text):
    eng = ""
    boolean_num = False
    boolean_cap = False

    for i in range(0, len(text), 6):
        word = text[i:i+6]
        
        if word == ".....0":  # Capital
            boolean_cap = True
            continue
        elif word == '......':  # Space
            eng += ' '
            boolean_cap = False
            boolean_num = False
            continue
        elif word == '.0...O':  # Decimal indicator
            eng += '.'
            boolean_cap = False
            continue
        elif word == '.0.000':  # Number indicator
            boolean_num = True
            continue

        if boolean_num:
            eng += braille_dict_num[word] 
        else:
            if boolean_cap:
                eng += braille_dict[word].upper() 
                boolean_cap = False 
            else:
                eng += braille_dict[word]

    return eng


    

