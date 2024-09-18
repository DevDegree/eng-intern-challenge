
import sys

# Braille dictionary: English to Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
    '.': '..OO.O', ',': '..O...'
}

# English dictionary: Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: str(i) for i, v in enumerate(braille_alphabet.values(), 1) if i <= 10}

# Check if input is in Braille or English
def is_braille(input_string):
    return all(char in ['O', '.'] for char in input_string)

# Function to split Braille strings into substrings of length 6
def split_string(s, length=6):
    return [s[i:i+length] for i in range(0, len(s), length)]

# Translate English to Braille
def translate_to_braille(english_text):
    braille_text = []
    is_number_mode = False
    
    for char in english_text:
        if char.isupper():
            braille_text.append(braille_alphabet['capital'])
        
        if char.isdigit() and not is_number_mode:
            braille_text.append(braille_alphabet['number'])
            is_number_mode = True

        if char == ' ':
            is_number_mode = False

        if char == '.' and braille_text and braille_text[-1] in braille_alphabet.values():
            braille_text.append(braille_alphabet['decimal'])

        braille_char = braille_alphabet.get(char.lower(), '......')
        braille_text.append(braille_char)

    return ''.join(braille_text)

# Translate Braille to English
def translate_to_english(braille_text):
    english_text = []
    braille_chars = split_string(braille_text)
    is_capital = False
    is_number_mode = False
    
    for braille_char in braille_chars:
        if braille_char == '.....O':
            is_capital = True
            continue
        if braille_char == '.O.OOO':
            is_number_mode = True
            continue
        
        if is_number_mode:
            translated_char = english_numbers.get(braille_char, '')
        else:
            translated_char = english_alphabet.get(braille_char, '')

        if is_capital:
            translated_char = translated_char.upper()
            is_capital = False

        english_text.append(translated_char)
        
        if braille_char == '......':
            is_number_mode = False

    return ''.join(english_text)

# Main function
def main():
    input_text = ' '.join(sys.argv[1:])

    if not input_text:
        print("Please provide a string to translate.")
        return

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
