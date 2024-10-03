import sys
from typing import Dict, Set

BRAILLE_MAP: Dict[str, Dict[str, str]] = {
    'letters': {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
    },
    'numbers': {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }
}

SPECIAL_SYMBOLS: Dict[str, str] = {
    'SPACE': '......',
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO'
}

def create_reverse_maps() -> Dict[str, Dict[str, str]]:
    return {
        'letters': {v: k for k, v in BRAILLE_MAP['letters'].items()},
        'numbers': {v: k for k, v in BRAILLE_MAP['numbers'].items()}
    }

REVERSE_BRAILLE_MAP: Dict[str, Dict[str, str]] = create_reverse_maps()

def is_braille(text: str) -> bool:
    if len(text) % 6 != 0:
        return False
    valid_chars: Set[str] = set('O.')
    return all(char in valid_chars for char in text)

def braille_to_text(braille: str) -> str:
    result = []
    is_capital = is_number = False
    
    for i in range(0, len(braille), 6):
        chunk = braille[i:i+6]
        if chunk == SPECIAL_SYMBOLS['SPACE']:
            result.append(' ')
            is_number = False
        elif chunk == SPECIAL_SYMBOLS['NUMBER']:
            is_number = True
        elif chunk == SPECIAL_SYMBOLS['CAPITAL']:
            is_capital = True
        elif is_number:
            result.append(REVERSE_BRAILLE_MAP['numbers'].get(chunk, chunk))
        elif is_capital:
            result.append(REVERSE_BRAILLE_MAP['letters'].get(chunk, chunk).upper())
            is_capital = False
        else:
            result.append(REVERSE_BRAILLE_MAP['letters'].get(chunk, chunk))
    
    return ''.join(result)

def text_to_braille(text: str) -> str:
    result = []
    is_number = False
    
    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(SPECIAL_SYMBOLS['NUMBER'])
                is_number = True
            result.append(BRAILLE_MAP['numbers'][char])
        elif char.isspace():
            result.append(SPECIAL_SYMBOLS['SPACE'])
            is_number = False
        elif char.isupper():
            result.append(SPECIAL_SYMBOLS['CAPITAL'])
            result.append(BRAILLE_MAP['letters'][char.lower()])
        else:
            result.append(BRAILLE_MAP['letters'].get(char, char))
    
    return ''.join(result)

def main(args: list) -> None:
    if len(args) < 2:
        print("Usage: python braille_translator.py <string>")
        return
    
    input_text = ' '.join(args[1:])
    if is_braille(input_text):
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))

if __name__ == '__main__':
    main(sys.argv)