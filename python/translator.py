import sys

# Function to detect input type (either English or Braille)


def detect_input_type(input_string):
    # Check if the input contains Braille symbols (O and . only)
    if all(c in "O. " for c in input_string):
        return "Braille"
    else:
        return "English"


# Dictionary for letters and numbers
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}


# Special characters and punctuations
braille_special = {
    "..O...": ",",        # Comma
    "..OO..": ";",        # Semicolon
    "..OOO.": ":",        # Colon
    "..O.O.": ".",        # Period
    ".O..O.": "!",        # Exclamation mark
    ".O.O..": "?",        # Question mark
    "....O.": "'",        # Apostrophe
    "....OO": "-",        # Dash
    "..O.OO": "/",        # Slash
    "..OO.O": "<",        # Less than
    ".O.OO.": ">",        # Greater than
    ".OO..O": "(",        # Open parenthesis
    ".OO.OO": ")"         # Close parenthesis
}


def braille_to_english(braille_string):
    result = []
    is_number_mode = False  # Check if we are currently in number mode
    capitalize_next = False  # Check if the next letter should be capitalized

    # Split the Braille string into 6-character groups
    braille_chars = [braille_string[i:i+6]
                     for i in range(0, len(braille_string), 6)]

    for braille_char in braille_chars:
        if braille_char == braille_letters['number']:  # Number indicator
            is_number_mode = True
        elif braille_char == braille_letters[' ']:  # Space
            result.append(" ")
            is_number_mode = False  # Reset to letter mode after a space
        elif braille_char == braille_letters['capital']:  # Capital indicator
            capitalize_next = True
        elif braille_char in braille_special:
            result.append(braille_special[braille_char])
        else:
            # Handle both numbers and letters
            if is_number_mode:
                # Look for digits first
                char = next((k for k, v in braille_letters.items()
                            if v == braille_char and k.isdigit()), "?")
                if char == "?":
                    # If not a digit, reset number mode
                    is_number_mode = False
                    # Look for letters (if not found in numbers)
                    char = next((k for k, v in braille_letters.items()
                                if v == braille_char and k.isalpha()), "?")
            else:
                char = next((k for k, v in braille_letters.items()
                            if v == braille_char and k.isalpha()), "?")

            if capitalize_next:
                char = char.upper()
                capitalize_next = False  # Reset capitalization after use

            result.append(char)

    return "".join(result)


def english_to_braille(input_string):
    result = []
    is_number = False

    for char in input_string:
        if char.isdigit():
            if not is_number:
                # Add the number indicator
                result.append(braille_letters['number'])
                is_number = True
            result.append(braille_letters[char])
        elif char.isalpha():
            if char.isupper():
                # Add the capital letter indicator
                result.append(braille_letters['capital'])
                result.append(braille_letters[char.lower()])
            else:
                result.append(braille_letters[char])
            is_number = False
        elif char == ' ':
            result.append(braille_letters[' '])
            is_number = False
        else:
            # Handle special characters
            result.append(
                next((v for k, v in braille_special.items() if k == char), "?"))

    return ''.join(result)


if __name__ == "__main__":
    # Check if there are sufficient arguments
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input_string>")
        sys.exit(1)

    # Join all command-line arguments into a single string
    input_string = " ".join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "English":
        print(english_to_braille(input_string))
    elif input_type == "Braille":
        print(braille_to_english(input_string))
    else:
        print("Invalid input.")
