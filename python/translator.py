# Braille translation dictionary for letters, numbers, and special markers
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O',  # Capital follows
    'number': '.O.OOO',   # Number follows marker
}

braille_numbers = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Reverse Braille dictionary to translate from Braille to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

def braille_to_english(braille_string):
    result = ''
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille_string):
        # Read the current Braille character (6 dots)
        braille_char = braille_string[i:i + 6]
        
        # Check for capital marker
        if braille_char == braille_alphabet['capital']:
            capitalize_next = True
            i += 6
            continue
        
        # Check for number marker
        if braille_char == braille_alphabet['number']:
            number_mode = True
            i += 6
            continue
        
        # Translate the Braille character
        char = reverse_braille_alphabet[braille_char]

        if char == ' ':
            number_mode = False

        if number_mode and char in 'abcdefghij':
            # Translate as a number (a=1, b=2, ..., j=0)
            char = str('abcdefghij'.index(char) + 1) if char != 'j' else '0'
        
        # Apply capitalization if needed
        if capitalize_next:
            char = char.upper()
            capitalize_next = False
        
        # Append the translated character
        result += char
        
        # Move to the next Braille character
        i += 6
    
    return result

def english_to_braille(english_string):
    result = ''
    number_mode = False

    for char in english_string:
        if char.isupper():
            # Add the capitalization marker for uppercase letters
            result += braille_alphabet['capital']
            result += braille_alphabet[char.lower()]
        elif char.isdigit():
            # Add the number marker if it's the first digit
            if not number_mode:
                result += braille_alphabet['number']
                number_mode = True
            result += braille_numbers[str('0123456789'.index(char))]
        elif char == ' ':
            # Reset number mode and add space
            number_mode = False
            result += braille_alphabet[' ']
        else:
            # Normal lowercase letter
            result += braille_alphabet[char]
    
    return result

def is_braille(input_string):
    # Check if all characters are 'O' or '.' and the string length is a multiple of 6
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0

def translate(input_string):
    # Determine if input is Braille or English
    if is_braille(input_string):
        # Braille to English
        return braille_to_english(input_string)
    else:
        # English to Braille
        return english_to_braille(input_string)

if __name__ == "__main__":
    import sys
    # Read the input string from command line arguments
    input_string = sys.argv[1]
    print(translate(input_string))