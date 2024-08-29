from .constants import *

def braille_to_english(text: str) -> str:
    res = ''
    number = False
    upper = False

    for i in range(0, len(text), 6):
        braille = text[i: i+6]

        if braille == NUMBER:
            number = True
        elif braille == UPPERCASE:
            upper = True
        elif number:
            if braille == PUNCTUATION[' ']:
                number = False
                res += ' '
            elif braille == DECIMAL:
                continue
            elif braille == PUNCTUATION['.']:
                res += '.'
            else:
                res += BRAILLE_NUMBERS[braille]
        elif braille in BRAILLE_ALPHABET:
            res += BRAILLE_ALPHABET[braille].upper() if upper else BRAILLE_ALPHABET[braille]
            upper = False
        elif braille in BRAILLE_PUNCTUATION:
            res += BRAILLE_PUNCTUATION[braille]

    return res

def english_to_braille(text: str) -> str:
    res = ''
    number = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                res += UPPERCASE
            res += ALPHABET[char.lower()]
        elif char in NUMBERS:
            if not number:
                number = True
                res += NUMBER

            res += NUMBERS[char]
        elif char in PUNCTUATION:
            if char == ' ' and number:
                number = False
            if char == '.' and number:
                res += DECIMAL

            res += PUNCTUATION[char]

    return res

if __name__ == '__main__':
    import sys
    args = sys.argv
    args.pop(0)

    text = ' '.join(args)
    chars = set(text)

    res = braille_to_english(text) if chars == BRAILLE else english_to_braille(text)

    print(res)