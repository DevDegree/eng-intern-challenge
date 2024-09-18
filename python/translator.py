import sys #to read cmd arguments

#filling out this dict was the hardest part T-T
en_to_br = {
    ' ': '......',
    'capital': '.....O',
    'num': '.O.OOO',
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O...',
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
    'z': 'O..OOO'
    }

num_to_br = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O...',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

#invert maps
br_to_en = {v: k for k, v in en_to_br.items()}
br_to_num = {v: k for k, v in num_to_br.items()}

def transl8_to_en(braille):
    cap = False
    num = False
    chars = []

    #divide input every 6 char, then add to output sting, print
    for i in range(0, len(braille), 6):
        current = braille[i:i+6]
        if current == '.....O': #capital
            cap = True
        elif current ==  '.O.OOO': #num
            num = True
        elif current == '......': #space
            num = False
            chars.append(' ')
            continue
        else:
            if num:
                chars.append(br_to_num[braille[i:i+6]])
            elif cap:
                chars.append(br_to_en[braille[i:i+6]].upper())
                cap = False
            else:
                chars.append(br_to_en[braille[i:i+6]])
    print(''.join(chars))
        

        
    
def transl8_to_br(english):
    #simply check if num or not, then use correspong dict to substitute
    num = False
    
    chars = []
    for i in range(0, len(english)):
        current = english[i]
        if current.isdigit():
            #print("NUM")
            if not num:
                chars.append('.O.OOO')
                num = True
            chars.append(num_to_br[current])
        else:
            num = False
            if current.isupper():
                chars.append('.....O')
            chars.append(en_to_br[current.lower()])
    print(''.join(chars))

def main():
    #print(sys.argv[1])
    input_string = ' '.join(sys.argv[1:])
    if all(char == 'o' or char == '.' for char in input_string.lower()):
        transl8_to_en(input_string)
    else:
        transl8_to_br(input_string)

#for testing
if __name__ == '__main__':
    main()