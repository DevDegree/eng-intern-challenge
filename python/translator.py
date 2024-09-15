import sys

# Braille dictionary for letters, numbers, and punctuation
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.'
}

braille_to_char = {v: k for k, v in braille_dict.items()}

def is_braille(input_string):
    return all(c in {'O', '.', ' '} for c in input_string)

def braille_to_english(input_braille):
    input_braille = ''.join(input_braille.split())
    symbols = [input_braille[i:i+6] for i in range(0, len(input_braille), 6)]

    output = []
    capital_next = False
    number_mode = False

    for symbol in symbols:
        if symbol == braille_dict[' ']:
            output.append(' ')
            capital_next = number_mode = False
        elif symbol == braille_dict['cap']:
            capital_next = True
        elif symbol == braille_dict['num']:
            number_mode = True
        else:
            char = braille_to_char.get(symbol)
            if char:
                if number_mode and char.isdigit():
                    output.append(char)
                elif capital_next:
                    output.append(char.upper())
                    capital_next = False
                else:
                    output.append(char)
                number_mode = False
    return ''.join(output)

def english_to_braille(input_text):
    output = []
    number_mode = False

    for char in input_text:
        if char == ' ':
            output.append(braille_dict[' '])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                output.append(braille_dict['num'])
                number_mode = True
            output.append(braille_dict[char])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                output.append(braille_dict['cap'])
                char = char.lower()
            braille_char = braille_dict.get(char)
            if braille_char:
                output.append(braille_char)

    return ''.join(output)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
