import sys

# Mapping dictionary to convert English to Braille representation
EN_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

# Reverse mapping to convert Braille back to English
BRAILLE_TO_EN = {v: k for k, v in EN_TO_BRAILLE.items()}

# Special Braille symbols
CAPITAL_BRAILLE = '.....O'
NUMBER_BRAILLE = '.O.OOO'

def is_braille_input(text):
    """Check if the input consists entirely of Braille symbols (O and .) and its length is valid."""
    return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

def translate_english_to_braille(english_text):
    """Translate English text to Braille."""
    
    result_braille = []
    number_mode = False  # Indicates if the number mode is active

    for character in english_text:
        if character == ' ':
            result_braille.append(EN_TO_BRAILLE[' '])
            number_mode = False
        elif character.isdigit():
            if not number_mode:
                result_braille.append(NUMBER_BRAILLE)
                number_mode = True
            result_braille.append(EN_TO_BRAILLE[character])
        else:
            if character.isupper():
                result_braille.append(CAPITAL_BRAILLE)
            result_braille.append(EN_TO_BRAILLE[character.lower()])

    return ''.join(result_braille)

def translate_braille_to_english(braille_text):
    """Translate Braille text back to English."""

    result_english = []
    is_capital = False  # Tracks if the next letter should be capitalized
    is_number_mode = False  # Tracks if the number mode is on

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        if braille_char == CAPITAL_BRAILLE:
            is_capital = True
        elif braille_char == NUMBER_BRAILLE:
            is_number_mode = True
        elif braille_char == '......':
            result_english.append(' ')
            is_number_mode = False
        elif is_number_mode:
            result_english.append(BRAILLE_TO_EN[braille_char])
        else:
            letter = BRAILLE_TO_EN[braille_char]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            result_english.append(letter)

    return ''.join(result_english)

def main():
    # Ensure at least one argument is passed
    if len(sys.argv) < 2:
        sys.exit("Usage: python translator.py <text-to-translate>")

    # Combine the input arguments to form the full text
    input_text = ' '.join(sys.argv[1:])

    # Decide if the input is Braille or English and call the appropriate translation function
    if is_braille_input(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))

if __name__ == '__main__':
    main()