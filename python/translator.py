import sys

# Dictionary to map English letters to Braille
ENG_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
    ' ': '......'
}

# Dictionary to map numbers to Braille
NUM_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mapping of Braille to English letters and numbers
BRAILLE_TO_ENG = {v: k for k, v in ENG_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {v: k for k, v in NUM_TO_BRAILLE.items()}

# Function to check if a string is Braille based on its structure
def detect_braille(input_text):
    if len(input_text) % 6 != 0:
        return False
    return all(char in 'O.' for char in input_text)

# Convert Braille text to English
def translate_braille_to_english(braille_text):
    result = ""
    num_mode = False
    cap_mode = False
    segment_size = 6

    for index in range(0, len(braille_text), segment_size):
        segment = braille_text[index: index + segment_size]
        char = BRAILLE_TO_ENG.get(segment, ' ')
        
        if char == 'capital':
            cap_mode = True
            continue
        elif char == 'number':
            num_mode = True
            continue
        elif char == ' ':
            num_mode = False
            result += ' '
            continue

        if num_mode:
            char = BRAILLE_TO_NUM.get(segment, '')
            result += char
        elif cap_mode:
            result += char.upper()
            cap_mode = False
        else:
            result += char

    return result

# Convert English text to Braille
def translate_english_to_braille(english_text):
    braille_result = ""
    number_mode = False

    for character in english_text:
        if character.isdigit():
            if not number_mode:
                braille_result += ENG_TO_BRAILLE['number']
                number_mode = True
            braille_result += NUM_TO_BRAILLE[character]
        else:
            if character.isupper():
                braille_result += ENG_TO_BRAILLE['capital']
                character = character.lower()
            braille_result += ENG_TO_BRAILLE.get(character, '......')
            number_mode = False

    return braille_result

# Main script execution
if len(sys.argv) < 2:
    print('Insufficient argument to translate')
    sys.exit(1)

# Join command line arguments as input text
input_text = ' '.join(sys.argv[1:])
# Check if input is Braille and translate accordingly
if detect_braille(input_text):
    print(translate_braille_to_english(input_text))
else:
    print(translate_english_to_braille(input_text))
