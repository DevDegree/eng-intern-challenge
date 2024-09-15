import re
import sys

# Braille dictionary
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse Braille dictionary
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Function to translate English text to Braille with markers
def to_braille(text):
    # Initialize variables
    braille_translation = ""
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Check if the character is uppercase
            if char.isupper():
                braille_translation += ".....O"
            # Convert the character to lowercase for lookup in braille_dict
            braille_translation += braille_dict[char.lower()]
        
        elif char.isdigit():
            braille_translation += ".O.OOO" + braille_dict[char]
        
        elif char == ' ':
            braille_translation += braille_dict[char]
    
    return braille_translation

# Function to translate Braille to English
def to_english(braille_text):
    # Initialize variables
    english_translation = ""
    in_letter_sequence = False
    in_number_sequence = False
    capital_next = False

    # Split the Braille text into Braille characters (6 dots each)
    i = 0
    while i < len(braille_text):
        char = braille_text[i]

        # Check for markers ".....O" (capital letters) and ".O.OOO" (numbers)
        if braille_text[i:i+6] == ".....O":
            capital_next = True
            i += 6
            continue
        elif braille_text[i:i+6] == ".O.OOO":
            in_number_sequence = True
            i += 6
            continue
        
        # Extract the next 6-dot Braille character
        braille_char = braille_text[i:i+6]
        
        # Convert to the corresponding English character
        if braille_char in reverse_braille_dict:
            translated_char = reverse_braille_dict[braille_char]
            if in_number_sequence and translated_char.isalpha():
                # If we are in a number sequence and the character is a letter, convert to digit
                number_map = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
                              'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
                translated_char = number_map.get(translated_char, translated_char)
            elif capital_next:
                translated_char = translated_char.upper()
                capital_next = False
            english_translation += translated_char
        
        # Move to the next Braille character (6 dots)
        i += 6
    
    return english_translation

def text_analysis(input_text):
    # Remove spaces and check if it's potentially Braille (contains only 'O' and '.' and has length multiple of 6)
    braille_pattern = re.fullmatch(r'[O.]+', input_text.replace(" ", ""))
    
    if braille_pattern and len(input_text.replace(" ", "")) % 6 == 0:
        return to_english(input_text)
    else:
        return to_braille(input_text)

# Run the script with command-line arguments
if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    print(text_analysis(input_text))
