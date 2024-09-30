import sys

# Braille alphabet and punctuation dictionary
braille_translation = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# Braille number dictionary
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

reverse_braille_translation = {value: key for key, value in braille_translation.items()}
reverse_braille_numbers = {value: key for key, value in braille_numbers.items()}

# Convert regular text to braille
def text_to_braille(text):
    result = ''
    in_number_mode = False

    for character in text:
        # Handle numbers
        if character.isdigit():
            if not in_number_mode:
                result += braille_translation['number']
            result += braille_numbers[character]
            in_number_mode = True
        # Handle capital letters
        elif character.isupper():
            result += braille_translation['capital']
            result += braille_translation[character.lower()]
            in_number_mode = False
        # Handle lowercase letters and punctuation
        else:
            result += braille_translation.get(character, '......')
            in_number_mode = False

    return result

# Convert braille to regular text
def braille_to_text(braille_code):
    output = ''
    capital_next = False
    number_mode = False

    for idx in range(0, len(braille_code), 6):
        braille_char = braille_code[idx:idx+6]

        if braille_char == braille_translation['capital']:
            capital_next = True
        elif braille_char == braille_translation['number']:
            number_mode = True
        elif braille_char == '......':
            output += ' '
            number_mode = False
        elif number_mode:
            output += reverse_braille_numbers.get(braille_char, '?')
        else:
            char = reverse_braille_translation.get(braille_char, '?')
            if capital_next:
                output += char.upper()
                capital_next = False
            else:
                output += char

    return output

# Main function to handle the input and switch between modes
def process_input():
    input_text = " ".join(sys.argv[1:])
    if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))

if __name__ == "__main__":
    process_input()
