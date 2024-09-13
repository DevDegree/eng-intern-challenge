
import sys

main_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO'
}

digits_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

reverse_main_dict = {v: k for k, v in main_dict.items()}
reverse_digits_dict = {v: k for k, v in digits_dict.items()}


def fn_is_braille(text):
    return all(c in 'O.' for c in text)


def fn_braille_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == main_dict['cap']:
            next_char = braille[i+6:i+12]
            result.append(reverse_main_dict[next_char].upper())
            i += 12
        elif braille_char == main_dict['num']:
            number_mode = True
            i += 6
        elif braille_char in reverse_digits_dict if number_mode else reverse_main_dict:
            if number_mode:
                result.append(reverse_digits_dict[braille_char])
            else:
                result.append(reverse_main_dict[braille_char])
            i += 6
        elif braille_char == main_dict[' ']:
            result.append(' ')
            number_mode = False
            i += 6
        else:
            i += 6  # Skip unrecognized patterns
    return ''.join(result)


def fn_english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(main_dict['num'])
                number_mode = True
            result.append(digits_dict[char])
        elif char.isalpha():
            if char.isupper():
                result.append(main_dict['cap'])
            result.append(main_dict[char.lower()])
            number_mode = False
        elif char == ' ':
            result.append(main_dict[' '])
            number_mode = False
    return ''.join(result)


# Main function to handle input and perform translation
def main():
    input_text = ' '.join(sys.argv[1:])

    if fn_is_braille(input_text):
        print(fn_braille_to_english(input_text))
    else:
        print(fn_english_to_braille(input_text))


if __name__ == "__main__":
    main()
