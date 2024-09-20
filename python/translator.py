import sys

def invert_dictionary(original: dict) -> dict:
    inverted = {}
    for key, value in original.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

def convert_braille_to_alpha(arg: str, braille_to_alpha: dict, 
                              alpha_to_braille: dict) -> str:
    numeric_flag = 0
    capital_flag = 0
    result = ''

    for j in range(6, len(arg) + 1, 6):
        brailles = arg[j-6:j]

        if brailles == alpha_to_braille['capital_follows']:
            capital_flag = 1
            continue

        if (brailles == alpha_to_braille['number_follows'] 
        or brailles == alpha_to_braille['decimal_follows']):
            numeric_flag = 1
            continue

        if brailles == alpha_to_braille[' ']:
                numeric_flag = 0

        if capital_flag == 1:
            result += (braille_to_alpha[brailles][0]).upper()
            capital_flag = 0
        elif numeric_flag == 1:
            result += braille_to_alpha[brailles][1]
        else:
            result += braille_to_alpha[brailles][0]

        capital_flag = 0

    return result

def main():

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
        ' ': '......'
    }

    braille_to_alpha = invert_dictionary(alpha_to_braille)

    length = len(sys.argv)
    result = ''

    for i in range(1, length):
        arg = sys.argv[i]
        if '.' in arg:
            result = convert_braille_to_alpha(arg, braille_to_alpha, alpha_to_braille)
        else:
            numeric_flag = 0
            if i > 1:
                result += alpha_to_braille[' ']
            for char in arg:
                if char.isupper():
                    result += alpha_to_braille['capital_follows'] + alpha_to_braille[char.lower()]
                elif (not char.isalpha()) & (numeric_flag == 0):
                    result += alpha_to_braille['number_follows'] + alpha_to_braille[char]
                    numeric_flag = 1
                else:
                    result += alpha_to_braille[char]

    print(result)

main()