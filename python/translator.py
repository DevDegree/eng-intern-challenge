import sys

english_to_braille_map = {
    # Numbers (preceded by a number indicator in Braille)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Punctuation and special characters
    '.': '..OO.O',          # Period
    ',': '..O...',          # Comma
    '?': '..O.OO',          # Question mark
    '!': '..OOO.',          # Exclamation mark
    ':': '..OO..',          # Colon
    ';': '..O.O.',          # Semicolon
    '-': '....OO',          # Hyphen
    '/': '.O..O.',          # Forward slash
    '<': '.OO..O',          # Less than
    '>': 'O..OO.',          # Greater than
    '(': 'O.O..O',          # Open parenthesis
    ')': '.O.OO.',          # Close parenthesis
    ' ': '......',           # Space

    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    
    # Special symbols
    'capital': '.....O',    # Capital follows indicator
    'decimal': '.O...O',    # Decimal follows indicator
    'number': '.O.OOO',     # Number follows indicator
}

braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}

braille_to_numbers_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def english_to_braille(text):
    braille_output = []
    number_flag = False

    for char in text:
        if char.isnumeric():
            if not number_flag:
                braille_output.append(english_to_braille_map['number'])
                number_flag = True

        elif char == '.':
            if number_flag:
                braille_output.append(english_to_braille_map['decimal'])

        elif char.isupper():
            braille_output.append(english_to_braille_map['capital'])
            char = char.lower()
            number_flag = False
        
        else:
            number_flag = False

        braille_output.append(english_to_braille_map.get(char, ''))

    return ''.join(braille_output)
            

def braille_to_english(text):
    braille_chars = [text[i:i+6] for i in range(0, len(text), 6)]
    english_output = []

    # possible contexts: letter, capital, number
    context = 'letter'

    for char in braille_chars:
        mapped_english_char = braille_to_english_map[char]
        if mapped_english_char == 'capital' or mapped_english_char == 'number':
            context = mapped_english_char
            continue

        if context == 'capital':
            english_output.append(mapped_english_char.upper())
            context = 'letter'

        elif context == 'number':
            english_output.append(braille_to_numbers_map[char])
        
        else:
            english_output.append(mapped_english_char)

    return ''.join(english_output)
    
def translate(text):
    if all(char in 'O.' for char in text) and len(text) % 6 == 0:
        return braille_to_english(text)
    else:
        return english_to_braille(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py [text to translate]")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    translation = translate(input_text)
    print(translation)

if __name__ == "__main__":
    main()