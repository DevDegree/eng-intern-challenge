import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', "'": '....O.'
}

# Special symbols
capital_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'

def english_to_braille(text):
    braille_output = []
    in_number_mode = False

    for char in text:
        if char.isdigit():
            if not in_number_mode:
                braille_output.append(number_follows)
                in_number_mode = True
            braille_output.append(braille_dict[char])
        elif char == '.':
            braille_output.append(decimal_follows)
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            in_number_mode = False
            if char.isupper():
                braille_output.append(capital_follows)
            braille_output.append(braille_dict[char.lower()])
        elif char == ' ':
            in_number_mode = False
            braille_output.append('......')
        else:
            braille_output.append(braille_dict.get(char, '......'))
    return ''.join(braille_output)

def braille_to_english(braille):
    english_output = []
    i = 0
    in_number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == number_follows:
            in_number_mode = True
            i += 6
            continue
        elif symbol == decimal_follows:
            english_output.append('.')
            i += 6
            continue
        elif symbol == capital_follows:
            i += 6
            next_symbol = braille[i:i+6]
            letter = list(braille_dict.keys())[list(braille_dict.values()).index(next_symbol)].upper()
            english_output.append(letter)
        elif symbol == '......':
            english_output.append(' ')
            in_number_mode = False
        else:
            if in_number_mode:
                number_index = list(braille_dict.values()).index(symbol)
                if 0 <= number_index <= 9:
                    english_output.append(str(number_index + 1))
            else:
                english_output.append(list(braille_dict.keys())[list(braille_dict.values()).index(symbol)])
        i += 6

    return ''.join(english_output)

def detect_input_type(text):
    return all(c in 'O.' for c in text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    if detect_input_type(input_text):
        translation = braille_to_english(input_text)
    else:
        translation = english_to_braille(input_text)
    
    print(translation)

