import sys

# Define mappings for Braille and English letters/numbers
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'  # Space in Braille is represented by six empty dots
}

# Special markers
braille_capital = '.....O'
braille_number = '.O.OOO'

# Braille mapping for digits (0-9)
braille_digits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


def is_braille(input_str):
    """Determine if the input is Braille by checking for 'O' and '.'"""
    return all(c in 'O.' for c in input_str)


def translate_to_braille(text):
    """Translate English text to Braille"""
    braille_translation = []
    number_mode = False  # Track when we're translating numbers
    for char in text:
        if char.isdigit() and not number_mode:
            braille_translation.append(braille_number)
            number_mode = True  # We're now in number mode
        elif not char.isdigit():
            number_mode = False  # No longer translating numbers
        if char.isupper():
            braille_translation.append(braille_capital)
            char = char.lower()

        if char.isdigit():
            braille_translation.append(braille_digits[char])
        else:
            braille_translation.append(braille_alphabet.get(char, '......'))

    return ''.join(braille_translation)


def translate_to_english(braille):
    """Translate Braille to English text"""
    i = 0
    english_translation = []
    is_number = False
    is_capital = False

    while i < len(braille):
        current_char = braille[i:i+6]

        if current_char == braille_capital:
            is_capital = True
            i += 6
            continue

        if current_char == braille_number:
            is_number = True
            i += 6
            continue

        if current_char == '......':
            english_translation.append(' ')
            is_number = False  # Exiting number mode
        else:
            if is_number:
                letter = next(
                    (k for k, v in braille_digits.items() if v == current_char), ' ')
            else:
                letter = next(
                    (k for k, v in braille_alphabet.items() if v == current_char), ' ')

            if is_capital:
                letter = letter.upper()
                is_capital = False  # Reset the capitalization
            english_translation.append(letter)

        i += 6

    return ''.join(english_translation)


def main(input_str):
    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        main(input_str)
    else:
        print("Please provide input to translate.")
