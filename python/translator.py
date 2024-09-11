# Importing necessary modules 
import sys

# Dictionaries to store Braille conversions for lowercase alphabets, numbers, and special characters
braille_dict = {
    # Lowercase alphabets
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',

    # Braille Verifiers
    'caps': '.....O',  # Indicates uppercase letters
    'decimal': '.O...O',  # Indicates decimal point
    'number': '.O.OOO',  # Indicates the following characters are numbers

    # Special Characters
    '.': '..OO.O',  # Period
    ',': '..O...',  # Comma
    '?': '..O.OO',  # Question mark
    '!': '..OOO.',  # Exclamation mark
    ':': '..OO..',  # Colon
    ';': '..O.O.',  # Semicolon
    '-': '....OO',  # Hyphen
    '/': '.O..O.',  # Slash
    '(': 'O.O..O',  # Left parenthesis
    ')': '.O.OO.',  # Right parenthesis
    ' ': '......'   # Space
}

numbers_braille_dict = {
    # Numbers
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '<': '.OO..O',  # Less than
    '>': 'O..OO.',  # Greater than
}

def break_into_list(input_text):
    """
    Split the Braille text into chunks of 6 characters each.
    
    Args:
        input_text (str): The Braille text to split.
    
    Returns:
        list: A list of Braille letter chunks.
    """
    return [input_text[i:i+6] for i in range(0, len(input_text), 6)]

def is_braille(input_text):
    """
    Check if the provided text consists only of Braille characters ('.' and 'O').
    
    Args:
        input_text (str): The text to check.
    
    Returns:
        bool: True if all characters are '.' or 'O', False otherwise.
    """
    return all(char in '.O' for char in input_text)

def braille_validator(input_text):
    """
    Validate if the provided Braille text has a length that is a multiple of 6.
    
    Args:
        input_text (str): The Braille text to validate.
    
    Returns:
        bool: True if the length of the text is a multiple of 6, False otherwise.
    """
    return (len(input_text) % 6) == 0

def english_to_braille(input_text):
    """
    Convert English text to Braille.
    
    Args:
        input_text (str): The English text to convert.
    
    Returns:
        str: The converted Braille text.
    """
    output_text = ''
    number_flag = False  # Flag to track if the current sequence is numbers
    space_flag = False  # Flag to track if a space has been encountered
    
    try:
        for letter in input_text:
            if letter == '.' and number_flag:
                # Add decimal point symbol if it's part of a number sequence
                output_text += braille_dict['decimal']
                continue
            elif letter == ' ':
                # Set space_flag when encountering a space
                space_flag = True

            if letter.isdigit():
                if not number_flag:
                    # Add number follows symbol before the first digit in a sequence
                    output_text += braille_dict['number']
                    number_flag = True
                # Append Braille for digit
                if letter not in numbers_braille_dict:
                    print("Invalid Entry")
                    sys.exit(1)
                output_text += numbers_braille_dict[letter]
            else:
                if number_flag and space_flag:
                    # Reset number flag if transitioning from numbers to other characters with a space
                    number_flag = False
                    space_flag = False
                elif number_flag and not space_flag:
                    print("No space provided to signify end of numbers")
                    sys.exit(1)
                if letter.isupper():
                    # Add capitalization symbol and then Braille for letter
                    output_text += braille_dict['caps']
                    output_text += braille_dict[letter.lower()]
                else:
                    # Append Braille for letter or character
                    output_text += braille_dict.get(letter, '......')
    
    except KeyError as e: 
        print(f"Invalid Braille Sequence: {e}")
        sys.exit(1)
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    return output_text

def braille_to_english(input_text):
    """
    Convert Braille text to English.
    
    Args:
        input_text (str): The Braille text to convert.
    
    Returns:
        str: The converted English text.
    """
    try: 
        # Check if the provided Braille text is valid
        if braille_validator(input_text):
            # Split Braille text into letter chunks
            braille_letters = break_into_list(input_text)
            # Create reversed dictionaries for conversion
            reversed_braille_dict = {value: key for key, value in braille_dict.items()}
            reversed_numbers_braille_dict = {value: key for key, value in numbers_braille_dict.items()}
            
            output_text = ""
            number_flag = False
            Caps_flag = False  # Flag to track if the next letter should be capitalized

            for letter in braille_letters:
                if reversed_braille_dict[letter] == 'caps':
                    # Set Caps_flag if capitalization symbol is encountered
                    Caps_flag = True
                    continue
                elif reversed_braille_dict[letter] == 'number':
                    # Set number_flag if number symbol is encountered
                    number_flag = True
                    continue
                elif reversed_braille_dict[letter] == ' ':
                    # Reset number_flag if space is encountered
                    number_flag = False
                    
                if number_flag:
                    if reversed_braille_dict[letter] == 'decimal':
                        output_text += '.'
                    else:
                        if letter not in reversed_numbers_braille_dict:
                            print("No space provided to signify end of numbers")
                            sys.exit(1)
                        output_text += reversed_numbers_braille_dict[letter]
                else:
                    if Caps_flag: 
                        output_text += reversed_braille_dict[letter].upper()
                        Caps_flag = False
                    else:
                        output_text += reversed_braille_dict[letter]

            return output_text
        
        else:
            # Print error message for invalid Braille
            print("Please enter a valid Braille statement")
            sys.exit(1)
    
    except KeyError as e: 
        print(f"Invalid Braille Sequence: {e}")
        sys.exit(1)
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try: 
        # Check if at least one argument is provided
        if len(sys.argv) < 2:
            print("Please provide text as an argument.")
            sys.exit(1)

        # Get the input text from command-line arguments
        input_text = ' '.join(sys.argv[1:])
        
        # Determine the type of conversion needed and call the appropriate function
        if is_braille(input_text):
            output_text = braille_to_english(input_text)
        else:
            output_text = english_to_braille(input_text)
        
        # Print the result
        print(output_text)
    except ValueError as e: 
        print(f"Error: {e}")
        sys.exit(1)
