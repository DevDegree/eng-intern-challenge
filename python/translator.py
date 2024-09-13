import sys

braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_punctuation = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', 
    '(': 'O.O..O', ')': '.O.OO.'
}

braille_markers = {
    'capitalFollows': '.....O',
    'numberFollows': '.O.OOO',
    ' ': '......'
}

# Reverse mappings for translating Braille back to English
english_from_braille_letters = {v: k for k, v in braille_letters.items()}
english_from_braille_numbers = {v: k for k, v in braille_numbers.items()}
english_from_braille_punctuation = {v: k for k, v in braille_punctuation.items()}
english_from_braille_markers = {
    braille_markers[' ']: ' ',
    braille_markers['capitalFollows']: 'CAPITAL_MARKER',
    braille_markers['numberFollows']: 'NUMBER_MARKER'
}

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def translate_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(braille_markers['capitalFollows'])
            result.append(braille_letters[char.lower()])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(braille_markers['numberFollows'])
                number_mode = True
            result.append(braille_numbers[char])
        elif char in braille_punctuation:
            result.append(braille_punctuation[char])
            number_mode = False
        else:
            if number_mode:
                number_mode = False
            result.append(braille_letters.get(char, braille_markers[' ']))

    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    capital = False
    number_mode = False

    while i < len(braille):
        current_braille = braille[i:i+6]

        # Check for special markers first
        if current_braille in english_from_braille_markers:
            marker = english_from_braille_markers[current_braille]
            if marker == 'CAPITAL_MARKER':
                capital = True
                number_mode = False
            elif marker == 'NUMBER_MARKER':
                number_mode = True
            elif marker == ' ':
                result.append(' ')
            i += 6
            continue

        if number_mode:
            letter = english_from_braille_numbers.get(current_braille, ' ')
            if not letter.isdigit():  # Reset number mode if it's not a digit
                number_mode = False
                letter = (
                english_from_braille_letters.get(current_braille) or
                english_from_braille_punctuation.get(current_braille) or
                ' '
            )
        else:
            letter = (
                english_from_braille_letters.get(current_braille) or
                english_from_braille_punctuation.get(current_braille) or
                ' '
            )

        # Handle capitalization
        if capital and letter.isalpha():
            letter = letter.upper()
            capital = False

        result.append(letter)
        i += 6

    return ''.join(result).strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string to translate>")
        sys.exit(1)

    # Join all command-line arguments into one input string
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))



