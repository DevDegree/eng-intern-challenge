import sys

ENGLISH_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
ENGLISH_NUMBERS = set('0123456789')
ENGLISH_CHARACTERS = ENGLISH_LETTERS.union(ENGLISH_NUMBERS)

BRAILLE_CHARACTERS = set('O.')

def is_english(text):
    # TODO: Check if text is English or not
    pass

def is_braille(text):
    # TODO: Check if text is Braille or not
    pass

def translate(text):
    if is_english(text):
        # TODO: Translate to Braille
        pass
    elif is_braille(text):
        # TODO: Translate to English
        pass

if __name__ == "__main__":
    argvs = sys.argv
    text = argvs[1:]

    print(text)
    translate(text)