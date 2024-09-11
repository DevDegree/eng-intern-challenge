import sys

# Braille mappings for alphabets and numbers
BRAILLE_ALPHABET_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
}

BRAILLE_NUMERIC_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Special prefix codes for capitalization, numbers, and space
BRAILLE_PREFIXES = {
    'SPACE': '......',
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO',
}

# Reverse maps for Braille to text conversion
REVERSE_ALPHABET_MAP = {value: key for key, value in BRAILLE_ALPHABET_MAP.items()}
REVERSE_NUMERIC_MAP = {value: key for key, value in BRAILLE_NUMERIC_MAP.items()}


def translate_text_to_braille(text):
    """Converts an English sentence into Braille."""
    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(BRAILLE_PREFIXES['NUMBER'])
                number_mode = True
            braille_output.append(BRAILLE_NUMERIC_MAP[char])
        elif char.isupper():
            braille_output.append(BRAILLE_PREFIXES['CAPITAL'])
            braille_output.append(BRAILLE_ALPHABET_MAP[char.lower()])
        elif char == ' ':
            braille_output.append(BRAILLE_PREFIXES['SPACE'])
            number_mode = False
        else:
            braille_output.append(BRAILLE_ALPHABET_MAP[char])
            number_mode = False

    return ''.join(braille_output)


def translate_braille_to_text(braille_sequence):
    """Converts a Braille string into an English sentence."""
    text_output = []
    number_mode = False
    capital_mode = False

    for i in range(0, len(braille_sequence), 6):
        braille_char = braille_sequence[i:i + 6]

        if braille_char == BRAILLE_PREFIXES['NUMBER']:
            number_mode = True
            capital_mode = False
            continue
        elif braille_char == BRAILLE_PREFIXES['CAPITAL']:
            capital_mode = True
            continue
        elif braille_char == BRAILLE_PREFIXES['SPACE']:
            text_output.append(' ')
            number_mode = False
            capital_mode = False
        elif number_mode:
            text_output.append(REVERSE_NUMERIC_MAP[braille_char])
            number_mode = False
        elif capital_mode:
            text_output.append(REVERSE_ALPHABET_MAP[braille_char].upper())
            capital_mode = False
        else:
            text_output.append(REVERSE_ALPHABET_MAP[braille_char])

    return ''.join(text_output)


def is_braille_sequence(input_string):
    """Checks if the input string is a valid Braille sequence."""
    valid_braille_chars = {'.', 'O'}
    
    if len(input_string) % 6 != 0:
        return False

    return all(char in valid_braille_chars for char in input_string)


def main():
    if len(sys.argv) < 2:
        raise Exception("Usage: python script.py <sentence or braille_sequence>")

    input_text = " ".join(sys.argv[1:])

    if is_braille_sequence(input_text):
        print(translate_braille_to_text(input_text))
    else:
        print(translate_text_to_braille(input_text))


if __name__ == "__main__":
    main()

