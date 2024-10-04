import sys

# as per given figure
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',  # space
    'cap': '.....O',  # caps
    'num': '.O.OOO',   # number
    'dec': '.O....O'   # decimal
}

# as per given figure
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# using spread syntax to combine the dictionaries
english_to_braille = {**braille_alphabet, **braille_numbers}

# divide into text and numbers for lookup
braille_to_english = {"text": {v: k for k, v in braille_alphabet.items(
)}, "numbers": {v: k for k, v in braille_numbers.items()}}


def translate_to_braille(text):
    braille_output = []
    is_number_mode = False

    for char in text:
        if char.isupper():
            braille_output.append(braille_alphabet['cap'])
            char = char.lower()

        if char.isdigit():
            if not is_number_mode:
                braille_output.append(braille_alphabet['num'])
                is_number_mode = True
            braille_output.append(braille_numbers[char])

        elif char == ' ':
            braille_output.append(braille_alphabet[' '])
            is_number_mode = False

        else:
            braille_output.append(english_to_braille[char])
            is_number_mode = False

    return ''.join(braille_output)


def translate_to_english(braille):
    english_output = []
    i = 0
    is_number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_alphabet['cap']:
            next_symbol = braille[i+6:i+12]
            letter = braille_to_english["text"][next_symbol].upper()
            english_output.append(letter)
            i += 12
        elif symbol == braille_alphabet['num']:
            is_number_mode = True
            i += 6
        elif symbol == braille_alphabet['dec']:
            english_output.append('.')
            i += 6
        elif symbol == braille_alphabet[' ']:
            is_number_mode = False
            english_output.append(' ')
            i += 6
        else:
            if is_number_mode:
                char = braille_to_english["numbers"][symbol]
                english_output.append(char)
            else:
                char = braille_to_english["text"][symbol]
                english_output.append(char)
            i += 6
    return ''.join(english_output)


if len(sys.argv) < 2:
    print("Enter input text to translate")

else:
    input_text = ' '.join(sys.argv[1:])

    # check if english or braille
    if set(input_text) <= {'.', 'O'}:
        translated_text = translate_to_english(input_text)
    else:
        translated_text = translate_to_braille(input_text)
    print(translated_text)
