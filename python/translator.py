import sys
from typing import Dict

BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS = '.O.OOO'

# dictionary mapping alphanumeric chars to their equivalent braille
ALPHANUM_TO_BRAILLE: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..', 
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
    ' ': '......',
}

# dictionary mapping braille to its respective letter
BRAILLE_TO_LETTER: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 
    'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', 
    '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', 
    '......': ' '
}

# dictionary mapping braille to its respective number
BRAILLE_TO_NUMBER: Dict[str, str] = {
    '.OOO..': '0', 
    'O.....': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO.O..': '4', 
    'O..O..': '5', 
    'OOO...': '6', 
    'OOOO..': '7', 
    'O.OO..': '8', 
    '.OO...': '9', 
}


def is_braille(input_str: str) -> bool:
    """
    Check if the input string is braille or not.
    
    Args:
        input_str (str): The string to check.
    
    Returns:
        bool: True if the string is in braille, False otherwise.
    """
    return len(input_str) % 6 == 0 and all(char in "O." for char in input_str)


def english_to_braille(input_str: str) -> str:
    """
    Translates english to braille.

    Args:
        input_str (str): The english string to translate.
    
    Returns:
        str: A translated braille string.
    """
    res = ''
    for i, char in enumerate(input_str):
        braille = ALPHANUM_TO_BRAILLE[char.lower()]
        if char.isdigit():
            if i == 0 or input_str[i-1] == ' ':
                res += BRAILLE_NUMBER_FOLLOWS
            res += braille
        elif char.isupper():
            res += BRAILLE_CAPITAL_FOLLOWS + braille
        else:
            res += braille
    return res


def braille_to_english(input_str: str) -> str:
    """
    Translates braille to english.
    
    Args:
        input_str (str): The braille string to translate.
    
    Returns:
        str: The translated english string.
    """
    res = ''
    is_number = False
    is_capital = False

    for i in range(0, len(input_str), 6):
        braille = input_str[i:i+6]
        
        if braille == BRAILLE_NUMBER_FOLLOWS:
            is_number = True
        elif braille == BRAILLE_CAPITAL_FOLLOWS:
            is_capital = True
        else:
            char = BRAILLE_TO_LETTER[braille]
            if is_number:
                if char == ' ':
                    res += char
                    is_number = False
                else:
                    res += BRAILLE_TO_NUMBER[braille]
            elif is_capital:
                res += char.upper()
                is_capital = False
            else:
                res += char
    
    return res


def main() -> None:
    """
    Main function that handles input and translation.

    Args:
        None
    
    Returns:
        None
    """
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        res = braille_to_english(input_text)
    else:
        res = english_to_braille(input_text)

    print(res)

if __name__ == "__main__":
    main() 