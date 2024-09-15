import sys

# Braille mappings for letters a-z based on the chart
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# Braille mappings for numbers 1-0
braille_numbers = {
    '1': braille_letters['a'], '2': braille_letters['b'], '3': braille_letters['c'], 
    '4': braille_letters['d'], '5': braille_letters['e'], '6': braille_letters['f'], 
    '7': braille_letters['g'], '8': braille_letters['h'], '9': braille_letters['i'], 
    '0': braille_letters['j']
}

# Correct Braille punctuation based on your feedback
braille_punctuation = {
    '.': '..OO.O',  # Period
    ',': '..O...',  # Comma
    '?': '..O.OO',  # Question mark
    '!': '..OOO.',  # Exclamation mark
    ':': '..OO..',  # Colon
    ';': '..O.O.',  # Semicolon
    '-': '....OO',  # Hyphen
    '/': '.O..OO',  # Slash
    '<': '.OO..O',  # Less-than
    '>': 'O..OO.',  # Greater-than
    '(': 'O.O..O',  # Left parenthesis
    ')': '.O.OO.',  # Right parenthesis
    'decimal': '.O...O'  # Decimal point
}

# Reverse mappings for Braille to English
letters_braille = {v: k for k, v in braille_letters.items()}
numbers_braille = {v: k for k, v in braille_numbers.items()}
punctuation_braille = {v: k for k, v in braille_punctuation.items()}

# Special Braille signs
capital_sign = '.....O'
number_sign = '.O.OOO'

def is_braille(input_str):
    # Check if the input consists only of O, ., and spaces
    allowed_chars = {'O', '.', ' '}
    return set(input_str).issubset(allowed_chars)

def english_to_braille(text):
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        
        # Handle capital letters
        if char.isupper():
            result.append(capital_sign)
            char = char.lower()  # Convert to lowercase for translation
        
        # Handle numbers
        if char.isdigit():
            result.append(number_sign)
            while i < len(text) and text[i].isdigit():
                result.append(braille_numbers[text[i]])
                i += 1
            continue  # Skip increment since digits are already handled
        
        # Handle spaces
        elif char == ' ':
            result.append('......')
        
        # Handle punctuation and decimal point
        elif char == '.':
            # Check if it's part of a number (for decimal point)
            if i > 0 and text[i-1].isdigit() and (i + 1 < len(text) and text[i+1].isdigit()):
                result.append(braille_punctuation['decimal'])  # Decimal point in numbers
            else:
                result.append(braille_punctuation['.'])  # Regular period
        
        elif char in braille_punctuation:
            result.append(braille_punctuation[char])
        
        # Handle regular letters
        elif char in braille_letters:
            result.append(braille_letters[char])
        
        i += 1
    
    # Join the Braille result into a single string
    return ''.join(result)

def braille_to_english(braille):
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]  # Split into chunks of 6
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille_chars):
        symbol = braille_chars[i]
        
        # Handle spaces
        if symbol == '......':  
            result.append(' ')
        
        # Handle capitalization
        elif symbol == capital_sign:
            capitalize_next = True
        
        # Handle number mode
        elif symbol == number_sign:
            number_mode = True
        
        # Handle numbers after number sign
        elif number_mode:
            if symbol in numbers_braille:
                result.append(numbers_braille[symbol])
            elif symbol == braille_punctuation['decimal']:  # Check for decimal point in number mode
                result.append('.')
            else:
                number_mode = False  # Exit number mode when a non-digit is found
        
        # Handle decimal point outside number mode
        elif symbol == braille_punctuation['decimal']:
            result.append('.')
        
        # Handle other punctuation
        elif symbol in punctuation_braille:
            result.append(punctuation_braille[symbol])
        
        # Handle letters
        elif symbol in letters_braille:
            char = letters_braille[symbol]
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            result.append(char)
        
        i += 1

    return ''.join(result)


def main():
    input_args = sys.argv[1:]
    input_str = ' '.join(input_args)
    
    if is_braille(input_str):
        translated = braille_to_english(input_str)
    else:
        translated = english_to_braille(input_str)
    
    print(translated)

if __name__ == '__main__':
    main()
