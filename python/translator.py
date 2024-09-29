
import sys

# Braille dictionaries
BRAILLE_ALPHABET = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_NUMBERS = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

BRAILLE_SPECIAL = {
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
}

def detect_input_type(input_string):
    return "braille" if set(input_string).issubset({'O', '.', ' '}) else "english"

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isalpha():
            if number_mode:
                result.append(BRAILLE_SPECIAL['number'])
                number_mode = False
            if char.isupper():
                result.append(BRAILLE_SPECIAL['capital'])
            result.append(BRAILLE_ALPHABET[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(BRAILLE_SPECIAL['number'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            result.append(BRAILLE_SPECIAL[' '])
            number_mode = False
    
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    capital_next = False
    number_mode = False

    reverse_alphabet = {v: k for k, v in BRAILLE_ALPHABET.items()}
    reverse_numbers = {v: k for k, v in BRAILLE_NUMBERS.items()}

    while i < len(braille):
        chunk = braille[i:i+6]
        
        if chunk == BRAILLE_SPECIAL['capital']:
            capital_next = True
        elif chunk == BRAILLE_SPECIAL['number']:
            number_mode = True
        elif chunk == BRAILLE_SPECIAL[' ']:
            result.append(' ')
            number_mode = False
        elif number_mode:
            result.append(reverse_numbers[chunk])
        else:
            char = reverse_alphabet[chunk]
            if capital_next:
                char = char.upper()
                capital_next = False
            result.append(char)
        
        i += 6

    return ''.join(result)

def main():
    input_string = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "english":
        result = english_to_braille(input_string)
    else:
        result = braille_to_english(input_string)

    print(result, end='')  # Remove newline at the end

if __name__ == "__main__":
    main()