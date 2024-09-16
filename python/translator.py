import sys

# Braille mappings for letters, digits, and special symbols
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..O.OO', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Control characters
CONTROL_CHARACTERS = {
    'number_follows': '.O.OOO',
    'capital_follows': '.....O',
}

def translate_to_braille(text):
    """Translate English text to Braille."""
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(CONTROL_CHARACTERS['capital_follows'])
            char = char.lower()
        elif char.isdigit():
            if not number_mode:
                result.append(CONTROL_CHARACTERS['number_follows'])
                number_mode = True
        else:
            number_mode = False
        
        result.append(ENGLISH_TO_BRAILLE.get(char, '......'))
    return ''.join(result)

def translate_to_english(braille):
    """Translate Braille text to English."""
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    number_mode = False
    capital_mode = False

    for char in braille_chars:
        if char == CONTROL_CHARACTERS['number_follows']:
            number_mode = True
        elif char == CONTROL_CHARACTERS['capital_follows']:
            capital_mode = True
        elif char == '......':
            number_mode = False
            result.append(' ')
        else:
            if number_mode:
                result.append(BRAILLE_TO_ENGLISH.get(char, '?'))
                number_mode = False
            else:
                english_char = BRAILLE_TO_ENGLISH.get(char, '?')
                if capital_mode:
                    english_char = english_char.upper()
                    capital_mode = False
                result.append(english_char)
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide input text.")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    
    # Determine if the input is Braille or English based on its characters
    if all(c in 'O.' for c in input_string.replace(' ', '')):
        # Input is Braille, translate to English
        output = translate_to_english(input_string)
    else:
        # Input is English, translate to Braille
        output = translate_to_braille(input_string)
    
    print(output)

if __name__ == '__main__':
    main()

