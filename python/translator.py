import sys

# Define mappings from english to Braille
BRAILLE_DICT =  {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O',
    'number': '.O.OOO'
}

# Define mappings from Braille to english
REVERSE_BRAILLE_DICT_NUMBERS = {v: k for k, v in BRAILLE_DICT.items() if k.isdigit()}
REVERSE_BRAILLE_DICT_LETTERS = {v: k for k, v in BRAILLE_DICT.items() if k.isalpha()}

def braille_to_english(braille):
    """Translate Braille to English"""
    result = []
    is_number = False
    i = 0
    
    while i < len(braille):
        braille_char = braille[i:i+6]
        
        if braille_char == '.....O':  # Capitalize next letter
            i += 6
            braille_char = braille[i:i+6]
            result.append(REVERSE_BRAILLE_DICT_LETTERS[braille_char].upper())
        elif braille_char == '.O.OOO':  # Start of numbers
            is_number = True
        elif braille_char == '......':  # Space character
            result.append(' ')
            is_number = False # Space character ends number
        else:
            if is_number:
                translated_char = REVERSE_BRAILLE_DICT_NUMBERS[braille_char]
            else:
                translated_char = REVERSE_BRAILLE_DICT_LETTERS[braille_char]
            result.append(translated_char if not is_number else translated_char)
        
        i += 6
    
    return ''.join(result)

def english_to_braille(english):
    """Translate English to Braille"""
    result = []
    is_number = False
    for char in english:
        if char.isupper(): # Capital symbol followed by latter
            result.append(BRAILLE_DICT['capital'])
            result.append(BRAILLE_DICT[char.lower()])
        elif char.isdigit(): # Number symbol followed by number
            if not is_number: # Start of number
                result.append(BRAILLE_DICT['number'])
                is_number = True
            result.append(BRAILLE_DICT[char])
        else:
            result.append(BRAILLE_DICT[char])
            if char == ' ': # Space character ends number
                is_number = False
    return ''.join(result)

text = " ".join(sys.argv[1:])

for c in text:
    if c not in {'.', 'O'}: # Detect if english or braille
        print(english_to_braille(text))
        exit()
print(braille_to_english(text))
