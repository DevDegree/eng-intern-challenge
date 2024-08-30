import sys

SPACE = '......'
CAP_FOLLOWS = '.....O'
NUM_FOLLOWS = '.O.OOO'

# braille dictionary
braille_dict = {
    # letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    
    # numbers 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    
    # space
    ' ': '......',

    # symbols 
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '.....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# separate dictionaries for letters and numbers
reverse_braille_dict_letters = {v: k for k, v in braille_dict.items() if k.isalpha() or k in '.,?!:;-/<>()'}
reverse_braille_dict_numbers = {v: k for k, v in braille_dict.items() if k.isdigit() or k in '.,?!:;-/<>()'}

def is_braille(input_str):
    # check if the input string is in braille format
    return all(c in 'O.' for c in input_str)

def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            # indicates next character is uppercase
            result.append(CAP_FOLLOWS)  
            char = char.lower()
        if char.isdigit() and not number_mode:
            # indicates next characters are numbers
            result.append(NUM_FOLLOWS) 
            number_mode = True
        elif char == ' ':
            # reset number mode when encountering a space
            number_mode = False
        # append the braille representation character
        result.append(braille_dict[char])  
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == CAP_FOLLOWS:  
            # handle uppercase letters
            i += 6
            symbol = braille[i:i+6]
            result.append(reverse_braille_dict_letters[symbol].upper())
        elif symbol == NUM_FOLLOWS:  
            # handle numbers
            i += 6
            number_mode = True
            continue
        elif symbol == SPACE:
            # handle space
            result.append(' ')
            number_mode = False
        else:
            # handle regular characters
            if number_mode:
                result.append(reverse_braille_dict_numbers[symbol])
            else:
                result.append(reverse_braille_dict_letters[symbol])
        i += 6
    return ''.join(result)

def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()
