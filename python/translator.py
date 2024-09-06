import sys

ALPHANUMERIC_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......',
}

BRAILLE_TO_ALPHABET = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

def is_braille(text):
    return all(c in 'O.' for c in text)

def translate_to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            braille_output.append(BRAILLE_CAPITAL)
            char = char.lower()
        
        if char.isdigit() and not number_mode:
            braille_output.append(BRAILLE_NUMBER)
            number_mode = True
        
        if char == ' ':
            number_mode = False
        
        braille_output.append(ALPHANUMERIC_TO_BRAILLE.get(char, '......'))
    
    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    capital_flag = False
    number_flag = False
    
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    
    for braille_char in braille_chars:
        if braille_char == BRAILLE_CAPITAL:
            capital_flag = True
            continue
        if braille_char == BRAILLE_NUMBER:
            number_flag = True
            continue
        
        if braille_char == '......':
            english_output.append(' ')
            number_flag = False
            continue
        
        if number_flag:
            english_output.append(BRAILLE_TO_NUMBER.get(braille_char, ' '))
        else:
            char = BRAILLE_TO_ALPHABET.get(braille_char, ' ')
            if capital_flag:
                english_output.append(char.upper())
                capital_flag = False
            else:
                english_output.append(char)
    
    return ''.join(english_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text or braille>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        result = translate_to_english(input_text)
    else:
        result = translate_to_braille(input_text)
    
    print(result)

if __name__ == "__main__":
    main()