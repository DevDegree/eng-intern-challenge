import re
import sys

# Braille dictionary
brailledict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'cf': '.....O', 'df': '.O...O', 'nf': '.O.OOO', '.': '..OO.O',
    ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O',
    ')': '.O.OO.', ' ': '......'
}

# Create separate dictionaries for letters and numbers to avoid conflicts
letters_to_braille = {k: v for k, v in brailledict.items() if k.isalpha()}
numbers_to_braille = {k: v for k, v in brailledict.items() if k.isdigit()}

# Reverse dictionaries for conversion from braille to English
braille_to_letters = {v: k for k, v in letters_to_braille.items()}
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}

# Function to detect whether the input string is Braille or English
def is_braille(input_string):
    # Braille patterns are groups of 6 characters consisting of only 'O' and '.'
    braille_pattern = r'^[O.]{6}$'
    # Check if all segments of input string match the braille pattern
    return all(re.match(braille_pattern, input_string[i:i+6]) for i in range(0, len(input_string), 6))

# Function to convert English to Braille
def english_to_braille(input_string):
    newstring = ''
    is_number_sequence = False  # Boolean to track number sequences

    for char in input_string:
        if char.isupper():
            newstring += brailledict['cf'] + brailledict[char.lower()]
            is_number_sequence = False  # Reset number sequence on encountering a non-number
        elif char.isdigit():
            if not is_number_sequence:
                # Add the number flag (nf) only once before the sequence of numbers
                newstring += brailledict['nf']
                is_number_sequence = True
            newstring += brailledict[char]
        elif char == ' ':
            newstring += brailledict[' ']
            is_number_sequence = False  # Reset number sequence on encountering a space
        else:
            newstring += brailledict[char]
            is_number_sequence = False  # Reset number sequence on encountering a non-number
    
    return newstring

# Function to convert Braille to English
def braille_to_english(input_string):
    newstring = ''
    is_capital = False
    is_digit = False
    
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]
        
        if braille_char == brailledict['cf']:
            is_capital = True
        elif braille_char == brailledict['nf']:
            is_digit = True
        elif braille_char == brailledict[' ']:
            # Add space and reset digit flag if the previous sequence was a number
            newstring += ' '
            is_digit = False
        elif is_digit and braille_char in braille_to_numbers:
            newstring += braille_to_numbers[braille_char]
        elif not is_digit and braille_char in braille_to_letters:
            char = braille_to_letters[braille_char]
            if is_capital:
                char = char.upper()
                is_capital = False
            newstring += char
        else:
            # If the braille character does not match any known pattern, just reset the digit flag
            is_digit = False
    
    return newstring

# Main function to handle user input and trigger appropriate conversion
def braille_converter(input_strings):
    results = []
    for input_string in input_strings:
        if is_braille(input_string):
            results.append(braille_to_english(input_string))
        else:
            results.append(english_to_braille(input_string))
    
    # Join results into a single output string
    return '......'.join(results)

# Entry point for the terminal application
if __name__ == '__main__':
    input_strings = sys.argv[1:]  # Read all input strings from command-line arguments
    if not input_strings:
        sys.exit(1)

    result = braille_converter(input_strings)
    print(result)
