braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_capital = '.....O'
braille_number = '.O.OOO'
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def detect_input_type(input_string):
    if all(char in ['O', '.'] for char in input_string.replace(' ', '')):
        return 'braille'
    else:
        return 'english'

def english_to_braille(text):
    braille_output = ""
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output += braille_number
                number_mode = True
            braille_output += braille_numbers[char]
        elif char.isalpha():
            if char.isupper():
                braille_output += braille_capital
            braille_output += braille_alphabet[char.lower()]
            number_mode = False
        elif char == ' ':
            braille_output += braille_alphabet[' ']
            number_mode = False
    return braille_output

def braille_to_english(braille):
    braille_list = [braille[i:i+6] for i in range(0, len(braille), 6)]
    english_output = ""
    number_mode = False
    capitalize_next = False
    
    for code in braille_list:
        if code == braille_capital:
            capitalize_next = True
            continue
        elif code == braille_number:
            number_mode = True
            continue
        elif code == '......':
            english_output += ' '
            number_mode = False
        else:
            if number_mode:
                english_output += list(braille_numbers.keys())[list(braille_numbers.values()).index(code)]
            else:
                char = list(braille_alphabet.keys())[list(braille_alphabet.values()).index(code)]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                english_output += char
    
    return english_output

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    input_string = sys.argv[1]
    input_type = detect_input_type(input_string)

    if input_type == 'english':
        result = english_to_braille(input_string)
    else:
        result = braille_to_english(input_string)

    print(result)

if __name__ == "__main__":
    main()

