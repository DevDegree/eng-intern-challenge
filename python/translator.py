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
    'z': 'O..OOO'
}

digits_to_braille = {
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

capital_follows = '.....O'
number_follows = '.O.OOO'
space = '......'

braille_to_alpha = dict((v, k) for k,v in alpha_to_braille.items())

braille_to_digits = dict((v,k) for k,v in digits_to_braille.items())

# Returns True if english, False if braille
def check_input(user_input):
    for i in user_input:
        if i.isspace():
            continue
        if not i.isalpha():
            if not i.isdigit():
                return False
    return True

def convert_braille(user_input):
    n = 0
    translated = []
    is_num = 0
    is_cap = 0

    while n < len(user_input):

        section = user_input[n:n+6]    

        if section == space:
            translated.append(' ')
            is_num = 0
            n+=6

        elif section == number_follows:
            is_num = 1
            n+=6
        
        elif section == capital_follows:
            is_cap = 1
            n+=6

        elif is_num == 1:
            translated.append(braille_to_digits[section])
            n+=6

        elif is_cap == 1:
            translated.append(braille_to_alpha[section].upper())
            is_cap = 0
            n+=6
        
        else:
            translated.append(braille_to_alpha[section])
            n+=6
        
    return ''.join(translated)
        
def convert_alpha(user_input):
    n = 0
    translated = []
    is_num = 0

    while n < len(user_input):
        
        section = user_input[n]

        if section.isspace():
            translated.append(space)
            is_num = 0
            n+=1

        elif section.isdigit():
            if is_num == 1:
                translated.append(digits_to_braille[section])
            else:
                is_num = 1
                translated.append(number_follows)
                translated.append(digits_to_braille[section])
            n+=1
        
        elif section.isalpha():
            if section.isupper():
                translated.append(capital_follows)
                translated.append(alpha_to_braille[section.lower()])
            else:
                translated.append(alpha_to_braille[section])
            n+=1
        
    return ''.join(translated)


def main(input):
    if check_input(input):
        return convert_alpha(input)
    else:
        return convert_braille(input)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = ' '.join(sys.argv[1:])
        print(main(input.strip()))
    else:
        print("Invalid input. Please try again")