import sys

ENGLISH_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
ENGLISH_NUMBERS = set('0123456789')
ENGLISH_CHARACTERS = ENGLISH_LETTERS.union(ENGLISH_NUMBERS)

BRAILLE_CHARACTERS = set('O.')

def translate(text):
    # TODO: if English then translate to Braille
    # TODO: if Braille then translate to English
    pass

if __name__ == "__main__":
    argvs = sys.argv
    text = argvs[1:]

    print(text)
    translate(text)