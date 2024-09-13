import sys

# Dictionaries for translation
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' ',
    '..O...': ',', '..O.O.': ';', '..OO..': ':', '..OOO.': '!', '..O.OO': '?',
    '..OO.O': '.', '....OO': '-', '.O..O.': '/', 'O.O..O': '(', '.O.OO.': ')',
    '.OO..O': '<', '.O.OO.': '>'}

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
    ',': '..O...', ';': '..O.O.', ':': '..OO..', '!': '..OOO.', '?': '..O.OO',
    '.': '..OO.O', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
    '<': '.OO..O', '>': '.O.OO.'}

# Numbers are like a-j but with the number symbol in front
NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def detect_input_type(input_str):
    # Detect whether the input is Braille or English
    if 'O' in input_str or '.' in input_str:
        return 'braille'
    else:
        return 'english'
    

def braille_to_english(braille_str):
    english_output = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille_str):
        symbol = braille_str[i:i+6]
        
        if symbol == '.....O':  # Capital symbol
            capitalize_next = True
            i += 6
            continue
        elif symbol == '.O.OOO':  # Number symbol
            number_mode = True
            i += 6
            continue

        char = BRAILLE_TO_ENGLISH.get(symbol, '?')  # Handle unknown symbols
        
        if number_mode:
            if char == ' ':  # Exit number mode after space
                number_mode = False
            else:
                # Convert the letter to a number
                for key, value in NUMBERS.items():
                    if value == symbol:
                        char = key
                        break

        if capitalize_next and char != ' ':
            char = char.upper()
            capitalize_next = False

        english_output.append(char)
        i += 6

    return ''.join(english_output)

def english_to_braille(english_str):
    braille_output = []
    number_mode = False
    for char in english_str:
        if char.isupper():
            braille_output.append(ENGLISH_TO_BRAILLE['capital'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille_output.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            braille_output.append(NUMBERS[char])
        else:
            if number_mode:
                number_mode = False
            braille_output.append(ENGLISH_TO_BRAILLE.get(char, '......'))
    return ''.join(braille_output)

if __name__ == "__main__":
    # Join all command-line arguments with a single space
    input_str = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else ''
    
    # Detect input type and perform the appropriate translation
    input_type = detect_input_type(input_str)
    
    if input_type == 'braille':
        print(braille_to_english(input_str), end='')
    else:
        print(english_to_braille(input_str), end='')