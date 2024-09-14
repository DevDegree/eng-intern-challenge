import sys

alpha_to_braille = {
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
    'z': 'O..OOO',
    ' ': '......'
}

num_to_braille = {
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

space = '......'
cap_next = '.....O'
num_next = '.O.OOO'

def braille_to_english(args: str) -> str:
    braille_to_alpha = dict((braille, alpha) for alpha, braille in alpha_to_braille.items())
    braille_to_num = dict((braille, num) for num, braille in num_to_braille.items())

    is_cap_next = False
    is_num_next = False
    result = ''

    for i in range(0, len(args), 6):
        braille = args[i:i+6]

        if braille == cap_next:
            is_cap_next = True
            continue
        elif braille == num_next:
            is_num_next = True
            continue
        elif braille == space:
            result += ' '
            is_num_next = False
        elif is_num_next:
            result += braille_to_num[braille]
            continue
        else:
            letter = braille_to_alpha[braille]

            if (is_cap_next):
                letter = letter.upper()
                is_cap_next = False

            result += letter

    return result

def english_to_braille(args: str) -> str:
    result = ''
    prev_is_num = False

    for char in args:
        if char.isalpha():
            prev_is_num = False
            if char.isupper():
                result += cap_next
            
            result += alpha_to_braille[char.lower()]
        elif char == ' ':
            prev_is_num = False
            result += space
        else:
            if not prev_is_num:
                prev_is_num = True
                result += num_next
            
            result += num_to_braille[char]
    
    return result

def main() -> None:
    args = ' '.join(sys.argv[1:])

    is_braille = True

    for i in args:
        if not i in '.O':
            is_braille = False
            break
        
    result = ''

    if (is_braille):
        result = braille_to_english(args)
    else:
        result = english_to_braille(args)
    
    print(result)

if (__name__ == '__main__'):
    main()