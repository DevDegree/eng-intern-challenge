import sys

# Mapping dictionaries for Braille to English and English to Braille conversions
braille_to_english = {
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
    "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
    "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
    "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
    "O..OOO": "Z", ".OOOOO": "0", "O.....": "1", "O.O...": "2", "OO....": "3", 
    "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
    ".OOO..": "9", "......": " "
}

# Create reverse mapping for English to Braille conversion
english_to_braille = {v: k for k, v in braille_to_english.items()}


def braille_to_english_translator(text):
    final_result = ''
    i = 0
    # Process Braille string character by character
    while i < len(text):
        char = text[i:i+6]
        # Check for capital letter indicator
        if char == '.....O':
            i += 6
            final_result += braille_to_english[text[i:i+6]].upper()
        # Check for number indicator
        elif char == '.O.OOO':
            i += 6
            while i < len(text) and text[i:i+6] != '......':
                final_result += braille_to_english[text[i:i+6]]
                i += 6
            i -= 6  # To reprocess the space after numbers mode
        else:
            final_result+= braille_to_english[char]
        i += 6
    return ''.join(final_result)


def english_to_braille_translator(text):
    final_result = ''
    capitalize_next = False
    numbers_mode = False
    # Process each character in the English string
    for char in text:
        # Handle uppercase letters
        if char.isupper():
            final_result += '.....O'
            capitalize_next = False
        
        # Handle digits
        elif char.isdigit():
            final_result += '.O.OOO'
            numbers_mode = True
        
        # Convert character to Braille
        braille_char = english_to_braille[char.upper()]
        
        # Apply capitalization if needed
        if capitalize_next:
            braille_char = '.....O' + braille_char
            capitalize_next = False
        
        final_result += braille_char
        
        # Exit numbers mode if necessary
        if not numbers_mode and char != ' ':
            numbers_mode = False
    
    # Remove spaces from the result
    return final_result.replace(' ', '')

# Function to determine whether input is Braille or English
def determine_input_type(input_str):
    # Check if input contains only O and . characters
    return 'braille' if set(input_str).issubset({'O', '.'}) else 'english'

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python braille_translator.py <input_string>")
        sys.exit(1)

    # Get input string from command-line argument
    input_str = sys.argv[1]
    
    # Determine input type
    input_type = determine_input_type(input_str)

    # Convert input based on its type
    if input_type == 'braille':
        output = braille_to_english_translator(input_str)
    else:
        output = english_to_braille_translator(input_str)

    # Print the translated output
    print(output)