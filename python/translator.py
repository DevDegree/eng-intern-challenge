import sys
import re

str_braille_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......'
}

int_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital_follows = '.....O'
number_follows = '.O.OOO'
decimal_follows = '.O...O'

braille_str_dict = {v: k for k, v in str_braille_dict.items()}
braille_int_dict = {v: k for k, v in int_braille_dict.items()}

def text_to_braille(text:str):
    braille = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:                
                braille.append(number_follows)
                number_mode = True
            braille.append(int_braille_dict[char])
        elif char.isalpha():
            if char.isupper():
                braille.append(capital_follows)
            braille.append(str_braille_dict[char.upper()])
            number_mode = False
        else:
            braille.append(str_braille_dict.get(char, '......'))
            number_mode = False
    
    return ''.join(braille)

def braille_to_text(braille_text):
    if not (len(braille_text)%6) == 0:
        return "Invalid input"
    
    text = []
    number_mode, capital_mode, decimal_mode = False, False, False
    start_index = 0 
    end_index = start_index+6
    while end_index <= len(braille_text):
        braille_char = braille_text[start_index:end_index]
        if braille_char == number_follows:
            number_mode = True
        elif braille_char == capital_follows:
            capital_mode = True
        elif braille_char == decimal_follows:
            decimal_mode = True
        elif braille_char == '......':
            text.append(' ')
            number_mode, capital_mode, decimal_mode = False, False, False
        else:
            if number_mode:
                char = braille_int_dict.get(braille_char, ' ')
                text.append(char)
            elif capital_mode:
                char = braille_str_dict.get(braille_char, ' ')
                text.append(char.upper())
                capital_mode = False
            elif decimal_mode:
                char = braille_int_dict.get(braille_char, ' ')
                text.append('.'+char)
                decimal_mode = False
            else:
                char = braille_str_dict.get(braille_char, ' ')
                text.append(char.lower())
        start_index, end_index = end_index, end_index+6

    return ''.join(text)

def is_braille(input_string):
    return bool(re.match(r'^[O\.]{6,}$', input_string))


if __name__ == "__main__":
    if len(sys.argv) <=1:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)
    text = ' '.join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_text(text))
    else:
        print(text_to_braille(text))