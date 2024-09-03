import sys

BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

BRAILLE_DIGITS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_PUNCTUATION = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '..O..O', '/': '.O..O.', '<': 'O...OO', '>': 'O..OOO',
    '(': 'O.OO..', ')': '.O.OO.'
}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'  
BRAILLE_SPACE = '......'

# Reverse mappings for decoding
ENGLISH_LETTERS = {v: k for k, v in BRAILLE_LETTERS.items()}
ENGLISH_DIGITS = {v: k for k, v in BRAILLE_DIGITS.items()}
ENGLISH_PUNCTUATION = {v: k for k, v in BRAILLE_PUNCTUATION.items()}


def is_braille(text):
    return all(c in {'O', '.', ' '} for c in text)


def english_to_braille(text):
    result = []
    in_number = False

    for char in text:
        if char.isupper():
            result.append(BRAILLE_CAPITAL)
            char = char.lower()
        if char.isdigit():
            if not in_number:
                result.append(BRAILLE_NUMBER)
                in_number = True
            result.append(BRAILLE_DIGITS[char])
        elif char.isalpha():
            in_number = False
            result.append(BRAILLE_LETTERS[char])
        elif char in BRAILLE_PUNCTUATION:
            in_number = False
            result.append(BRAILLE_PUNCTUATION[char])
        elif char == ' ':
            in_number = False
            result.append(BRAILLE_SPACE)

    return ''.join(result)


def braille_to_english(braille):
    result = []
    i = 0
    in_number = False
    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == BRAILLE_CAPITAL:
            next_symbol = braille[i+6:i+12]
            result.append(ENGLISH_LETTERS[next_symbol].upper())
            i += 12
        elif symbol == BRAILLE_NUMBER:
            in_number = True
            i += 6
        elif symbol == BRAILLE_SPACE:
            result.append(' ')
            in_number = False
            i += 6
        elif symbol in ENGLISH_PUNCTUATION:
            result.append(ENGLISH_PUNCTUATION[symbol])
            i += 6
        else:
            if in_number:
                result.append(ENGLISH_DIGITS[symbol])
            else:
                result.append(ENGLISH_LETTERS[symbol])
            i += 6

    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    main()
