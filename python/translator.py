import sys

# Constants for Braille indicators
NUMERIC_PREFIX = '.O.OOO'
CAPITAL_PREFIX = '.....O'

# Dictionary for Braille to English letter conversion
braille_to_letter = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

# Dictionary for Braille to English number conversion
braille_to_number = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def validate_braille_characters(braille_text):
    """Checks if the given text is in Braille format."""
    for character in braille_text:
        if character != 'O' and character != '.':
            return False
    return True

def translate_braille_to_text(braille_text):
    """Converts Braille text to English letters and numbers."""
    text_lookup = {v: k for k, v in braille_to_letter.items()}
    number_lookup = {v: k for k, v in braille_to_number.items()}
    translated_text = ""
    number_mode = False
    capital_mode = False

    # Process every 6 characters as one Braille character
    for index in range(0, len(braille_text), 6):
        braille_character = braille_text[index:index + 6]

        # Check for special Braille indicators
        if braille_character == NUMERIC_PREFIX:
            number_mode = True
            continue
        if braille_character == CAPITAL_PREFIX:
            capital_mode = True
            continue
        
        # Translate Braille characters to English
        if braille_character in text_lookup:
            if braille_character == '......':
                number_mode = False  # Reset after space
            if number_mode:
                translated_text += number_lookup[braille_character]
            elif capital_mode:
                translated_text += text_lookup[braille_character].upper()
                capital_mode = False
            else:
                translated_text += text_lookup[braille_character]
    return translated_text

def convert_text_to_braille(plain_text):
    """Converts English text to Braille characters."""
    braille_output = ""
    numeric_mode = False

    for char in plain_text:
        if char.isdigit():
            if not numeric_mode:
                braille_output += NUMERIC_PREFIX
                numeric_mode = True
            braille_output += braille_to_number[char]
        elif char == ' ':
            numeric_mode = False
            braille_output += braille_to_letter[char]
        elif char.isalpha():
            if char.isupper():
                braille_output += CAPITAL_PREFIX
            braille_output += braille_to_letter[char.lower()]
    return braille_output

def main():
    if len(sys.argv) < 2:
        return

    input_text = ' '.join(sys.argv[1:])
    
    # Determine the conversion direction and print the result
    if validate_braille_characters(input_text[0]):
        print(translate_braille_to_text(input_text))
    else:
        print(convert_text_to_braille(input_text))

if __name__ == "__main__":
    main()
