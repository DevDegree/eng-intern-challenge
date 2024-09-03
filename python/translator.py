import sys

dict = {
    32: '......', #space
    33: '..OOO.', #!
    40: 'O.O..O', #(
    41: '.O.OO.', #)
    44: '..O...', #,
    45: '....OO', #-
    46: '..OO.O', #.
    47: '.O..O.', #/
    48: '.OOO..', #0
    49: 'O.....', #1
    50: 'O.O...', #2
    51: 'OO....', #3
    52: 'OO.O..', #4
    53: 'O..O..', #5
    54: 'OOO...', #6
    55: 'OOOO..', #7
    56: 'O.OO..', #8
    57: '.OO...', #9
    58: '..OO..', #:
    59: '..O.O.', #;
    60: '.OO..O', #<
    62: 'O..OO.', #>
    63: '..O.OO', #?
    97: 'O.....', #A
    98: 'O.O...', #B
    99: 'OO....', #C
    100: 'OO.O..', #D
    101: 'O..O..', #E
    102: 'OOO...', #F
    103: 'OOOO..', #G
    104: 'O.OO..', #H
    105: '.OO...', #I
    106: '.OOO..', #J
    107: 'O...O.', #K
    108: 'O.O.O.', #L
    109: 'OO..O.', #M
    110: 'OO.OO.', #N
    111: 'O..OO.', #O
    112: 'OOO.O.', #P
    113: 'OOOOO.', #Q
    114: 'O.OOO.', #R
    115: '.OO.O.', #S
    116: '.OOOO.', #T
    117: 'O...OO', #U
    118: 'O.O.OO', #V
    119: '.OOO.O', #W
    120: 'OO..OO', #X
    121: 'OO.OOO', #Y 
    122: 'O..OOO', #Z
}

def translate_string(inp):
    cap = False
    num = False
    dec = False
    for char in inp:
        #check if capital follows
        if char.isupper() and cap == False:
            print('.....O'+dict[ord(char)+32], end='')
            cap = True
        elif char.isupper() and cap == True:
            print(dict[ord(char)+32], end='')
        #find if next char after decimal is a number
        elif char == '.' and inp[inp.index(char)+1].isdigit() and dec == False:
            print('.O...O'+dict[ord(char)], end='')
            dec = True
        #check if number follows
        elif char.isdigit() and num == False:
            print('.O.OOO'+dict[ord(char)], end='')
            num = True
        elif char == ' ':
            print(dict[ord(char)], end='')
            cap = False
            num = False
            dec = False
        #generic case if char exists in dict
        elif ord(char) in dict:
            print(dict[ord(char)], end='')
        #throw error if char not in dict
        else:
            print('Character not found in dictionary')
            break
    

def translate_braille(inp):
    num = False
    cap = False
    for i in range(0, len(inp), 6):
        braille = inp[i:i+6]
        
        #first, check if number or digit
        if braille == '......':
            print(' ', end='')
            num = False
            cap = False
        elif braille == '.O.OOO' or braille == '.O...O':
            num = True
        elif num == True:
            print(chr(list(dict.keys())[list(dict.values()).index(braille)]), end='')
        #Now check if Capital follows
        elif braille == '.....O':
            cap = True
        #a-j only, check ascii value of braille
        elif num == False and list(dict.keys())[list(dict.values()).index(braille)] == 48:
            if cap == True:
                print('J', end='')
            else:
                print('j', end='')
        elif num == False and list(dict.keys())[list(dict.values()).index(braille)] < 58 and list(dict.keys())[list(dict.values()).index(braille)] > 48:
            if cap == True:
                print(chr(list(dict.keys())[list(dict.values()).index(braille)]+16), end='')
                cap = False
            else:
                print(chr(list(dict.keys())[list(dict.values()).index(braille)]+48), end='')
        #o
        elif list(dict.keys())[list(dict.values()).index(braille)] == 62:
            if num == True:
                print('>', end='')
            else:
                if cap == True:
                    print('O', end='')
                else:
                    print('o', end='')
        #any other letter
        elif list(dict.keys())[list(dict.values()).index(braille)] < 123 and list(dict.keys())[list(dict.values()).index(braille)] > 106:
            if cap == True:
                print(chr(list(dict.keys())[list(dict.values()).index(braille)]-32), end='')
                cap = False
            else:
                print(chr(list(dict.keys())[list(dict.values()).index(braille)]), end='')
        elif braille in dict.values():
            print(chr(list(dict.keys())[list(dict.values()).index(braille)]), end='')
        else:
            print('Character not found in dictionary')
            break

def main():
    # check if input is braille vs regular string, use approp. func.
    inp = ' '.join(sys.argv[1:])
    
    #check if '.' and 'O' are the only characters in the input
    if all(c in ['.', 'O', ' '] for c in inp):
        translate_braille(inp)
    else:
        translate_string(inp)

if __name__ == '__main__':
    main()