import sys
from typing import Dict

# Braille mappings
BRAILLE_ALPHABET: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', ' ': '......'
}

BRAILLE_NUMBERS: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Precomputed reverse mappings for faster lookups
REVERSE_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
REVERSE_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

def is_braille(text: str) -> bool:
    """
    Check if the input text is Braille.
    
    Args:
        text (str): Input text to check

    Returns:
        bool: True if the text is Braille, False otherwise

    Note: Checks only the first 12 characters for efficiency.
    """
    sample = text[:12]
    return set(sample).issubset({'O', '.'}) and len(text) % 6 == 0

def english_to_braille(text: str) -> str:
    """
    Convert English text to Braille.

    Args:
        text (str): English text to convert

    Returns:
        str: Braille representation of the input text
    """
    braille = bytearray()
    is_number_mode = False

    for char in text:
        if char.isdigit():
            if not is_number_mode:
                braille.extend(BRAILLE_ALPHABET['num'].encode())
                is_number_mode = True
            braille.extend(BRAILLE_NUMBERS[char].encode())
        elif char.isalpha():
            is_number_mode = False
            if char.isupper():
                braille.extend(BRAILLE_ALPHABET['cap'].encode())
            braille.extend(BRAILLE_ALPHABET[char.lower()].encode())
        elif char.isspace():
            is_number_mode = False
            braille.extend(BRAILLE_ALPHABET[' '].encode())
        else:
            is_number_mode = False

    return braille.decode()

def braille_to_english(braille: str) -> str:
    """
    Convert Braille to English text.

    Args:
        braille (str): Braille text to convert

    Returns:
        str: English representation of the input Braille
    """
    symbols = [braille[i:i+6] for i in range(0, len(braille), 6)]
    english = []
    is_capital = False
    is_number_mode = False

    for symbol in symbols:
        if symbol == BRAILLE_ALPHABET['cap']:
            is_capital = True
        elif symbol == BRAILLE_ALPHABET['num']:
            is_number_mode = True
        elif symbol == BRAILLE_ALPHABET[' ']:
            is_number_mode = False
            english.append(' ')
        elif is_number_mode:
            english.append(REVERSE_NUMBERS[symbol])
        else:
            char = REVERSE_ALPHABET[symbol]
            if char in ('cap', 'num'):
                continue
            if is_capital:
                char = char.upper()
                is_capital = False
            english.append(char)

    return ''.join(english)

def braille_translator(text: str) -> str:
    """
    Translate between English and Braille.

    Args:
        text (str): Input text to translate

    Returns:
        str: Translated text (Braille if input is English, English if input is Braille)
    """
    return braille_to_english(text) if is_braille(text) else english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text to translate>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(braille_translator(input_text))