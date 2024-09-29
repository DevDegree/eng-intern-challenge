import sys, re

CAPITAL_FOLLOWS = 'capital follows'
NUMBER_FULLOWS = 'number follows'

BRAILLE_CHAR_SIZE = 6

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
    CAPITAL_FOLLOWS: '.....O', 
    NUMBER_FULLOWS: '.O.OOO',
    ' ': '......',
}

NUMBER_TO_BRAILLE = {
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

BRAILLE_TO_ENGLISH = dict(zip(ENGLISH_TO_BRAILLE.values(), ENGLISH_TO_BRAILLE.keys()))
BRAILLE_TO_NUMBER = dict(zip(NUMBER_TO_BRAILLE.values(), NUMBER_TO_BRAILLE.keys()))

def is_english(input):
    if len(input) > 1 or len(input[0]) % BRAILLE_CHAR_SIZE != 0:
        return True
    return not bool(re.fullmatch(r'[O.]*', input[0]))

def translate_english_to_braille(string):
    braille = ''
    ind = 0
    while ind < len(string):
        char = string[ind]
        if char.isupper():
            braille += ENGLISH_TO_BRAILLE[CAPITAL_FOLLOWS] + ENGLISH_TO_BRAILLE[char.lower()]
            ind += 1
        elif char.isnumeric():
            braille += ENGLISH_TO_BRAILLE[NUMBER_FULLOWS]
            while string[ind] != ' ' and ind < len(string):
                braille += NUMBER_TO_BRAILLE[string[ind]]
                ind += 1
        elif char.islower():
            braille += ENGLISH_TO_BRAILLE[char]
            ind += 1
        elif char == ' ':
            braille += ENGLISH_TO_BRAILLE[' ']
            ind += 1
        
    return braille

def translate_braille_to_english(string):
    english = ''
    ind = 0
    while ind < len(string):
        char = string[ind:ind + BRAILLE_CHAR_SIZE]
        if char == ENGLISH_TO_BRAILLE[CAPITAL_FOLLOWS]:
            ind += BRAILLE_CHAR_SIZE
            char = string[ind:ind + BRAILLE_CHAR_SIZE]
            english += BRAILLE_TO_ENGLISH[char].upper()
            ind += BRAILLE_CHAR_SIZE
        elif char == ENGLISH_TO_BRAILLE[NUMBER_FULLOWS]:
            ind += BRAILLE_CHAR_SIZE
            while string[ind:ind + BRAILLE_CHAR_SIZE] != ENGLISH_TO_BRAILLE[' '] and ind < len(string):
                english += BRAILLE_TO_NUMBER[string[ind:ind + BRAILLE_CHAR_SIZE]]
                ind += BRAILLE_CHAR_SIZE
        else:
            english += BRAILLE_TO_ENGLISH[char]
            ind += BRAILLE_CHAR_SIZE
        
    return english
        

def translate(input):
    if is_english(input):
        return translate_english_to_braille(' '.join(input))
    else:
        return translate_braille_to_english(input[0])


if __name__ == "__main__":
    print(translate(sys.argv[1:]))
