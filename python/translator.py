import sys

# Braille encoding
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap_marker': '.....O',
}

braille_numbers_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'num_marker': '.O.OOO',
}

# Reverse mappings for decoding Braille into characters
reverse_braille_dict = {v: k for k, v in braille_dict.items()}
reverse_number_dict = {v: k for k, v in braille_numbers_dict.items()}

# Detect input type (Braille or English)
def identify_input_type(input_text):
    return 'braille' if all(ch in 'O.' for ch in input_text) else 'english'

# Function to convert English text to Braille
def english_to_braille(text):
    result = []
    in_num_mode = False
    for ch in text:
        if ch.isupper():
            result.append(braille_dict['cap_marker'])
            ch = ch.lower()

        if ch.isdigit():
            if not in_num_mode:
                result.append(braille_numbers_dict['num_marker'])
                in_num_mode = True
            result.append(braille_numbers_dict.get(ch, ''))
        else:
            in_num_mode = False
            result.append(braille_dict.get(ch, ''))
    
    return ''.join(result)

# Function to convert Braille to English
def braille_to_english(braille_text):
    result = []
    idx = 0
    in_cap_mode = False
    in_num_mode = False

    while idx < len(braille_text):
        current_braille = braille_text[idx:idx + 6]
        if current_braille == braille_dict['cap_marker']:
            in_cap_mode = True
        elif current_braille == braille_numbers_dict['num_marker']:
            in_num_mode = True
        else:
            if in_num_mode:
                char = reverse_number_dict.get(current_braille, '')
                if char:
                    result.append(char)
                else:
                    in_num_mode = False
            else:
                char = reverse_braille_dict.get(current_braille, '')
                if char:
                    if in_cap_mode:
                        char = char.upper()
                        in_cap_mode = False
                    result.append(char)
        idx += 6

    return ''.join(result)

# Main function
def translator():
    if len(sys.argv) < 2:
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])
    if identify_input_type(input_text) == 'english':
        print(english_to_braille(input_text), end='')
    else:
        print(braille_to_english(input_text), end='')

if __name__ == "__main__":
    translator()
