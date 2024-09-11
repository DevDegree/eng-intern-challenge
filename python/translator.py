import sys

# Braille alphabet mapping
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Invert the braille_map to go from braille to English
english_map = {v: k for k, v in braille_map.items() if len(v) == 6}

# Special braille sequences
capital_prefix = '.....O'
number_prefix = '.O.OOO'

# Function to check if the input is braille or English
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

# Function to translate English to Braille
def english_to_braille(english_str):
    braille_translation = []
    is_num = False

    for char in english_str:
        if char.isupper():
            braille_translation.append(braille_map['cap'])  # Capitalization prefix
            braille_translation.append(braille_map[char])
        elif char.isdigit():
            if not is_num:
                braille_translation.append(braille_map['num'])  # Number prefix
                is_num = True
            braille_translation.append(braille_map[char])
        elif char == ' ':
            is_num = False  # Reset after space
            braille_translation.append(braille_map[' '])  # Space
        else:
            is_num = False  # Reset for regular characters
            braille_translation.append(braille_map.get(char, ''))
    
    return ''.join(braille_translation)

# Function to translate Braille to English
def braille_to_english(braille_str):
    english_translation = []
    i = 0
    is_cap = False
    is_num = False

    while i < len(braille_str):
        if braille_str[i:i+6] == capital_prefix:
            is_cap = True
            i += 6
        elif braille_str[i:i+6] == number_prefix:
            is_num = True
            i += 6
        else:
            symbol = braille_str[i:i+6]
            if is_cap:
                english_translation.append(english_map.get(symbol).upper())
                is_cap = False
            elif is_num:
                english_translation.append(english_map.get(symbol))
            else:
                english_translation.append(english_map.get(symbol))
            i += 6
        
        # Reset number mode after space
        if symbol == '......':
            is_num = False

    return ''.join(english_translation)

# Main function to handle input and output
def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate")
        return
    
    # Combine all arguments into a single string, separated by a space
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        # Input is Braille, translate to English
        print(braille_to_english(input_str), end='')  # Use `end=''` to avoid extra newlines
    else:
        # Input is English, translate to Braille
        print(english_to_braille(input_str), end='')

if __name__ == '__main__':
    main()