import sys

# Braille alphabet and special symbols
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'k': 'O...O.'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_special_chars = {
    'capital': '.....O',  # Capital indicator
    'decimal': '.O...O',  # Decimal indicator
    'number': '.O.OOO',   # Number indicator
    '.': '..OO.O',      # Full stop (period) symbol
    ',': '..O...',    # Comma symbol
    '?': '..O.OO', # Question mark symbol
    '!':'..OOO.', # Exclamation mark symbol
    ':':'..OO..',     # Colon symbol
    ';': '..O.O.', # Semicolon symbol
    '-': '....OO',     # Dash symbol
    '/': '.O..O.', # Forward slash symbol
    '<': '.OO..O',     # Less than symbol
    '>': 'O..OO.',  # Greater than symbol
    '(': 'O.O..O', # Left parenthesis symbol
    ')': '.O.OO.', # Right parenthesis symbol
    'space': '......'     # Space symbol
}

# Translate to Braille
def to_braille(text):
    result = []
    is_number_mode = False
    
    for i, char in enumerate(text):
        if char.isupper():
            # Capital letter, use the capital indicator
            result.append(braille_special_chars['capital'])
            result.append(braille_letters[char.lower()])
        elif char.isdigit():
            # Number mode, use the number indicator if not already in number mode
            if not is_number_mode:
                result.append(braille_special_chars['number'])
                is_number_mode = True
            result.append(braille_numbers[char])
        elif char == '.':
            # Handle decimal point vs full stop
            if is_number_mode:
                # Decimal point in number mode, add the decimal indicator first, then the dot
                result.append(braille_special_chars['decimal'])  # Decimal point indicator
                result.append(braille_special_chars['.'])       # Actual dot for decimal
            else:
                # Full stop (period) when not in number mode
                result.append(braille_special_chars['.'])
        elif char == ' ':
            # Space, reset number mode
            result.append(braille_special_chars['space'])
            is_number_mode = False  # Exit number mode after space
        elif char in braille_special_chars:
            # Special characters (punctuation, symbols, etc.)
            result.append(braille_special_chars[char])
        elif char in braille_letters:
            # Regular lowercase letters
            result.append(braille_letters[char])
        else:
            raise ValueError(f"Unsupported character: {char}")
        
        # Handle case where decimal starts the number 
        if char == '.' and (i == 0 or not text[i - 1].isdigit()):
            result.insert(-1, braille_special_chars['number'])  # Add number sign before decimal if no digit precedes

    return ''.join(result)



# Translate to English
def to_english(braille):
    result = []
    is_capital = False
    is_number = False
    
    # Process Braille in chunks of 6 characters
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]  

        if symbol == braille_special_chars['capital']:
            is_capital = True
        elif symbol == braille_special_chars['number']:
            is_number = True
        elif symbol == braille_special_chars['space']:
            result.append(' ')
            is_capital = False
            is_number = False
        elif symbol == braille_special_chars['.']:  # Full stop or period
            result.append('.')
        elif symbol == braille_special_chars['decimal']:  # Decimal point
            result.append('.')
        else:
            if is_number:
                for digit, braille_digit in braille_numbers.items():
                    if symbol == braille_digit:
                        result.append(digit)
                        break
                # Stay in number mode after decimal until space or end of number sequence
            else:
                for letter, braille_letter in braille_letters.items():
                    if symbol == braille_letter:
                        if is_capital:
                            result.append(letter.upper())
                            is_capital = False
                        else:
                            result.append(letter)
                        break
    return ''.join(result)


def translate(input_string):
    if all(c in "O. " for c in input_string):  # Check to see if it's Braille or English
        return to_english(input_string)
    else:
        return to_braille(input_string)
    


# Main function to handle command-line arguments
def main():
    translations = [to_braille(arg) for arg in sys.argv[1:]]  # Translate each argument
    print('......'.join(translations))
    
main()