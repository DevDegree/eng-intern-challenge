import sys

BRAILLE_ALPHABET = {
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
	' ': '......',
    'cap': '.....O',
    'num': '.O.OOO',
}

BRAILLE_NUMBERS = {
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
}

def braille_to_english(braille):
    translation = ''
    is_cap = False
    is_num = False
    reverse_alphabet = {v: k for k, v in BRAILLE_ALPHABET.items()}
    reverse_nums = {v: k for k, v in BRAILLE_NUMBERS.items()}

    for i in range(0, len(braille), 6):
        sym = braille[i:i+6]

        if sym == BRAILLE_ALPHABET['cap']:
            is_cap = True
        elif sym == BRAILLE_ALPHABET['num']:
            is_num = True
        else:
            if sym == BRAILLE_ALPHABET[' ']:
                is_num = False
            if is_num:
                char = reverse_nums.get(sym, '')
            elif is_cap:
                char = reverse_alphabet.get(sym, '')
                char = char.upper()
                is_cap = False
            else:
                char = reverse_alphabet.get(sym, '')
            
            translation += char
    
    return translation

def english_to_braille(text):
    translation = ''
    is_num = False

    for char in text:
        if char.isdigit():
            if is_num:
                translation += BRAILLE_NUMBERS[char]
            else:
                is_num = True
                translation += BRAILLE_ALPHABET['num'] + BRAILLE_NUMBERS[char]
        else:
            if char.isupper():
                translation += BRAILLE_ALPHABET['cap']
                char = char.lower()
            if char == ' ':
                is_num = False
            translation += BRAILLE_ALPHABET[char]
    
    return translation

if __name__ == "__main__":
    text = ' '.join(sys.argv[1:])
    isBraille = all(c in 'O.' for c in text) and len(text) % 6 == 0

    if isBraille:
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))
