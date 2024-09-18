import sys

ENGLISH_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
ENGLISH_NUMBERS = set('0123456789')
ENGLISH_CHARACTERS = ENGLISH_LETTERS.union(ENGLISH_NUMBERS)

BRAILLE_CHARACTERS = set('O.')

CAPITAL_FOLLOWS = 'CAPITAL_FOLLOWS'
DECIMAL_FOLLOWS = 'DECIMAL_FOLLOWS'
NUMBER_FOLLLOWS = 'NUMBER_FOLLLOWS'
SPACE = 'SPACE'

def is_english(text):
    for word in text:
        if not set(word.lower()).issubset(ENGLISH_CHARACTERS):
            return False
    return True

def is_braille(text):
    if len(text) != 1:
        return False
    if not set(text[0]).issubset(BRAILLE_CHARACTERS):
        return False
    return True

def translate_to_braille(text):
    # TODO: Implement translate to Braille
    pass

def translate_to_english(text):
    # TODO: Implement translate to English
    pass

def translate(text):
    if is_english(text):
        return translate_to_braille(text)
    elif is_braille(text):
        return translate_to_english(text)

if __name__ == "__main__":
    argvs = sys.argv
    text = argvs[1:]

    print(text)
    translate(text)