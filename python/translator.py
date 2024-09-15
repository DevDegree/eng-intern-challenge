

import sys


BRAILLE_DICT = {
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
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    'CAPITAL': '.....O',
    'DECIMAL': '.O...O',
    'NUMBER': '.O.OOO',
    '.': '..OO.O',
    ' ': '......'
}

ALPHA_DICT = dict((v, k) for k, v in BRAILLE_DICT.items())

def is_brail (msg):
    return msg in BRAILLE_DICT.values()

def translate_num(num) :
    translation = BRAILLE_DICT["NUMBER"]
    for digit in num:
        translation += BRAILLE_DICT[digit]
    return translation        

def translate_word(word) :
    translation = ""
    for char in word:
        if char.isupper():
            translation += BRAILLE_DICT["CAPITAL"]
        translation += BRAILLE_DICT[char.upper()]
    
    return translation        

if __name__ == '__main__':
    arg = sys.argv[1:]

    if (len (arg) < 1) :
        exit

    #If there are more than one arguments
    #or the first token has less than 6 characters
    #or the first 6 letters contain chars other than O and .
    # then it is english
    if (len(arg) > 1 or len(arg[0]) < 6 or not is_brail(arg[0][:6])):
        #ENGLISH
        translation = ""
        for token in arg: 
            if (token[0].isdigit()):
                translation += translate_num(token)
            else: 
                translation += translate_word(token)
        
            translation += BRAILLE_DICT[" "]
        print(translation[:-6])
    else:
        #BRAILLE
        braille = arg[0]
        isUpper = False
        isNum = False
        translation = ""
        for i in range (0, len(arg[0]), 6): 
            token = braille[i:i+6]
            if (ALPHA_DICT[token] == 'CAPITAL'):     
                isUpper = True;
            elif (ALPHA_DICT[token] == 'NUMBER'):    
                isNum = True;
            elif (isNum): 
                if (ALPHA_DICT[token] == 'DECIMAL'):
                    translation += '.'
                
                elif (ALPHA_DICT[token].isalpha()) :
                    translation += chr((ord(ALPHA_DICT[token]) - ord('@')) % 10 + 48)

                else: 
                    translation += ALPHA_DICT[token]
            
            elif (isUpper):
                translation += ALPHA_DICT[token]
                isUpper = False
            else :
                translation += ALPHA_DICT[token].lower()
            if (isNum and ALPHA_DICT[token] == ' '):
                isNum = False
        print(translation)




# .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
# .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..