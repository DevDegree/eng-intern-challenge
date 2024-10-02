
CAPITAL_FOLLOWS = '.....O'

NUMBER_FOLLOWS = '.O.OOO'

BRAILLE_SPACE = '......'

ENGLISH_TO_BRAILLE = {
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
    ' ': '......',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

BRAILLE_TO_ENGLISH = {
    '......': ' ',
    
    'letters': {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f', 
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',
    },

    'numbers' : {
        'O.....': '1',
        'O.O...': '2', 
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': '0'
    }
}

def translate(input_string):
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)

def is_braille(input_string):
    return all(c in ['O', '.'] for c in input_string)

def translate_braille_to_english(braille_string):
    english_string = ''
    num_buffer = ''
    write_capital = False
    write_number = False

    for i in range(0, len(braille_string), 6):
        char = braille_string[i:i+6]

        if write_capital:
            english_string += BRAILLE_TO_ENGLISH['letters'][char].upper()
            write_capital = False
        elif (char == BRAILLE_SPACE):
            if num_buffer:
                english_string += num_buffer
                num_buffer = ''
            english_string += ' '
            write_number = False
        elif write_number:
            num_buffer += BRAILLE_TO_ENGLISH['numbers'][char]
        elif (char == CAPITAL_FOLLOWS):
            write_capital = True
        elif (char == NUMBER_FOLLOWS):
            write_number = True
        else:
            english_string += BRAILLE_TO_ENGLISH['letters'][char]
    
    if num_buffer:
        english_string += num_buffer

    return english_string

def translate_english_to_braille(english_string):
    braille_string = ''
    num_buffer = ''

    for char in english_string:
        if (char == ' '):
            if num_buffer:
                braille_string += (NUMBER_FOLLOWS + num_buffer)
                num_buffer = ''
            braille_string += ENGLISH_TO_BRAILLE[' ']
            
        elif (char.isupper()):
            braille_string += (CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.lower()])
        elif (char.isnumeric()):
            num_buffer += ENGLISH_TO_BRAILLE[char]
        else:
            braille_string +=  ENGLISH_TO_BRAILLE[char]
    
    if num_buffer:
        braille_string += (NUMBER_FOLLOWS + num_buffer)

    return braille_string


if __name__ == "__main__":
    import sys
    sep = '......' if is_braille(sys.argv[1]) else ' '
    input_string = sep.join(sys.argv[1:])
    print(translate(input_string))
