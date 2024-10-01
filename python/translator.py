import sys
from typing import List, Dict

ENGLISH = True
BRAILLE = False

english_to_braille_map: Dict[str, str] = {
    ' ': '......',
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

braille_to_number_map: Dict[str, str] = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

braille_to_english_map: Dict[str, str] = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z'
}

def main() -> None:
    tokens: List[str] = get_tokenized_args()
    result: str = ''
    if english_or_braille(tokens) == ENGLISH:
        result = translate_english_to_braille(tokens)
    else:
        result = translate_braille_to_english(group_braille_tokens(tokens))
    print(result)

def get_tokenized_args() -> List[str]:
    return list(' '.join(sys.argv[1:]))

def english_or_braille(tokens: List[str]) -> bool:
    if all(token == '.' or token == 'O' for token in tokens):
        return BRAILLE
    return ENGLISH

def translate_english_to_braille(tokens: List[str]) -> str:
    result: str = ''
    is_number: bool = False
    for token in tokens:
        # if token is number
        if token.isnumeric():
            if not is_number:
                result += '.O.OOO'
                is_number = True
            result += english_to_braille_map[token]
            continue

        # for non-numeric tokens
        is_number = False
        if token.isupper():
            result += '.....O' + english_to_braille_map[token.lower()]
            continue
        result += english_to_braille_map[token]

    return result

def group_braille_tokens(tokens: List[str]) -> List[str]:
    grouped_tokens : List[str] = []
    for i in range(0, len(tokens), 6):
        grouped_tokens.append(''.join(tokens[i:i+6]))
    return grouped_tokens


def translate_braille_to_english(tokens: List[str]) -> str:
    result: str = ''
    is_number: bool = False
    is_upper: bool = False
    for token in tokens:
        if token == '.....O':
            is_upper = True
            continue
        if token == '.O.OOO':
            is_number = True
            continue
        if token == '......':
            is_number = False
            result += ' '
            continue
        if is_number:
            result += braille_to_number_map[token]
            continue
        if is_upper:
            is_upper = False
            result += braille_to_english_map[token].upper()
            continue
        result += braille_to_english_map[token]
    return result


if __name__=='__main__':
    main()
