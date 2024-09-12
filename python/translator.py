import sys

# Braille mappings for alphabet letters, space, capitalization, and numbers
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', " ": '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Braille mappings specifically for numbers
braille_number_map = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    'number': '.O.OOO'
}

# Reverse maps to convert Braille back to English
reverse_braille_map = {v: k for k, v in braille_map.items()}
reverse_braille_number_map = {v: k for k, v in braille_number_map.items()}

def is_braille(input_string):
    """
    Determine if the input string is in Braille format.
    
    A string is considered Braille if it contains only 'O' and '.' characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is Braille, False otherwise.
    """
    return all(c in 'O.' for c in input_string)

def english_to_braille(text):
    """
    Convert English text to Braille.

    Handles both uppercase letters (by adding a 'capital' Braille indicator)
    and numbers (by adding a 'number' Braille indicator).

    Args:
        text (str): The English text to convert.

    Returns:
        str: The Braille representation of the text.
    """
    result = []
    is_number = False  # Track if currently in a numeric sequence
    
    for char in text:
        if char.isupper():  # Check for uppercase letters
            result.append(braille_map['capital'])
            char = char.lower()  # Convert to lowercase for Braille mapping

        if char.isdigit() and not is_number:  # Start of a numeric sequence
            result.append(braille_map['number'])
            is_number = True  # Continue treating subsequent digits as numbers
        
        if char == " ":  # Handle spaces
            result.append(braille_map[" "])
            is_number = False  # Reset number tracking

        elif char in braille_map:  # Map letters and space
            result.append(braille_map[char])

        elif char in braille_number_map:  # Map numbers
            result.append(braille_number_map[char])
    
    return ''.join(result)

def braille_to_english(braille_string):
    """
    Convert Braille back to English text.

    Handles capitalization and numeric sequences as denoted in the Braille input.

    Args:
        braille_string (str): The Braille string to convert.

    Returns:
        str: The English representation of the Braille input.
    """
    output = []
    i = 0
    is_number = False  # Track if currently in a numeric sequence
    
    while i < len(braille_string):
        braille_char = braille_string[i:i+6]  # Braille characters are 6 dots long
        
        if braille_char == '.....O':  # Capital letter indicator
            output.append('capital')
            i += 6
        elif braille_char == '.O.OOO':  # Start of numeric sequence indicator
            is_number = True
            i += 6
        else:
            char = reverse_braille_map.get(braille_char, '')  # Convert Braille to English
            if output and output[-1] == 'capital':  # Handle capitalization
                char = char.upper()
                output.pop()  # Remove the capital indicator
            elif is_number and char.isalpha():  # Handle numeric sequences
                char = str(ord(char) - ord('a') + 1)  # Convert 'a'-'j' to '1'-'0'
                if char == '10':
                    char = '0'
            elif char == " ":  # Reset numeric sequence on space
                is_number = False
            output.append(char)
            i += 6
    return ''.join(output)

def main():
    """
    Main function to run the Braille translator.

    This function takes a single command-line argument: the text to translate.
    It determines whether the input is Braille or English and performs the
    appropriate conversion, printing the result to the console.
    """
    if len(sys.argv) < 2:
        print("Usage: python braille_translator.py 'text to translate '")
        return
    
    input_text = " ".join(sys.argv[1:])  # Combine all command-line arguments (starting from index 1) into a single string with spaces between them.

    # Determine if the input is Braille or English, and translate accordingly
    if is_braille(input_text):
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)
    
    print(translated_text)

# Entry point of the script
if __name__ == "__main__":
    main()
