import sys

# Dictionary mapping English letters and some punctuation to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO',
    'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  # Space
    ',': '..O...', ';': '..O.O.', ':': '..OO..', '.': '..OO.O',
    '?': '..O.OO', '!': '..OOO.', '-': '....OO','/' : '.O..O.', 
    '(': 'O.O..O', ')': '.O.OO.',
}

# Dictionary mapping numbers and some punctuation to Braille
numbers_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '.': '..OO.O',
    '<': '.O.O.O', '>': 'O.O.O.', # not unique
}

# Dictionary for special Braille markers (e.g., capitalization, number mode)
special_to_braille = {
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 2:
        return
    
    # Join all command-line arguments into a single string, ignoring the script name
    input_string = ' '.join(sys.argv[1:])
    
    # Function to convert Braille to English
    def b_to_e(input_string):
        is_num = False  # Flag to track if we're in number mode
        is_cap = False  # Flag to track if the next letter should be capitalized
        string_output = ""  # Initialize the output string

        # Process the input string in chunks of 6 characters (each Braille character)
        for i in range(0, len(input_string), 6):
            chunk = input_string[i:i+6]  # Extract a chunk of 6 characters
            
            if chunk == '......':  # Reset number mode when encountering a space
                is_num = False
            
            if chunk == special_to_braille['number']:
                is_num = True
                continue  # Skip further processing for this chunk
                
            if chunk == special_to_braille['capital']:
                is_cap = True
                continue  # Skip further processing for this chunk

            # If in number mode, match against the numbers dictionary
            if is_num:
                for key, value in numbers_to_braille.items():
                    if chunk == value:
                        string_output += key  # Add the corresponding number to the output
                        break
            else:
                # Match against the English to Braille dictionary
                for key, value in english_to_braille.items():
                    if chunk == value:
                        if is_cap:  # If the capital flag is set, capitalize the letter
                            string_output += key.upper()
                            is_cap = False  # Reset capitalization flag
                        else:
                            string_output += key  # Add the letter to the output
                        break
        
        print(string_output)  # Print the final translated string
        
    # Function to convert English to Braille
    def e_to_b(input_string):    
        braille_output = ""  # Initialize an empty string to store the Braille output
        is_num = False  # Flag to track if the current context is a number
        
        for i, char in enumerate(input_string):  # Iterate over each character in the input string
            
            if char == " ":
                braille_output += '......'  # Add Braille representation for a space
                is_num = False  # Reset the number flag after a space
                continue  # Skip to the next character
                
            if char == '.':
                # Check if the previous character was a number (i.e., decimal point follows a number)
                if i > 0 and input_string[i - 1].isdigit():
                    braille_output += special_to_braille['decimal']  # Add Braille for decimal indicator
                braille_output += english_to_braille['.']  # Add Braille for the period

            elif char in numbers_to_braille:
                if not is_num:  # If the number flag is not set
                    braille_output += special_to_braille['number']  # Add Braille for number indicator
                    is_num = True  # Set the number flag to true
                    
                braille_output += numbers_to_braille[char]  # Add Braille for the current number
            
            elif char.lower() in english_to_braille:
                if char.isupper():
                    braille_output += special_to_braille['capital']  # Add Braille for capitalization
                    
                braille_output += english_to_braille[char.lower()]  # Add Braille for the current letter
                
            else:
                continue  # Skip the character if it's not found in the dictionary

        print(braille_output)  # Output the final Braille string to the console
    
    # Check if the input string is valid Braille (only contains 'O' and '.')
    if all(c in 'O.' for c in input_string):
        b_to_e(input_string)  # Convert Braille to English
    else:
        e_to_b(input_string)  # Convert English to Braille

if __name__ == "__main__":
    main()