import sys

# Dictionary to map English letters, spaces, punctuation, and special symbols to Braille representations
english_to_braille = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',

    # Capital follows
    'capital follows': '.....O',

    # Number follows
    'number follows': '.O.OOO',

    # Space
    ' ': '......',

    # Punctuation (from the provided image)
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}

# Reverse mapping from Braille representations back to English characters
braille_to_english = {value: key for key, value in english_to_braille.items()}

# Dictionary to map numerical characters to their corresponding Braille representations
number_to_braille = {
    # Numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    #Decimal
    'decimal follows' : '.0...0'
}

# Reverse mapping from Braille representations back to numerical characters
braille_to_number = {value : key for key, value in number_to_braille.items()}


def translate_to_braille(input_string):

    """
    Translates a given input string into its corresponding Braille representation.
    
    This function handles letters (both uppercase and lowercase), digits, punctuation, 
    and determines the context of periods to differentiate between decimal points and regular periods.
    
    Parameters:
    input_string (str): The string to be translated into Braille.
    
    Returns:
    str: A string representing the Braille translation of the input string.
    """

    # Initialize an empty string to hold the resulting Braille output.
    output_braille = ""
    
    # Get the length of the input string for boundary checks.
    length = len(input_string)
    
    # Flag to track if a "number follows" indicator has been output.
    number_flag = False 


    for i, char in enumerate(input_string):

        if not input_string:
            return "Input string is empty."
        
        if char.isalpha():
            if char.isupper():
                output_braille += english_to_braille['capital follows']  # Add capital follows indicator
                output_braille += english_to_braille[char.lower()]  # Add lower case equivalent
            else:
                output_braille += english_to_braille[char]  # Add braille for lowercase
        
            number_flag = False  # Reset number flag when encountering a letter

        elif char.isdigit():  # Check if the character is a digit
            if not number_flag:  # If number_flag is False, output "number follows"
                output_braille += english_to_braille['number follows']  # Add number follows indicator
                number_flag = True  # Set the number flag to True
            output_braille += number_to_braille[char]  # Add Braille for the digit

        elif char == '.':  # Check for period or decimal point
            # Determine the context of the period
            is_decimal = False
            
            # Check preceding and succeeding characters

            # Preceded by space and succeeded by digit
            if (i > 0 and input_string[i - 1].isdigit() and 
                (i + 1 < length and input_string[i + 1].isdigit())):
                is_decimal = True  

            # Preceded by space and succeeded by digit
            elif (i > 0 and input_string[i - 1] == ' ' and 
                  (i + 1 < length and input_string[i + 1].isdigit())):
                is_decimal = True  
            # Preceded by digit and succeeded by a space
            elif (i > 0 and input_string[i - 1].isdigit() and 
                  (i + 1 < length and input_string[i + 1] == ' ')):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character

            # Preceded by letter and succeeded by a space
            elif (i > 0 and input_string[i - 1].isalpha() and 
                  (i + 1 < length and input_string[i + 1] == ' ')):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character

            # Preceded by space and succeeded by alphabet
            elif (i > 0 and input_string[i - 1] == ' ' and 
                  (i + 1 < length and input_string[i + 1].isalpha())):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character

            # Preceded by alphabet and succeeded by alphabet
            elif (i > 0 and input_string[i - 1].isalpha() and 
                  (i + 1 < length and input_string[i + 1].isalpha())):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character

            # Preceded by digit and succeeded by alphabet
            elif (i > 0 and input_string[i - 1].isdigit() and 
                  (i + 1 < length and input_string[i + 1].isalpha())):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character
            # Preceded by alphabet and succeeded by digit
            elif (i > 0 and input_string[i - 1].isalpha() and 
                  (i + 1 < length and input_string[i + 1].isdigit())):
                output_braille += english_to_braille['.']  # Period
                continue  # Skip to next character
            
            # If it's identified as a decimal
            if is_decimal:
                output_braille += number_to_braille['decimal follows']
                output_braille += english_to_braille['.']  # Use your Braille notation for period
            else:
                output_braille += english_to_braille['.']  # Use your Braille notation for period

        elif char in english_to_braille:  # Handle other punctuation
            output_braille += english_to_braille[char]  # Add Braille for punctuation

        # Reset number flag on space
        if char == ' ':
            number_flag = False  # Reset number flag on space

        else:
            continue  # For unsupported characters

    return output_braille




def translate_to_string(braille_string):

    """
    Translates a given Braille string into its corresponding English text representation.

    This function processes Braille representations for letters, numbers, 
    spaces, and capital letters, converting them into their English equivalents.
    
    Parameters:
    braille_string (str): The Braille string to be translated into English text.
    
    Returns:
    str: A string representing the English translation of the input Braille string.
    """

    # Initialize an empty string to hold the resulting English output.
    output_string = ""
    
    # Get the length of the input Braille string for boundary checks.
    length = len(braille_string)
    
    # Initialize an index for traversing the Braille string.
    i = 0

    while i < length:
        # Check for space
        if braille_string[i:i + 6] == english_to_braille[' ']:
            output_string += ' '
            i += 6  # Move past the space Braille representation
            continue

        # Check for numbers
        if braille_string[i:i + 6] == english_to_braille['number follows']:
            i += 6  # Move past the number follows Braille representation
            while i < length:
                char_braille = braille_string[i:i + 6]
                if char_braille in braille_to_number:
                    output_string += braille_to_number[char_braille]  # Add the corresponding digit
                    i += 6  # Move past the digit Braille representation
                elif braille_string[i:i + 6] == english_to_braille[' ']:
                    output_string += ' '  # Add space if encountered
                    i += 6
                    break
                else:
                    break
            continue

        # Check for capital letters
        if braille_string[i:i + 6] == english_to_braille['capital follows']:
            i += 6  # Move past the capital follows Braille representation
            if i + 6 <= length:  # Ensure there are enough characters left
                char_braille = braille_string[i:i + 6]
                if char_braille in braille_to_english:
                    output_string += braille_to_english[char_braille].upper()  # Add uppercase character
                    i += 6  # Move past the letter Braille representation
                continue

        # Regular characters
        char_braille = braille_string[i:i + 6]
        if char_braille in braille_to_english:
            output_string += braille_to_english[char_braille]  # Add the corresponding character
            i += 6  # Move past the letter Braille representation
        else:
            # Handle unknown Braille (optional)
            output_string += '?'  # Placeholder for unsupported characters
            i += 6  # Move to next character

    return output_string


def main():
    if len(sys.argv) == 1:
        print("Please provide the input text.")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:]).strip()

    # Check if the input is Braille or English
    if all(char in "O." for char in input_text) and len(input_text) % 6 == 0:
        # The input is Braille
        translated_output = translate_to_string(input_text)
        print(translated_output)
    else:
        # The input is English
        translated_output = translate_to_braille(input_text)
        print(translated_output)

if __name__ == "__main__":
    main()
