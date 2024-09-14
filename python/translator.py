import sys

# Dictionary for translating from Braille to English for Letters
braille_dict_LS = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '(': 'O.O..O',
    ')': '.O.OO.', '<': '.O..O.', ':': '..OO..', ';': '..O...', '/': '.O..O.', 
    '!': '..OOO.', '?': '..O.OO', '-': '....OO'
}

# Dictionary for translating from Braille to English for Numbers
braille_dict_N = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '>': 'O..OO.', '.': '..OO.O', ',': '..O...', '(': 'O.O..O', ')': '.O.OO.',
    '<': '.O..O.', ':': '..OO..', ';': '..O...', '/': '.O..O.', '!': '..OOO.',
    '?': '..O.OO', '-': '....OO', ' ': '......'
}

# Reverse Braille dictionaries
reverse_braille_dict_LS = {v: k for k, v in braille_dict_LS.items()}
reverse_braille_dict_N = {v: k for k, v in braille_dict_N.items()}

# Function for translating from text to braille
def text_to_braille(text):

    # Local Variables
    braille = ''
    isNumber = False

    # Iterates for each character
    for char in text:
        if char.isupper(): # Capital inclusion
            braille += '.....O' + braille_dict_LS[char]
        elif char.isdigit() and not isNumber: # Number inclusion
            isNumber = True
            braille += '.O.OOO' + braille_dict_N[char]
        elif char == ' ': # Space inclusion
            braille += '......'
            isNumber = False
        elif char == '.': # Decimal inclusion
            braille += '.O...O'
        elif isNumber:
            braille += braille_dict_N[char]
        else:
            braille += braille_dict_LS[char.upper()]
            isNumber = False

    return braille

# Function for translating from braille to text
def braille_to_text(braille):

    # Local Variables
    text = ''
    isNumber = False
    i = 0

    # Iterates over every braille character
    while i < len(braille):
        segment = braille[i:i+6]
        if segment == '......': # Space inclusion
            text += ' '
            isNumber = False
        elif segment == '.O.OOO': # Number inclusion
            isNumber = True
        elif segment == '.....O': # Capital inclusion
            i += 6
            segment = braille[i:i+6]
            text += reverse_braille_dict_LS.get(segment, '')
        elif isNumber:
            text += reverse_braille_dict_N.get(segment, '')
        else:
            text += reverse_braille_dict_LS.get(segment, '').lower()
        i += 6
    return text

# Main
if __name__ == "__main__":

    # Local Variables
    result = ''
    num_inputs = len(sys.argv) - 1

    # Iterates over every argument
    for index, input_str in enumerate(sys.argv[1:]):
        if all(c in 'O.' for c in input_str):
            result += braille_to_text(input_str)
        else:
            result += text_to_braille(input_str)
        
        if index < num_inputs - 1:
            result += '......'

    # Output
    print(result)