import sys

# Define Braille mappings
english_characters = {
    'a': 'O.....', 'b': 'O.O...',
    'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO',
    'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

english_numbers = {
    '0': '.OOO..', '1': 'O.....',
    '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...',
}

# Reverse mapping for Braille to English
braille_to_english_characters = {v: k for k, v in english_characters.items()}
braille_to_english_numbers = {v: k for k, v in english_numbers.items()}

CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '.O.OOO'
SPACE_INDICATOR = '......'

# Check if all characters are 'O' or '.' and length is multiple of 6
def is_braille(text):
    return all(c in ['O', '.'] for c in text) and len(text) % 6 == 0

def english_to_braille(text):
    braille = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(NUMBER_INDICATOR)
                number_mode = True
            braille.append(english_numbers[char])
        elif char == " ":
            braille.append(SPACE_INDICATOR)
            if number_mode:
                number_mode = False
        else:
            if char.isupper():
                braille.append(CAPITAL_INDICATOR)
                char = char.lower()
            braille.append(english_characters.get(char))
    return ''.join(braille)

def braille_to_english(braille):
    text = []
    i = 0
    number_mode = False
    capitalize_next = False
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        if braille_char == CAPITAL_INDICATOR:
            capitalize_next = True
        elif braille_char == NUMBER_INDICATOR:
            number_mode = True
        elif braille_char == SPACE_INDICATOR:
            text.append(' ')
            number_mode = False
        else:
            if number_mode:    
                char = braille_to_english_numbers.get(braille_char)
            else:
                char = braille_to_english_characters.get(braille_char)
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
            text.append(char)
    return ''.join(text)

def main():
    if len(sys.argv) < 2:
        sys.exit()
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    print(output)

if __name__ == "__main__":
    main()