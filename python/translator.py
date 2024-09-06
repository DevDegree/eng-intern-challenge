import sys

eng_alphabet = {
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
    'z': 'O..OOO'
}

capital_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'
space = '......'


eng_numbers = {
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
}

period = {'.': '..OO.O'}

eng_special_chars = {
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

brl_alphabet = {v: k for k, v in eng_alphabet.items()}
brl_numbers = {v: k for k, v in eng_numbers.items()}
brl_special_chars = {v: k for k, v in eng_special_chars.items()}


def braille(string_input):
    
    if len(string_input) % 6 != 0:
        return False
    
    for char in string_input:
        if (char != 'O') and (char != '.'):
            return False
    
    return True


def eng_to_braille(text):
    braille = ''
    
    numbers = False
    
    # loop through each symbol
    # check if capital
        # add capital follows + braille ver of letter
    # check if decimal
        # add decimal follows + braille ver of period
    # check if number
        # add number follows
        # while not a space and less than len(text)
            # add braille ver of nums
    # check if part of the alphabet
        # add braille ver of said letter
    # check if part of special char list
        # add braille ver of said special char
    # else
        # raise error or print("Error!")
    
    for symbol in text:
        if symbol.lower() in eng_alphabet:
            if numbers:
                braille += space
                numbers = False
            if symbol.isupper():
                braille += capital_follows
            
            braille += eng_alphabet[symbol.lower()]
        
        elif symbol == ".":
            braille += decimal_follows + '..OO.O'
        
        elif symbol in eng_numbers:
            if not numbers:
                braille += number_follows
                numbers = True
            
            braille += eng_numbers[symbol]
            
        elif symbol == ' ':
            braille += space
            numbers = False
            
        elif symbol in eng_special_chars:
            if numbers:
                braille += space
                numbers = False
            
            braille += eng_special_chars[symbol]
        
        else:
            print("The symbol, '{symbol}', is unrecognizable.")
            

    return braille

def braille_to_eng(brayle):
    eng = ''
    
    brayle_symbol = []
    for i in range(0, len(brayle), 6):
        brayle_symbol.append(brayle[i:i+6])
    
    # loop through all indices
    # check if capital follows -> only next symbol is capital
    # check if decimal follows -> only next symbol is a decimal (assumption)
    # check if number follows -> all following numbers until space symbol
    # check for alphabet and special chars (w/o periods)
    
    i = 0
    while i < len(brayle_symbol):
        if brayle_symbol[i] == capital_follows:
            if brayle_symbol[i+1] in brl_alphabet:
                eng += brl_alphabet[brayle_symbol[i+1]].capitalize()
                i += 2
            else:
                print("The symbol, '{brayle_symbol[i+1]}' has been incorrectly placed after 'capital follows'")
                i += 1
        elif brayle_symbol[i] == decimal_follows:
            if brayle_symbol[i+1] == '..OO.O':
                eng += '.'
                i += 2
            else:
                print("The symbol, '{brayle_symbol[i+1]}' has been incorrectly placed after 'decimal follows'")
                i += 1
        
        elif brayle_symbol[i] == number_follows:
            i += 1
            while i < len(brayle_symbol) and brayle_symbol[i] != space:
                if brayle_symbol[i] in brl_numbers:
                    eng += brl_numbers[brayle_symbol[i]]
                else:
                    print("The symbol, '{brayle_symbol[i]}' is not a number.'")

                i += 1
            
        elif brayle_symbol[i] == space:
            eng += ' '
            i += 1
        
        elif brayle_symbol[i] in brl_alphabet:
            eng += brl_alphabet[brayle_symbol[i]]
            i += 1
        
        elif brayle_symbol[i] in brl_special_chars:
            eng += brl_special_chars[brayle_symbol[i]]
            i += 1
            
        else:
            print("Symbol, '{brayle_symbol[i]}', is unrecognizable, please check again!")
            i += 1
            
    
    return eng



def main():
    arg_inp = ' '.join(sys.argv[1:]).strip()
    if braille(arg_inp): 
        eng_ver = braille_to_eng(arg_inp)
        print(eng_ver)
        
    else:
        braille_ver = eng_to_braille(arg_inp)
        print(braille_ver)

if __name__ == "__main__":
    main()

