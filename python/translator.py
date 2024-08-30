import sys


english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital_follows': '.....O', 'number_follows': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}


def translate_to_braille(english_text: str) -> str:
    """
    :param english_text: English text
    :return: Braille text
    """
    braille_text = ''
    is_last_char_digit = False

    for char in english_text:
        if char.isupper():
            braille_text += english_to_braille['capital_follows']

        if char.isdigit():
            if not is_last_char_digit:
                braille_text += english_to_braille['number_follows']
                is_last_char_digit = True

        if char.isspace():
            is_last_char_digit = False
        braille_text += english_to_braille[char.lower()]

    return braille_text


braille_to_english = {}


def translate_to_english(braille_text: str) -> str:
    """
    When a Braille capital follows symbol is read,
        assume only the next symbol should be capitalized.
    When a Braille number follows symbol is read,
        assume all following symbols are numbers until the next space symbol
    :param braille_text: Braille text
    :return: English text
    """
    return 'English text'


def is_braille(text: str) -> bool:
    """
    Adapted from https://www.tutorialspoint.com/how-to-check-if-a-string-only-contains-certain-characters-in-python
    :param text: User input
    :return: True if text is Braille, False if English
    """
    braille_chars = ['O', '.']
    braille_validation = [c in braille_chars for c in text]
    return all(braille_validation)


def main():
    tokens = sys.argv[1:]
    text = ' '.join(tokens)

    if is_braille(text):
        translated_text = translate_to_english(text)
    else:
        translated_text = translate_to_braille(text)

    print(translated_text)


if __name__ == '__main__':
    main()
