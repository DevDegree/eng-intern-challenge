braille_alphabet = {
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
    ' ': '......'
}

braille_numbers = {
    '0': '.OOOO.',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

capital_prefix = '.....O'
number_prefix = '.O.OOO'

# Reverse mappings
eng_alphabet = {v: k for k, v in braille_alphabet.items()}
eng_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

def eng_to_braille(input_str):
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit():
            if not number_mode:
                result.append(number_prefix)
                number_mode = True
            result.append(braille_numbers[char])
        else:
            if char.isalpha():
                if char.isupper():
                    result.append(capital_prefix)
                    char = char.lower()
                result.append(braille_alphabet[char])
            elif char.isspace():
                result.append(braille_alphabet[char])
            number_mode = False
    return ''.join(result)

def braille_to_eng(input_str):
    result = []
    i = 0
    length = len(input_str)
    capital_next = False
    number_next = False

    while i < length:
        braille_char = input_str[i:i+6]

        if braille_char == capital_prefix:
            capital_next = True
            i += 6
            continue
        elif braille_char == number_prefix:
            number_next = True
            i += 6
            continue
        elif number_next:
            result.append(eng_numbers[braille_char])
            number_next = False
        else:
            char = eng_alphabet[braille_char]
            if capital_next:
                char = char.upper()
                capital_next = False
            result.append(char)

        i += 6

    return ''.join(result)

def translate(string):

    if is_braille(input_str):
        print(braille_to_eng(input_str))
    else:
        print(eng_to_braille(input_str))

if __name__ == "__main__":

    input_str = ' '.join(sys.argv[1:])

    translate(input_str)