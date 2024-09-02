import sys

# Dictionary mapping from English characters to Braille
ALPHA_TO_BRAILLE = {
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
    'z': 'O..OOO'
}

# Dictionary mapping from numbers to Braille
NUM_TO_BRAILLE = {
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

# Dictionary mapping from instructions to Braille
INSTRUCT_TO_BRAILLE = {
    'CAPITAL': '.....O',
    'DECIMAL': '.O...O',
    'NUMBER': '.O.OOO'
}

# Dictionary mapping from symbol to Braille
SYMBOL_TO_BRAILLE = {
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
    ')': '.O.OO.',
    ' ': '......'
}

# Dictionary mappings from Braille to English characters, numbers, instructions, and symbols
BRAILLE_TO_ALPHA = dict(map(reversed, ALPHA_TO_BRAILLE.items()))
BRAILLE_TO_NUM = dict(map(reversed, NUM_TO_BRAILLE.items()))
BRAILLE_TO_INSTRUCT = dict(map(reversed, INSTRUCT_TO_BRAILLE.items()))
BRAILLE_TO_SYMBOL = dict(map(reversed, SYMBOL_TO_BRAILLE.items()))

# Check if text is Braille or English
def is_braille(text):
    return all(c in 'O.' for c in text)

# Translate English text to Braille
def english_to_braille(english):
    braille = []
    is_number = False

    for char in english:
        if char.isupper():
            braille.append(INSTRUCT_TO_BRAILLE['CAPITAL'])
            braille.append(ALPHA_TO_BRAILLE[char.lower()])
        elif char.isdigit():
            if not is_number:
                braille.append(INSTRUCT_TO_BRAILLE['NUMBER'])
                is_number = True
            braille.append(NUM_TO_BRAILLE[char])
        elif char in ALPHA_TO_BRAILLE:
            braille.append(ALPHA_TO_BRAILLE[char])
        elif char in SYMBOL_TO_BRAILLE:
            braille.append(SYMBOL_TO_BRAILLE[char])
            if char == ' ':
                is_number = False
    return ''.join(braille)

# Translate Braille to English
def braille_to_english(braille):
    result = []
    is_number = False
    i = 0

    if len(braille) % 6 != 0:
        return ''

    while i < len(braille):
        char = braille[i:i+6]
        
        if char in BRAILLE_TO_INSTRUCT:
            if BRAILLE_TO_INSTRUCT[char] == 'CAPITAL':
                next_char = braille[i+6:i+12]
                result.append(BRAILLE_TO_ALPHA.get(next_char, '').upper())
                i += 6
            elif BRAILLE_TO_INSTRUCT[char] == 'NUMBER':
                is_number = True
        elif char in BRAILLE_TO_ALPHA and not is_number:
            result.append(BRAILLE_TO_ALPHA[char])
        elif char in BRAILLE_TO_NUM and is_number:
            result.append(BRAILLE_TO_NUM[char])
        elif char in BRAILLE_TO_SYMBOL:
            result.append(BRAILLE_TO_SYMBOL[char])
            if char == BRAILLE_TO_SYMBOL[' ']:
                is_number = False
        i += 6

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        return
    
    input_text = sys.argv[1]
    translated_text = ''

    if is_braille(input_text):
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)
        
    print(translated_text)

if __name__ == "__main__":
    main()
