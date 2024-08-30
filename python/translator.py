import sys

BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

ENGLISH_ALPHABET = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}


NUMBER_ALPHABET = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


def is_braille(input_str):
    # Check if the input is in Braille
    return all(c in 'O.' for c in input_str)

def english_to_braille(english):
    result = []
    isDigit = False
    for char in english:
        if char.isdigit():
            if not isDigit:
                isDigit = True
                result.append(BRAILLE_NUMBER)
            result.append(BRAILLE_ALPHABET[char])
        elif char == ' ':
            result.append(BRAILLE_ALPHABET[char])
            isDigit = False
        elif char.isupper():
            result.append(BRAILLE_CAPITAL)
            result.append(BRAILLE_ALPHABET[char.lower()])
        else:
            # Lowercase char
            result.append(BRAILLE_ALPHABET[char])
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    is_number_mode = False

    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == BRAILLE_CAPITAL:
            i += 6
            symbol = braille[i:i + 6]
            result.append(ENGLISH_ALPHABET[symbol].upper())
        elif symbol == BRAILLE_NUMBER:
            is_number_mode = True
        elif symbol == BRAILLE_ALPHABET[' ']:
            result.append(' ')
            is_number_mode = False
        else:
            if is_number_mode:
                result.append(NUMBER_ALPHABET[symbol])
            else:
                result.append(ENGLISH_ALPHABET[symbol])
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)

    # Concatenate all arguments with a space
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
