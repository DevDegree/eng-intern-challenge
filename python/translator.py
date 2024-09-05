import sys

# For case .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.. output should be Abc 234 instead of Abc 123

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number' : '.O.OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..'
}


BRAILLE_TO_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

def to_braille(text):
    braille = ''
    on_number = False

    for c in text:
        if c.isupper():
            braille += ENGLISH_TO_BRAILLE['capital']
            braille += ENGLISH_TO_BRAILLE.get(c.lower(), '')
            on_number = False
        elif c.isdigit():
            if not on_number:
                braille += ENGLISH_TO_BRAILLE['number']
                on_number = True
            braille += NUMBER_TO_BRAILLE.get(c, '')
        else:
            braille += ENGLISH_TO_BRAILLE.get(c, '')
            on_number = False

    return braille

def from_braille(braille):
    text = ''
    on_number = False
    i = 0

    while i < len(braille):
        c = braille[i: i + 6]

        if c == ENGLISH_TO_BRAILLE['capital']:
            i += 6
            text += BRAILLE_TO_LETTER.get(braille[i: i + 6], '').upper()
            on_number = False
        elif c == ENGLISH_TO_BRAILLE['number']:
            i += 6
            text += BRAILLE_TO_NUMBER.get(braille[i: i + 6], '')
            on_number = True
        elif on_number:
            text += BRAILLE_TO_NUMBER.get(c, '')
        else:
            text += BRAILLE_TO_LETTER.get(c, '')
            on_number = False

        i += 6
        
    return text

if __name__ == '__main__':
    input_text = sys.argv[1:]

    is_braille = (len(input_text) == 1 and len(input_text[0]) % 6 == 0 and all([x in 'O.' for x in input_text[0]]))

    if is_braille:
        print(from_braille(input_text[0]))
    else:
        print(to_braille(' '.join(input_text)))

