import sys

BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

REVERSE_BRAILLE_LETTERS = {v: k for k, v in BRAILLE_DICT.items() if k.isalpha() or k == ' '}
digit_mapping = {
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

def english_to_braille(text):
    braille_text = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            braille_text.append(BRAILLE_DICT['number'])
            number_mode = True
        elif char.isalpha() and number_mode:
            number_mode = False
                
        if char.isupper():
            braille_text.append(BRAILLE_DICT['capital'])
            char = char.lower()
        
        braille_char = BRAILLE_DICT.get(char, '......')  
        braille_text.append(braille_char)
    
    return ''.join(braille_text)

def braille_to_english(braille):
    english_text = []
    capital_next = False
    number_mode = False
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    
    for braille_char in braille_chars:
        if braille_char == BRAILLE_DICT['capital']:
            capital_next = True
            continue
        elif braille_char == BRAILLE_DICT['number']:
            number_mode = True
            continue
        
        if number_mode:
            if braille_char in digit_mapping:
                char = digit_mapping[braille_char]
                english_text.append(char)
                continue
            else:
                number_mode = False  
        
        char = REVERSE_BRAILLE_LETTERS.get(braille_char, '')
        
        if capital_next and char:
            char = char.upper()
            capital_next = False
        
        english_text.append(char)
    
    return ''.join(english_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text to translate>")
        return
    
    input_text = ' '.join(sys.argv[1:])

    if all(char in 'O.' for char in input_text):
        result = braille_to_english(input_text)
    else:
        result = english_to_braille(input_text)

    print(result)

if __name__ == "__main__":
    main()

