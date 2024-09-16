import sys

# Mappings for letters, numbers, and special symbols to braille
TEXT_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', ',': '.O....', ';': '.OO...', ':': '.O.O..',
    '.': '.O.OO.', '!': '.OO.O.', '?': '.OO..O', '-': '..O.O.', '/': '.O.O..',
    '(': '.O.O.O', ')': 'O..O.O', '<': 'OO...O', '>': '..OO.O',
    'CAP_NEXT': '.....O', 'NUM_NEXT': '.O.OOO'
}

DIGIT_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mapping for braille to text
BRAILLE_TO_TEXT = {v: k for k, v in TEXT_TO_BRAILLE.items()}
BRAILLE_TO_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}


def decode_braille(braille):
    result = []
    index = 0
    uppercase_flag = False
    numeric_flag = False

    while index < len(braille):
        block = braille[index:index+6]
        if block == TEXT_TO_BRAILLE['CAP_NEXT']:
            uppercase_flag = True
        elif block == TEXT_TO_BRAILLE['NUM_NEXT']:
            numeric_flag = True
        elif block in BRAILLE_TO_TEXT:
            char = BRAILLE_TO_TEXT[block]
            if numeric_flag and block in BRAILLE_TO_DIGIT:
                result.append(BRAILLE_TO_DIGIT[block])
            else:
                if uppercase_flag:
                    char = char.upper()
                    uppercase_flag = False
                result.append(char)
            if char == ' ':
                numeric_flag = False
        index += 6

    return ''.join(result)


def encode_to_braille(text):
    braille_output = []
    in_number_mode = False

    for character in text:
        if character.isupper():
            braille_output.append(TEXT_TO_BRAILLE['CAP_NEXT'])
            character = character.lower()

        if character.isdigit():
            if not in_number_mode:
                braille_output.append(TEXT_TO_BRAILLE['NUM_NEXT'])
                in_number_mode = True
            braille_output.append(DIGIT_TO_BRAILLE[character])
        else:
            braille_output.append(TEXT_TO_BRAILLE[character])
            if character == ' ':
                in_number_mode = False

    return ''.join(braille_output)


def check_if_braille(input_string):
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0


def convert(input_data):
    if check_if_braille(input_data):
        return decode_braille(input_data)
    else:
        return encode_to_braille(input_data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
        print(convert(user_input))
    else:
        print("Please provide input text.")
