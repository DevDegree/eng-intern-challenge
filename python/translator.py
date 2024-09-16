# translator.py

""" Description: Command-line/terminal Braille-English Translator
               The string to translate will be passed into your application 
               as an argument at runtime. Your application must be smart 
               enough to determine if the string given to it is either Braille 
               or English and automatically convert it to the appropriate 
               opposite.

               For the purposes of this challenge Braille must be displayed 
               as O and . where O represents a raised dot. You must include 
               the entire English alphabet, the ability to capitalize letters, 
               add spaces, and the numbers 0 through 9 as well.

               After conversion, output the translated string--and nothing 
               else--to the terminal. """

# Name: Felicia Jiang
# Date: Sept 01, 2204

# Import the sys module for accessing command-line arguments
import sys

# Dictionary for English to Braille mapping
# NOTE: Includes extra mappings for future use cases:
#       punctuation, the decimal indicator etc (not required)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', 'capital': '.....O', 'decimal': '.O...O','number': '.O.OOO', 
    '.': '..OO.O', ',': '..O...', ';': '..OO..', ':': '..OOO.', '?': '..O.O.', 
    '!': '..OOOO','-': '....O.', '/': '....OO', '<': '..O...', '>': '..OO..', 
    '(': '..OOO.', ')': '..OO.O', 'space': '......'
}


# Reverse mappings for letters, numbers, and punctuation
braille_to_letter = {}
braille_to_number = {}

# Separately populate the dictionaries for letter and number mappings
for key, value in braille_alphabet.items():
    if key.isalpha() or key in '.,;:?!-/<>':
        braille_to_letter[value] = key
    elif key.isdigit():
        braille_to_number[value] = key
 

# Function to detect if input is Braille or English
def is_braille(text):
    # Define braille_chars as a set (for fast membership testing)
    braille_chars = {'O', '.'}

    # If all char is found to be either 'O' or '.' then it is braille
    for c in text:
        if c not in braille_chars:
            return False
    return True

# Function to translate English to Braille
# NOTE: Includes cases that handle spaces, capital letters, numbers, and decimals
def eng_to_braille(text):

    # Initialize list to hold the translated Braille
    result = []
    # Keep track of the previous character in the text (to detect decimals)
    prev_char = ''
    # To track if we're in number mode
    is_number_mode = False
    
    # Loop through all characters in the input
    for char in text:
        # Handle spaces
        if char == ' ':
            result.append(braille_alphabet['space'])
            # Exit number mode after a space
            is_number_mode = False
        
        # Handle uppercase letters
        elif char.isupper():
            result.append(braille_alphabet['capital'])
            result.append(braille_alphabet.get(char.lower(), ''))
            # Exit number mode after a letter
            is_number_mode = False
        
        # Handle numbers and check for decimals
        elif char.isdigit():
            if prev_char == '.':
                result.append(braille_alphabet['decimal'])
            elif not is_number_mode:
                result.append(braille_alphabet['number'])
                # Enter number mode when a digit is found
                is_number_mode = True
            result.append(braille_alphabet.get(char.lower(), ''))
        
        # Handle letters and punctuation
        else:
            result.append(braille_alphabet.get(char.lower(), ''))
            # Exit number mode after a non-digit character
            is_number_mode = False
        
        prev_char = char

    return ''.join(result)

# Function to translate Braille to English
def braille_to_eng(text):
    result = []
    i = 0
    # To track if we're in number mode
    is_number_mode = False

    while i < len(text):
        # Check for incomplete Braille symbols
        if len(text) - i < 6:
            result.append(' [Error: Incomplete Braille symbol]')
            break

        symbol = text[i:i+6]

        # Handle capital letters
        if symbol == braille_alphabet['capital']:
            i += 6
            if len(text) - i < 6:
                result.append(' [Error: Incomplete Braille symbol after capital indicator]')
                break
            symbol = text[i:i+6]
            result.append(braille_to_letter.get(symbol, '').upper())

            # Exit number mode after capital letter
            is_number_mode = False 
            i += 6
            continue

        # Handle number indicator
        elif symbol == braille_alphabet['number']:
            # Enter number mode
            is_number_mode = True
            i += 6
            continue

        # Handle spaces
        elif symbol == braille_alphabet['space']:
            result.append(' ')
            # After a space, exit number mode after a space
            is_number_mode = False 
            i += 6
            continue

        # Handle letters, punctuation and numbers
        else:
            if is_number_mode:
                # If in number mode it's a number
                result.append(braille_to_number.get(symbol, ''))
            else:
                # Otherwise it's letter or punctuation
                result.append(braille_to_letter.get(symbol, ''))

        i += 6

    return ''.join(result)


def main():
    # Check if the necessary command-line arguments are provided
    if len(sys.argv) < 2:
        # Print how to use the script if arguments aren't provided
        print("Usage: python braille_translator.py <text>")
        return

    # Combine all command-line arguments into a single string
    input = ' '.join(sys.argv[1:])

    # Check if the input is in Braille or English
    if is_braille(input):
        print(braille_to_eng(input))
    else:
        print(eng_to_braille(input))

if __name__ == "__main__":
    main()