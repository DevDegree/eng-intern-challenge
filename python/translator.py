# Braille to English mapping (Braille represented as a tuple of 'O' and '.')

braille_to_english = {
    ('O.', '..', '..'): 'a', ('O.', 'O.', '..'): 'b', ('OO', '..', '..'): 'c',
    ('OO', '.O', '..'): 'd', ('O.', '.O', '..'): 'e', ('OO', 'O.', '..'): 'f',
    ('OO', 'OO', '..'): 'g', ('O.', 'OO', '..'): 'h', ('.O', 'O.', '..'): 'i',
    ('.O', 'OO', '..'): 'j', ('O.', '..', 'O.'): 'k', ('O.', 'O.', 'O.'): 'l',
    ('OO', '..', 'O.'): 'm', ('OO', '.O', 'O.'): 'n', ('O.', '.O', 'O.'): 'o',
    ('OO', 'O.', 'O.'): 'p', ('OO', 'OO', 'O.'): 'q', ('O.', 'OO', 'O.'): 'r',
    ('.O', 'O.', 'O.'): 's', ('.O', 'OO', 'O.'): 't', ('O.', '..', 'OO'): 'u',
    ('O.', 'O.', 'OO'): 'v', ('.O', 'OO', '.O'): 'w', ('OO', '..', 'OO'): 'x',
    ('OO', '.O', 'OO'): 'y', ('O.', '.O', 'OO'): 'z', ('..', 'OO', '.O'): '.',
    ('..', 'O.', '..'): ',', ('..', 'O.', 'OO'): '?', ('..', 'OO', 'O.'): '!',
    ('..', 'OO', '..'): ':', ('..', 'O.', 'O.'): ';', ('..', '..', 'OO'): '-',
    ('.O', '..', 'O.'): '/', ('.O', 'O.', '.O'): '<', ('OO', 'OO', '.O'): '>',
    ('O.', 'O.', '.O'): '(', ('.O', '.O', 'O.'): '('
}

braille_to_number = {
    '1': ('O.', '..', '..'), '2': ('O.', 'O.', '..'), '3': ('OO', '..', '..'),
    '4': ('OO', '.O', '..'), '5': ('O.', '.O', '..'), '6': ('OO', 'O.', '..'),
    '7': ('OO', 'OO', '..'), '8': ('O.', 'OO', '..'), '9': ('.O', 'O.', '..')
}

capital_ahead = '.....O'
decimal_ahead = '.O...O'
number_ahead = '.O.OOO'
space_ahead = '......'


# Create the reverse dictionary with joined strings
number_to_braille = {k: ''.join(v) for k, v in braille_to_number.items()}

english_to_braille = {v: ''.join(k) for k, v in braille_to_english.items()}

def is_braille(input_string):
    """Helper function to detect whether input is in English or Braille"""
    return all(char in ('O', '.') for char in input_string)

def translate_braille_to_english(braille_string):
    """This function translates the given braille string to english."""
    if len(braille_string) % 6 != 0:
        raise ValueError("Invalid Braille string. Length must be divisible by 6.")

    # Split the input into chunks of six characters per line
    substrings = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]
    english_output = []

    capital_next = False
    number_next = False

    for substring in substrings:
        if substring == capital_ahead:
            capital_next = True
            continue
        elif substring == number_ahead:
            number_next = True
            continue
        elif substring == space_ahead:
            english_output.append(' ')
            number_next = False
            continue

        # Handle numbers
        if number_next:
            english_output.append(next(key for key, value in number_to_braille.items() if value == substring))
            continue

        # Handle capital letters
        if capital_next:
            english_output.append(next(key.upper() for key, value in english_to_braille.items() if value == substring))
            capital_next = False
            continue

        # Handle regular letters and punctuation
        english_output.append(next(key for key, value in english_to_braille.items() if value == substring))

    return ''.join(english_output)


# Translate English to Braille
def translate_english_to_braille(english_input):
    """This function processes each English character and translates it into the corresponding Braille pattern."""
    braille_output = []
    in_number_mode = False  # To track if we're currently in a chain of numbers

    for char in english_input:
        if char == ' ':
            braille_output.extend(space_ahead)
            in_number_mode = False  # Reset the number mode after encountering a space
        elif char.isupper():
            char = char.lower()
            braille_output.extend(capital_ahead)
            braille_output.extend(english_to_braille[char])
            in_number_mode = False  # Exiting number mode when encountering a letter
        elif char.isdigit():
            if not in_number_mode:
                braille_output.extend(number_ahead)
                in_number_mode = True  # Enter number mode
            braille_output.extend(number_to_braille[char])
        elif char == '.':
            braille_output.extend(decimal_ahead)
            in_number_mode = False  # Exiting number mode for non-number characters
        else:
            braille_output.extend(english_to_braille[char])
            in_number_mode = False  # Exiting number mode when encountering a letter

    # Join the list of Braille patterns into a final string.
    return ''.join(braille_output)


def braille_translator(input_string):
    """Main function to handle translation. This function first detects if the input is Braille or English and calls
    the appropriate translation function. """
    # If the input contains only 'O' and '.', treat it as Braille input. There might be some edge cases.
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    else:
        # Otherwise, assume it's English and translate to Braille.
        return translate_english_to_braille(input_string)


# This block makes the script executable from the command line.
if __name__ == "__main__":
    # Take input from the user via the terminal.
    user_string = input()

    # Call the translator function and print the result.
    print(braille_translator(user_string))