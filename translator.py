import sys

# Braille marker symbols
capital_follows = '.....O'
number_follows = '.O.OOO'

# Braille to letters mapping
braille_alpha = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

# Braille to numbers mapping
braille_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '......': ' '
}


def is_braille(sequence):
    """
    Returns whether the input sequence is written in Braille.
    Braille sequences can only contain '.' and 'O'.

    :param sequence: str input sequence
    :return: bool
    """
    return all(char in "O." for char in sequence)


def translate(sequence):
    """

    :param sequence:
    :return:
    """
    if is_braille(sequence):
        return braille_to_english(sequence)
    else:
        return english_to_braille(sequence)


def braille_to_english(sequence):
    """

    :param sequence:
    :return:
    """
    return 'english'


def english_to_braille(sequence):
    """

    :param sequence:
    :return:
    """
    return 'braille'


if __name__ == '__main__':
    input_sequence = ' '.join(sys.argv[1:])
    print(translate(input_sequence))






