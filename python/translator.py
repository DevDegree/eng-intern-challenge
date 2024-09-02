import sys
#LETS CREATE A DICTIONARY FOR BRAILE TO ENGLISH

braille_dict = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
    '.....O_act': 'capital',
    '.O...O_act': 'decimal',
    '.O.OOO_act': 'number',
    '..O..._punct': ',',
    '..OO.O_punct': '.',
    '..O.OO_punct': '?',
    '..OO.._punct': ':',
    '..O.O._punct': ';',
    '....OO_punct': '-',
    '.O..O._punct': '/',
    '.OO..O_punct': '<',
    'O..OO._punct': '>',
    'O.O..O_punct': '(',
    '.O.OO._punct': ')',
}

#act = action

braille_dict_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
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
            braille += eng_to_braille[char].split('_')[0]
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
        
        if word == ".....O":  # Capital
            boolean_cap = True
            continue
        elif word == '......':  # Space
            eng += ' '
            boolean_cap = False
            boolean_num = False
            continue
        elif word == '.O...O':  # Decimal indicator
            eng += '.'
            boolean_cap = False
            continue
        elif word == '.O.OOO':  # Number indicator
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


def main():
    input_str = " ".join(sys.argv[1:])
    if all(c in '.O' for c in input_str):
        output = trans_brail_to_eng(input_str)
    else:
        output = trans_eng_to_braille(input_str)
    print(output)
    return output

if __name__ == "__main__":
    main()