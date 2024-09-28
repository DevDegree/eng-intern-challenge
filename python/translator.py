
import sys

# Braille representations: each Braille character is represented as a 6-character string
# using 'o' for raised dots and '.' for flat dots, starting from the top-left dot.
braille_dict = {
    'a': 'o.....', 'b': 'o.o...', 'c': 'oo....', 'd': 'oo.o..', 'e': 'o..o..', 'f': 'ooo...', 'g': 'oooo..', 'h': 'o.oo..',
    'i': '.oo...', 'j': '.ooo..', 'k': 'o...o.', 'l': 'o.o.o.', 'm': 'oo..o.', 'n': 'oo.oo.', 'o': 'o..oo.', 'p': 'ooo.o.',
    'q': 'ooooo.', 'r': 'o.ooo.', 's': '.oo.o.', 't': '.oooo.', 'u': 'o...oo', 'v': 'o.o.oo', 'w': '.ooo.o', 'x': 'oo..oo',
    'y': 'oo.ooo', 'z': 'o..ooo',
    'capital': '.....o', 'number': '.o.ooo', ' ': '......',
    '1': 'o.....', '2': 'o.o...', '3': 'oo....', '4': 'oo.o..', '5': 'o..o..', '6': 'ooo...', '7': 'oooo..', '8': 'o.oo..',
    '9': '.oo...', '0': '.ooo..'
}

# Function to translate text to Braille
def text_to_braille(text):
    braille_translation = ''
    number_mode = False
    for char in text:
        if char.isdigit() and not number_mode:
            braille_translation += braille_dict['number']  # Switch to number mode
            number_mode = True
        elif char == ' ':
            braille_translation += braille_dict[' ']  # Add space
            number_mode = False  # Reset number mode after a space
        elif char.isalpha():
            if char.isupper():
                braille_translation += braille_dict['capital']  # Capitalize next letter
                char = char.lower()  # Convert to lowercase for actual Braille letter
            braille_translation += braille_dict[char]
            number_mode = False  # Reset number mode when switching back to letters
        else:
            braille_translation += '?'  # Handle unknown characters
    return braille_translation

# Function to translate Braille to text
def braille_to_text(braille):
    text = ''
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]  # Read the next 6-character Braille symbol
        if symbol == braille_dict['number']:
            number_mode = True
        elif symbol == braille_dict['capital']:
            i += 6  # Skip to the next letter after capitalization
            letter_symbol = braille[i:i+6]
            for key, value in braille_dict.items():
                if value == letter_symbol:
                    text += key.upper()  # Capitalize the next letter
                    break
        elif symbol == braille_dict[' ']:
            text += ' '  # Add space
            number_mode = False  # Reset number mode after space
        else:
            for key, value in braille_dict.items():
                if value == symbol:
                    if number_mode and key.isdigit():
                        text += key  # Translate number if in number mode
                    else:
                        text += key  # Translate letter or number
                    break
        i += 6
    return text

# Function to determine whether the input is Braille or English
def is_braille(input_str):
    # Braille will consist only of the characters 'o', '.', and spaces
    return all(char in 'o. ' for char in input_str)

# Main function to handle input and translation
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        return

    # Combine all arguments into one string (in case of spaces)
    input_string = ' '.join(sys.argv[1:])
    
    # Determine if input is Braille or English
    if is_braille(input_string):
        # Translate Braille to English
        translated = braille_to_text(input_string)
        print(translated)
    else:
        # Translate English to Braille
        translated = text_to_braille(input_string)
        print(translated)

# Run the main function if this script is being executed
if __name__ == "__main__":
    main()
