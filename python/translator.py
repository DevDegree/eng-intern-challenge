import sys

# English to Braille dictionary
english_to_braille = {
    # Letters a-z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Numbers 0-9 (Braille numbers are represented by A-J with a preceding number sign)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '#': '.O.OOO',  # Number sign (updated to match expected output)

    # Punctuation and symbols
    '.': '..OO.O', ',': 'O.....', '?': '..O.OO', '!': '..OOO.', ':': 'OO....',
    ';': 'O.O...', '-': '....OO', '/': 'O.OO..', '(': 'OOO...', ')': 'OO.O..',
    '<': 'OOO...', '>': 'OO.O..', ' ': '......',  # Space

    # Capital, decimal, and number follows symbols
    'capital_follows': '.....O',   # Capital follows symbol
    'decimal_follows': '..O.OO',   # Decimal follows symbol
    'number_follows': '.O.OOO'      # Number follows symbol (updated)
}

# Braille to English dictionary (reverse of the above)
braille_to_english = {v: k for k, v in english_to_braille.items()}

# Add the capital, decimal, and number follows symbols to the Braille to English dictionary
braille_to_english.update({
    '.....O': 'capital_follows',
    '..O.OO': 'decimal_follows',
    '.O.OOO': 'number_follows'
})

# Mapping from Braille letters A-J to digits 1-0
braille_number_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Inverse mapping for numbers
braille_number_map_inverse = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

def translate_braille_to_english(braille_input):
    english_output = ""
    capitalize_next = False
    number_mode = False
    decimal_mode = False
    first_decimal_number = True  # To handle decimal point insertion

    # Split the braille input into individual braille symbols (assuming a space between each symbol)
    braille_chars = braille_input.split()

    for braille_char in braille_chars:
        # Handle capitalization follows
        if braille_char == english_to_braille['capital_follows']:
            capitalize_next = True
            continue

        # Handle number follows symbol
        if braille_char == english_to_braille['number_follows']:
            number_mode = True
            decimal_mode = False  # Exit decimal mode if active
            first_decimal_number = True
            continue

        # Handle decimal follows symbol
        if braille_char == english_to_braille['decimal_follows']:
            decimal_mode = True
            number_mode = True  # Decimal mode is a subset of number mode
            first_decimal_number = True
            continue

        # Look up the English translation for the current braille character
        english_char = braille_to_english.get(braille_char, '')

        # If braille_char is space, reset modes
        if english_char == ' ':
            number_mode = False
            decimal_mode = False
            english_output += ' '
            continue

        # If in number mode and braille_char represents a number
        if number_mode and braille_char in braille_number_map:
            number = braille_number_map[braille_char]
            # If in decimal mode, insert a decimal point before the first number
            if decimal_mode and first_decimal_number:
                english_output += '.'
                first_decimal_number = False
            english_char = number

        # If capitalization is required
        if capitalize_next:
            english_char = english_char.upper()
            capitalize_next = False

        # Append the translated English character to the output
        english_output += english_char

    return english_output

def translate_english_to_braille(english_input):
    braille_output = ""
    number_mode = False
    decimal_mode = False

    # Iterate over each character in the input string
    i = 0
    while i < len(english_input):
        char = english_input[i]

        # Handle capitalization
        if char.isupper():
            braille_output += english_to_braille['capital_follows']
            char = char.lower()

        # Handle digits
        if char.isdigit():
            if not number_mode:
                # Add the "number follows" symbol only once at the start of a number sequence
                braille_output += english_to_braille['number_follows']
                number_mode = True
                decimal_mode = False  # Ensure decimal mode is off
            # Map numbers to corresponding Braille (1 -> 'a', 2 -> 'b', etc.)
            braille_char = english_to_braille.get(braille_number_map_inverse.get(char, ''), '')
            braille_output += braille_char
            i += 1
            continue

        # Handle decimal point
        if char == '.':
            braille_output += english_to_braille['decimal_follows']
            decimal_mode = True
            number_mode = True  # Decimal mode implies number mode
            i += 1
            continue

        # Reset number mode when a non-digit character is encountered
        if not char.isdigit() and number_mode:
            number_mode = False
            decimal_mode = False

        # Look up the Braille representation for the current English character
        braille_char = english_to_braille.get(char.lower(), '')
        if braille_char:
            braille_output += braille_char

        i += 1

    return braille_output

def is_braille_or_english(input_string):
    """
    Check if the input string is in Braille or English.
    Braille patterns are composed of dot patterns (like 'O.....').
    English inputs are alphabetic characters, numbers, or punctuation.
    """
    # Check for a Braille pattern (only 'O' and '.' characters)
    if all(char in 'O.' for char in input_string.replace(' ', '')):
        # Additionally, ensure the length is a multiple of 6
        if len(input_string.replace(' ', '')) % 6 == 0:
            return "Braille"

    # Check for English characters (letters, numbers, and punctuation)
    elif any(char.isalnum() or char in ".,?!:;-()/" for char in input_string):
        return "English"

    # If it doesn't match either, return unknown
    return "Unknown"

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    # Join all arguments into a single string separated by spaces
    input_string = ' '.join(sys.argv[1:])
    detected_language = is_braille_or_english(input_string)

    if detected_language == "Braille":
        translated = translate_braille_to_english(input_string)
        print(translated)
    elif detected_language == "English":
        translated = translate_english_to_braille(input_string)
        print(translated)
    else:
        print("Unknown input type. Please provide valid English or Braille input.")

if __name__ == "__main__":
    main()
