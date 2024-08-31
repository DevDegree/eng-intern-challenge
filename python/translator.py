import sys

braille_to_eng_map = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 'f': '000...',
    'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..', 'k': '0...0.', 'l': '0.0.0.',
    'm': '00..0.', 'n': '00.00.', 'o': '0..00.', 'p': '000.0.', 'q': '00000.', 'r': '0.000.',
    's': '.00.0.', 't': '.0000.', 'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00',
    'y': '00.000', 'z': '0..000', '1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..',
    '5': '0..0..', '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...', '0': '.000..',
    'capital follows': '.....0', 'decimal follows': '.0...0', 'number follows': '.0.000',
    '.': '..00.0', ',': '..0...', '?': '..0.00', '!': '..000.', ':': '..00..', ';': '..0.0.',
    '-': '....00', '/': '.0..0.', '<': '.0.0.0', '>': '0.0.0.', '(': '0.0..0', ')': '.0.00.',
    ' ': '......'
}

# Create a reverse mapping
eng_to_braille_map = {v: k for k, v in braille_to_eng_map.items()}

def braille_to_eng(text: str) -> str:
    pass

def eng_to_braille(text: str) -> str:
    pass

def is_braille(text: str) -> bool:
    """
    Returns True if text is in Braille, False otherwise.

    Args:
        text (str): A string of text to check.

    Returns:
        bool: True if text is in Braille, False otherwise.
    """
    return all(c in '0.' for c in text)

if __name__ == '__main__':
    # Read command line arguments
    text = ' '.join(sys.argv[1:])

    # Convert the input to the appropriate format
    if is_braille(text):
        print(braille_to_eng(text))
    else:
        print(eng_to_braille(text))