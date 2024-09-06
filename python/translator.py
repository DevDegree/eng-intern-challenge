import sys

# Define the Braille symbols for capital and number modes
CAPITAL_FOLLOWS = '.....O'  # Marks the next letter as capital
NUMBER_FOLLOWS = '.O.OOO'   # Marks the following characters as numbers

# Define the Braille alphabet with periods and circles
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}

# Define the Braille alphabet for numbers
braille_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

# Create reverse dictionaries for English to Braille and numbers
english_to_braille = {v: k for k, v in braille_to_english.items()}
number_to_braille = {v: k for k, v in braille_numbers.items()}

def braille_to_text(braille_string):
    """Translate Braille representation to English text.
	
	Args:
		braille_string (str): The Braille representation to be translated.
		
	Returns:
		str: The English text of the input text.
	"""
    output = []
    i = 0
    is_number_mode = False  # Flag to indicate number mode
    is_capital_mode = False  # Flag to indicate capital mode

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]

        # Handle special symbols
        if braille_char == NUMBER_FOLLOWS:
            is_number_mode = True  # Enter number mode
            i += 6  # Move to the next character after detecting number mode
            continue
        elif braille_char == CAPITAL_FOLLOWS:
            is_capital_mode = True  # Enter capital mode
        elif braille_char == '......':  # Handle spaces
            output.append(' ')
            is_number_mode = False  # Reset number mode after a space
        else:
            # Handle number mode as a loop: Process until we encounter a non-number or a space
            if is_number_mode:
                while i < len(braille_string) and braille_string[i:i+6] in braille_numbers:
                    output.append(braille_numbers[braille_string[i:i+6]])
                    i += 6  # Move to the next Braille character
                is_number_mode = False  # Exit number mode after processing all numbers
                continue

            # Handle letters
            if braille_char in braille_to_english:
                letter = braille_to_english[braille_char]
                if is_capital_mode:
                    letter = letter.upper()  # Capitalize the next letter
                    is_capital_mode = False  # Reset capital mode after one letter
                output.append(letter)

        i += 6  # Move to the next Braille character

    return ''.join(output)

def text_to_braille(text_string):
    """Translate English text to Braille representation.
	
	Args:
		text_string (str): The English text to be translated.
		
	Returns:
		str: The Braille representation of the input text.
	"""
    output = []
    is_number_mode = False

    for char in text_string:
        if char.isdigit():
            if not is_number_mode:
                output.append(NUMBER_FOLLOWS)  # Enter number mode
                is_number_mode = True
            output.append(number_to_braille[char])
        elif char == ' ':
            output.append('......')  # Space
            is_number_mode = False  # Exit number mode after space
        else:
            if is_number_mode:
                is_number_mode = False  # Exit number mode for letters
            if char.isupper():
                output.append(CAPITAL_FOLLOWS)  # Capital symbol for next letter
                char = char.lower()
            output.append(english_to_braille[char])
    return ''.join(output)

def detect_translation_mode(input_string):
    """Determine if input is Braille or English
    
    Args:
		input_string (str): The input string to be analyzed.
    
	Returns:
		str: 'braille_to_text' if the input is Braille, 'text_to_braille' otherwise.
    """
    # Check if the input contains only Braille symbols (O, ., and space)
    if all(c in ['O', '.', ' '] for c in input_string):
        return 'braille_to_text'
    return 'text_to_braille'

if __name__ == "__main__":
    # Collect input from command-line arguments
    input_strings = sys.argv[1:]
    
    # Combine input strings
    combined_input = ' '.join(input_strings)
    
    # Detect if the input is Braille or English
    translation_mode = detect_translation_mode(combined_input)
    
    if translation_mode == 'braille_to_text':
        # Translate Braille to English
        result = braille_to_text(combined_input)
    else:
        # Translate English to Braille
        result = text_to_braille(combined_input)
    
    # Output the result
    print(result)
