# Define the Braille mappings
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_SPACE = '......'

# Combine letters and numbers into a single dictionary for reverse lookup
ENGLISH_TO_BRAILLE = {**BRAILLE_LETTERS, **BRAILLE_NUMBERS}
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}


def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            result.append(BRAILLE_NUMBER)
            number_mode = True
        
        if char.isalpha():
            if char.isupper():
                result.append(BRAILLE_CAPITAL)
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
            number_mode = False
        
        elif char == ' ':
            result.append(BRAILLE_SPACE)
            number_mode = False
            
        elif char.isdigit():
            result.append(BRAILLE_NUMBERS[char])
    
    return ''.join(result)


def braille_to_english(braille):
    result = []
    index = 0
    number_mode = False
    
    while index < len(braille):
        symbol = braille[index:index + 6]
        
        if symbol == BRAILLE_CAPITAL:
            index += 6
            next_symbol = braille[index:index + 6]
            result.append(BRAILLE_TO_ENGLISH[next_symbol].upper())
        
        elif symbol == BRAILLE_NUMBER:
            number_mode = True
        
        elif symbol == BRAILLE_SPACE:
            result.append(' ')
            number_mode = False
        
        else:
            if number_mode:
                result.append(BRAILLE_TO_ENGLISH[symbol])
            else:
                result.append(BRAILLE_TO_ENGLISH[symbol])
        
        index += 6
        
    return ''.join(result)


# Example usage
if __name__ == "__main__":
    import sys

#    input_text = sys.argv[1]
    input_text = ' '.join(sys.argv[1:])

    
    # Determine if input is Braille or English
    if all(c in "O." for c in input_text):  # Check if the input is Braille
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
