import sys

def text_to_braille(text):
    braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..', '.': 'O.O.OO', ',': 'O.....', ';': 'O.O...', ':': 'OO....',
        '?': 'OO.O..', '!': 'O..O..', '(': 'OOO...', ')': 'OOOO..', '-': 'O.OO..', 
        '/': '.OO...', '<': '.OO..O', '>': 'O..OO.', 'capital-follows': '.....O', 
        'number-follows': '....OO', 'decimal-follows': '.O...O', 'space': '......'
    }
    
    braille_eq = ''
    for char in text:
        if char.isupper():
            braille_eq += braille_dict['capital-follows']
            braille_eq += braille_dict[char.lower()]
        elif char == '.':
            braille_eq += braille_dict['decimal-follows']
        elif char.isdigit():
            braille_eq += braille_dict['number-follows']
            braille_eq += braille_dict[char]
        elif char == ' ':
            braille_eq += braille_dict['space']
        else:
            braille_eq += braille_dict[char]
    
    return braille_eq


def braille_to_text(braille):
    braille_dict = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
        'O..OOO': 'z', '.....O': 'capital-follows', '....OO': 'number-follows', 
        '.O...O': 'decimal-follows', '......': 'space'
    }
    
    text = ''
    i = 0
    while i < len(braille):
        char = braille[i:i+6]
        if char == '.....O':
            i += 6
            char = braille[i:i+6]
            text += braille_dict[char].upper()
        elif char == '....OO':
            i += 6
            char = braille[i:i+6]
            text += braille_dict[char]
        elif char == '......':
            text += ' '
        else:
            text += braille_dict[char]
        i += 6
    
    return text

def detect_and_translate(input_text):
    if all(char in 'O. ' for char in input_text)and len(input_text.replace(' ', '')) % 6 == 0:
        return braille_to_text(input_text)
    else:
        return text_to_braille(input_text)

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    print(detect_and_translate(input_text))
