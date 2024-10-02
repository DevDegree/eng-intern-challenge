import sys 

# Dictionary to map lowercase letters to their Braille representation
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'  # space
}

# Dictionary to map punctuation to their Braille representation
braille_punctuation = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
}

# Dictionary to map digits to their Braille representation
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
}

# Constants for Braille indicators
capital_follows = '.....O'  # Indicator for capital letters
number_follows = '.O.OOO'     # Indicator for numbers
decimal_follows = '.0...0' #Indicator for decimals

# Size of a Braille character in terms of dots (6)
braille_char_size = 6
# Check if the input string is in Braille format (only contains 'O' and '.')
def is_braille_format(input_str):
    return all(char in ['O', '.'] for char in input_str)

#Translate an English string to its Braille representation 
def english_to_braille(input_str):
    output_braille = ''
    number_mode = False  # Flag to indicate if the last character was a number

    for character in input_str:
        if character.isupper():  # Handle uppercase letters
            output_braille += capital_follows + braille_letters[character.lower()]
            number_mode = False
        elif character.isdigit():  # Handle digits
            if number_mode:
                output_braille += braille_numbers[character]
            else:
                output_braille += number_follows + braille_numbers[character]
                number_mode = True
        elif character in braille_letters:  # Handle letters
            output_braille += braille_letters[character]
            number_mode = False
        elif character in braille_punctuation:  # Handle punctuation
            output_braille += braille_punctuation[character]
            number_mode = False
        elif character == ' ':  # Handle spaces
            output_braille += braille_letters[' ']  # Add Braille representation of space
            number_mode = False  # Reset number mode after space

    return output_braille
#Translate a Braille string to its English representation 
def braille_to_english(input_str):

    output_english = ''
    capital_mode = False  # Flag for capital letters
    number_mode = False   # Flag for number sequences

    # Reverse mapping for quick lookup from Braille to English
    reverse_braille_map = {v: k for k, v in braille_letters.items()}
    reverse_braille_punct_map = {v: k for k, v in braille_punctuation.items()}
    reverse_braille_num_map = {v: k for k, v in braille_numbers.items()}

    # Process the Braille string in chunks of Braille character size
    for i in range(0, len(input_str), braille_char_size):
        braille_chunk = input_str[i:i + braille_char_size]

        # Check if the current chunk is an indicator
        if braille_chunk == capital_follows:
            capital_mode = True  # Next character should be uppercase
        elif braille_chunk == number_follows:
            number_mode = True  # Next characters should be treated as numbers
        elif braille_chunk in reverse_braille_map.values():
            # Decode Braille character
            if number_mode:
                output_english += reverse_braille_num_map[braille_chunk]  # Append as number
                number_mode = False  # Reset number mode after using it
            elif capital_mode:
                output_english += reverse_braille_map[braille_chunk].upper()  # Uppercase letter
                capital_mode = False  # Reset after use
            else:
                output_english += reverse_braille_map[braille_chunk]  # Regular character
        elif braille_chunk in reverse_braille_punct_map.values():
            output_english += reverse_braille_punct_map[braille_chunk]  # Punctuation character
        else:
            output_english += ' '  # Handle unrecognized Braille character

    return output_english

def main():
    # Take input from command line arguments
    input_string = ' '.join(sys.argv[1:])

    # Determine if the input is Braille or English and translate accordingly
    if is_braille_format(input_string):
        translated_output = braille_to_english(input_string)
    else:
        translated_output = english_to_braille(input_string)

    print(translated_output)

if __name__ == "__main__":
    main()
