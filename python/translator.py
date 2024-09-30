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
number_sign = '.O.OOO'  # Braille number sign to indicate numbers

def is_braille(input_string):
    """Determine if the input string is Braille based on dot pattern."""
    return all(c in 'O.' for c in input_string)

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_output = ''
    is_number = False
    for char in text:
        if char.isupper():
            # Add the capital sign before uppercase letters
            braille_output += capital_sign + braille_dict[char.lower()]
        elif char.isdigit():
            if not is_number:  # Add number sign before first digit
                braille_output += number_sign
                is_number = True
            braille_output += braille_dict[char]
        elif char == ' ':
            is_number = False  # Reset number flag on space
            braille_output += braille_dict[' ']
        elif char in braille_dict:
            is_number = False
            braille_output += braille_dict[char]
    return braille_output

def translate_to_english(braille_text):
    """Translate Braille to English."""
    english_output = ''
    i = 0
    is_capital = False
    is_number = False
    while i < len(braille_text):
        # Check for the capital sign
        if braille_text[i:i+6] == capital_sign:
            is_capital = True
            i += 6  # Skip the capital sign
        elif braille_text[i:i+6] == number_sign:
            is_number = True
            i += 6  # Skip the number sign
        else:
            braille_char = braille_text[i:i+6]
            if braille_char in reverse_braille_dict:
                char = reverse_braille_dict[braille_char]
                if is_capital:
                    char = char.upper()
                    is_capital = False
                if is_number:
                    # Reset number state after one translation
                    is_number = False
                english_output += char
            i += 6
    return english_output

def braille_translator(input_string):
    """Main function to translate between Braille and English."""
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
    else:
        # Join all arguments into a single string to handle multi-word input
        input_string = ' '.join(sys.argv[1:])
        result = braille_translator(input_string)
        print(result)
