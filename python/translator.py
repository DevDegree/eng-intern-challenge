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
    'capital_follows': '.....O', 
    'number_follows': '.O.OOO', 
    ' ': '......'
}

NUMS_TO_BRAILLE: dict[str, str] = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

BRAILLE_TO_ENGLISH: dict[str, str] = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMS: dict[str, str] = {v: k for k, v in NUMS_TO_BRAILLE.items()}
BRAILLE_CHAR_LEN: int = 6

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
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

def is_braille(input_string: str) -> bool:
    """ Return True if the given string is braille, False otherwise """

    if len(input_string) % 6 != 0:
        return False

    return all(char in {'O', '.'} for char in input_string)

def translate_braille_to_english(braille_string: str) -> str:
    """ Translates a braille string to an english string """

    result: list[str] = []
    capital_mode: bool = False
    number_mode: bool = False

    for i in range(0, len(braille_string), BRAILLE_CHAR_LEN):
        segment: str = braille_string[i:i + BRAILLE_CHAR_LEN]

        if segment == ENGLISH_TO_BRAILLE['capital_follows']:
            capital_mode = True
            continue
        elif segment == ENGLISH_TO_BRAILLE['number_follows']:
            number_mode = True
            continue
        elif segment == ENGLISH_TO_BRAILLE[' ']:
            result.append(' ')
            number_mode = False
            continue

        if number_mode:
            char = BRAILLE_TO_NUMS[segment]
        else:
            char = BRAILLE_TO_ENGLISH[segment]

        if capital_mode:
            char = char.upper()
            capital_mode = False

        result.append(char)

    return ''.join(result)

def translate_english_to_braille(english_string: str) -> str:
    """ Translates an english string to a braille string """

    result: list[str] = []
    number_mode: bool = False

    for char in english_string:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number_follows'])
                number_mode = True
            result.append(NUMS_TO_BRAILLE[char])
            continue

        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['capital_follows'])
            char = char.lower()

        number_mode = False 
        result.append(ENGLISH_TO_BRAILLE.get(char, '......')) 

    return ''.join(result)

if __name__ == '__main__':
    main()