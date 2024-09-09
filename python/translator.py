import sys
from typing import Dict, List

# Braille mapping constants
BRAILLE_TO_ENGLISH: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital_follows', '.O.OOO': 'number_follows'
}

ENGLISH_TO_BRAILLE: Dict[str, str] = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

NUMBER_MAPPING: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def braille_to_english(braille: str) -> str:
    """
    Convert Braille to english.

    Args:
        braille (str): The Braille string to convert.

    Returns:
        str: The converted english.
    """
    english = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        if char == '.....O':
            capitalize_next = True
        elif char == '.O.OOO':
            number_mode = True
        elif char in BRAILLE_TO_ENGLISH:
            letter = BRAILLE_TO_ENGLISH[char]
            if number_mode and char in NUMBER_MAPPING.values():
                english.append(next(k for k, v in NUMBER_MAPPING.items() if v == char))
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                english.append(letter)
                if letter == ' ':
                    number_mode = False
        i += 6
    return ''.join(english)

def english_to_braille(english: str) -> str:
    """
    Convert english to Braille.

    Args:
        english (str): The english to convert.

    Returns:
        str: The converted Braille string.
    """
    braille = []
    number_mode = False
    
    for char in english:
        if char.isdigit():
            if not number_mode:
                braille.append(ENGLISH_TO_BRAILLE['number_follows'])
                number_mode = True
            braille.append(NUMBER_MAPPING[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                braille.append(ENGLISH_TO_BRAILLE['capital_follows'])
            braille.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char == ' ':
            braille.append(ENGLISH_TO_BRAILLE[char])
            number_mode = False
    return ''.join(braille)

def is_braille(input_string: str) -> bool:
    """
    Check if the input string is valid Braille.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is valid Braille, False otherwise.
    """
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0

def translate(input_string: str) -> str:
    """
    Translate between Braille and english.

    Args:
        input_string (str): The string to translate.

    Returns:
        str: The translated string.
    """
    return braille_to_english(input_string) if is_braille(input_string) else english_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)
    
    input_string = " ".join(sys.argv[1:])
    result = translate(input_string)
    print(result, end='')