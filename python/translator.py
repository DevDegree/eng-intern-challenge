'''
    Braille Translator:
    This command_line program takes a string and 
    determines if the string is either Braille or English
    and coverts it to the correct opposite
    Gavin Xu
    Aug 30, 2024
'''

import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    'capital_follows': '.....O', 
    'decimal_follows': '.O...O', 
    'number_follows': '.O.OOO',

    ' ': '......'
    # '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    # ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    # '(': 'O.O..O', ')': '.O.OO.', 
}

# letter 'a' - 'j' are overwritten by number '1' to '0' 
BRAILLE_TO_ENGLISH = {val: key for key, val in ENGLISH_TO_BRAILLE.items()}

def determine_braille(text):
    '''
        Determine if the input text is braille or not
    '''
    braille_characters = ('.', 'O')
    if len(text) % 6:
        return False
    for c in text:
        if c not in braille_characters:
            return False
    return True


def convert_to_letter(num_str):
    '''
        Convert number string [1-0] to letter [a-j] correspondingly
    '''
    if num_str == '0':
        return 'j'
    return chr(ord(num_str) - ord('1') + ord('a'))

def braille_to_english(text):
    '''
        Convert Braille to English
    '''
    size = 6

    # flag to determine if it is reading numbers 
    read_numbers = False
    # flag to determine if it is reading capital letter
    read_uppercase = False
    english_result = ""
    for i in range(0, len(text), size):
        char = BRAILLE_TO_ENGLISH[text[i: i + size]]
        # next braille word should be a uppercase english letter
        if char == 'capital_follows':
            read_uppercase = True
            continue
        # the following braille words should all be numbers
        # until the next space symbol
        elif char == 'number_follows':
            read_numbers = True
            continue
    
        # turn off 'read numbers' mode
        elif char == ' ':
            read_numbers = False

        # read numbers
        if read_numbers:
            english_result += char

        # read other characters
        else:
            # if not in 'read numbers' mode
            # we should convert [1-0] to [a-j] correspondingly
            if char >= '0' and char <= '9':
                char = convert_to_letter(char)
            
            # capitalize
            if read_uppercase:
                char = char.upper()
                read_uppercase = False
            
            english_result += char

    return english_result


def english_to_braille(text):
    '''
        Convert English to Braille
    '''
    braille_result = ""
    # flag to determine if it is reading numbers 
    read_numbers = False
    for char in text:

        if char.isdigit():
            # if it just starts to read number
            if not read_numbers:
                braille_result += ENGLISH_TO_BRAILLE['number_follows']
                read_numbers = True
        
        # if it is reading a uppercase letter
        elif char.isupper():
            braille_result += ENGLISH_TO_BRAILLE['capital_follows']
            char = char.lower()
            read_numbers = False
        
        # other characters
        else:
            read_numbers = False
            
        braille_result += ENGLISH_TO_BRAILLE[char]
        
    return braille_result


def main():
    if len(sys.argv) < 2:
        print('Please provide the string to translate!')

    text = ' '.join(sys.argv[1:])
    # if the given string is braille 
    if determine_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

if __name__ == '__main__':
    main()
    
