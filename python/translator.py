import sys

braille_map = {
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

braille_special = {
    'capital_marker': '.....O',
    'decimal_marker': '.O...O',
    'number_marker': '.O.OOO'
}


def text_to_braille(input_text):
    braille_output = []
    in_number_mode = False
    for char in input_text:
        if char == ' ':
            in_number_mode = False
        if char.isdigit() and not in_number_mode:
            braille_output.append(braille_special['number_marker'])
            in_number_mode = True
        if char.isupper():
            braille_output.append(braille_special['capital_marker'])
            char = char.lower()
        braille_output.append(braille_map[char])
    return ''.join(braille_output)


def braille_to_text(input_braille):
    text_output = []
    in_capital_mode = False
    in_number_mode = False
    for i in range(len(input_braille) // 6):
        current_symbol = input_braille[i * 6:(i + 1) * 6]
        if current_symbol == braille_special['capital_marker']:
            in_capital_mode = True
        elif current_symbol == braille_special['number_marker']:
            in_number_mode = True
        else:
            for char, braille_code in braille_map.items():
                if braille_code == current_symbol:
                    if char == ' ':
                        in_number_mode = False
                        text_output.append(' ')
                        break
                    if in_number_mode and char.isdigit():
                        text_output.append(char)
                        break
                    elif not in_number_mode and in_capital_mode:
                        text_output.append(char.upper())
                        in_capital_mode = False
                        break
                    elif not in_number_mode:
                        text_output.append(char)
                        break
    return ''.join(text_output)


def main():
    input_text = ' '.join(sys.argv[1:])
    if len(input_text) % 6 > 0:
        print(text_to_braille(input_text))
    else:
        for char in input_text:
            if char != '.' and char != 'O':
                print(text_to_braille(input_text))
                return
        print(braille_to_text(input_text))


if __name__ == '__main__':
    main()
