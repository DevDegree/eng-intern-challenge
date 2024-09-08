import sys

# Constants for Braille indicators
BRAILLE_NUMBER_INDICATOR = '.O.OOO'
BRAILLE_CAPITAL_INDICATOR = '.....O'

# Braille translation dictionaries
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse lookup dictionaries for translation from Braille to English
REVERSED_BRAILLE_LETTERS = {v: k for k, v in BRAILLE_LETTERS.items()}
REVERSED_BRAILLE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}


def is_braille(input_string):
    """
    Check if the input string is written in Braille (contains only 'O' and '.' characters).
    """
    return all(char in ['O', '.'] for char in input_string)


def translate_braille_to_english(braille_string):
    """
    Translate a Braille string to English.
    Handles number and capital indicators.
    """
    result = []
    number_mode = False
    capital_mode = False

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        # Handle number and capital indicators
        if braille_char == BRAILLE_NUMBER_INDICATOR:
            number_mode = True
            continue
        if braille_char == BRAILLE_CAPITAL_INDICATOR:
            capital_mode = True
            continue

        # Translate numbers
        if number_mode:
            if braille_char in REVERSED_BRAILLE_NUMBERS:
                result.append(REVERSED_BRAILLE_NUMBERS[braille_char])
                continue
            number_mode = False

        # Translate letters
        if braille_char in REVERSED_BRAILLE_LETTERS:
            letter = REVERSED_BRAILLE_LETTERS[braille_char]
            if capital_mode:
                letter = letter.upper()
                capital_mode = False
            result.append(letter)
        else:
            result.append('?')  # Handle unknown Braille characters

    return ''.join(result)


def translate_english_to_braille(english_string):
    """
    Translate an English string to Braille.
    Handles number and capital indicators.
    """
    result = []
    number_mode = False

    for char in english_string:
        # Handle numbers
        if char.isdigit():
            if not number_mode:
                result.append(BRAILLE_NUMBER_INDICATOR)
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
            continue

        # Handle spaces
        if char == ' ':
            result.append(BRAILLE_LETTERS[char])
            number_mode = False
            continue

        # Handle letters
        if char.isalpha():
            if char.isupper():
                result.append(BRAILLE_CAPITAL_INDICATOR)
                char = char.lower()
            result.append(BRAILLE_LETTERS[char])

    return ''.join(result)


def handle_translation(input_string):
    """
    Determine whether the input is Braille or English and perform the appropriate translation.
    """
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)


def main():
    """
    Main function to handle command-line inputs and trigger translation.
    """
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])
    translated_string = handle_translation(input_string)
    print(translated_string)


if __name__ == "__main__":
    main()
