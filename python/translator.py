import sys


ENGLISH_TO_BRAILLE: dict[str, str] = {
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
    ' ': '......'
}

NUMBERS_TO_BRAILLE: dict[str, str] = {
    '0': '.OOO..',
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

BRAILLE_TO_ENGLISH: dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS: dict[str, str] = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

BRAILLE_SPACE: str = '......'
BRAILLE_CAPITAL_FOLLOWS: str = '.....O'
BRAILLE_NUMBER_FOLLOWS: str = '.O.OOO'


def main():
    if len(sys.argv) < 2:
        print("""
            Incorrect program usage.
            Example usage:
            >> python3 translator.py Hello World
            >> python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
            """)
        return

    input_string: str = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

def is_braille(input_string: str) -> bool:
    """ Return True if the given string is braille, False otherwise """
    if len(input_string) % 6 != 0:
        return False

    return all(char in {'O', '.'} for char in input_string)

def translate_to_english(braille_string: str) -> str:
    """ Translates a braille string to an english string """
    translated: str = ''
    braille_chars: list[str] = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]

    capital_mode: bool = False
    number_mode: bool = False

    for char in braille_chars:
        if char == BRAILLE_CAPITAL_FOLLOWS:
            capital_mode = True
            continue
        elif char == BRAILLE_NUMBER_FOLLOWS:
            number_mode = True
            continue
        elif char == BRAILLE_SPACE and number_mode:
            number_mode = False
            continue

        if capital_mode:
            translated += BRAILLE_TO_ENGLISH.get(char).upper()
            capital_mode = False
        elif number_mode:
            translated += BRAILLE_TO_NUMBERS.get(char)
        else:
            translated += BRAILLE_TO_ENGLISH.get(char)

    return translated

def translate_to_braille(english_string: str) -> str:
    """ Translates an english string to a braille string """
    translated: str = ''
    number_mode: bool = False

    for char in english_string:
        if char.isalpha():
            if number_mode:
                translated += BRAILLE_SPACE
                number_mode = False
            if char.isupper():
                translated += BRAILLE_CAPITAL_FOLLOWS
            translated += ENGLISH_TO_BRAILLE[char.lower()]
        elif char.isspace():
            if number_mode:
                # translated += BRAILLE_SPACE
                number_mode = False
            translated += BRAILLE_SPACE
        else:
            if not number_mode:
                translated += BRAILLE_NUMBER_FOLLOWS
                number_mode = True
            translated += NUMBERS_TO_BRAILLE[char]

    return translated

if __name__ == '__main__':
    main()