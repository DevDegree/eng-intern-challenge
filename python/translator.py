import sys

# Mapping English to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Mapping Braille to English
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english['.....O'] = 'Capital'
braille_to_english['.O.OOO'] = 'Number'

def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(english_to_braille['Capital'])
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            result.append(english_to_braille['Number'])
            result.append(english_to_braille[char])
        else:
            result.append(english_to_braille[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        pattern = braille[i:i+6]
        if pattern == '......':
            result.append(' ')
        elif pattern in braille_to_english:
            translation = braille_to_english[pattern]
            if translation == 'Capital':
                i += 6
                pattern = braille[i:i+6]
                result.append(braille_to_english[pattern].upper())
            elif translation == 'Number':
                i += 6
                pattern = braille[i:i+6]
                result.append(braille_to_english[pattern])
            else:
                result.append(translation)
        i += 6
    return ''.join(result)

def solve():
    if len(sys.argv) != 2:
        print("Please provide a single argument to translate.")
        return
    
    input_string = sys.argv[1]

    if all(c in 'O.' for c in input_string):
        # Input is Braille
        translated = translate_to_english(input_string)
    else:
        # Input is English
        translated = translate_to_braille(input_string)
    
    print(translated)

if name == 'main':
    solve()
