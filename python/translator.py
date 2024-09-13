import sys

# Braille dictionary for English to Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', ',': '..O...', ';': '..OO..', ':': 'O..O..', '.': '..OOO.', '?': '..O.OO',
    '!': '..OO.O', '-': '..O..O', '/': 'O.O...', '(': 'O..OO.', ')': '.OOOOO',
    'capital': '.....O', 'number': '.O.OOO'
}

# Function to translate English to Braille
def english_to_braille(text):
    braille_output = []
    number_mode = False  # Used to track if we are in number mode
    for char in text:
        if char.isdigit():  # Handle numbers
            if not number_mode:
                braille_output.append(braille_alphabet['number'])  # Prefix number mode
                number_mode = True
            braille_output.append(braille_alphabet[char])
        elif char.isalpha():  # Handle letters
            if char.isupper():
                braille_output.append(braille_alphabet['capital'])  # Prefix capital mode
            braille_output.append(braille_alphabet[char.lower()])  # Add lowercase version
            number_mode = False  # Exit number mode
        else:
            # Handle unsupported characters (like spaces, punctuation)
            braille_output.append(braille_alphabet.get(char, '......'))  # Defaults to space
            number_mode = False  # Exit number mode for spaces or unsupported chars
    return ''.join(braille_output)

# Main function to handle multiple arguments and convert them
if __name__ == "_main_":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    # Combine all arguments into one string
    input_text = ' '.join(sys.argv[1:])
    
    # Translate the combined input to Braille
    translated_text = english_to_braille(input_text)
    
    # Output the translated Braille text
    print(translated_text, end="")  # No newline at the end