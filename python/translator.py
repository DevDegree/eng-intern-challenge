import sys

# Separate dictionaries for letters and numbers
BRAILLE_ALPHABET_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'CAPITAL': '.....O', 'DECIMAL': '.O...O', 'NUMBER': '.O.OOO', ' ': '......'
}

BRAILLE_NUMBER_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionaries for Braille to English translation
ENGLISH_ALPHABET_DICT = {v: k for k, v in BRAILLE_ALPHABET_DICT.items()}
ENGLISH_NUMBER_DICT = {v: k for k, v in BRAILLE_NUMBER_DICT.items()}

def detect_input_type(input_str):
    return 'braille' if set(input_str) <= {'O', '.'} else 'english'

def translate_to_braille(input_str):
    result = []
    number_mode = False  # Tracks whether we are in number mode
    
    for char in input_str:
        if char.isdigit() and not number_mode:
            result.append(BRAILLE_ALPHABET_DICT['NUMBER'])
            number_mode = True
        
        if char.isdigit():
            result.append(BRAILLE_NUMBER_DICT[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False  # Exiting number mode when a letter is encountered
            if char.isupper():
                result.append(BRAILLE_ALPHABET_DICT['CAPITAL'])
                char = char.lower()
            result.append(BRAILLE_ALPHABET_DICT[char])
        else:
            result.append(BRAILLE_ALPHABET_DICT[char])
            number_mode = False  # Reset number mode on spaces or special characters
    
    return ''.join(result)


def translate_to_english(input_str):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(input_str):
        symbol = input_str[i:i+6]
        
        if symbol == BRAILLE_ALPHABET_DICT['CAPITAL']:
            capitalize_next = True
            i += 6
            continue
        elif symbol == BRAILLE_ALPHABET_DICT['NUMBER']:
            number_mode = True
            i += 6
            continue
        
        if number_mode:
            char = ENGLISH_NUMBER_DICT.get(symbol, '?')  # Use a placeholder if not found
        else:
            char = ENGLISH_ALPHABET_DICT.get(symbol, '?')
        
        if capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        
        # Reset number mode after space
        if symbol == BRAILLE_ALPHABET_DICT[' ']:
            number_mode = False
            
        i += 6
    
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        return

    # Combine all command-line arguments into a single string
    input_str = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_str)

    if input_type == 'english':
        print(translate_to_braille(input_str))
    else:
        print(translate_to_english(input_str))

if __name__ == "__main__":
    main()
