import sys

# Braille mappings for the alphabet and space.
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'  # Space in Braille
}

# Special Braille signs for capitalization and numbers
capital_sign = '.....O'
number_sign = '.O.OOO'

# Braille mappings for numbers (0-9).
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse lookup dictionaries for Braille-to-English translation.
inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
inverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_string):
    """
    Check if the input string is written in Braille.
    Braille consists of only 'O' (raised dot) and '.' (no dot).
    """
    return all(c in 'O.' for c in input_string)

def english_to_braille(text):
    """
    Translate English text to Braille.
    Handles uppercase letters and numbers. Adds necessary Braille signs.
    """
    result = []
    number_mode = False  # Tracks if we're in number mode.

    for char in text:
        # Handle capitalization
        if char.isupper():
            result.append(capital_sign)
            char = char.lower()  # Convert to lowercase for mapping.

        # Handle digits
        if char.isdigit():
            if not number_mode:
                result.append(number_sign)  # Enter number mode if needed.
                number_mode = True
            result.append(braille_numbers[char])
        else:
            # Exiting number mode after encountering a non-number.
            if number_mode and char != ' ':
                number_mode = False
            result.append(braille_alphabet[char])
    
    return ''.join(result)

def braille_to_english(braille):
    """
    Translate Braille back to English.
    Handles capitalization, numbers, and spaces.
    """
    result = []
    i = 0
    number_mode = False  # Indicates whether numbers are being read.
    capital_mode = False  # Indicates whether the next letter should be capitalized.

    while i < len(braille):
        current_symbol = braille[i:i+6]  # Read each Braille symbol (6 characters).

        # Handle capitalization
        if current_symbol == capital_sign:
            capital_mode = True
        # Handle number mode
        elif current_symbol == number_sign:
            number_mode = True
        # Handle spaces
        elif current_symbol == '......':
            result.append(' ')
            number_mode = False  # Exit number mode on encountering space.
        else:
            if number_mode:
                # Translate numbers in Braille mode.
                result.append(inverse_braille_numbers.get(current_symbol, '?'))
            else:
                # Translate regular letters.
                letter = inverse_braille_alphabet.get(current_symbol, '?')
                if capital_mode:
                    letter = letter.upper()  # Capitalize the letter.
                    capital_mode = False  # Reset capital mode after one letter.
                result.append(letter)
        i += 6  # Move to the next Braille symbol.
    
    return ''.join(result)

def main():
    # Get input from the command line.
    input_string = ' '.join(sys.argv[1:]).strip()  # Read and sanitize the input.

    if is_braille(input_string):
        # If input is Braille, translate to English.
        print(braille_to_english(input_string))
    else:
        # If input is English, translate to Braille.
        print(english_to_braille(input_string))

if __name__ == '__main__':
    main()
