import sys

# Braille and English character mapping
# This dictionary maps English symbols to their corresponding Braille representations
english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', ',': '..O...', '.': '..OO.O', '!': 'O.OOOO',
    '?': '..O.OO', '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
    '(': 'O.O..O', ')': '.O.OO.', ':': '..OO..', ';': '..O.O.',
    'capital_follows': '.....O',  
    'number_follows': '.O.OOO',  
    'decimal_follows': '.O...O'  
}

# Mapping for numbers to Braille and numbers
# This dictionary maps digits to their corresponding Braille representations
numbers_to_braille_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Reverse mappings for Braille to English and numbers
# These dictionaries map Braille representations back to their English or numeric equivalents
braille_to_numbers_map = {v: k for k, v in numbers_to_braille_map.items()}
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}

def main(args):
    # Combine all command-line arguments into a single string
    input_str = ' '.join(args[1:])  

    # Determine if the input string is Braille (only contains 'O' and '.' and its length is a multiple of 6)
    is_braille = all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

    ans = []  # This will hold the final translated result
    index = 0  # This index will be used to iterate over the input string
    capitalize = False  # This flag indicates whether the next character should be capitalized
    number_follows = False  # This flag indicates whether the following characters are numbers

    if is_braille:
        # Process Braille input
        while index < len(input_str):
            # Extract the next 6 characters, which correspond to one Braille character
            char = input_str[index:index+6]
            index += 6
            
            # Handle special cases for capitalization and number sequences
            if char == english_to_braille_map['capital_follows']:
                capitalize = True
            elif char == english_to_braille_map['number_follows']:
                number_follows = True
            elif char == english_to_braille_map[' ']:
                # If it's a space, add a space to the result and reset the flags
                ans.append(' ')
                capitalize = False
                number_follows = False
            else:
                # Translate the Braille character to its English equivalent
                if number_follows and char in braille_to_numbers_map:
                    letter = braille_to_numbers_map[char]  # Translate as a number
                else:
                    letter = braille_to_english_map.get(char, '')  # Default to empty if not found
                if capitalize:
                    letter = letter.upper()  # Capitalize if the flag is set
                    capitalize = False
                ans.append(letter)  # Append the translated character to the result

    else:
        # Process English input
        for char in input_str:
            if char.isupper():
                ans.append(english_to_braille_map['capital_follows'])  # Add the capitalization marker
                char = char.lower()  # Convert to lowercase for translation
            if char.isdigit():
                if not number_follows:
                    ans.append(english_to_braille_map['number_follows'])  # Add the number marker
                    number_follows = True
                # Translate the digit to its Braille representation (using letters 'a' to 'j')
                char = 'abcdefghij'[int(char) - 1] if char != '0' else 'j'
            else:
                number_follows = False  # Reset the number marker after non-digit character
            ans.append(english_to_braille_map.get(char, '......'))  # Default to space for unknown characters

    # Print the final translated result
    print(''.join(ans))

if __name__ == "__main__":
    main(sys.argv)
