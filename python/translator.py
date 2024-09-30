import sys

# Braille alphabet mapping (raised dots as O, empty dots as .)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '..O.OO', ',': '..O...', '?': '..OO.O', '!': '..OOO.', ';': '..O.O.', '-': '..O..O'
}

# Reverse mapping to go from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Braille capital sign for raised dots indicating capital letters
capital_sign = '.....O'

def is_braille(input_string):
    """Determine if the input string is Braille based on dot pattern."""
    return all(c in 'O.' for c in input_string)

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_output = ''
    for char in text:
        if char.isupper():
            # Add the capital sign before uppercase letters
            braille_output += capital_sign + braille_dict[char.lower()]
        elif char in braille_dict:
            braille_output += braille_dict[char.lower()]
    return braille_output

def translate_to_english(braille_text):
    """Translate Braille to English."""
    english_output = ''
    i = 0
    while i < len(braille_text):
        # Check for the capital sign
        if braille_text[i:i+6] == capital_sign:
            i += 6  # Skip the capital sign
            # Get the next Braille character and capitalize it
            braille_char = braille_text[i:i+6]
            if braille_char in reverse_braille_dict:
                english_output += reverse_braille_dict[braille_char].upper()
        else:
            braille_char = braille_text[i:i+6]
            if braille_char in reverse_braille_dict:
                english_output += reverse_braille_dict[braille_char]
        i += 6
    return english_output

def braille_translator(input_string):
    """Main function to translate between Braille and English."""
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_string>")
    else:
        input_string = sys.argv[1]
        result = braille_translator(input_string)
        print(result)
