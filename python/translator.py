braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......'
}

braille_special = {
    'capital': '.....O',
    'number': '.O.OOO'
}

reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_special = {v: k for v, k in braille_special.items()}

def is_braille(input_string):
    return all(c in 'O. ' for c in input_string)

def translate_to_braille(text):
    braille_translation = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille_translation.append(braille_special['capital'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                braille_translation.append(braille_special['number'])
                number_mode = True
            braille_translation.append(braille_alphabet[char])
        elif char.isalpha():
            number_mode = False
            braille_translation.append(braille_alphabet.get(char, '......'))
        else:
            braille_translation.append(braille_alphabet.get(char, '......'))

    return ''.join(braille_translation)

def translate_to_english(braille_text):
    english_translation = []
    i = 0
    number_mode = False
    capitalize_next = False

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]

        if braille_char == braille_special['capital']:
            capitalize_next = True
            i += 6
            continue

        if braille_char == braille_special['number']:
            number_mode = True
            i += 6
            continue

        letter = reverse_braille_alphabet.get(braille_char, ' ')

        if capitalize_next:
            letter = letter.upper()
            capitalize_next = False

        if number_mode and letter.isdigit():
            english_translation.append(letter)
        else:
            english_translation.append(letter)

        i += 6
        number_mode = False

    return ''.join(english_translation)

def main(input_string):
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        main(input_string)
    else:
        print("Please provide a string to translate.")
