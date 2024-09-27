import sys

# Braille dictionary for English letters (a-z), space, and digits (0-9)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionaries to decode from Braille to English
braille_to_english = {v: k for k, v in braille_alphabet.items()}
braille_to_number = {v: k for k, v in braille_numbers.items()}

# Special prefixes
capital_prefix = '.....O'
number_prefix = '.O.OOO'

def translate_to_braille(text):
    """Translates English text to Braille."""
    braille_text = []
    is_space = False
    for char in text:
        print(char)
        if char.isdigit():
            # Add number prefix and then the Braille for the number
            if is_space==False:
                braille_text.append(number_prefix)
                is_space = True
            braille_text.append(braille_numbers[char])
            print(braille_text)
        elif char == ' ':
            # Handle spaces
            braille_text.append(braille_alphabet[' '])
            is_space = False
        elif char.isalpha():
            if char.isupper():
                # Add capital prefix before uppercase letters
                braille_text.append(capital_prefix)
            # Append the Braille for the letter (lowercase or uppercase treated the same here)
            braille_text.append(braille_alphabet[char.lower()])
            print(braille_text)
    return ''.join(braille_text)

def is_braille(text):
    """Checks if the input is Braille (valid Braille symbols)."""
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]
    print(sys.argv[0]+" "+ input_text)
    if is_braille(input_text):
        # Translate Braille to English
        print("Braille")
    else:
        # Translate English to Braille
        print("English")
        print(translate_to_braille(input_text))
