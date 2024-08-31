import sys

char_to_braille = {
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

    'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

braille_to_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': 'O',
}

braille_to_letter = {
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
            output += char_to_braille['capital']
            output += char_to_braille[char.lower()]
        elif char.islower() or number_mode:
            output += char_to_braille[char]
        elif char.isdigit() and not number_mode:
            number_mode = True
            output += char_to_braille['number']
            output += char_to_braille[char]
        else: 
            number_mode = False
            output += char_to_braille[' ']
    
    return output

def translate_to_english(braille: str) -> str:
    output = ""
    number_mode = False
    capitalize_next = True
    for i in range(0, len(braille), 6):
        b_char = braille[i:i+6]

        if b_char == char_to_braille['number']:
            number_mode = True
        elif b_char == char_to_braille[' ']:
            number_mode = False
            output += ' '
        elif b_char == char_to_braille['capital']:
            capitalize_next = True
        elif number_mode:
            output += braille_to_number[b_char]
        elif capitalize_next:
            output += braille_to_letter[b_char].upper()
            capitalize_next = False
        else:
            output += braille_to_letter[b_char]

    return output

def process_input():
    arguments = sys.argv[1:]
    string = (" ".join(arguments))

    is_braille = all(char in 'O.' for char in string) and len(string) % 6 == 0

    if is_braille:
        print(translate_to_english(string))
    else:
        print(translate_to_braille(string))

process_input()