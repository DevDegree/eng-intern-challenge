# Dictionary for translating English characters and numbers to Braille (represented with O and .)
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......',  # space
    # Special symbols
    'capital': '.....O',  # Capital letter indicator
    'number': '.O.OOO'    # Number indicator
}

# Reverse mapping for Braille to English translation
REVERSE_BRAILLE_DICT = {v: k for k, v in BRAILLE_DICT.items()}

def is_braille(input_string):
    """Check if the input string is Braille by checking if it contains only O and ."""
    return all(c in 'O.' for c in input_string)

def english_to_braille(english_text):
    """Translate English text to Braille."""
    braille_text = ''
    number_mode = False

    for char in english_text:
        # Handle capitalization
        if char.isupper():
            braille_text += BRAILLE_DICT['capital']  # Add capital indicator
            char = char.lower()  # Convert to lowercase after adding indicator

        # Handle numbers
        if char.isdigit() and not number_mode:
            braille_text += BRAILLE_DICT['number']  # Add number indicator
            number_mode = True
        
        if not char.isdigit() and number_mode:
            number_mode = False

        # Append the corresponding Braille code
        braille_text += BRAILLE_DICT.get(char, '......')  # Convert letter/number

    return braille_text

def braille_to_english(braille_text):
    """Translate Braille text to English."""
    english_text = ''
    number_mode = False
    capital_mode = False
    
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]

        if braille_char == BRAILLE_DICT['capital']:
            capital_mode = True
            continue
        elif braille_char == BRAILLE_DICT['number']:
            number_mode = True
            continue

        # Convert Braille to corresponding English character
        english_char = REVERSE_BRAILLE_DICT.get(braille_char, '?')

        if number_mode and english_char.isdigit():
            english_text += english_char
        elif capital_mode:
            english_text += english_char.upper()
            capital_mode = False
        else:
            english_text += english_char

        if english_char == ' ':  # Reset modes on space
            number_mode = False
            capital_mode = False

    return english_text

def main():
    import sys
    input_text = ' '.join(sys.argv[1:])
    if all(c in "O."for c in input_text):
        print(braille_to_english(input_text))
    else:

        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()