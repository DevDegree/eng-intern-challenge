import sys

def is_braille(arg):
    braille_chars = ['.', 'O']
    braille = True
    if len(arg) == 1:
        if arg[0] not in braille_chars:
            braille = False
    else:
        for i in range(2):
            if arg[i] not in braille_chars:
                braille = False
    return braille

def main():
    eng_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    'capital follows': '.....O', 'decimal follows': '.O...O', 'number follows': '.O.OOO',
    ',': 'O.....', '?': 'O.O..O', '!': 'O.OOO.',':': 'O.OO..', ';': 'O.O...', 
    '-': 'OO....', '/': 'O..O.O', '<': 'O...O.', '>': 'O..OOO', '(': 'O..OOO', ')': 'O..OOO',
    ' ': '......'
    }
    numbers_and_decimal = {
    'O..OO.': '.', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }

    user_input = ' '.join(sys.argv[1:])

    if is_braille(user_input):
        capitalize = False
        number = False
        for num in range(len(user_input)//6):
            char = user_input[num*6:num*6+6]
            for key, value in eng_to_braille.items():
                if value == char:
                    if key == ' ':
                        print(' ', end='')
                        number = False
                        break
                    if key == 'capital follows':
                        capitalize = True
                        break
                    elif key == 'decimal follows':
                        print('.', end='')
                        num += 1
                        break
                    elif key == 'number follows':
                        number = True
                        break
                    elif number:
                        print(numbers_and_decimal[value], end='')
                        break
                    elif capitalize:
                        print(key.upper(), end='')
                        capitalize = False
                        break
                    else:
                        print(key, end='')
                        break
    else:
        first_number = True
        for char in user_input:
            if char.isdigit() and first_number:
                first_number = False
                print(eng_to_braille['number follows'], end='')
                for key, value in numbers_and_decimal.items():
                    if value == char:
                        print(key, end='')
                        break
            elif char.isdigit():
                for key, value in numbers_and_decimal.items():
                    if value == char:
                        print(key, end='')
                        break
            elif char.isupper():
                print(eng_to_braille['capital follows'], end='')
                print(eng_to_braille[char.lower()], end='')
            elif char in eng_to_braille:
                print(eng_to_braille[char], end='')

main()