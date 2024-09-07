
import sys

ENGLISH_TO_BRAILLE = {
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
}

NUMBER_TO_BRAILLE = {
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

SENTENCE_AUGMENT_TO_BRAILLE = {
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO',
    ' ': '......'

}

BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}

BRAILLE_TO_SENTENCE_AUGMENT = {value: key for key,
                               value in SENTENCE_AUGMENT_TO_BRAILLE.items()}

BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}


def is_braille(text):
    if len(text) % 6 != 0:
        return False
    valid_chars = 'O.'
    for char in text:
        if char not in valid_chars:
            return False
    return True


def english_to_braille(text):
    braille = ''
    number = False

    for char in text:
        if char.isupper():
            braille += SENTENCE_AUGMENT_TO_BRAILLE['CAPITAL']
            char = char.lower()
            braille += ENGLISH_TO_BRAILLE[char]

        elif char.isdigit():
            if not number:
                braille += SENTENCE_AUGMENT_TO_BRAILLE['NUMBER']
                number = True
            braille += NUMBER_TO_BRAILLE[char]

        elif char == ' ':
            braille += SENTENCE_AUGMENT_TO_BRAILLE[' ']
            number = False

        else:
            braille += ENGLISH_TO_BRAILLE[char]
    return braille


def braille_to_english(braille):
    text = ''
    capital = False
    number = False
    while braille:
        if braille[:6] in BRAILLE_TO_SENTENCE_AUGMENT:
            if BRAILLE_TO_SENTENCE_AUGMENT[braille[:6]] == 'CAPITAL':
                capital = True
            elif BRAILLE_TO_SENTENCE_AUGMENT[braille[:6]] == 'NUMBER':
                number = True
            elif BRAILLE_TO_SENTENCE_AUGMENT[braille[:6]] == ' ':
                text += ' '
                number = False
            braille = braille[6:]
            continue
        if capital:
            text += BRAILLE_TO_ENGLISH[braille[:6]].upper()
            capital = False
        elif number and braille[:6] in BRAILLE_TO_NUMBER:
            text += BRAILLE_TO_NUMBER[braille[:6]]
        else:
            text += BRAILLE_TO_ENGLISH[braille[:6]]
        braille = braille[6:]
    return text


def translate_text(input_text):
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        translate_text(input_text)
