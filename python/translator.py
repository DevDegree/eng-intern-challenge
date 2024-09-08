import sys

# Define constants for special Braille symbols
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_SPACE = '......'

# Mappings for English to Braille
BRAILLE_LETTER_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_NUMBER_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings for Braille to English
REVERSE_BRAILLE_LETTER_MAP = {v: k for k, v in BRAILLE_LETTER_MAP.items()}
REVERSE_BRAILLE_NUMBER_MAP = {v: k for k, v in BRAILLE_NUMBER_MAP.items()}

def is_braille(input_str: str) -> bool:
    """Check if the input string is a valid Braille sequence."""
    if len(input_str) % 6 != 0:
        return False

    for i in range(0, len(input_str), 6):
        symbol = input_str[i:i + 6]
        if (
            symbol not in REVERSE_BRAILLE_LETTER_MAP and 
            symbol not in REVERSE_BRAILLE_NUMBER_MAP and 
            symbol not in {BRAILLE_CAPITAL, BRAILLE_NUMBER, BRAILLE_SPACE}
        ):
            return False
    return True

def translate_to_braille(text: str) -> str:
    """Translate English text to Braille."""
    result = []
    number_mode = False  # Track whether number mode is active

    for char in text:
        if char.isupper():
            number_mode = False
            result.append(BRAILLE_CAPITAL)
            result.append(BRAILLE_LETTER_MAP[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_NUMBER)
                number_mode = True
            result.append(BRAILLE_NUMBER_MAP[char])
        elif char == " ":
            result.append(BRAILLE_SPACE)
        else:
            if number_mode and char.isalpha():
                number_mode = False
            result.append(BRAILLE_LETTER_MAP[char])

    return ''.join(result)

def translate_to_english(braille: str) -> str:
    """Translate Braille to English text."""
    result = []
    number_mode = False
    capital_mode = False

    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]

        if braille_char == BRAILLE_CAPITAL:
            capital_mode = True
        elif braille_char == BRAILLE_NUMBER:
            number_mode = True
        elif braille_char == BRAILLE_SPACE:
            result.append(" ")
            number_mode = False
        else:
            if number_mode:
                result.append(REVERSE_BRAILLE_NUMBER_MAP.get(braille_char, ''))
            else:
                char = REVERSE_BRAILLE_LETTER_MAP.get(braille_char, '')
                if capital_mode:
                    char = char.upper()
                    capital_mode = False
                result.append(char)
            number_mode = False  # End number mode after use

    return ''.join(result)

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])

    # Determine if the input is Braille or English and translate accordingly
    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)

    # Print the translated result
    print(output)

