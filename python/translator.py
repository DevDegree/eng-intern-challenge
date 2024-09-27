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

# Special prefixes
capital_prefix = '.....O'
number_prefix = '.O.OOO'

def translate_to_braille(text):
    """Translates English text to Braille."""
    braille_text = []
    is_space = False
    for char in text:
        if char.isdigit():
            # Add number prefix and then the Braille for the number
            if is_space==False:
                braille_text.append(number_prefix)
                is_space = True
            braille_text.append(braille_numbers[char])
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
    return ''.join(braille_text)

def translate_to_english(braille):
    """Translates Braille text to English."""
    english_text = []
    is_capital = False
    is_number = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == capital_prefix:
            is_capital = True
            i += 6
            continue
        elif symbol == number_prefix:
            # Start reading numbers until a space or end of string
            i += 6  # Skip the number prefix
            while i < len(braille):
                num_symbol = braille[i:i + 6]
                if num_symbol in braille_to_number:
                    english_text.append(braille_to_number[num_symbol])
                    i += 6
                elif num_symbol == braille_alphabet[' ']:
                    english_text.append(' ')  # Add space
                    i += 6
                    break
                else:
                    break
            continue

        if symbol in braille_to_english:
            letter = braille_to_english[symbol]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            english_text.append(letter)
        else:
            english_text.append('?')  # Handle unknown symbols

        i += 6
    return ''.join(english_text)


# Reverse dictionaries to decode from Braille to English
braille_to_english = {v: k for k, v in braille_alphabet.items()}
braille_to_number = {v: k for k, v in braille_numbers.items()}

def is_braille(text):
    """Checks if the input is Braille (valid Braille symbols)."""
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]
    if is_braille(input_text):
        # Translate Braille to English
        print(translate_to_english(input_text))
    else:
        # Translate English to Braille
        print(translate_to_braille(input_text))
