import sys

# Braille translation constants
BRAlPHABET_MAP = {
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
}

BR_NUMBER_MAP = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

BR_SPECIAL_MAP = {
    '.': '..OO.O',
    ',': '..O...',
    ';': '..OO..',
    '!': '..O.O.',
    '?': '..OO.O',
    '-': '....O.',
    "'": '....OO',
    '(': '...O..',
    ')': '...OO.',
    ' ': '......',
}

CAP_PREFIX = '.....O'
NUM_PREFIX = '.O.OOO'

# Reverse mappings for Braille to English
BR_TO_ENG_LETTER = {v: k for k, v in BRAlPHABET_MAP.items()}
BR_TO_ENG_NUMBER = {v: k for k, v in BR_NUMBER_MAP.items()}
BR_TO_ENG_SPECIAL = {v: k for k, v in BR_SPECIAL_MAP.items()}


# Translation functions
def translate_text(input_str):
    # Check if input is in Braille or English
    if all(char in 'O.' for char in input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)


def braille_to_english(braille_str):
    english_str = ''
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille_str):
        char_braille = braille_str[i:i + 6]

        # Check for special characters
        if char_braille == CAP_PREFIX:
            is_capital = True
            i += 6
            continue
        # Check for number prefix
        elif char_braille == NUM_PREFIX:
            is_number = True
            i += 6
            continue
        # Check for special characters
        elif char_braille == '......':
            english_str += ' '
        # Check for letters
        elif char_braille in BR_TO_ENG_LETTER and not is_number:
            letter = BR_TO_ENG_LETTER[char_braille]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            english_str += letter
        # Check for numbers
        elif char_braille in BR_TO_ENG_NUMBER and is_number:
            english_str += BR_TO_ENG_NUMBER[char_braille]
        # Check for special characters
        elif char_braille in BR_TO_ENG_SPECIAL:
            english_str += BR_TO_ENG_SPECIAL[char_braille]

        i += 6

        # Reset number flag if space is found
        if char_braille == '......':
            is_number = False

    return english_str


def english_to_braille(english_str):
    output = ''
    is_number = False

    for char in english_str:
        # Check if character is a letter
        if char.isalpha():
            if char.isupper():
                output += CAP_PREFIX
                char = char.lower()
            output += BRAlPHABET_MAP[char]
        # Check if character is a number
        elif char.isdigit():
            if not is_number:
                output += NUM_PREFIX
                is_number = True
            output += BR_NUMBER_MAP[char]
        # Check if character is a special character
        elif char in BR_SPECIAL_MAP:
            output += BR_SPECIAL_MAP[char]
                # If character is a space
        else:
            output += BR_SPECIAL_MAP[' ']
            is_number = False

    return output


def main():
    if len(sys.argv) < 2:
        print("ERROR: Invalid number of arguments")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    print(translate_text(input_text))


if __name__ == '__main__':
    main()