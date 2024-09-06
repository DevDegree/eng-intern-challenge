import sys

# Define Braille patterns for letters, numbers, and symbols
braille_char_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'cap': '.....O', # Capital prefix in Braille
    'num': '.O.OOO', # Number prefix in Braille 
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......' # space
}

braille_num_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

# Reverse mapping for translating Braille back to English
reverse_braille_char_map = {v: k for k, v in braille_char_map.items()}
reverse_braille_num_map = {v: k for k, v in braille_num_map.items()}

# Detect if input is Braille or English
def is_braille(input_string: str):
    return all(c in 'O.' for c in input_string)

# Convert English to Braille
def english_to_braille(text: str):
    result = []
    num_mode = False
    for char in text:
        if char.isupper():
            result.append(braille_char_map['cap'])  # Add capital prefix
            result.append(braille_char_map[char.lower()])
        elif char.isdigit():
            if not num_mode: 
                result.append(braille_char_map['num'])  # Add number prefix
                num_mode = True
            result.append(braille_num_map[char])
        else:
            num_mode = False
            result.append(braille_char_map.get(char, '......'))  # Handle unknown characters
    return ''.join(result)

# Convert Braille to English
def braille_to_english(braille: str):
    result = []
    cap = False
    num = False
    for i in range(0, len(braille), 6):
        chunk = braille[i : i + 6]
        if chunk == braille_char_map['num']: num = True
        elif chunk == braille_char_map['cap']: cap = True
        else:
            if chunk == braille_char_map[' ']:
                num = False
            elif cap:
                result.append(reverse_braille_char_map[chunk].upper())
                cap = False
            else:
                if num: result.append(reverse_braille_num_map[chunk])
                else: result.append(reverse_braille_char_map[chunk])
    return ''.join(result)

# Main function to detect input and perform translation
def main():
    input_string = ' '.join(sys.argv[1 :])

    if is_braille(input_string):
        # Input is Braille, translate to English
        translated_text = braille_to_english(input_string)
    else:
        # Input is English, translate to Braille
        translated_text = english_to_braille(input_string)

    print(translated_text)

if __name__ == "__main__":
    main()
