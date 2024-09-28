import sys

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
    'O..OOO': 'z'
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
    '.OOO..': '0'
}

# Braille special symbols
capital_follows = '.....O'
number_follows = '.O.OOO'
space = '......'


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
    Convert a Braille sequence to English text.

    :param sequence: A string representing the Braille sequence
    :return: The translated English text
    """
    translation = ''
    length = len(sequence)
    curr = 0

    number_flag = False  # Indicates that following symbols are numbers
    capital_flag = False  # Indicates that following letter is capitalized

    while curr < length:
        symbol = sequence[curr:curr + 6]

        # Check for special symbols
        if symbol == number_follows:
            number_flag = True
        elif symbol == capital_follows:
            capital_flag = True
        elif symbol == space:
            translation += ' '
            number_flag = False  # Reset number flag after space

        # Process symbols as numbers
        elif number_flag:
            num = braille_num[symbol]
            translation += num

        # Process symbols as letters
        else:
            char = braille_alpha[symbol]
            if capital_flag:
                # Capitalize next letter and reset flag
                char = char.upper()
                capital_flag = False
            translation += char

        curr += 6

    return translation


def english_to_braille(text):
    """
    Convert English text to a Braille sequence.

    :param text: A string representing the English text
    :return: The translated Braille sequence
    """
    translation = ''

    # Invert Braille to English mappings
    alpha_braille = {v: k for k, v in braille_alpha.items()}
    num_braille = {v: k for k, v in braille_num.items()}

    number_flag = False  # Indicates that sequence is already in numbers mode

    for char in text:
        if char.isspace():
            translation += '......'
            number_flag = False  # Disable numbers mode

        # Convert letters to Braille
        elif char.isalpha():
            if char.isupper():
                char = char.lower()
                translation += capital_follows  # Add capital_follows symbol to sequence
            translation += alpha_braille[char]

        # Convert numbers to Braille
        elif char.isnumeric():
            if not number_flag:
                number_flag = True
                translation += number_follows  # Add number_follows symbol to sequence
            translation += num_braille[char]

    return translation


if __name__ == '__main__':
    input_sequence = ' '.join(sys.argv[1:])
    print(translate(input_sequence))
