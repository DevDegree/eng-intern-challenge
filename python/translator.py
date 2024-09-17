import sys

#Braille to English mappings
braille_to_english = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')'
}

#English to Braille mappings
english_to_braille = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

#Numbers and their Braille equivalents
convert_nums = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
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

def is_braille(text):
    return all(c in '.O' for c in text)

def braille_to_english_conversion(braille):
    translation = ''
    numbers = False
    cap = False
    
    while braille:
        temp, braille = braille[:6], braille[6:]
        
        if temp == '......':
            numbers = False
            translation += ' '
        elif temp == '.....O':
            cap = True
        elif temp == '.O.OOO':
            numbers = True
        elif numbers:
            translation += convert_nums.get(temp, 'error')
        elif cap:
            translation += braille_to_english.get(temp, 'error').upper()
            cap = False
        else:
            translation += braille_to_english.get(temp, 'error')
    
    return translation

def english_to_braille_conversion(text):
    translation = ''
    numbers = False
    
    for char in text:
        if char == ' ':
            numbers = False
            translation += '......'
        elif char.isnumeric():
            if not numbers:
                numbers = True
                translation += '.O.OOO'
            translation += convert_nums.get(char, 'error')
        elif char.isupper():
            translation += '.....O' + english_to_braille.get(char.lower(), 'error')
        else:
            translation += english_to_braille.get(char, 'error')
    
    return translation

def main():

    args = sys.argv[1:]
    input_text = ' '.join(args) if not is_braille(args[0]) else '......'.join(args)
    conversion_func = braille_to_english_conversion if is_braille(input_text) else english_to_braille_conversion
    print(conversion_func(input_text))

if __name__ == "__main__":
    main()