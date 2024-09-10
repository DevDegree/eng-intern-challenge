# English to Braille dictionary (6 character strings)
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..', '.': '..O.OO', ',': '..O...', '?': '..OO.O',
    '!': '..OOO.', ':': 'OOO..O', ';': 'O.O...', '-': '......'
}

# Braille to English dictionary (reverse of above)
braille_to_english = {v: k for k, v in english_to_braille.items()}

# Capital and number indicators
CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '..0000'

def text_to_braille(text):
    result = []
    is_number_sequence = False  # To track if we're in a number sequence

    for char in text:
        if char.isupper():
            result.append(CAPITAL_INDICATOR)  # Capital indicator
            char = char.lower()
        
        if char.isdigit():
            if not is_number_sequence:  # Add number indicator once at the start of a number sequence
                result.append(NUMBER_INDICATOR)
                is_number_sequence = True
        else:
            is_number_sequence = False  # Reset when the sequence of digits ends
            
        # Add the Braille representation for the character
        result.append(english_to_braille.get(char, ''))
    
    return ''.join(result)

def braille_to_text(braille):
    result = []
    capital = False
    number = False
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == CAPITAL_INDICATOR:
            capital = True
        elif symbol == NUMBER_INDICATOR:
            number = True
        else:
            char = braille_to_english.get(symbol, '')
            if number and char in '1234567890':
                result.append(char)
            elif capital:
                result.append(char.upper())
                capital = False
            else:
                result.append(char)
            number = False
    return ''.join(result)

if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    
    # Check if input is Braille or English (assume English if no numbers or dots)
    if all(char in ['O', '.', ' '] for char in input_text):
        # Assume input is Braille, convert to English
        print(braille_to_text(input_text))
    else:
        # Otherwise, assume it's English, convert to Braille
        print(text_to_braille(input_text))
