import sys

BRAILLE_DICT = {
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
    '.....O': 'capital',
    '.O.OOO': 'number',
    '......': ' ',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '_',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}
ENG_DICT = {value: key for key, value in BRAILLE_DICT.items()}

def to_english(input):
    english = []
    special = 0  # 0: none, 1: capital, 2: number

    
    for i in range(0, len(input), 6):
        braille = input[i:i+6]
        if braille in BRAILLE_DICT:
            braille = BRAILLE_DICT[braille]
            if braille == 'capital':
                special = 1
            elif braille == 'number':
                special = 2
            elif braille == ' ':
                special = 0
                english.append(' ')
            else:
                match special:
                    case 1:
                        braille = braille.upper()
                        special = 0
                    case 2:
                        braille = BRAILLE_DICT[braille] #translate to num        
                english.append(braille)
    return ''.join(english)
            

def to_braille(input):
    braille = []
    num = False

    for char in input:
        if char.isupper():
            braille.append(ENG_DICT['capital'])
            char = char.lower()
        if char.isdigit():
            if not num:
                braille.append(ENG_DICT['number'])
                num = True
            braille.append(ENG_DICT[ENG_DICT[char]])
        else:
            num = False
            braille.append(ENG_DICT[char])
    return ''.join(braille)
            

def braille_or_english(input):
    if (all(char in ['O', '.'] for char in input)):
        translated = to_english(input)
        sys.stdout.write(translated)
    else:
        translated = to_braille(input)
        sys.stdout.write(translated)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("No argument Found")
    else:
        input = ' '.join(sys.argv[1:])
        braille_or_english(input)
