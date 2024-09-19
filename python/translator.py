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
    ('OO', '.O', 'OO'): 'y', ('O.', '.O', 'OO'): 'z',
    # Capital sign
    ('..', '..', '.O'): 'CAP',  # Used to capitalize the next letter
    # Numbers (using the same pattern as letters a-j, but prefixed with the number sign)
    ('..', 'OO', 'O.'): '1', ('..', 'OO', 'OO'): '2', ('..', 'O.', 'O.'): '3',
    ('..', 'O.', 'OO'): '4', ('..', '.O', 'O.'): '5', ('..', 'O.', '.O'): '6',
}

# Reverse the mapping for English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Helper function to detect whether input is in English or Braille
def is_braille(input_string):
    return all(char in ('O', '.') for char in input_string)

# This function processes the Braille input in sets of 3 lines (since Braille letters are formed with 3 rows).
def translate_braille_to_english(braille_input):
    # Split the input into chunks of two characters per line (since Braille uses two dots per row).
    lines = [braille_input[i:i + 2] for i in range(0, len(braille_input), 2)]

    # To store the output English characters.
    english_output = []

    # Track if the next letter should be capitalized (after encountering a 'CAP' sign in Braille).
    capital_next = False

    # Process 3-line chunks, since Braille letters are defined by 3 rows.
    for i in range(0, len(lines), 3):
        braille_char = tuple(lines[i:i + 3])

        # If the Braille character is the capitalization sign, set the flag and continue to the next character.
        if braille_char == ('..', '..', '.O'):
            capital_next = True
            continue

        # Lookup the letter in the Braille-to-English dictionary.
        letter = braille_to_english.get(braille_char, '?')

        # If the capitalization flag is set, convert the letter to uppercase.
        if capital_next:
            letter = letter.upper()
            capital_next = False  # Reset capitalization flag.

        # Add the letter to the output list.
        english_output.append(letter)

    # Join the list of letters into a final string.
    return ''.join(english_output)