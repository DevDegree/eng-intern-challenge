import sys
from typing import Dict, List, Tuple

# Constants for special Braille symbols
CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'
SPACE_SYMBOL = '......'

# Braille to English mapping
BRAILLE_TO_ENG: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', SPACE_SYMBOL: ' '
}

# English to Braille mapping (reverse of BRAILLE_TO_ENG)
ENG_TO_BRAILLE: Dict[str, str] = {v: k for k, v in BRAILLE_TO_ENG.items()}

# Number to Braille letter mapping
NUMBER_MAP: Dict[str, str] = {str(i): ch for i, ch in enumerate('abcdefghij', 1)}
NUMBER_MAP['0'] = 'j'  # Special case for zero

def braille_to_english(braille: str) -> str:
    """
    Convert Braille to English.
    
    Args:
    braille (str): The Braille string to convert.
    
    Returns:
    str: The English translation.
    """
    result = []
    i = 0
    capitalize_next = number_mode = False

    while i < len(braille):
        symbol, i = braille[i:i+6], i + 6

        if symbol == CAPITAL_SYMBOL:
            capitalize_next = True
        elif symbol == NUMBER_SYMBOL:
            number_mode = True
        elif symbol == SPACE_SYMBOL:
            result.append(' ')
            number_mode = False
        elif symbol in BRAILLE_TO_ENG:
            char = BRAILLE_TO_ENG[symbol]
            if number_mode and char in 'abcdefghij':
                # Convert Braille letter to corresponding number
                char = next(k for k, v in NUMBER_MAP.items() if v == char)
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False

            result.append(char)
            if char.isalpha():
                number_mode = False

    return ''.join(result)

def english_to_braille(text: str) -> str:
    """
    Convert English to Braille.
    
    Args:
    text (str): The English string to convert.
    
    Returns:
    str: The Braille translation.
    """
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_SYMBOL)
                number_mode = True
            result.append(ENG_TO_BRAILLE[NUMBER_MAP[char]])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(CAPITAL_SYMBOL)
                char = char.lower()
            result.append(ENG_TO_BRAILLE.get(char, ''))

    return ''.join(result)

def is_braille(text: str) -> bool:
    """
    Check if the given text is in Braille format.
    
    Args:
    text (str): The text to check.
    
    Returns:
    bool: True if the text is in Braille format, False otherwise.
    """
    return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

def main(args: List[str]) -> None:
    if len(args) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(args[1:])
    # Choose the appropriate translation function based on input
    translator = braille_to_english if is_braille(input_text) else english_to_braille
    print(translator(input_text))

if __name__ == "__main__":
    main(sys.argv)