import sys

CAPITAL = '.....O'
NUMBER = '.O.OOO'
SPACE = '......'

CHAR_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', 'O': '.OOO..',
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': 'O',
}

BRAILLE_TO_LETTER = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
}

def translate_to_braille(text: str) -> str:
    output = ""
    number_mode = False
    for char in text:
        if char.isupper():
            output += CAPITAL
            output += CHAR_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if not number_mode:
                number_mode = True
                output += NUMBER
            output += CHAR_TO_BRAILLE[char]
        elif char.islower():
            output += CHAR_TO_BRAILLE[char]
        else: 
            number_mode = False
            output += SPACE
    
    return output

def translate_to_english(braille: str) -> str:
    output = ""
    number_mode = False
    capitalize_next = False
    for i in range(0, len(braille), 6):
        b_char = braille[i:i+6]

        if b_char == CAPITAL:
            capitalize_next = True
        elif b_char == NUMBER:
            number_mode = True
        elif b_char == SPACE:
            number_mode = False
            output += ' '
        else:
            if number_mode:
                output += BRAILLE_TO_NUMBER[b_char]
            elif capitalize_next:
                output += BRAILLE_TO_LETTER[b_char].upper()
                capitalize_next = False
            else:
                output += BRAILLE_TO_LETTER[b_char]
                
    return output

def is_braille(string: str) -> bool:
    all_chars_valid = all(char in 'O.' for char in string)
    length_is_valid = len(string) % 6 == 0
    return all_chars_valid and length_is_valid

def is_english(string: str) -> bool:
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ')
    return all(char in valid_chars for char in string)

def process_input():
    arguments = sys.argv[1:]
    string = (" ".join(arguments))

    if is_braille(string):
        print(translate_to_english(string))
    elif is_english(string):
        print(translate_to_braille(string))
    else:
        print("Error: Input contains invalid characters. Only letters, numbers, and spaces are allowed.")

process_input()