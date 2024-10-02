import sys

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

number_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
}

braille_to_english = {v: k for k, v in english_to_braille.items()}

braille_to_number = {v: k for k, v in number_to_braille.items()}

def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number'])
                number_mode = True
            result.append(number_to_braille[char])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(english_to_braille['capital'])
                char = char.lower()
            result.append(english_to_braille[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == english_to_braille['capital']:
            capitalize_next = True
        elif symbol == english_to_braille['number']:
            number_mode = True
        else:
            if number_mode and symbol in braille_to_number:
                char = braille_to_number[symbol]
                result.append(char)
            else:
                char = braille_to_english[symbol]
                if number_mode:
                    number_mode = False
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
        i += 6
    return ''.join(result)


def is_braille(text):
    return set(text) <= set('O.') and len(text) % 6 == 0

def main(text):
    if is_braille(text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))

if __name__ == '__main__':
    text = ' '.join(sys.argv[1:])
    main(text)