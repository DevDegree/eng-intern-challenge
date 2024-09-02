# Was unable to complete the challenge



import sys

# Dictionary used for mapping 
braille_letters_symbols = {
    # Letters (a-z)
    'a': 'O......', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO..O.', 'e': 'O...O.',
    'f': 'OOO...', 'g': 'OOO.O.', 'h': 'O.O.O.', 'i': '.OO...', 'j': '.OO.O.',
    'k': 'O..O..', 'l': 'O.O.O.', 'm': 'OO.O..', 'n': 'OO.OO.', 'o': 'O...O.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O....O', 's': '.OO.O.', 't': '.O....',
    'u': 'O..O.O', 'v': 'O.O..O', 'w': '.O...O', 'x': 'OO.O.O', 'y': 'OO.OOO',
    'z': 'O..OOO',  # Corrected mapping for 'z'

    # Capital letter indicator
    'capital': '.....O',

    # Punctuation and special symbols
    ',': '.O....',  # Comma
    '.': '.O..OO',  # Period
    '?': '.OO.O.',  # Question mark
    '!': '.OOO.O',  # Exclamation mark
    ':': '.O..O.',  # Colon
    ';': '.OO...',  # Semicolon
    '-': '..O.O.',  # Hyphen
    '/': '..O.O.',  # Slash
    '<': '.O...O',  # Less than
    '>': 'OOO...',  # Greater than
    '(': '.OO..O',  # Open parenthesis
    ')': '.OO..O',  # Close parenthesis

    # Space
    ' ': 'OOOOOO'
}

braille_numbers = {
    # Number indicator
    'number': '..O...',

    # Numbers (0-9)
    '1': 'O......', '2': 'O.O...', '3': 'OO....', '4': 'OO..O.', '5': 'O...O.',
    '6': 'OOO...', '7': 'OOO.O.', '8': 'O.O.O.', '9': '.OO...', '0': '.OO.O.',

    # Decimal point indicator
    'decimal': '.O..OO'
}

def translate_to_braille(text):
    result = []
    number = False

    for char in text:
        if char.isdigit():
            if number == False:  # Explicit check if number is False
                result.append(braille_numbers['number'])
                number = True
            result.append(braille_numbers[char])
        
        elif char == '.' and number == True:  # Explicit check if number is True
            result.append(braille_numbers['decimal'])
        
        elif char.isalpha():
            number = False  # Set number to False since we encountered a letter
            if char.isupper():
                result.append(braille_letters_symbols['capital'])
                char = char.lower()
            result.append(braille_letters_symbols[char])
        
        else:
            try:
                result.append(braille_letters_symbols[char])  # This will handle the space if it is defined
            except KeyError:  
                print(f"Error: '{char}' is not a recognized symbol.")

    return ''.join(result)



braille_to_english_numbers = {
    # Numbers
    'O......': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO..O.': '4', 
    'O...O.': '5', 
    'OOO...': '6', 
    'OOO.O.': '7', 
    'O.O.O.': '8', 
    '.OO...': '9', 
    '.OO.O.': '0',

    # Number mode indicator
    '..O...': 'number follows'  # Indicates numbers to follow
}

braille_to_english_letters_symbols = {
    # Letters
    'O......': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO..O.': 'd',
    'O...O.': 'e',
    'OOO...': 'f',
    'OOO.O.': 'g',
    'O.O.O.': 'h',
    '.OO...': 'i',
    '.OO.O.': 'j',
    'O..O..': 'k',
    'O.O.O.': 'l',
    'OO.O..': 'm',
    'OO.OO.': 'n',
    'O...O.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O....O': 'r',
    '.OO.O.': 's',
    '.O....': 't',
    'O..O.O': 'u',
    'O.O..O': 'v',
    '.O...O': 'w',
    'OO.O.O': 'x',
    'OO.OOO': 'y',
    'O..0OO': 'z',  # Note the 'z' mapping might be incorrect

    # Symbols
    '.O.OOO': 'capital follows',  # Capitalization symbol
    '..O.O.': '.',  # Period
    '..O.O.': ',',  
    '..OO.O': '?',  
    '..O..O': '!',  
    '..OO..': ':',  
    '..O...': ';',  
    '..O..O': '-',  
    '..O...': '/',  
    '..O..O': '<',  
    '..O...': '>',  
    '..O..O': '(',  
    '..O...': ')',
    'OOOOOO': 'space'
}

def translate_to_english(text):
    result = []
    cap_letter = False
    number = False

    if len(text) % 6 != 0:
        print("Error: Input length is not divisible by 6. Please check the input.")
    else:
        for i in range(0, len(text),6):
            braille_character = text[i:i+6]
            if braille_character == '0.00.0':
                result.append('.')
            elif braille_character == '00000.':
                cap_letter = True
            elif braille_character == '0.0...':
                number = True
            elif braille_character == '000000':
                number = False
                result.append(' ')
            if number == False and cap_letter == True:
                try:
                    result.append(braille_to_english_letters_symbols[braille_character].upper())
                    cap_letter = False
                except KeyError:
                    print(f"Error: '{braille_character}' is not in the braille dictionary.")
            elif number == False:
                try:
                    result.append(braille_to_english_letters_symbols[braille_character])
                except KeyError:
                    print(f"Error: '{braille_character}' is not in the braille dictionary.")
            elif number == True:
                try: 
                    result.append(braille_to_english_numbers[braille_character])
                except KeyError:
                    print(f"Error: '{braille_character}' is not in the braille dictionary or is not a number.")
        return result

def is_it_braille_or_english(text):
    is_brail = all(char in {'0', '1'} for char in text)
    if len(text) >= 6 and is_brail:
        return translate_to_english(text)
    else:
        return translate_to_braille(text)

def main():
    # Get command-line arguments excluding the script name
    args = sys.argv[1:]

    # Combine arguments into a single string
    text = ' '.join(args)

    # Determine if input is Braille or English and translate
    result = is_it_braille_or_english(text)

    # Print the translated result
    print(result)

if __name__ == "__main__":
    main()

















