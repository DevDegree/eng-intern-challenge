BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

BRAILLE_TO_TEXT = {value: key for key, value in BRAILLE_ALPHABET.items()}

def translate_to_braille(text):
    braille_translation = []
    is_number = False
    for char in text:
        if char.isupper():
            braille_translation.append(BRAILLE_ALPHABET['capital'])
            char = char.lower()
        if char.isdigit():
            if not is_number:
                braille_translation.append(BRAILLE_ALPHABET['number'])
                is_number = True
        else:
            is_number = False
        braille_translation.append(BRAILLE_ALPHABET[char])
    return ''.join(braille_translation)

def translate_to_english(braille):
    english_translation = []
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        i += 6
        if symbol == BRAILLE_ALPHABET['capital']:
            symbol = braille[i:i+6]
            english_translation.append(BRAILLE_TO_TEXT[symbol].upper())
            i += 6
        elif symbol == BRAILLE_ALPHABET['number']:
            continue
        else:
            char = BRAILLE_TO_TEXT[symbol]
            english_translation.append(char)
    return ''.join(english_translation)

def main():
    import sys
    input_text = ' '.join(sys.argv[1:])
    if input_text.startswith(('O', '.')):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
