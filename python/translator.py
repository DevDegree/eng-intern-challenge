import sys

# Braille to English dictionary
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# Reverse dictionary for Braille to English
ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items()}

# Function to translate English to Braille
def english_to_braille(text):
    result = []
    num_mode = False
    for char in text:
        if char.isupper():
            result.append(BRAILLE_DICT['cap'])
            result.append(BRAILLE_DICT[char.lower()])
        elif char.isdigit():
            if not num_mode:
                result.append(BRAILLE_DICT['num'])
                num_mode = True
            result.append(BRAILLE_DICT[char])
        else:
            num_mode = False
            result.append(BRAILLE_DICT[char])
    return ''.join(result)

# Function to translate Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    num_mode = False
    while i < len(braille):
        current_char = braille[i:i+6]
        if current_char == BRAILLE_DICT['cap']:
            capitalize_next = True
            i += 6
        elif current_char == BRAILLE_DICT['num']:
            num_mode = True
            i += 6
        else:
            if num_mode and current_char in BRAILLE_DICT.values():
                result.append(ENGLISH_DICT[current_char])
                num_mode = False if ENGLISH_DICT[current_char] == ' ' else num_mode
            elif capitalize_next:
                result.append(ENGLISH_DICT[current_char].upper())
                capitalize_next = False
            else:
                result.append(ENGLISH_DICT[current_char])
            i += 6
    return ''.join(result)

# Function to detect input type and translate
def detect_and_translate(input_strings):
    combined_input = ' '.join(input_strings)
    if set(combined_input).issubset({'O', '.'}):
        # Translate Braille to English
        return braille_to_english(combined_input)
    else:
        # Translate English to Braille
        return english_to_braille(combined_input)

if __name__ == '__main__':
    input_strings = sys.argv[1:]  # Collect all arguments passed at runtime
    translated_output = detect_and_translate(input_strings)
    print(translated_output)