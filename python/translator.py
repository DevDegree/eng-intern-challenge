# Mappings for English characters to Braille and vice versa
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO',
    '.': '.O....'
}

# Mapping for digits to Braille and vice versa
numbers_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings
reverse_braille_dict = {v: k for k, v in braille_dict.items() if k not in ['capital', 'number', '.']}
reverse_numbers_dict = {v: k for k, v in numbers_dict.items()}

def english_to_braille(english_str: str) -> str:
    """Converts an English string to Braille representation."""
    braille_str = ""
    number_mode = False  # Track if the current mode is number mode
    
    for char in english_str:
        if char.isdigit():
            if not number_mode:
                braille_str += braille_dict['number']  # Add number mode symbol
                number_mode = True
            braille_str += numbers_dict[char]  # Add Braille for the digit
        elif char == '.':
            braille_str += braille_dict['.']  # Add Braille for decimal point
        elif char.isalpha():
            if number_mode:
                number_mode = False  # Switch back to letter mode
            
            # Check if the character is uppercase
            if char.isupper():
                braille_str += braille_dict['capital']  # Add capitalization symbol
            braille_str += braille_dict[char.lower()]  # Add Braille for the character
        elif char == ' ':
            number_mode = False
            braille_str += braille_dict[' ']  # Add Braille for space
    
    return braille_str

def braille_to_english(braille_str: str) -> str:
    """Converts a Braille string to English representation."""
    english_str = ""
    # Split the Braille string into cells of 6 dots each
    braille_cells = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    
    number_mode = False
    capitalize_next = False  # Flag to indicate if the next letter should be capitalized
    
    for cell in braille_cells:
        if cell == braille_dict['number']:
            number_mode = True  # Enter number mode
            continue
        
        if number_mode:
            if cell in reverse_numbers_dict:
                english_str += reverse_numbers_dict[cell]  # Convert Braille digit to English
            elif cell == braille_dict['.']:
                english_str += '.'  # Handle decimal point
            else:
                number_mode = False  # Reset if encountering a non-numeric cell
                english_str += '?'  # Placeholder for unrecognized cell
        elif cell == braille_dict['capital']:
            capitalize_next = True  # Prepare to capitalize next letter
            continue  # Ignore capitalization symbol
        elif cell in reverse_braille_dict:
            char = reverse_braille_dict[cell]
            if capitalize_next:
                char = char.upper()  # Capitalize the character if flag is active
                capitalize_next = False  # Reset flag
            english_str += char
        else:
            english_str += '?'  # Placeholder for unrecognized cell
    
    return english_str.strip()  # Remove any leading or trailing whitespace

if __name__ == "__main__":
    import sys
    input_str = " ".join(sys.argv[1:])
    
    if all(c in "O." for c in input_str):
        # Input is in Braille
        print(braille_to_english(input_str))
    else:
        # Input is in English
        print(english_to_braille(input_str))
