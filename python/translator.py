import sys

# Braille mappings for text characters (letters, space)
text_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Braille signs
capital_sign = '.....O'
number_sign = '.O.OOO'

# Braille mappings for numbers (0-9)
numbers_to_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Inverted dictionary for translating Braille back to text (letters, space)
inverse_braille_text = {v: k for k, v in text_to_braille_dict.items()}

# Inverted dictionary for translating Braille back to numbers
inverse_braille_numbers = {v: k for k, v in numbers_to_braille_dict.items()}

# Function to check if a string is valid Braille (all dots or spaces)
def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def text_to_braille(text):
    """
    Converts text to braille
    
     Algorithm:
    -Iterates through each character in the input text.
    -Checks if the character is uppercase, and if so, adds the capital sign and converts the character to lowercase.
    -Checks if the character is a digit, and if so, enters number mode and adds the number sign if necessary. Then, adds the corresponding Braille representation of the digit.
    -If the character is not a digit or uppercase letter, adds the corresponding Braille representation from the text_to_braille_dict.
    -Returns the concatenated Braille string.
            """
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(capital_sign)
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(number_sign)
                number_mode = True
            result.append(numbers_to_braille_dict[char])
        else:
            if number_mode and char != ' ':
                number_mode = False
            result.append(text_to_braille_dict[char])
    
    return ''.join(result)

def braille_to_text(braille):
    """
    Converts braille into text.

    Algorithm:
    -Iterates through the Braille string in chunks of 6 dots (representing individual Braille characters).
    -Checks if the current chunk is the capital sign or number sign, and sets the corresponding flags.
    -If the current chunk is a space, adds a space to the text and resets the number mode.
    -If the current chunk is a valid Braille character, looks up its corresponding English character in the appropriate dictionary (either inverse_braille_text or inverse_braille_numbers).
    -If the capital mode is set, capitalizes the translated character.
    -Adds the translated character to the result.
    -Returns the concatenated English text.
    """

    result = []
    i = 0
    number_mode = False
    capital_mode = False
    
    while i < len(braille):
        current_symbol = braille[i:i+6]
        
        if current_symbol == capital_sign:
            capital_mode = True
        elif current_symbol == number_sign:
            number_mode = True
        elif current_symbol == '......':
            result.append(' ')
            number_mode = False  # Reset number mode on space
        else:
            if number_mode:
                result.append(inverse_braille_numbers.get(current_symbol, '?'))  
            else:
                letter = inverse_braille_text.get(current_symbol, '?') 
                if capital_mode:
                    letter = letter.upper()
                    capital_mode = False
                result.append(letter)
        i += 6
    
    return ''.join(result)

def main():
    # Get input from the command line
    input_string = ' '.join(sys.argv[1:]).strip()
    
    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))

if __name__ == '__main__':
    main()