import sys

# Define the Braille alphabet (lowercase letters and numbers)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Define special symbols for capitalization and numbers
braille_capital = '.....O'
braille_number = '.O.OOO'

# Reverse the braille_alphabet dictionary for Braille-to-English conversion
english_alphabet = {v: k for k, v in braille_alphabet.items()}

def translate_to_braille(text):
    """Converts English text to Braille."""
    braille_translation = []
    number_mode = False
    for char in text:
        if char.isupper():
            braille_translation.append(braille_capital)
            braille_translation.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            if not number_mode:
                braille_translation.append(braille_number)
                number_mode = True
            braille_translation.append(braille_alphabet[char])
        else:
            if number_mode:
                number_mode = False  # Reset number mode after encountering a non-digit
            braille_translation.append(braille_alphabet[char])
    return ''.join(braille_translation)

def translate_to_english(braille_text):
    """Converts Braille to English text."""
    english_translation = []
    i = 0
    capital_mode = False
    number_mode = False
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        if braille_char == braille_capital:
            capital_mode = True
        elif braille_char == braille_number:
            number_mode = True
        else:
            char = english_alphabet[braille_char]
            if capital_mode:
                char = char.upper()
                capital_mode = False  # Only capitalize the next character
            if number_mode and char.isalpha():
                char = str(ord(char) - ord('a') + 1)  # Convert to number (1-9)
                number_mode = False  # Reset number mode after translation
            english_translation.append(char)
        i += 6
    return ''.join(english_translation)

def is_braille(text):
    """Checks if the input text is in Braille format."""
    return all(c == 'O' or c == '.' for c in text)

if __name__ == "__main__":
    # Read the input string from the command line
    input_string = sys.argv[1]

    if is_braille(input_string):
        # Translate from Braille to English
        print(translate_to_english(input_string))
    else:
        # Translate from English to Braille
        print(translate_to_braille(input_string))
