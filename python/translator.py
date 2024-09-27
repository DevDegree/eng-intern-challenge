import sys

ENGLISH_TO_BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# Create the reverse dictionary for alphabets
BRAILLE_TO_ENGLISH_ALPHABET = {b: e for e, b in ENGLISH_TO_BRAILLE_ALPHABET.items()}

ENGLISH_TO_BRAILLE_NUMBERS = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
}

# Create the reverse dictionary for numbers
BRAILLE_TO_ENGLISH_NUMBERS = {b: e for e, b in ENGLISH_TO_BRAILLE_NUMBERS.items()}

BRAILLE_SPECIAL_CHARACTERS = {
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',
    'space': '......'
}


def is_braille(input: str) -> bool:
    return len(input) % 6 == 0 and all(char in ['.', 'O'] for char in input)

def is_english(input: str) -> bool:
    return all(char.isalnum() for char in input)


def translate_english_to_braille(input: str) -> str:
    braille_string = ""
    number_follows = False

    for char in input:
        if char.isnumeric():
            if not number_follows:
                braille_string += BRAILLE_SPECIAL_CHARACTERS['number_follows']
                number_follows = True

            braille_string += ENGLISH_TO_BRAILLE_NUMBERS[char]
        elif char.isalpha():
            if number_follows:
                braille_string += BRAILLE_SPECIAL_CHARACTERS['space']
                number_follows = False

            if char.isupper():
                braille_string += BRAILLE_SPECIAL_CHARACTERS['capital_follows']

            braille_string += ENGLISH_TO_BRAILLE_ALPHABET[char.lower()]
        elif char.isspace():
            braille_string += BRAILLE_SPECIAL_CHARACTERS['space']
            number_follows = False
        else:
            print(f'Invalid character: {char}')
            sys.exit(1)

    return braille_string


def translate_braille_to_english(input: str) -> str:
    english_string = ""
    number_follows = False
    capital_follows = False

    for i in range(0, len(input), 6):
        char = input[i: i + 6]

        if char == BRAILLE_SPECIAL_CHARACTERS['capital_follows']:
            capital_follows = True
        elif char == BRAILLE_SPECIAL_CHARACTERS['number_follows']:
            number_follows = True
        elif char == BRAILLE_SPECIAL_CHARACTERS['space']:
            if number_follows:
                number_follows = False
            else:
                english_string += ' '
        elif number_follows:
            if char in BRAILLE_TO_ENGLISH_NUMBERS:
                english_string += BRAILLE_TO_ENGLISH_NUMBERS[char]
            else:
                print(f'Invalid character: {char}')
                sys.exit(1)
        elif char in BRAILLE_TO_ENGLISH_ALPHABET:
            if capital_follows:
                english_string += BRAILLE_TO_ENGLISH_ALPHABET[char].upper()
                capital_follows = False
            else:
                english_string += BRAILLE_TO_ENGLISH_ALPHABET[char]
        else:
            print(f'Invalid character: {char}')
            sys.exit(1)

    return english_string


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: Invalid number of arguments')

    input = sys.argv[1:]

    if is_braille(input[0]):
        print(translate_braille_to_english(input[0]))
    elif is_english(input):
        print(translate_english_to_braille(' '.join(input)))
    else:
        print("Invalid Input")
        sys.exit(1)

    sys.exit(0)
