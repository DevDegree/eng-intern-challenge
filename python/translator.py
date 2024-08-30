import sys

alphabet_to_braille = {
    'a': 'O.....',
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
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
    'z': 'O..OOO',
    ' ': '......'
}

numbers_to_braille = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..'
}

braille_to_alpha = {v:k for k,v in alphabet_to_braille.items()}
braille_to_number = {v:k for k,v in numbers_to_braille.items()}


is_capital = '.....O'

is_num = '.O.OOO'

def is_braille(word):
    if len(set(word)) == 2 and '.' in word:
        return True
    return False

def convert_braille(word):
    res = ''
    num_follows = False
    capital_follows = False

    for i in range(0,len(word),6):
        s = word[i:i+6]

        if s == is_capital:
            capital_follows = True
            continue
        elif s == is_num:
            num_follows = True
            continue
        elif braille_to_alpha[s] == ' ':
            num_follows = False
        
        if num_follows:
            res += braille_to_number[s]
        elif capital_follows:
            res += braille_to_alpha[s].upper()
            capital_follows = False
        else:
            res += braille_to_alpha[s]
        
    return res

def convert_english(word):
    res  = ''
    num_follows = False

    for s in word:
        if s.isalpha():
            if s.isupper():
                res += is_capital
            res += alphabet_to_braille[s.lower()]
        elif s.isdigit():
            if num_follows == False:
                num_follows = True
                res += is_num
            res += numbers_to_braille[s]
        elif s == ' ':
            num_follows = False
            res += alphabet_to_braille[s]

    return res        


def main():
    if len(sys.argv)<2:
        return
    
    args_to_be_converted = ' '.join(sys.argv[1:])

    if is_braille(args_to_be_converted):
        print(convert_braille(args_to_be_converted))  
    else:
        print(convert_english(args_to_be_converted))

if __name__ == '__main__':
    main()