import sys

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
}

braille_to_numbers = {
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
    '......': ' ',
    '..O...': ',',
    '..OO.O': '.',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '..O.OO': '?',
    '..OOO.': '!',
    'O.O..O': '(',
    '.O.OO.': ')',
    '.O..O.': '/',
    '.OO..O': '<',
    '.O...O': '.',

}

english_to_braille = {
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
    ' ': '......',
    ',': '..O...',
    '.': '..OO.O',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '?': '..O.OO',
    '!': '..OOO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    '/': '.O..O.',
    '<': '.OO..O',
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
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
}

# o and > have the exact same braille notation.
# In my implementation I assume it is o rather than > as it is a more common symbol

def braille_to_text(braille):
    result = []
    capitalize_next = False
    number_mode = False
    
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        
        if symbol == english_to_braille['capital']:
            capitalize_next = True
            continue
        elif symbol == english_to_braille['number']:
            number_mode = True
            continue
        
        if symbol == english_to_braille[' ']:
            char = ' '
            number_mode = False
        elif number_mode:
            char = braille_to_numbers.get(symbol, '')
        else:
            char = braille_to_english.get(symbol, '')
        
        if capitalize_next:
            char = char.upper()
            capitalize_next = False
        
        result.append(char)
    
    return ''.join(result)

def text_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(english_to_braille['capital'])
            char = char.lower()
                
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number'])
                number_mode = True
        elif number_mode and char == ' ':
            number_mode = False
        
        result.append(english_to_braille.get(char, ''))
    
    return ''.join(result)

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def translate(input_string):
    if is_braille(input_string):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string))