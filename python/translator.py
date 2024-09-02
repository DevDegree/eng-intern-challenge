import sys

# Braille mappings for the alphabet (lowercase)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

# Braille mappings for capitalization and numbers
capital_prefix = '.....O'
number_prefix = '.O.OOO'

# Braille mappings for numbers (0-9)
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Invert the dictionaries for reverse lookup
inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
inverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def translate(input_string):
    # Check if the input is Braille
    if len(input_string) % 6 == 0 and all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

def english_to_braille(input_string):
    result = []
    number_mode = False
    for char in input_string:
        if char.isupper():
            result.append(capital_prefix)
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                result.append(number_prefix)
                number_mode = True
            result.append(braille_numbers[char])
        else:
            if number_mode:
                number_mode = False  # Reset after non-digit
            result.append(braille_alphabet[char])
    return ''.join(result)


def braille_to_english(input_string):
    result = []
    i = 0
    number_mode = False
    while i < len(input_string):
        current_symbol = input_string[i:i+6]
        if current_symbol == capital_prefix:
            i += 6
            current_symbol = input_string[i:i+6]
            result.append(inverse_braille_alphabet[current_symbol].upper())
        elif current_symbol == number_prefix:
            number_mode = True
        elif current_symbol == '......':  # Space
            result.append(' ')
            number_mode = False  # Reset number mode after a space
        elif number_mode:
            result.append(inverse_braille_numbers[current_symbol])
        else:
            result.append(inverse_braille_alphabet[current_symbol])
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    # Join the arguments to handle spaces in input
    input_string = ' '.join(sys.argv[1:])

    # Automatically determine translation direction
    translated_output = translate(input_string)
    print(translated_output)

if __name__ == "__main__":
    main()
