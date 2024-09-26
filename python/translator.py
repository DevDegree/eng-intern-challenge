import sys

ENGLISH_TO_BRAILLE = {
    ' ': '......',
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
    'capital': '.....O',
    'number': '.O.OOO',
    '.': '.O...O',
}

NUMBERS_TO_BRAILLE = {
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
}


BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

def get_input_string():
    return ' '.join(sys.argv[1:]).strip()

def is_braille(s):
    valid_chars = {'O', '.', ' '}
    return all(char in valid_chars for char in s) and (len(s) % 6 == 0)

def translate_to_braille(s):
    result = []
    number_mode = False

    for char in s:
        if char == ' ':
            result.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            braille_char = NUMBERS_TO_BRAILLE[char]
            result.append(braille_char)
        elif char == '.':
            result.append(ENGLISH_TO_BRAILLE['.'])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
            braille_char = ENGLISH_TO_BRAILLE[char.lower()]
            result.append(braille_char)
        else:
            pass

    return ''.join(result)

def translate_to_english(s):
    result = []
    index = 0
    s = s.replace(' ', '')
    length = len(s)
    number_mode = False
    capital_next = False

    while index <= length - 6:
        braille_char = s[index:index+6]

        if braille_char == ENGLISH_TO_BRAILLE['number']:
            number_mode = True
            index += 6
            continue
        elif braille_char == ENGLISH_TO_BRAILLE['capital']:
            capital_next = True
            index += 6
            continue
        elif braille_char == ENGLISH_TO_BRAILLE[' ']:
            result.append(' ')
            number_mode = False
            capital_next = False
            index += 6
            continue
        elif braille_char == ENGLISH_TO_BRAILLE['.']:
            result.append('.')
            index += 6
            continue

        if number_mode:
            char = BRAILLE_NUMBERS.get(braille_char, '')
            if char:
                result.append(char)
            else:
                number_mode = False
                continue
        else:
            char = BRAILLE_TO_ENGLISH.get(braille_char, '')
            if char:
                if capital_next:
                    result.append(char.upper())
                    capital_next = False
                else:
                    result.append(char)
            else:
                pass

        index += 6

    return ''.join(result)

def main():
    input_str = get_input_string()
    if is_braille(input_str):
        # print('Braille ')
        output = translate_to_english(input_str)
    else:
        # print('English ')
        output = translate_to_braille(input_str)
    print(output)

if __name__ == "__main__":
    main()
