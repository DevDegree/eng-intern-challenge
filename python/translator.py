import sys

braille_alphabet = {
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
    'cf': '.....O',
    'df': '.O...O',
    'nf': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ":": '..OO..',
    ";": '..O.O.',
    "-": '....OO',
    "/": '.O..O.',
    "<": '.OO.O.',
    ">": 'O..OO.',
    "(": 'O.O..O',
    ")": '.O.OO.',
    " ": '......' 
}

def braille_translator(sentence):
    flag = False
    for character in sentence:
        if character == '.' or character == 'O':
            flag = False
        else: 
            flag = True
            break
    if flag:
        return english_to_braille(sentence)
    else:
        return braille_to_english(sentence)
        
def english_to_braille(sentence):
    output = ''
    previous_character = ''
    digit_flag = False
    for character in sentence:
        if character == '......':
            output += ' '
            digit_flag = False
        elif character.isupper():
            output += braille_alphabet['cf']
            character = character.lower()
        elif character.isdigit() and digit_flag is False:
            output += braille_alphabet['nf']
            digit_flag = True
        elif character == '.':
            if previous_character != '.':
                output += braille_alphabet['df']
        output += braille_alphabet[character]
        previous_character = character
    return output

def braille_to_english(sentence):
    output = ''
    c_f = False
    d_f = False
    n_f = False
    for i in range(0, len(sentence), 6):
        current_string = sentence[i:i+6]
        for k, v in braille_alphabet.items():
            if current_string == v and k not in ['cf', 'df', 'nf']:
                if k == ' ':
                    output += ' '
                    n_f = False
                    break
                elif c_f:
                    if k.isalpha():
                        output += k.upper()
                        c_f = False
                        break
                elif d_f:
                    if k == '.':
                        output += k
                        d_f = False
                        break
                elif n_f:
                    if k.isdigit():
                        output += k
                        break
                elif k.isalpha():
                    output += k
                    break
                elif k.isdigit():
                    output += k
                    break
                elif c_f is False and d_f is False and n_f is False:
                    output += k
                    break
        if current_string == braille_alphabet['cf']:
            c_f = True
        elif current_string == braille_alphabet['df']:
            d_f = True
        elif current_string == braille_alphabet['nf']:
            n_f = True
    return output

if __name__ == '__main__':
    sentence = ' '.join(sys.argv[1:])
    print(braille_translator(sentence))

