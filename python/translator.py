import sys

BRAILLE_ALPHABET = {
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
BRAILLE_NUMBERS = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
BRAILLE_SPACE = '......'


def is_braille(input_str: str):
    """ Determines if an input string is valid Braille.

    :param input_str: a string of either Braille or English
    :return: True if Braille. False Otherwise
    """
    if len(input_str) % 6 != 0:  # valid braille will be divisible by 6 because each 'letter' is 6 chars
        return False
    return all(char in '.O' for char in input_str)


def english_to_braille(input_str: str):
    num_code_prepended = False
    translated = []
    for char in input_str:
        if char.isupper():
            translated.append(CAPITAL_FOLLOWS + BRAILLE_ALPHABET[char.lower()])
        elif char.isnumeric():
            if not num_code_prepended:
                translated.append(NUMBER_FOLLOWS)
                num_code_prepended = True
            translated.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            translated.append(BRAILLE_SPACE)
            num_code_prepended = False  # 'number mode' should be reset after a space
        else:
            translated.append(BRAILLE_ALPHABET[char])
    return ''.join(translated)


def braille_to_english(input_str: str):
    num_mode = False
    is_capital = False
    translated = []

    # swap keys and values in original Braille Alphabet for simplification
    braille_english_letters = {v: k for k, v in BRAILLE_ALPHABET.items()}
    braille_english_nums = {v: k for k, v in BRAILLE_NUMBERS.items()}

    for i in range(0, len(input_str), 6):
        char = input_str[i: i + 6]
        if char == BRAILLE_SPACE:
            translated.append(' ')
            num_mode = False  # 'number mode' should be reset after a space
        elif is_capital:
            translated.append(braille_english_letters[char].upper())
            is_capital = False
        elif char == CAPITAL_FOLLOWS:
            is_capital = True
        elif num_mode:
            translated.append(braille_english_nums[char])
        elif char == NUMBER_FOLLOWS:
            num_mode = True
        else:
            translated.append(braille_english_letters[char])

    return ''.join(translated)


def main():
    if len(sys.argv) < 2:
        print("Usage: translator.py <text_to_translate>")

    args = sys.argv[1:]  # Skip the first argument (script name)
    # print('......'.join(english_to_braille(arg) for arg in args))
    print(' '.join(braille_to_english(arg) for arg in args))


if __name__ == '__main__':
    main()
