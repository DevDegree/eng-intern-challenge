import sys

# Dictionary for English to Braille and Braille to English mapping
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Reverse dictionary for Braille to English conversion
english_dict = {v: k for k, v in braille_dict.items()}

def translate_braille(input_str):
    # Auto-detect if the input is Braille or English and call the right function
    return braille_to_english(input_str) if all(c in 'O.' for c in input_str) else english_to_braille(input_str)

def braille_to_english(braille):
    # Split input into chunks of 6 (since each Braille character is 6 dots)
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    english_output = ""
    capital_mode = False
    number_mode = False

    for char in braille_chars:
        if char == braille_dict['capital']:
            capital_mode = True  # Activate capital mode for the next letter
        elif char == braille_dict['number']:
            number_mode = True  # Activate number mode for the next digits
        else:
            letter = english_dict.get(char, '')  # Get the corresponding letter from Braille

            # Apply number mode: Only digits are expected when this is active
            if number_mode:
                # Number mode means the character should be a digit
                if letter.isdigit():
                    english_output += letter
                    number_mode = False  # Reset number mode after processing the digit
                    continue  # Skip to the next character
                else:
                    # If a non-digit is encountered, reset number mode
                    number_mode = False

            # Apply capital mode if needed
            if capital_mode:
                letter = letter.upper()
                capital_mode = False  # Reset capital mode after applying it

            english_output += letter
    
    return english_output

def english_to_braille(english):
    braille_output = ''
    number_mode = False

    for char in english:
        if char.isupper():
            braille_output += braille_dict['capital']  # Add capital symbol for uppercase letters
            char = char.lower()
        if char.isdigit() and not number_mode:
            braille_output += braille_dict['number']  # Add number symbol before digits
            number_mode = True
        elif not char.isdigit():
            number_mode = False
        braille_output += braille_dict.get(char, '')  # Get the Braille char, default to '' if not found
    return braille_output

if __name__ == "__main__":
    # If there is an argument passed, combine and translate it
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        print(translate_braille(input_string))
    else:
        print("Please provide an input string.")
