import sys

CHAR_TO_BRAILLE = {
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
    ' ': '......',
}

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

BRAILLE_TO_CHAR = {val: key for key, val in CHAR_TO_BRAILLE.items()}


def capitalize_letter(ch: str) -> str:
    """
    Capitilizes alphabetic letter.

    Args:
        ch (str): The letter to capitalize.

    Returns:
        str: The capital letter.
    """
    return ch.upper()


def to_number(ch: str) -> str:
    """
    Converts alphabetic letter to corresponding number in braille.

    Args:
        ch (str): The alphabetic letter to covert.

    Returns:
        str: The corresponding number.
    """
    return chr((ord(ch) - ord('a') + 1) % 10 + ord('0'))


def to_alpha(ch: str) -> str:
    """
    Converts number to corresponding alphabetic character in braille.

    Args:
        ch (str): The number to covert.

    Returns:
        str: The corresponding alphabetic character.
    """
    return chr((ord(ch) - ord('0') + 9) % 10 + ord('a'))


def is_braille(text: str) -> bool:
    """
    Determines whether the text is braille or not (english).

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is in braille, false otherwise.
    """
    return text.count('.') > 0 and len(text) % 6 == 0


def braille_to_english(text: str) -> str:
    """
    Translates the braille text into english and returns the result.

    Args:
        text (str): The braille text being translated.

    Returns:
        str: The translated english string.
    """
    text_arr = [text[i:i+6] for i in range(0, len(text), 6)]

    ind = 0
    res = ""
    is_capital = False
    is_number = False

    while ind < len(text_arr):
        cur_str = text_arr[ind]

        if cur_str in BRAILLE_TO_CHAR:
            english_char = BRAILLE_TO_CHAR[cur_str]

            if english_char == ' ':
                res += ' '
                is_number = False

            elif is_capital:
                res += capitalize_letter(english_char)
                is_capital = False

            elif is_number:
                res += to_number(english_char)

            else:
                res += english_char

        else:
            if cur_str == CAPITAL_FOLLOWS:
                is_capital = True

            elif cur_str == NUMBER_FOLLOWS:
                is_number = True

        ind += 1

    return res


def english_to_braille(text: str) -> str:
    """
    Translates the english text into braille and returns the result.

    Args:
        text (str): The english text being translated.

    Returns:
        str: The translated braille string.
    """

    res = ""
    is_number = False

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                res += CAPITAL_FOLLOWS

            ch = ch.lower()
            res += CHAR_TO_BRAILLE[ch]

        elif ch.isnumeric():
            if not is_number:
                is_number = True
                res += NUMBER_FOLLOWS

            res += CHAR_TO_BRAILLE[to_alpha(ch)]

        else:
            res += CHAR_TO_BRAILLE[ch]
            is_number = False

    return res


def translate(text: str) -> str:
    """
    Translates the braille or english text to the opposite.

    Args:
        text (str): The text being translated.

    Returns:
        str: The translated string.
    """
    translated_input = ''
    if is_braille(text):
        translated_input = braille_to_english(text)
    else:
        translated_input = english_to_braille(text)

    return translated_input


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        TEXT = ' '.join(sys.argv[1:])
        print(translate(TEXT))
