# Braille to English translator by Massimo Scanga
import sys

# Library of each English letter corresponding to Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  
}

# Braille numbers use a special symbol to mark the start of a number block
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Special symbols for capital letters and numbers
capital_sign = '.....O'
number_sign = '.O.OOO'

# Reverse dictionaries for Braille to English
english_braille_alpha = {v: k for k, v in braille_alphabet.items()}
english_braille_num = {v: k for k, v in braille_numbers.items()}

# Validate Braille input to ensure correct length
def validate_braille(braille_string):
    if len(braille_string) % 6 != 0:
        raise ValueError("Braille string must be of 6 characters of . or O")

# Detect whether the input string is Braille or English
def detect_language(input_string):
    braille_chars = set('O.')
    first_char = input_string[0]

    if first_char in braille_chars:
        if set(input_string) <= braille_chars:
            return 'braille'
    elif first_char.isalnum() or first_char.isspace():
        if all(c.isalnum() or c.isspace() for c in input_string):
            return 'english'

    raise ValueError("Unsupported character detected. Only (O,.) or alphanumeric is accepted")

# Split Braille string into chunks of 6 characters
def split_braille(braille_string):
    return [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]

# Braille to English
def braille_to_english(braille_string):
    validate_braille(braille_string)
    result = []
    chunks = split_braille(braille_string)
    modes = {'number': False, 'capital': False}

    # Process each Braille chunk
    for chunk in chunks:
        if chunk in ('......', '.....O', '.O.OOO'):
            modes = {'number': chunk == '.O.OOO', 'capital': chunk == '.....O'}
            if chunk == '......':
                result.append(' ')
        elif modes['number']:
            result.append(english_braille_num.get(chunk, ''))
        else:
            letter = english_braille_alpha.get(chunk, '')
            result.append(letter.upper() if modes['capital'] else letter)
            modes['capital'] = False

    return ''.join(result)

# English to Braille
def english_to_braille(input_string):
    result = []
    is_number_mode = False

    for char in input_string:
        if char.isalpha():  # Handle letters
            if char.isupper():
                result.append('.....O' + braille_alphabet[char.lower()])
            else:
                result.append(braille_alphabet[char])
        elif char.isdigit():  # Handle numbers
            if not is_number_mode:
                result.append('.O.OOO')
                is_number_mode = True
            result.append(braille_numbers[char])
        elif char == ' ':  # Handle spaces
            is_number_mode = False
            result.append('......')

    return ''.join(result)

# Main for input detection and translation
def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 translator.py <input_to_translate>")

    input_text = " ".join(sys.argv[1:])
    is_braille = detect_language(input_text)
    if is_braille == 'braille':
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
