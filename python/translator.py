import sys

# Define constants for special Braille symbols
CAPITAL = '.....O'
NUMBER = '.O.OOO'

# Mappings for English to Braille
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

NUMERIC_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings for Braille to English
REVERSE_BRAILLE_LETTER_MAP = {v: k for k, v in BRAILLE_MAP.items()}
REVERSE_BRAILLE_NUMBER_MAP = {v: k for k, v in NUMERIC_MAP.items()}


def translate_to_braille(text):
    result = []
    for char in text:
        # Append the Braille capital indicator if the character is uppercase, then add its lowercase Braille mapping
        if char.isupper():
            result.append(CAPITAL)
            result.append(BRAILLE_MAP[char.lower()])
        # Append the Braille number indicator if the character is a digit, then add its numeric Braille mapping
        elif char.isdigit():
            result.append(NUMBER)
            result.append(NUMERIC_MAP[char])
        # Append the Braille mapping for regular characters (lowercase letters and spaces)
        else:
            result.append(BRAILLE_MAP[char])

    # Concatenate the list of Braille strings into a single string and return
    return ''.join(result)

def translate_to_english(braille):
    result = []
    index = 0
    number_mode = False

    while index < len(braille):
        braille_char = braille[index:index+6]

        # Check for the Braille capital indicator
        if braille_char == CAPITAL:
            index += 6
            next_braille_char = braille[index:index+6]
            result.append(REVERSE_BRAILLE_LETTER_MAP[next_braille_char].upper())
        # Check for the Braille number indicator
        elif braille_char == NUMBER:
            number_mode = True
            index += 6
        else:
            # Decide which map to use based on number mode
            if number_mode:
                char = REVERSE_BRAILLE_NUMBER_MAP.get(braille_char, '')
                if char:
                    result.append(char)
            else:
                char = REVERSE_BRAILLE_LETTER_MAP.get(braille_char, '')
                if char:
                    result.append(char)

        # Exit number mode if a letter is encountered
        if not number_mode and braille_char in REVERSE_BRAILLE_NUMBER_MAP:
            number_mode = False

        index += 6

    return ''.join(result)


if __name__ == '__main__':
    input_text = sys.argv[1]

    if all(c in 'O.' for c in input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))