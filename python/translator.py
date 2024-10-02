# Braille dictionary for letters, numbers (with number indicator ⠼), and punctuation
braille_dict = {
    # Letters
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.', 
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.', 
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 
    'z': '0..000',

    # Numbers (preceded by the number indicator ⠼, which is .000..)
    '1': '.000.. 0.....', '2': '.000.. 0.0...', '3': '.000.. 00....', '4': '.000.. 00.0..', 
    '5': '.000.. 0..0..', '6': '.000.. 000...', '7': '.000.. 0000..', '8': '.000.. 0.00..', 
    '9': '.000.. .00...', '0': '.000.. .000..',

    # Punctuation and special symbols
    ' ': '......', '.': '..00.0', ',': '..0...', '?': '..0.00', '!': '..000.',
    "'": '....0.', '-': '....00', ':': '..00..', ';': '..0.0.',

    # Number indicator (⠼)
    '#': '.000..'
}

# Inverse dictionary for Braille-to-English translation
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Function to convert English text to Braille
def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append('.....0')  # Add capitalization indicator for uppercase letters
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            result.append(braille_dict[char])  # Translate numbers with the number indicator
        else:
            result.append(braille_dict[char])  # Translate lowercase letters and punctuation
    return ' '.join(result)

# Function to convert Braille to English
def translate_to_english(braille):
    result = []
    capitalize_next = False
    number_mode = False

    # Split the Braille input by spaces to get individual symbols
    for symbol in braille.split(' '):
        if symbol == '.000..':  # Number indicator in Braille (⠼)
            number_mode = True  # Enter number mode
        elif symbol == '.....0':  # Capitalization indicator (capital letter follows)
            capitalize_next = True  # Mark the next character as uppercase
        else:
            if number_mode:  # If we are in number mode, translate as a number
                char = inverse_braille_dict.get(symbol, '')
                if char.isdigit():
                    result.append(char)
                number_mode = False  # Exit number mode after one number
            else:  # Otherwise, translate as a letter or punctuation
                char = inverse_braille_dict.get(symbol, '')
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)

    return ''.join(result)

# Main function to handle input and decide which translation to perform
def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text or braille>")
        return

    input_text = sys.argv[1]
    
    # Determine if the input is Braille or English based on the presence of '0' or '.'
    if '0' in input_text or '.' in input_text:
        print(translate_to_english(input_text))  # Translate Braille to English
    else:
        print(translate_to_braille(input_text))  # Translate English to Braille

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
