# Braille encoding for English letters and numbers
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_number_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Define the mapping from Braille symbols to English letters
braille_to_letter_map = {v: k for k, v in braille_alphabet.items() if k.isalpha() or k.isdigit()}

# Special Braille Symbols
CAPITAL_FOLLOWS = '.....O'  # Braille cell indicating capital letter follows (dots 1-5)
NUMBER_FOLLOWS = '.O.OOO'   # Braille cell indicating number follows (dots 2-4-5-6)
SPACE = '......'            # Braille cell for space (all dots off)

def is_braille(input_str: str) -> bool:
    return all(char in 'O.' for char in input_str)

def braille_to_letter(symbol: str) -> str:
    # Look up the symbol in the dictionary
    return braille_to_letter_map.get(symbol, '?')  # '?' as a fallback for unknown symbols


def braille_to_number(symbol: str) -> str:
    """
    Translate a Braille number symbol to a digit.
    """
    return braille_number_map.get(symbol, '?')