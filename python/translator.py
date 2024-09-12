import sys

# Constants for Braille Patterns
BRAILLE_PATTERNS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '..O..O', '/': '..O..O', '<': '..O.O.',
    '>': '..OO.O', '(': '..OO..', ')': '..OO..', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO', 'decimal': '.O...O'
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '...O.O', ' ': '......'
}

# Reverse mappings for decoding
BRAILLE_TO_CHAR = {v: k for k, v in BRAILLE_PATTERNS.items()}
BRAILLE_TO_NUM = {v: k for k, v in NUMBER_TO_BRAILLE.items()}


def text_to_braille(text):
    """Converts a string of text to Braille encoding."""
    result = []
    number_mode = False
    decimal_mode = False

    for char in text:
        if char.isalpha():
            if number_mode or decimal_mode:
                number_mode = decimal_mode = False
            if char.isupper():
                result.append(BRAILLE_PATTERNS['capital'])
            result.append(BRAILLE_PATTERNS[char.lower()])
        elif char.isdigit():
            if not number_mode and not decimal_mode:
                result.append(BRAILLE_PATTERNS['number'])
                number_mode = True
            result.append(NUMBER_TO_BRAILLE[char])
        elif char == '.':
            if number_mode:
                result.append(BRAILLE_PATTERNS['decimal'])
                decimal_mode = True
                number_mode = False
            else:
                result.append(BRAILLE_PATTERNS['.'])
        else:
            number_mode = decimal_mode = False
            result.append(BRAILLE_PATTERNS.get(char, '......'))

    return ''.join(result)


def braille_to_text(braille):
    """Converts a string of Braille encoding to readable text."""
    result = []
    chunks = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize_next = False
    number_mode = False
    decimal_mode = False

    for chunk in chunks:
        if chunk == BRAILLE_PATTERNS['capital']:
            capitalize_next = True
        elif chunk == BRAILLE_PATTERNS['number']:
            number_mode = True
        elif chunk == BRAILLE_PATTERNS['decimal']:
            decimal_mode = True
            result.append('.')
        else:
            if number_mode or decimal_mode:
                char = BRAILLE_TO_NUM.get(chunk, '')
                if char in '0123456789':
                    result.append(char)
                elif char == ' ':
                    number_mode = decimal_mode = False
                    result.append(' ')
            else:
                char = BRAILLE_TO_CHAR.get(chunk, '')
                if char:
                    if capitalize_next:
                        char = char.upper()
                        capitalize_next = False
                    result.append(char)

    return ''.join(result)


def is_braille(text):
    """Checks if the input text is in Braille format."""
    return all(char in 'O.' for char in text)


def translate(input_text):
    """Translates between text and Braille based on the input."""
    if not input_text:
        return ""
    
    return braille_to_text(input_text) if is_braille(input_text) else text_to_braille(input_text)


def main():
    """Main function to handle command-line inputs."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    result = translate(input_string)
    print(result)


if __name__ == "__main__":
    main()

