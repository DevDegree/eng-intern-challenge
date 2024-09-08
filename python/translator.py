import sys

# Create dicts containing the translations
braille_english_chars = {
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

braille_english_nums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

braille_english_args = {
    'capital': '.....O',
    'number': '.O.OOO'
}
# English to Braille is just Braille to English reversed
english_braille_chars = dict((val, key) for key, val in braille_english_chars.items())
english_braille_nums = dict((val, key) for key, val in braille_english_nums.items())
english_braille_args = dict((val, key) for key, val in braille_english_args.items())


# Check if the given input is braille
def input_is_braille(text_input):
    if len(text_input) % 6 != 0:  # Braille text is in multiples of 6 always
        return False

    for char in text_input:
        if char != '.' and char != 'O':  # Check that all chars are Braille (. or O)
            return False

    return True


# Convert English text to Braille
def convert_to_braille(text_input):
    translation = ''
    number = False

    for char in text_input:
        if char.isdigit():
            if number:
                translation += braille_english_nums[char]
            else:
                number = True
                translation += braille_english_args['number']
                translation += braille_english_nums[char]

        elif char.isupper():
            translation += braille_english_args['capital']
            translation += braille_english_chars[char.lower()]

        else:
            if char == ' ':
                number = False
            translation += braille_english_chars[char]

    return translation


# Convert Braille to English
def convert_to_english(text_input):
    translation = ''
    letter_length = 6
    letters = [text_input[i:i+letter_length] for i in range(0, len(text_input), letter_length)]
    capital = False
    number = False

    for letter in letters:
        if letter == braille_english_args['capital']:
            capital = True
        elif letter == braille_english_args['number']:
            number = True
        elif letter == braille_english_chars[' ']:
            translation += ' '
            number = False
        elif capital:
            translation += english_braille_chars[letter].upper()
            capital = False
        elif number:
            translation += english_braille_nums[letter]
        else:
            translation += english_braille_chars[letter]

    return translation


def main():
    text_input = ' '.join(sys.argv[1:])
    if input_is_braille(text_input):
        print(convert_to_english(text_input))
    else:
        print(convert_to_braille(text_input))


if __name__ == '__main__':
    main()

