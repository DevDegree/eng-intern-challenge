import sys

# Braille codes for letters
braille_letters = {
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
}

braille_nums = {
    '1': 'O.....',  # a
    '2': 'O.O...',  # b
    '3': 'OO....',  # c
    '4': 'OO.O..',  # d
    '5': 'O..O..',  # e
    '6': 'OOO...',  # f
    '7': 'OOOO..',  # g
    '8': 'O.OO..',  # h
    '9': '.OO...',  # i
    '0': '.OOO..',  # j
}

# Braille special symbols
capital_sign = '.....O'
number_sign = '.O.OOO'
space_sign = '......'

# Reverse mappings for decoding
braille_to_letter = {v: k for k, v in braille_letters.items()}
braille_to_digit = {v: k for k, v in braille_nums.items()}

def is_braille(text):
    """
    Determines if the input text is Braille.
    """
    return all(c in ('O', '.') for c in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <text>')
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        # Convert Braille to English
        print("English")
    else:
        # Convert English to Braille
        print("Braille")

if __name__ == '__main__':
    main()
