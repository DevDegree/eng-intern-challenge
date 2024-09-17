import sys

BRAILLE_TO_ENG = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital follows', '.O.OOO': 'number follows'
}

ENG_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENG.items()}

NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def chunk_braille(braille):
    return [braille[i:i+6] for i in range(0, len(braille), 6)]

def braille_to_english(braille):
    chunks = chunk_braille(braille)
    result = []
    capitalize_next = False
    number_mode = False

    for chunk in chunks:
        if chunk == ENG_TO_BRAILLE['capital follows']:
            capitalize_next = True
        elif chunk == ENG_TO_BRAILLE['number follows']:
            number_mode = True
        else:
            if chunk in BRAILLE_TO_ENG:
                char = BRAILLE_TO_ENG[chunk]
                if number_mode and char in NUMBER_MAP:
                    result.append(NUMBER_MAP[char])
                else:
                    if capitalize_next:
                        char = char.upper()
                        capitalize_next = False
                    result.append(char)
                    if char == ' ':
                        number_mode = False
            else:
                result.append('?')

    return ''.join(result)

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENG_TO_BRAILLE['number follows'])
                number_mode = True
            result.append(ENG_TO_BRAILLE[next(k for k, v in NUMBER_MAP.items() if v == char)])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENG_TO_BRAILLE['capital follows'])
                char = char.lower()
            if char in ENG_TO_BRAILLE:
                result.append(ENG_TO_BRAILLE[char])
            else:
                result.append('......')  

    return ''.join(result)

def is_braille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
