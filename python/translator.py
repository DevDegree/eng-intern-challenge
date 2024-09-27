import sys  # Import the sys module for reading command-line arguments

# Mapping Braille patterns to their corresponding English characters
braille_to_text = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",  # Space character
    "..OO.O": ".",  # Period
    "..O...": ",",  # Comma
    "..O.OO": "?",  # Question mark
    "..OOO.": "!",  # Exclamation mark
    "..OO..": ":",  # Colon
    "..O.O.": ";",  # Semicolon
    "....OO": "-",  # Hyphen
    ".O..O.": "/",  # Forward slash
    ".OO..O": "<",  # Less than
    "O.O..O": "(",  # Opening parenthesis
    ".O.OO.": ")",  # Closing parenthesis
    ".....O": "Capital follows",  # Capitalization indicator
    ".O.OOO": "Number follows"    # Number mode indicator
}

# Inverse mapping for English characters to Braille patterns
text_to_braille = {v: k for k, v in braille_to_text.items()}

# Mapping for digits to Braille patterns
digit_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def braille_to_english(input_braille):
    """Convert a Braille string to its English equivalent."""
    english_output = []  # List to collect the translated English text
    index = 0  # Index to loop through the Braille string
    while index < len(input_braille):  # Iterate over the Braille input
        current_chunk = input_braille[index:index+6]  # Extract a Braille pattern (6 characters)
        if current_chunk == ".....O":  # If it's a capitalization indicator
            index += 6  # Move to the next pattern
            next_chunk = input_braille[index:index+6]  # Extract the next pattern
            english_output.append(braille_to_text[next_chunk].upper())  # Append the capital letter
        elif current_chunk == ".O.OOO":  # If it's a number mode indicator
            index += 6  # Move to the next pattern
            while index < len(input_braille) and input_braille[index:index+6] != "......":  # Keep adding digits until a space
                english_output.append(str(list(digit_to_braille.values()).index(input_braille[index:index+6]) + 1))  # Convert Braille to digit
                index += 6  # Move to the next pattern
            continue  # Skip adding the space in number mode
        else:  # For regular Braille patterns
            english_output.append(braille_to_text[current_chunk])  # Convert to English
        index += 6  # Move to the next pattern
    return ''.join(english_output)  # Join the list into a string and return it

def english_to_braille(input_text):
    """Convert an English string to Braille format."""
    braille_output = []  # List to collect the Braille representation
    in_number_mode = False  # Flag to track if number mode is active
    for char in input_text:  # Loop through each character in the input
        if char.isdigit():  # If the character is a number
            if not in_number_mode:  # If number mode is not active, activate it
                braille_output.append(".O.OOO")  # Add the number mode indicator
                in_number_mode = True  # Set the flag to True
            braille_output.append(digit_to_braille[char])  # Append Braille for the digit
        elif char.isalpha():  # If the character is a letter
            if in_number_mode:  # If we are in number mode, deactivate it
                braille_output.append("......")  # Add a space to exit number mode
                in_number_mode = False  # Reset the flag
            if char.isupper():  # If the character is uppercase
                braille_output.append(".....O")  # Add the capitalization indicator
            braille_output.append(text_to_braille[char.lower()])  # Add Braille for the letter
        else:  # For spaces and punctuation
            if in_number_mode:  # Exit number mode if we were in it
                in_number_mode = False  # Reset the flag
            braille_output.append(text_to_braille[char])  # Add Braille for punctuation/space
    return ''.join(braille_output)  # Join the list into a string and return it


def translator():
    """Main function to handle the translation between Braille and English."""
    user_input = ' '.join(sys.argv[1:])  # Combine the command-line arguments into a single string

    # Check if the input is Braille or English
    if all(char in 'O.' for char in user_input):
        # If only 'O' and '.' are present, assume it's Braille
        print(braille_to_english(user_input))  # Convert Braille to English
    else:
        # Otherwise, treat it as English
        print(english_to_braille(user_input))  # Convert English to Braille

if __name__ == "__main__":
    translator()  # Execute the translator function if the script is run directly
