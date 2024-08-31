import sys

alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x':   'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

symbols = {
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
    '(': '.O.OO.',
    ' ': '......'
}

modfiers = {
    'capital': '.....O',
    '.': '.O...O',
    '#': '.O.OOO'
}


def translate_from(text):
    for letter in text:
        if letter != 'O' and letter != '.':
            return False
    return True


def find_key(dict, tar_value):
    for key, value in dict.items():
        if value == tar_value:
            return key
    return None


def convert_string(string):
    is_braille = translate_from(string)
    is_number = False
    is_capital = False
    result = []

    # If converting english to braille
    if is_braille is False:
        for char in string:
            if char == ' ':
                is_number = False
                result.append(symbols[' '])
                continue
            elif char.isupper():
                result.append(modfiers['capital'] + alphabet[char.lower()])
            elif char.isnumeric():
                if is_number is False:
                    result.append(modfiers['#'] + numbers[char])
                    is_number = True
                else:
                    result.append(numbers[char])
            else:
                if char in symbols:
                    result.append(symbols[char])
                elif char in alphabet:
                    result.append(alphabet[char])

    # If converting braille to english
    if is_braille is True:
        for i in range(0, len(string), 6):
            block = string[i:i+6]
            modifier = find_key(modfiers, block)

            # handle modifiers
            if modifier == 'capital':
                is_capital = True
                continue
            elif modifier == '#':
                is_number = True
                continue
            elif modifier == '.':
                result.append('.')
            if block == '......':
                is_number = False
                result.append(' ')
                continue
            if is_capital:
                result.append(find_key(alphabet, block).upper())
                is_capital = False
                continue
            if is_number:
                result.append(find_key(numbers, block))
                continue
            if find_key(alphabet, block) is None:
                result.append(find_key(symbols, block))
            else:
                result.append(find_key(alphabet, block))
    return ''.join(result)


if __name__ == '__main__':
        s = " ".join(sys.argv[1:])
        print(convert_string(s))
