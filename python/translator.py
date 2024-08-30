import sys

braille_dict = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    
    # Numbers 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    
    # Special SymbOls
    'capital': '.....O',  # next letter is capitalized
    'number': '.O.OOO',  # numbers follow
    'decimal': '.O...O',
    ' ': '......',  
    '.': '..OO.O',  
    ',': '..O...',  
    '?': '..O.OO',  
    '!': '..OOO.',  
    ':': '..OO..',  
    ';': '..O.O.',  
    '-': '....OO',  
    '/': '.O..O.',  
    '<': '.OO..O',  
    '>': 'O..OO.',  
    '(': 'O.O..O',  
    ')': '.O.OO.'   
}

# Reverse mapping for non-conflicting symbols and letters
reverse_braille_dict = {v: k for k, v in braille_dict.items() if k not in 'abcdefghij0123456789'}

# hardcoding clashing chars
reverse_letter_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}


reverse_number_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


def translate_to_braille(text):
    res = ""
    num_mode = False
    for t in text:
        if t.isupper():
            res += braille_dict['capital']
            t = t.lower() # convert to lowercase

        if t.isdigit() and not num_mode:
            num_mode = True
            res += braille_dict['number']

        if t == ' ':
            num_mode = False

        res += braille_dict.get(t, '')

    return res

def translate_to_english(braille_text):
    res = ""
    i = 0
    num_mode = False
    cap_mode = False

    while i < len(braille_text):
        cur = braille_text[i:i+6] # current 6 character substring

        if cur == braille_dict['capital']:
            cap_mode = True
            i += 6
            continue
        elif cur == braille_dict['number']:
            num_mode = True
            i += 6
            continue
        elif cur == braille_dict[' ']:
            res += ' '
            num_mode = False  # Reset number mode after a space
            i += 6
            continue

        # if number mode, read the mappings from the digit dictionary, else from the others
        if num_mode:
            char = reverse_number_dict.get(cur, '')
        else:
            char = reverse_letter_dict.get(cur, '') or reverse_braille_dict.get(cur, '')

        if cap_mode:
            char = char.upper()
            cap_mode = False

        res += char
        i += 6

    return res

def detect_and_translate(input_text):
    if set(input_text) <= {'.', 'O'}:
        return translate_to_english(input_text)
    else:
        return translate_to_braille(input_text)

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    result = detect_and_translate(input_text)
    print(result)
