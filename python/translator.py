
import sys

# Braille dictionary from picture.
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..OO..', '!': '..O.O.', ':': '..OO..',
    '-': '..O..O', '/': '.O..O.', '(': '.O.O..', ')': '.O.OO.'
}

# Reverse dictionary (Braille --> English).
reverse_braille_dict = {v: k for k, v in braille_dict.items()}


CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.O..'

def english_to_braille(text):
    braille_translation = []
    for char in text:
        if char.isupper():
            braille_translation.append(CAPITAL_MARKER)  #capital marker before upper case letters
            braille_translation.append(braille_dict[char.lower()])
        elif char.isdigit():
            braille_translation.append(NUMBER_MARKER)  #number marker before digits
            braille_translation.append(braille_dict[char])
        else:
            braille_translation.append(braille_dict[char])
    return ''.join(braille_translation)

def braille_to_english(braille_text):
    english_translation = []
    i = 0
    length = len(braille_text)
    capital = False
    number = False
    
    while i < length:
        braille_char = braille_text[i:i+6]
        
        if braille_char == CAPITAL_MARKER:
            capital = True
            i += 6
            continue
        elif braille_char == NUMBER_MARKER:
            number = True
            i += 6
            continue
        else:
            if number and braille_char in reverse_braille_dict:
                english_translation.append(reverse_braille_dict[braille_char])
            elif capital and braille_char in reverse_braille_dict:
                english_translation.append(reverse_braille_dict[braille_char].upper())
            else:
                english_translation.append(reverse_braille_dict.get(braille_char, ''))
            
            # Reset flags
            capital = False
            number = False
        
        i += 6
    return ''.join(english_translation)

def main():
    input_text = ' '.join(sys.argv[1:])    
    if 'O' in input_text or '.' in input_text:
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
