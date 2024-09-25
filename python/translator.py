import sys

braille_dict_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
}

braille_dict_digits = {}
for digit_char, letter_char in zip('1234567890', 'abcdefghij'):
    braille_dict_digits[digit_char] = braille_dict_letters[letter_char]

braille_dict_full = braille_dict_letters.copy()
braille_dict_full.update(braille_dict_digits)

braille_to_letter = {v: k for k, v in braille_dict_letters.items() if k in 'abcdefghijklmnopqrstuvwxyz'}
braille_to_digit = {v: k for k, v in braille_dict_digits.items()}


def is_braille(input_str):
    for char in input_str:
        if char not in ['O', '.', ' ']:
            return False
    return True

def translate_to_braille(english_input):
    result = []
    number_flag = False

    for char in english_input:
        if char.isdigit():
            if not number_flag:
                result.append(braille_dict_letters['number'])
                number_flag = True
            result.append(braille_dict_digits[char])
        else:
            if number_flag:
                number_flag = False
            if char == ' ':
                result.append(braille_dict_letters[char])
            elif char.isupper():
                result.append(braille_dict_letters['capital'])
                result.append(braille_dict_letters[char.lower()])
            else:
                result.append(braille_dict_letters[char])
    return ''.join(result)

def translate_to_english(braille_input):
    result = []
    braille_chunks = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]
    capital_flag = False
    number_flag = False

    for braille_chunk in braille_chunks:
        if braille_chunk == braille_dict_letters['capital']:
            capital_flag = True
        elif braille_chunk == braille_dict_letters['number']:
            number_flag = True
        elif braille_chunk == braille_dict_letters[' ']:
            result.append(' ')
            number_flag = False
            capital_flag = False
        else:
            if number_flag:
                digit = braille_to_digit.get(braille_chunk)
                if digit:
                    result.append(digit)
            else:
                char = braille_to_letter.get(braille_chunk)
                if char:
                    if capital_flag:
                        result.append(char.upper())
                        capital_flag = False
                    else:
                        result.append(char)
    return ''.join(result)

def braille_translator(input_string):
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)


if __name__ == "__main__":
    input_args = sys.argv[1:]
    input_string = ' '.join(input_args)
    print(braille_translator(input_string))