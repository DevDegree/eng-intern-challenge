import sys

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
}

english_to_braille_numbers = {
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...',
}

braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english_numbers = {v: k for k,
                              v in english_to_braille_numbers.items()}


def is_braille(input_string):
    return all(c in 'O.' for c in input_string)


def translate_to_braille(text):
    braille_output = []
    num_mode = False

    for char in text:
        if char.isdigit():
            if not num_mode:
                braille_output.append(english_to_braille['num'])
                num_mode = True
            braille_output.append(english_to_braille_numbers[char])
        else:
            num_mode = False
            if char.isupper():
                braille_output.append(english_to_braille['cap'])
                char = char.lower()

            braille_output.append(english_to_braille[char])

    return ''.join(braille_output)


def translate_to_english(braille_text):
    english_output = []
    # Extract the 6 characters of braille which make up a english symbol
    braille_characters = [braille_text[i:i+6]
                          for i in range(0, len(braille_text), 6)]

    cap_next = False
    num_mode = False

    for braille_char in braille_characters:
        if braille_char == english_to_braille['cap']:
            cap_next = True
            continue
        elif braille_char == english_to_braille['num']:
            num_mode = True
            continue

        if num_mode:
            char = braille_to_english_numbers.get(braille_char, '')
            if char == ' ':
                num_mode = False
        else:
            char = braille_to_english.get(braille_char, '')
        if cap_next:
            char = char.upper()
            cap_next = False

        english_output.append(char)

    return ''.join(english_output)


def main():
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))


if __name__ == "__main__":
    main()
