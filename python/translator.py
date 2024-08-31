import sys

# Mapping of lowercase English letters and space to their Braille equivalents
lowercase_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

def invert_mapping(mapping):
    """Returns an inverted dictionary."""
    return {v: k for k, v in mapping.items()}

# Inverted mappings
braille_to_lowercase = invert_mapping(lowercase_to_braille)

# Mapping of decimal digits to their Braille equivalents
digit_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_to_digit = invert_mapping(digit_to_braille)

# Special markers
capital_marker = '.....O'  
number_marker = '.O.OOO'   

def is_braille_valid(braille_string):
    """Check if the input is a valid Braille string."""
    return all(c in 'O.' for c in braille_string) and len(braille_string) % 6 == 0

def english_to_braille(english_string):
    braille_string = ""
    number_mode = False

    for char in english_string:
        if char.isdigit():  
            if not number_mode:
                number_mode = True
                braille_string += number_marker
            braille_string += digit_to_braille[char]
        else:
            number_mode = False
            if char.isupper(): 
                braille_string += capital_marker
                char = char.lower()
            braille_string += lowercase_to_braille[char]

    return braille_string

def braille_to_english(braille_string):
    braille_cells = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    english_string = ""

    capital_mode = False
    number_mode = False
    for cell in braille_cells:
        if cell == capital_marker:
            capital_mode = True
            continue
        if cell == number_marker:
            number_mode = True
            continue
        if cell == lowercase_to_braille[' ']:
            number_mode = False
            english_string += ' '
        elif number_mode:
            english_string += braille_to_digit[cell]
        else:
            char = braille_to_lowercase[cell]
            if capital_mode:
                char = char.upper()
                capital_mode = False
            english_string += char

    return english_string

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    if is_braille_valid(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))
