#! python3
# translator.py - translates braille to english and vice versa

import sys

alphabet = {'a': 'O.....',
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
            'capital_follows': '.....O',
            'decimal_follows': '.O...O',
            'number_follows': '.O.OOO',
            '.': '..OO.O',
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
            ' ': '......'}

numbers = {'1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..'}

def english_or_braille(input):
    if (len(input) % 6 != 0) or (any((char not in set('.O')) for char in input)):
        return 'english'
    else:
        return 'braille'

def to_braille(english_phrase):
    braille_phrase = ''
    is_number = 0
    for char in english_phrase:
        if is_number > 0 and char == '.':
            braille_phrase = braille_phrase + alphabet['decimal_follows']
        else:
            if char.isupper():
                braille_phrase = braille_phrase + alphabet['capital_follows']
            if char.isdigit() and is_number == 0:
                braille_phrase = braille_phrase + alphabet['number_follows']
                is_number = 1

            if char == ' ':
                is_number = 0

            braille_phrase = braille_phrase + alphabet[char.lower()]

    return braille_phrase

def to_english(braille):
    english_phrase = ''
    is_number = 0
    is_capital = 0
    
    for char in braille:
        if char == alphabet['number_follows']:
            is_number = 1
        elif char == alphabet[' ']:
            is_number = 0
            english_phrase = english_phrase + list(alphabet.keys())[list(alphabet.values()).index(char)]
        elif char == alphabet['decimal_follows']:
            english_phrase = english_phrase + '.'
        elif is_number > 0:
            english_phrase = english_phrase + list(numbers.keys())[list(numbers.values()).index(char)]
        elif char == alphabet['capital_follows']:
            is_capital = 1
        elif is_capital > 0:
            english_phrase = english_phrase + list(alphabet.keys())[list(alphabet.values()).index(char)].upper() 
            is_capital = is_capital - 1
        else:
            english_phrase = english_phrase + list(alphabet.keys())[list(alphabet.values()).index(char)]

    return english_phrase
        
def listerator(braille):
    braille_list = []
    for x in range(0, len(braille), 6):
        braille_list.append(braille[x:x+6])
    return braille_list

def get_input():
    return ' '.join(sys.argv[1:])

def main():
    input_phrase = get_input()
    
    if english_or_braille(input_phrase) == 'english':
        print(to_braille(input_phrase), end='')
    else:
        print(to_english(listerator(input_phrase)), end='')
main()