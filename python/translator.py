import sys

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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'O': '.OOO..',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..O.OO',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}
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
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '!',
    '..O.OO': '?',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}

letter_to_number = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0',
}



def check_is_braille(text):
    return all(char in {'.', 'O'} for char in text)

def translate(text):
    is_braille =  check_is_braille(text)
    next_is_capital = False
    next_is_number = False
    
    result = ""
    
    if is_braille:
        for i in range(0, len(text), 6):
            braille_char = text[i:i+6]
            if next_is_capital:
                result += braille_to_english[braille_char].upper()
                next_is_capital = False
            elif next_is_number:
                result += letter_to_number[braille_to_english[braille_char]]
            elif braille_char == english_to_braille[' ']:
                result += ' '
                next_is_capital = False
            elif braille_char == english_to_braille['capital']:
                next_is_capital = True
            elif braille_char == english_to_braille['number']:
                next_is_number = True
            else:
                result += braille_to_english[braille_char]
    else:
        for char in text:
            if char.isnumeric():
                result += english_to_braille['number']
                result += english_to_braille[char]
            elif char.isupper():
                result += english_to_braille['capital']
                result += english_to_braille[char.lower()]
            else:
                result += english_to_braille[char]
            
    return result
        

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
        
    result = translate(text)
    
    print(result)
    
    return result

if __name__ == "__main__":
    main()
    
    
    