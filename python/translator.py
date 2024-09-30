import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

NUMBERS_TO_BRAILLE = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
}

BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            result.append(NUMBERS_TO_BRAILLE[char])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
                char = char.lower()
            result.append(ENGLISH_TO_BRAILLE[char])
    return ''.join(result)

def braille_to_english(text):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(text):
        symbol = text[i:i+6]
        if symbol == ENGLISH_TO_BRAILLE['capital']:
            capitalize_next = True
        elif symbol == ENGLISH_TO_BRAILLE['number']:
            number_mode = True
        else:
            if number_mode and symbol in BRAILLE_TO_NUMBERS:
                char = BRAILLE_TO_NUMBERS[symbol]
            else:
                char = BRAILLE_TO_ENGLISH[symbol]
                number_mode = False
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            result.append(char)
        i += 6
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    
    if not input_text:
        input_text = sys.stdin.read().strip()
    
    output_text = translate(input_text)
    print(output_text)
