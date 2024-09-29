import sys

# Define the Braille mappings for English letters, numbers, and space
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Create a reverse mapping for Braille to English
english_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_output = []
    for char in text:
        if char.lower() in braille_dict:
            braille_output.append(braille_dict[char.lower()])
        else:
            braille_output.append('?')  # Handle unknown characters
    return ''.join(braille_output)

def translate_to_english(braille):
    """Translate Braille to English text."""
    english_output = []
    # Split the Braille input into chunks of 6 characters
    braille_chars = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    
    for char in braille_chars:
        if char in english_dict:
            translated_char = english_dict[char]
            english_output.append(translated_char)
        else:
            english_output.append('?')  # Handle unknown Braille characters
    return ''.join(english_output).replace('?', '')  # Remove '?' characters

def main():
    """Main function to handle user input and output the translation."""
    if len(sys.argv) != 2:
        print("Usage: python translator.py '<text>'")
        sys.exit(1)

    input_text = sys.argv[1]

    # Check if the input is Braille (contains only 'O' and '.' and is a multiple of 6)
    if all(char in 'O.' for char in input_text) and len(input_text) % 6 == 0:
        translated_text = translate_to_english(input_text)
    else:
        # Assume input is in English
        translated_text = translate_to_braille(input_text)

    print(translated_text)

if __name__ == "__main__":
    main()
