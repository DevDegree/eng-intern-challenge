import sys

# Constants to translate between braille and english
class TranslatorConst:
    num = '.O.OOO'
    capital = '.....O'

    # Using characters as intermediate keys to translate numbers
    # Get character from digit
    num_to_char_dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

    # Get digit from number
    char_to_num_dict = {v: k for k, v in num_to_char_dict.items()}

    # Get character from braille
    char_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO',
        ' ': '......'
    }

    # Get character from braille
    braille_dict = {v: k for k, v in char_dict.items()}


def is_input_braille(val: str) -> bool:
    """
    This function determines if the input string is english or braille
    If the input string is braille, the function returns. Otherwise, it returns False
    :param val:
    :return: bool
    """

    if len(val) % 6 != 0:
        return False

    for char in val:
        if char != '.' and char != 'O':
            return False
    return True


def translate_english(english_str: str) -> str:
    """
    This function translates the english string into braille
    :param english_str:
    :return: braille_str
    """

    braille_str = ''
    is_num = False

    for char in english_str:
        if char.isdigit():
            if not is_num:
                braille_str += TranslatorConst.num
                is_num = True
            key = TranslatorConst.num_to_char_dict[char]
            braille_str += TranslatorConst.char_dict[key]

        elif char.isupper():
            braille_str += TranslatorConst.capital
            braille_str += TranslatorConst.char_dict[char.lower()]

        else:
            braille_str += TranslatorConst.char_dict[char]

            if char == ' ':
                is_num = False

    return braille_str


def translate_braille(braille_str: str) -> str:
    """
    This function translates the braille string into an english string
    :param braille_str:
    :return: english_str
    """

    english_str = ''
    is_num = False
    is_capital = False

    # Loop over
    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i:i+6]

        # Handle space
        if braille_char == TranslatorConst.char_dict[' ']:
            is_num = False
            english_str += TranslatorConst.braille_dict[braille_char]

        # Handle digit
        elif is_num:
            letter = TranslatorConst.braille_dict[braille_char]
            num = TranslatorConst.char_to_num_dict[letter]
            english_str += num

        # Handle number follows
        elif braille_char == TranslatorConst.num:
            is_num = True

        # Handle capital follows
        elif braille_char == TranslatorConst.capital:
            is_capital = True

        # Handle a-z
        else:
            letter = TranslatorConst.braille_dict[braille_char]

            if is_capital:
                letter = letter.upper()
                is_capital = False

            english_str += letter

    return english_str


def main():
    """
    Handles input and prints out translation received back
    :return: None
    """

    input_val = ' '.join(sys.argv[1:])

    is_braille = is_input_braille(input_val)

    if is_braille:
        res = translate_braille(input_val)
    else:
        res = translate_english(input_val)

    print(res)


if __name__ == '__main__':
    main()
