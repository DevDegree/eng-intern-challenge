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



def braille(string_input):
    
    if len(string_input) % 6 != 0:
        return False
    
    for char in string_input:
        if (char != 'O') or (char != '.'):
            return False
    
    return True


def eng_to_braille(text):
    braille = ''
    
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
            

    return braille

def braille_to_eng(brayle):
    eng = ''
    
    # loop through all indices
    # check if capital follows -> only next symbol is capital
    # check if decimal follows -> only next symbol is a decimal (assumption)
    # check if number follows -> all following numbers until space symbol
    # check for alphabet and special chars (w/o periods)
            
    
    return eng



def main():
    arg_inp = sys.argv[1].strip()
    if braille(arg_inp): 
        eng_ver = braille_to_eng(arg_inp)
        print(eng_ver)
        
    else:
        braille_ver = eng_to_braille(arg_inp)
        print(braille_ver)

if __name__ == "__main__":
    main()

