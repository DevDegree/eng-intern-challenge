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

braille_to_english_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' '
}

braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0'
}


def translate_to_braille(english_text: str) -> str:
    """ Translates English text to Braille """
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


def translate_to_english(braille_text: str) -> str:
    """ Translates Braille text to English """
    # Split the Braille text into Braille symbols of length 6
    # Code adapted from https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length
    symbol_length, text_length = 6, len(braille_text)
    symbols = [braille_text[i:i + symbol_length] for i in range(0, text_length, symbol_length)]

    english_text = ''
    is_capital = False
    is_number = False

    for symbol in symbols:
        if symbol == english_to_braille['capital_follows']:
            is_capital = True

        elif symbol == english_to_braille['number_follows']:
            is_number = True

        elif symbol == english_to_braille[' ']:
            english_text += braille_to_english_letters[symbol]
            is_number = False

        elif is_number:
            english_text += braille_to_english_numbers[symbol]

        elif is_capital:
            english_text += braille_to_english_letters[symbol].upper()
            is_capital = False

        else:
            english_text += braille_to_english_letters[symbol]

    return english_text


def is_braille(text: str) -> bool:
    """ Checks if text is Braille """
    # Adapted from https://www.tutorialspoint.com/how-to-check-if-a-string-only-contains-certain-characters-in-python
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
