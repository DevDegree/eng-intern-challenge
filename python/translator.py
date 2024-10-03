import sys
# accepts str as input
# detect braille or english
# map each eng char to braille - use dic
# define braille rep
# translate: check each char, if it is uppercase, add capital sym
#            for num, use num sym

braille_let = {
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
    'q': 'OOOO.O', 
    'r': 'O.OO.O', 
    's': '.OO.O.', 
    't': '.OOO.O',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

braille_num = {
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

eng_let = {v: k for k, v in braille_let.items()}
eng_num = {v: k for k, v in braille_num.items()}

capital_follows = '.....O'
number_follows = '.O.OOO' 
space_braille = '......'

# checks if is braille
def braille(input_str):
    braille_char = 'O' or '.'
    for char in input_str:
        if char not in braille_char:
            return False
    return True

#translates to braille
def translate_to_braille(text):
    result = []
    is_num = False

    for char in text:
        if char.isupper():
            result.append(capital_follows)
            char = char.lower()
        if char.isdigit() and not is_num:
            result.append(number_follows)
            is_num = True
        elif char == ' ':
            result.append(space_braille)
            is_num = False
        if char in braille_let:
            result.append(braille_let[char])
        elif char in braille_num:
            result.append(braille_num[char])

    # print(''.join(result))

    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    is_num = False
    is_capital = False
    braille_chars = braille_text.split()

    for char in braille_chars:
        if char == capital_follows:
            is_capital = True
        elif char == number_follows:
            is_num = True
        elif char == space_braille:
            result.append(' ')
            is_num = False
        elif is_num:
            result.append(eng_num[char])
        elif is_capital:
            result.append(eng_let[char].upper())
        else:
            result.append(eng_let[char])
    return ''.join(result)

def main():

    # print("hi")

    input = (sys.argv[1:])
    input_str = ' '.join(input)
    # print(input_str)

    if braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()