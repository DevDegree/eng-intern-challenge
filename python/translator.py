import sys

def reverse_map(hm):
    reversed_hm = dict()
    for key, value in hm.items():
        reversed_hm[value] = key
    return reversed_hm


CHAR_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...',
    ';': '..O.O.', ':': '..OO..', '!': '..OOO.', '?': '..O.OO',
    '(': '..OOOO', ')': '..OOOO', '/': '.O..O.', '-': '....O.',
    '<': '...OO.', '>': '...OOO', ' ': '......'
}

NUM_TO_BRAILLE = {
  
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", "0": ".OOO.."
}

BRAILLE_TO_NUM = reverse_map(NUM_TO_BRAILLE)
BRAILLE_TO_CHAR =  reverse_map(CHAR_TO_BRAILLE)


CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = '......'




#"Abc 123"
def word_to_braille(word):
    res = []
    is_number = False
    
    for ch in word:
        
        if ch.isdigit() == False:
            is_number = False
            
            if ch.isupper() == True:
                res.append(CAPITAL_FOLLOWS)
                res.append(CHAR_TO_BRAILLE[ch.lower()])
            
            elif ch == ' ':
                res.append(CHAR_TO_BRAILLE[' '])
            
            else:
                res.append(CHAR_TO_BRAILLE[ch.lower()])
            
        else:
            #number flag has not been set yet, number follows
            if is_number == False:
                res.append(NUMBER_FOLLOWS)
                
            #as long as number flag is set, then append 
            is_number = True
            res.append(NUM_TO_BRAILLE[ch])



    return "".join(res)
            




def braille_to_word(braille):
    res = []
    char_list = list(braille)
    is_number = False
    is_capital = False

    for i in range(0, len(char_list),6):

        substring = braille[i:i+6]

        if substring == CAPITAL_FOLLOWS:
            is_capital = True
            
            
        elif substring == NUMBER_FOLLOWS:
            is_number = True
        

        else:
             #braille converts to numbers as long as number flag true
             if is_number == True and substring in BRAILLE_TO_NUM:
                res.append(BRAILLE_TO_NUM[substring])
                #exits number mode if a space is encountered 
                if substring == SPACE:
                    is_number == False
             
             else:
                 #else convert braille to characters as long is_number flag is false
                 if substring in BRAILLE_TO_CHAR:
 
                    if is_capital == True:
                        res.append(BRAILLE_TO_CHAR[substring].upper())
                        is_capital = False
                    else:
                        res.append(BRAILLE_TO_CHAR[substring])
                        
        
    return "".join(res)
    
        


def translator_selector(st):
    if "O" in st or "." in st and len(st) == 1:
        return braille_to_word(st)
    else:
        return word_to_braille(st)



def main():
    arguments = ' '.join(sys.argv[1:])
    print(translator_selector(arguments))


if __name__ == "__main__":
    main()
