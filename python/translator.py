import sys

# Define the mappings for Braille and English characters
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}

CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'
BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings from Braille to English
REVERSE_BRAILLE_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
REVERSE_BRAILLE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

# Function to translate from English to Braille
def english_to_braille(input):
    result = []
    number_mode = False  # Track if we are in number mode

    for char in input:
        if char.isupper():
            result.append(CAPITAL_MARKER)  # Add the capital marker before capital letters
            result.append(BRAILLE_ALPHABET[char.lower()])
            number_mode = False  # Exit number mode if we encounter a capital letter
        elif char.isdigit():
            if not number_mode:
                result.append(NUMBER_MARKER)  # Only add the number marker once
                number_mode = True  # Enter number mode
            result.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            result.append(BRAILLE_ALPHABET[' '])  # Add space for spaces
            number_mode = False  # Reset number mode after space
        else:
            result.append(BRAILLE_ALPHABET.get(char, '......'))  # Default to space for unknown chars
            number_mode = False  # Reset number mode after a non-number character

    return ''.join(result)

# Function to translate from Braille to English
def braille_to_english(input):
    result = []
    capitalize_next = False
    number_mode = False

    # Process each 6-character Braille symbol
    for i in range(0, len(input), 6):
        symbol = input[i:i+6]

        if symbol == CAPITAL_MARKER:
            capitalize_next = True
            continue
        elif symbol == NUMBER_MARKER:
            number_mode = True
            continue

        if number_mode:
            result.append(REVERSE_BRAILLE_NUMBERS.get(symbol, ''))
            number_mode = False
        else:
            char = REVERSE_BRAILLE_ALPHABET.get(symbol, '')
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char)

    return ''.join(result)

# Main function to run the translator
if __name__ == '__main__':
    input_text = sys.argv[1]  # Take input from command line

    # Determine if the input is English or Braille
    if all(c in 'O.' for c in input_text):  # If the input contains only 'O' and '.'
        print(braille_to_english(input_text))  # Translate from Braille to English
    else:
        print(english_to_braille(input_text))  # Translate from English to Braille
