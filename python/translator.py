# Step 1: Create a dictionary (lookup table) to map English letters, numbers, and punctuation to their Braille equivalents.
braille_dict = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.', 
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.', 
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 
    'z': '0..000', '1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', 
    '5': '0..0..', '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', 
    '0': '.000..', ' ': '......', '.': '..00.0', ',': '..0...', '?': '..0.00', 
    '!': '..000.', "'": '....0.', '-': '....00', ':': '..00..', ';': '..0.0.'
}

# Step 2: Create the inverse dictionary (to go from Braille to English)
# We are reversing the braille_dict here, so Braille symbols become keys and English letters become values.
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Step 3: Function to convert English text to Braille
def translate_to_braille(text):
    """This function takes English text and converts it to Braille."""
    result = []  # Create an empty list to store the Braille output
    for char in text:
        if char.isupper():  # If the letter is uppercase, handle it by first adding a capitalization indicator.
            result.append('.....0')  # "Capital follows" Braille symbol
            result.append(braille_dict[char.lower()])  # Then convert the lowercase version of the letter to Braille
        else:
            result.append(braille_dict[char])  # Convert the lowercase letter directly
    return ' '.join(result)  # Join the Braille symbols with spaces and return them as a string

# Step 4: Function to convert Braille to English
def translate_to_english(braille):
    """This function takes Braille and converts it back to English text."""
    result = []  # Create an empty list to store the English output
    capitalize_next = False  # This flag will tell us if the next letter should be capitalized
    for symbol in braille.split(' '):  # Split the input by spaces to get each Braille symbol
        if symbol == '.....0':  # Check if it's the capitalization indicator
            capitalize_next = True  # If it is, set the flag to True
        else:
            char = inverse_braille_dict.get(symbol, '')  # Get the corresponding English letter for the Braille symbol
            if capitalize_next:  # If the flag is True, capitalize the letter
                char = char.upper()  # Capitalize the letter
                capitalize_next = False  # Reset the flag
            result.append(char)  # Add the letter to the result list
    return ''.join(result)  # Join the English letters into a string and return it

# Step 5: Main function to handle input and decide which translation to perform
def main():
    """Main function that handles user input and determines whether to translate to Braille or English."""
    import sys  # Import the sys module to access command-line arguments
    if len(sys.argv) != 2:  # Check if the user provided exactly one input (the text or Braille to translate)
        print("Usage: python translator.py <text or braille>")  # If not, print instructions
        return  # Exit the function if the input is incorrect

    input_text = sys.argv[1]  # Get the user input (from the command line)

    # Step 6: Determine if the input is Braille or English
    # If it contains '0' or '.', we assume it's Braille. Otherwise, it's English.
    if '0' in input_text or '.' in input_text:
        print(translate_to_english(input_text))  # If it's Braille, translate it to English and print the result
    else:
        print(translate_to_braille(input_text))  # If it's English, translate it to Braille and print the result

# Step 7: Run the main function when the script is executed
if __name__ == '__main__':
    main()  # Call the main function when the program is run
