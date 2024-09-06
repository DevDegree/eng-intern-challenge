import sys

# Braille dictionary for letters and numbers
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..', 
    '#': '.O.OOO', '^': '.....O'
}

# Inverse braille dictionary for decoding
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(text):
    # Checks if the text contains only Braille (O and .)
    return all(char in 'O.' for char in text)

def translate_to_braille(text):
    braille_translation = []
    number_mode = False
    for char in text:
        if char.isdigit() and not number_mode:
            braille_translation.append(braille_dict['#'])
            number_mode = True
        if char.isalpha() and char.isupper():
            braille_translation.append(braille_dict['^'])
            char = char.lower()
        if char == ' ':
            number_mode = False  # Reset number mode on space
        braille_translation.append(braille_dict[char])
    return ''.join(braille_translation)

def translate_to_english(braille):
    english_translation = []
    number_mode = False
    capitalize_next = False
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        if braille_char == braille_dict['#']:
            number_mode = True
            continue
        elif braille_char == braille_dict['^']:
            capitalize_next = True
            continue
        char = inverse_braille_dict.get(braille_char, '')
        if number_mode:
            if char.isdigit():
                english_translation.append(char)
            else:
                number_mode = False
        elif capitalize_next:
            english_translation.append(char.upper())
            capitalize_next = False
        else:
            english_translation.append(char)
    return ''.join(english_translation)

def main():
    # Join all the arguments passed into a single string
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        # If it's braille, translate to English
        print(translate_to_english(input_text))
    else:
        # If it's English, translate to Braille
        print(translate_to_braille(input_text))

if __name__ == '__main__':
    main()
