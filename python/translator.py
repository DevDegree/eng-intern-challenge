"""
This module translates text between English and Braille.
"""
import sys

# Dictionary mapping English alphabet to Braille patterns
ENGLISH_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

# Dictionary mapping digits to Braille patterns
ENGLISH_DIGITS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings from Braille to English alphabet and digits
BRAILLE_DICT = {value: key for key, value in ENGLISH_DICT.items()}
BRAILLE_DIGITS = {value: key for key, value in ENGLISH_DIGITS.items()}


# Function to translate English text to Braille
def translate_english_to_braille(input_text: str) -> str:
    """
    Translates English text to Braille.
    Args:
        input_text (str): The English text to translate.
    Returns:
        str: The translated Braille text.
    """
    outp = []  # Output list to collect Braille representation
    is_digit = False  # Flag to track if current context is numeric
    for char in input_text:
        # If we encounter a non-digit character while is_digit is set, reset the is_digit flag
        if is_digit and not char.isdigit():
            is_digit = False

        # Translate digits if is_digit flag is set
        if is_digit and char.isdigit():
            outp.append(ENGLISH_DIGITS[char])
        elif char.isupper():
            # Add capital Braille prefix and then lowercase equivalent
            outp.append(ENGLISH_DICT['capital'])
            outp.append(ENGLISH_DICT[char.lower()])
        elif char.islower():
            # Translate lowercase letters directly
            outp.append(ENGLISH_DICT[char])
        elif char.isdigit():
            # Set is_digit flag and translate the digit
            is_digit = True
            outp.append(ENGLISH_DICT['number'])
            outp.append(ENGLISH_DIGITS[char])
        elif char.isspace():
            # Add space in Braille
            outp.append(ENGLISH_DICT[' '])
        else:
            # Handle unexpected characters
            raise ValueError(f"Unexpected character encountered: {char}")


    # Join the Braille list into a single string and return
    return ''.join(outp)

# Function to translate Braille to English text
def translate_braille_to_english(input_text: str) -> str:
    """
    Translates Braille text to English.
    Args:
        input_text (str): The Braille text to translate.
    Returns:
        str: The translated English text.
    """
    outp = []  # Output list to collect English representation
    is_digit = False  # Flag to track if current context is numeric
    is_capital = False  # Flag to track if the next letter is capitalized
    # Constants for special Braille patterns
    CAPITAL_INDICATOR = '.....O'
    NUMBER_INDICATOR = '.O.OOO'
    BRAILLE_SPACE = '......' # 
    for i in range(0, len(input_text), 6):
        char = input_text[i:i+6]  # Each Braille character is 6 characters long

        # Handle Braille space pattern
        if char == BRAILLE_SPACE and not is_digit:
            outp.append(' ')
            continue

        if char not in BRAILLE_DICT and char not in BRAILLE_DIGITS:
            raise ValueError(f"Error: Undefined Braille pattern encountered - '{char}'")

        if is_capital:
            # Convert to uppercase English letter is flag is set
            outp.append(BRAILLE_DICT[char].upper())
            is_capital = False
        elif is_digit:
            # Check for space to reset digit context, otherwise convert digit
            if char == BRAILLE_SPACE:
                is_digit = False
                outp.append(BRAILLE_DICT[char])
            else:
                outp.append(BRAILLE_DIGITS[char])
        elif char == CAPITAL_INDICATOR:
            # If Braille capital indicator, set is_capital flag
            is_capital = True
        elif char == NUMBER_INDICATOR:
            # If Braille number indicator, set is_digit flag
            is_digit = True
        else:
            # Convert Braille to corresponding English character
            outp.append(BRAILLE_DICT[char])
    return ''.join(outp)

def main():
    # Check if there are any command-line arguments
    if len(sys.argv) <= 1:
        # If no input is given, print instructions and exit
        print("No command-line arguments were given. Enter an input after the program.")
        sys.exit()
    
    # Determine if the input is English or Braille based on the first argument
    is_english = not all(char in 'O.' for char in sys.argv[1])

    # Gather the input string
    input_text = ' '.join(sys.argv[1:]) if is_english else sys.argv[1]
    # Translate the input
    output = translate_english_to_braille(input_text) if is_english else translate_braille_to_english(input_text)

    # Print the translated output
    print(output)

if __name__ == "__main__":
    main()