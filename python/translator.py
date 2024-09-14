import sys

# Braille dictionary mapping characters (letters, numbers, punctuation) to their corresponding Braille patterns.
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    # 'cap' for capitalization, 'num' for numeric mode
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.'
}

# Reverse mappings for Braille to characters (used in Braille to English translation)
braille_to_char = {v: k for k, v in braille_dict.items()}

# Function to check if the input consists only of Braille patterns ('O', '.', or space)


def is_braille(input_string):
    return all(c in {'O', '.', ' '} for c in input_string)

# Function to convert Braille patterns to English text


def braille_to_english(input_braille):
    # Remove any spaces between the Braille characters for consistent processing
    input_braille = ''.join(input_braille.split())

    # Split the Braille string into chunks of 6 dots (Braille characters)
    symbols = [input_braille[i:i+6] for i in range(0, len(input_braille), 6)]

    output = []
    capital_next = False  # Flag to track if the next letter should be capitalized
    number_mode = False   # Flag to track if the current mode is numeric

    for symbol in symbols:
        if symbol == braille_dict[' ']:  # Handle spaces in the Braille text
            output.append(' ')
            capital_next = number_mode = False  # Reset both flags after a space
        # Check if the next letter should be capitalized
        elif symbol == braille_dict['cap']:
            capital_next = True
        elif symbol == braille_dict['num']:  # Enter numeric mode
            number_mode = True
        else:
            # Convert Braille symbol to corresponding character
            char = braille_to_char.get(symbol)
            if char:
                if number_mode and char.isdigit():  # If in numeric mode, handle digits
                    output.append(char)
                elif capital_next:  # Handle capitalization of the next character
                    output.append(char.upper())
                    capital_next = False  # Reset capitalization flag
                else:
                    output.append(char)
                number_mode = False  # Exit numeric mode after processing a character
    return ''.join(output)  # Join the list into a final string

# Function to convert English text to Braille patterns


def english_to_braille(input_text):
    output = []
    number_mode = False  # Flag to track if numeric mode is active

    for char in input_text:
        if char == ' ':  # Handle spaces in English text
            output.append(braille_dict[' '])
            number_mode = False  # Reset numeric mode after a space
        elif char.isdigit():  # Handle numbers
            if not number_mode:  # If not already in number mode, add the number mode indicator
                output.append(braille_dict['num'])
                number_mode = True
            # Add the Braille pattern for the digit
            output.append(braille_dict[char])
        else:
            if number_mode:
                number_mode = False  # Exit numeric mode when switching to letters
            if char.isupper():  # Handle uppercase letters
                output.append(braille_dict['cap'])
                char = char.lower()  # Convert to lowercase for lookup
            braille_char = braille_dict.get(char)
            if braille_char:
                # Add the Braille pattern for the character
                output.append(braille_char)

    return ''.join(output)  # Join the list into the final Braille string


# Main logic to handle command-line input and perform the appropriate conversion
if __name__ == "__main__":
    # Collect input from command-line arguments
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        # Convert Braille input to English
        print(braille_to_english(input_string))
    else:
        # Convert English input to Braille
        print(english_to_braille(input_string))
