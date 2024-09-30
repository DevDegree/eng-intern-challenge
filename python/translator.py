import sys

def detect_input_format(input_string):
    if all(c in 'O.' for c in input_string):  # Check if the string contains only Braille characters (O, .)
        return "Braille"
    elif all(c.isalnum() or c.isspace() for c in input_string):  # Check for English letters, digits, and spaces
        return "English"
    else:
        return "Unknown"

# Braille dictionary for letters and numbers
braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
    ' ': "......"  # Space
}

braille_to_english_letters = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y', "O..OOO": 'z',
    "......": ' ',  # Space
}

braille_to_english_numbers = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
    "OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
}

# Special characters for capitalization and numbers
capital_prefix = ".....O"
number_prefix = ".O.OOO"  # Corrected number prefix

def english_to_braille(english_text):
    braille_output = []
    number_mode = False
    
    for char in english_text:
        if char.isdigit():
            if not number_mode:  # If we're not already in number mode
                braille_output.append(number_prefix)
                number_mode = True
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            if number_mode:  # Reset number mode if a letter is encountered
                number_mode = False
            if char.isupper():  # Add capitalization prefix if letter is uppercase
                braille_output.append(capital_prefix)
            braille_output.append(braille_dict[char.lower()])
        elif char == ' ':
            braille_output.append(braille_dict[' '])
    
    return ''.join(braille_output)

def braille_to_english(braille_text):
    english_output = []
    capital_mode = False
    number_mode = False
    
    # Process the input string in chunks of 6 characters (each Braille character is 6 dots)
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        
        if braille_char == capital_prefix:
            capital_mode = True
            number_mode = False  # Exit number mode when capital mode is entered
        elif braille_char == number_prefix:
            number_mode = True
            capital_mode = False  # Exit capital mode when number mode is entered
        elif number_mode:
            # Use the number dictionary when in number mode
            if braille_char in braille_to_english_numbers:
                char = braille_to_english_numbers[braille_char]
                english_output.append(char)
        else:
            # Use the letter dictionary when not in number mode
            if braille_char in braille_to_english_letters:
                char = braille_to_english_letters[braille_char]
                
                # Handle capitalization
                if capital_mode:
                    if char.isalpha():
                        char = char.upper()
                    capital_mode = False  # Capitalize only the next letter
                
                english_output.append(char)
            
        # Exit number mode if a space is encountered
        if braille_char == "......":
            number_mode = False
    
    return ''.join(english_output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python braille_translator.py <input_string>")
        sys.exit(1)
    
    # Join all the arguments into a single input string
    input_string = ' '.join(sys.argv[1:])
    
    # Detect the input format and translate accordingly
    if detect_input_format(input_string) == "Braille":
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)  # Output the result directly, as required
