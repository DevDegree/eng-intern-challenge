import sys

# Braille dictionary for letters, numbers, and special symbols
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Symbols for capitalization and numbers in Braille
capital_prefix = '.....O'
number_prefix = '.O.OOOO'


def is_braille(text):
    """ Determine if the input is Braille or English. """
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]

    if is_braille(input_text):
        print("Braille")
    else:
        print("Not Braille")
