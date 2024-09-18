import sys

ENGLISH_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
ENGLISH_NUMBERS = set('0123456789')
ENGLISH_CHARACTERS = ENGLISH_LETTERS.union(ENGLISH_NUMBERS)

BRAILLE_CHARACTERS = set('O.')

CAPITAL_FOLLOWS = 'CAPITAL_FOLLOWS'
DECIMAL_FOLLOWS = 'DECIMAL_FOLLOWS'
NUMBER_FOLLLOWS = 'NUMBER_FOLLLOWS'
SPACE = 'SPACE'

BRAILLE_ALPHABET_SYMBOLS = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    CAPITAL_FOLLOWS: '.....O',
    DECIMAL_FOLLOWS: '.O...O',
    NUMBER_FOLLLOWS: '.O.OOO',
    SPACE: '......',
}

BRAILLE_NUMBERS_SYMBOLS = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

BRAILLE_SYMBOL_LEN = 6

BRAILLE_ALPHABET = {value: key for key,
                    value in BRAILLE_ALPHABET_SYMBOLS.items()}
BRAILLE_NUMBERS = {value: key for key,
                   value in BRAILLE_NUMBERS_SYMBOLS.items()}


def is_english(text):
    for word in text:
        if not set(word.lower()).issubset(ENGLISH_CHARACTERS):
            return False
    return True


def is_braille(text):
    if not set(text).issubset(BRAILLE_CHARACTERS):
        return False
    return True


def is_letter_upper_case(char):
    return char not in ENGLISH_LETTERS and char.lower() in ENGLISH_LETTERS


def translate_to_braille(english_text):
    does_number_follows = False

    output = ''
    for char in ' '.join(english_text):
        if is_letter_upper_case(char):
            output += BRAILLE_ALPHABET_SYMBOLS[CAPITAL_FOLLOWS]
            output += BRAILLE_ALPHABET_SYMBOLS[char]
        elif char in ENGLISH_NUMBERS:
            if not does_number_follows:
                does_number_follows = True
                output += BRAILLE_ALPHABET_SYMBOLS[NUMBER_FOLLLOWS]
            output += BRAILLE_NUMBERS_SYMBOLS[char]
        elif char == ' ':
            does_number_follows = False
            output += BRAILLE_ALPHABET_SYMBOLS[SPACE]
        else:
            output += BRAILLE_ALPHABET_SYMBOLS[char.upper()]

    return output


def get_symbols_from_braille(braille_text):
    return [
        braille_text[i:i + BRAILLE_SYMBOL_LEN]
        for i in range(0, len(braille_text), BRAILLE_SYMBOL_LEN)
    ]


def translate_to_english(braille_text):
    symbols = get_symbols_from_braille(braille_text)

    does_capital_follows = False
    does_number_follows = False

    output = ''
    for symbol in symbols:
        translated_symbol = BRAILLE_ALPHABET[symbol]

        if translated_symbol == CAPITAL_FOLLOWS:
            does_capital_follows = True
        elif translated_symbol == NUMBER_FOLLLOWS:
            does_number_follows = True
        elif translated_symbol == SPACE:
            does_number_follows = False
            output += ' '
        else:
            if does_capital_follows:
                does_capital_follows = False
                output += translated_symbol.upper()
            elif does_number_follows:
                output += BRAILLE_NUMBERS[symbol]
            else:
                output += translated_symbol.lower()

    return output


def translate(original_text):
    if is_english(original_text):
        return translate_to_braille(original_text)
    elif len(original_text) == 1 and is_braille(original_text[0]):
        return translate_to_english(original_text[0])
    return ''


if __name__ == "__main__":
    argvs = sys.argv
    original_text = argvs[1:]

    print(translate(original_text))
