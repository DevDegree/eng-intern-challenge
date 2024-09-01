import sys

# Separate dictionaries for letters, numbers, punctuation, and special symbols
LETTER_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..', ' ': '......',
}

PUNCTUATION_TO_BRAILLE = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
}

SYMBOL_TO_BRAILLE = {
    'cap': '.....O',
    'num': '.O.OOO',
    'dec': '.O...O',
}

BRAILLE_TO_LETTER = {v: k for k, v in LETTER_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_PUNCTUATION = {v: k for k, v in PUNCTUATION_TO_BRAILLE.items()}
BRAILLE_TO_SYMBOL = {v: k for k, v in SYMBOL_TO_BRAILLE.items()}

def is_braille(text):
    # Check if all characters are either 'O' or '.'
    if not all(char in 'O.' for char in text):
        return False

    # Check if the length is a multiple of 6
    if len(text) % 6 != 0:
        return False

    return True

def braille_to_english(braille):
    i = 0
    result = []
    capitalize = False
    num_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol in BRAILLE_TO_SYMBOL and BRAILLE_TO_SYMBOL[symbol] == 'cap':
            capitalize = True
        elif symbol in BRAILLE_TO_SYMBOL and BRAILLE_TO_SYMBOL[symbol] == 'num':
            num_mode = True
        elif num_mode and symbol in BRAILLE_TO_SYMBOL and BRAILLE_TO_SYMBOL[symbol] == 'dec':
            result.append('.')
        else:
            if num_mode:
                char = BRAILLE_TO_NUMBER.get(symbol, '')
                if char == ' ':  # Exit num_mode after a space
                    num_mode = False
            else:
                char = BRAILLE_TO_LETTER.get(symbol, '')
                if char == '':
                    char = BRAILLE_TO_PUNCTUATION.get(symbol, '')

            if capitalize:
                char = char.upper()
                capitalize = False  # Only capitalize the next letter

            result.append(char)
        i += 6

    return ''.join(result)

def english_to_braille(text):
    result = []
    num_mode = False

    for char in text:
        if char.isdigit():
            if not num_mode:
                result.append(SYMBOL_TO_BRAILLE['num'])
                num_mode = True
            result.append(NUMBER_TO_BRAILLE[char])
        elif num_mode and char == '.':
            result.append(SYMBOL_TO_BRAILLE['dec'])
        elif char in PUNCTUATION_TO_BRAILLE:
            result.append(PUNCTUATION_TO_BRAILLE[char])
        else:
            if num_mode and char == ' ':
                num_mode = False  # Reset number mode after a space
            if char.isupper():
                result.append(SYMBOL_TO_BRAILLE['cap'])
                result.append(LETTER_TO_BRAILLE[char.lower()])
            else:
                result.append(LETTER_TO_BRAILLE.get(char, '......'))
        if char == ' ':
            num_mode = False  # Reset number mode after a space
    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()
