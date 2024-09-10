import sys

braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

reverse_braille = {value: key for key,value in braille.items()}

def english_to_braille(english):
    output = []
    num = False
    for char in english:
        if char.isdigit():
            if not num:
                num = True
                output.append(braille['num'])
            output.append(braille[char])
        elif char.isalpha():
            if char.isupper():
                output.append(braille['cap'])
                char = char.lower()
            output.append(braille[char])
        elif char == ' ':
            num = False
            output.append(braille[' '])
    return ''.join(output)

print(english_to_braille("Hello world"))