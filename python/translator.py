import sys

# Braille dictionary for alphabets, numbers, capitalization, and space
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    'capital': '.....O', 'number': '.O.OOO', 'decimal': 'O.OOO.', 
    ' ': '......', '.': 'OO..O.', ',': 'OO.OOO', '!': 'OO...O', '?': 'OO.O..', 
    ':': 'OO..OO', ';': 'OO.O.O', '-': 'OOOO..', '/': 'O.OO.O', '<': 'O..OO.', 
    '>': '.OO..O', '(': '.O.OO.', ')': 'O.O..O'
}

# Reverse Braille dictionary for translation from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(text):
    braille_output = []
    is_number = False
    is_decimal = False

    for char in text:
        if char.isdigit():
            if not is_number:
                braille_output.append(braille_dict['number'])
                is_number = True
            if is_decimal:
                braille_output.append(braille_dict['decimal'])
                is_decimal = False
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            if is_number:
                is_number = False  # Reset if transitioning from number to letter
            if char.isupper():
                braille_output.append(braille_dict['capital'])
            braille_output.append(braille_dict[char.lower()])
        elif char == ' ':
            braille_output.append(braille_dict[' '])
            is_number = False  # Reset number flag for spaces
        elif char == '.':
            if is_number:
                is_decimal = True  # Set decimal flag if it's part of a number
            else:
                braille_output.append(braille_dict['.'])  # Regular period
    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    is_number = False
    capitalize_next = False
    decimal_next = False

    for char in chars:
        if char == braille_dict['number']:
            is_number = True
            continue
        if char == braille_dict['capital']:
            capitalize_next = True
            continue
        if char == braille_dict['decimal']:
            decimal_next = True
            continue
        if char in reverse_braille_dict:
            translated_char = reverse_braille_dict[char]
            if is_number and translated_char.isdigit():
                if decimal_next:
                    english_output.append('.')
                    decimal_next = False
                english_output.append(translated_char)
            else:
                if capitalize_next:
                    english_output.append(translated_char.upper())
                    capitalize_next = False
                else:
                    english_output.append(translated_char)
            is_number = False
        else:
            english_output.append(' ')  # This handles spaces
    return ''.join(english_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    
    # Determine if input is Braille or English
    if all(c in "O." for c in input_text) and (len(input_text) % 6) == 0:
        # If only contains 'O' and '.', treat it as Braille
        print(translate_to_english(input_text))
    else:
        # Otherwise, treat it as English
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
