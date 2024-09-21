import sys
from io import StringIO

# Define the Braille dictionary for letters and numbers separately
letters_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

numbers_dict = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}


# Combine both dictionaries for forward translation
braille_dict = {**letters_dict, **numbers_dict, 'cap': '.....O', 'num': '.O.OOO'}

# Create reverse dictionaries for Braille to English translation but separate for letters and numbers
#   since values like 'a' and '1' have the same key
reverse_letters_dict = {v: k for k, v in letters_dict.items()}
reverse_numbers_dict = {v: k for k, v in numbers_dict.items()}

# Translate English texts or numbers to Braille symbols
def english_to_braille_translation(text):
    braille_text = ''
    number_mode = False
    for char in text:
        if char.isupper():
            braille_text += braille_dict['cap']
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille_text += braille_dict['num']
                number_mode = True
            braille_text += braille_dict[char]
        else:
            number_mode = False
            braille_text += braille_dict[char]
    return braille_text

# Translate Braille symbols to English texts or numbers
def braille_to_english_translation(text):
    english_text = ''
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(text):
        symbol = text[i:i + 6]
        
        if symbol == braille_dict['cap']:
            capitalize_next = True
            i += 6
            continue

        if symbol == braille_dict['num']:
            number_mode = True
            i += 6
            continue

        if symbol == '......':  # Braille space
            english_text += ' '
            i += 6
            number_mode = False
            continue

        if number_mode:
            char = reverse_numbers_dict.get(symbol)
            english_text += char  # Add the digit
        else:
            char = reverse_letters_dict.get(symbol)
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english_text += char

        i += 6  # Move to the next Braille symbol

    return english_text

# Based on input parameter, identify if it's in Braille or English format
def detect_input_type(text):
    if set(text) <= set('O.'):
        return 'braille'
    return 'english'

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_values>")
        return

    # Join all arguments passed to the script to handle multi-word input
    text = ' '.join(sys.argv[1:])
    input_type = detect_input_type(text)

    if input_type == 'english':
        translated_text = english_to_braille_translation(text)
    else:
        translated_text = braille_to_english_translation(text)

    out = StringIO()
    sys.stdout = out
    sys.stdout = sys.__stdout__
    sys.stdout.write(translated_text.strip())

if __name__ == "__main__":
    main()
