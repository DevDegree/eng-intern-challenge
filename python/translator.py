import sys

# Braille dictionary for letters, numbers, and special symbols
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

# Reverse dictionary to convert back to eng
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(text):
    """Check if the input text is written in Braille (i.e., contains only 'O' and '.')"""
    return all(char in 'O.' for char in text)

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_translation = []
    number_mode = False
    
    for char in text:
        # Handling numbers
        if char.isdigit() and not number_mode:
            braille_translation.append(braille_dict['#'])
            number_mode = True
        
        # Handling uppercase letters
        if char.isalpha() and char.isupper():
            braille_translation.append(braille_dict['^'])
            char = char.lower()
        
        # Reset number mode on space
        if char == ' ':
            number_mode = False
        
        # Append the Braille translation for the character
        braille_translation.append(braille_dict.get(char, ''))

    return ''.join(braille_translation)

def translate_to_english(braille):
    """Translate Braille to English text."""
    english_translation = []
    number_mode = False
    capitalize_next = False
    
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        
        if braille_char == braille_dict['#']:
            number_mode = True
            continue
        
        if braille_char == braille_dict['^']:
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

def solve(input_text):
    """Main function to handle the translation based on whether the input is Braille or English."""
    if is_braille(input_text):
        return translate_to_english(input_text)
    else:
        return translate_to_braille(input_text)

def main():
    # Join all the command-line arguments into a single input string
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        print(solve(input_str))

if __name__ == "__main__":
    main()
