import sys

# Braille dictionary for letters
braille_dict_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO..OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Braille dictionary for numbers
braille_dict_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mapping for Braille to English translation
english_dict_letters = {v: k for k, v in braille_dict_letters.items()}
english_dict_numbers = {v: k for k, v in braille_dict_numbers.items()}

# Number and capital indicators
braille_number_indicator = '.O.OOO' 
braille_capital_indicator = '.....O'

def translate_to_braille(text):
    braille_text = ""
    numbers_mode = False

    for char in text:
        if char.isdigit():
            if not numbers_mode:
                braille_text += braille_number_indicator
                numbers_mode = True
            braille_text += braille_dict_numbers.get(char, '......')
        elif char.isalpha():
            if char.isupper():
                braille_text += braille_capital_indicator
            braille_text += braille_dict_letters.get(char.lower(), '......')
            numbers_mode = False
        elif char == ' ':
            braille_text += braille_dict_letters[' '] 
            numbers_mode = False
        else:
            braille_text += '......'
    return braille_text

def translate_from_braille(braille_text):
    text = ""
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    
    numbers_mode = False
    capital_mode = False
    
    for braille_char in braille_chars:
        if braille_char == braille_number_indicator:
            numbers_mode = True
            continue 
        if braille_char == braille_capital_indicator:
            capital_mode = True
            continue  
        if numbers_mode:
            char = english_dict_numbers.get(braille_char, '?')
            if char in '0123456789':
                text += char
            else:
                text += '?'
        else:
            char = english_dict_letters.get(braille_char, '?')
            if capital_mode:
                char = char.upper()
                capital_mode = False          
            if char == ' ':
                text += ' '
            else:
                text += char  
    return text

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])
    if all(char in '.O ' for char in input_text):
        print(translate_from_braille(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
