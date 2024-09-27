import sys

# map from letters and numbers to braille
ALPHABET_TO_BRAILLE = {
    "letters": {
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
        ' ': "......"
    },
    "numbers": {
        '0': ".OOO..",
        '1': "O.....",
        '2': "O.O...",
        '3': "OO....",
        '4': "OO.O..",
        '5': "O..O..",
        '6': "OOO...",
        '7': "OOOO..",
        '8': "O.OO..",
        '9': ".OO...",
    },
    "other": {
        "capital": ".....O",
        "number":  ".O.OOO"
    }
}

# invert the map so that we can translate braille back to letter and numbers
BRAILLE_TO_ALPHABET = dict()
BRAILLE_TO_ALPHABET["letters"] = {v: k for k, v in ALPHABET_TO_BRAILLE["letters"].items()}
BRAILLE_TO_ALPHABET["numbers"] = {v: k for k, v in ALPHABET_TO_BRAILLE["numbers"].items()}
BRAILLE_TO_ALPHABET["other"] = {v: k for k, v in ALPHABET_TO_BRAILLE["other"].items()}

# each braille sequence is 6 characters long
BRAILLE_SEQ_LEN = 6


def translate(str):
    translation = ""
    # since we assume the input text will be only letters, numbers or spaces 
    # we can just check for a period to verify it's braille
    if '.' in str:
        translation = braille_to_alphabet(str)
    else:
        translation = alphabet_to_braille(str)
    # output to console
    print(translation)


def braille_to_alphabet(braille):
    # variable to track when braille sequences refer to numbers vs letters
    # signalled by the "number follows" braille sequence
    number_mode = False
    # variable to track when we should capitalize the next letter
    # signalled by the "captial follows" braille sequence
    capital_mode = False
    translation = ""

    # assumes the braille is well formed, i.e. each sequence is of length 6
    for i in range(0, len(braille), BRAILLE_SEQ_LEN):
        seq = braille[i:i+BRAILLE_SEQ_LEN]

        if seq in BRAILLE_TO_ALPHABET["other"]:
            if BRAILLE_TO_ALPHABET["other"][seq] == "capital":
                capital_mode = True
            elif BRAILLE_TO_ALPHABET["other"][seq] == "number":
                number_mode = True
        elif seq in BRAILLE_TO_ALPHABET["numbers"] and number_mode:
            translation = translation + BRAILLE_TO_ALPHABET["numbers"][seq]
        elif seq in BRAILLE_TO_ALPHABET["letters"]:
            letter = BRAILLE_TO_ALPHABET["letters"][seq]
            if letter == ' ':
                number_mode = False
            if capital_mode:
                letter = letter.upper()
                capital_mode = False
            translation = translation + letter
        else:
            # can only enter here if the braille sequence is unknown (which should not happen if input is correct)
            print("ERROR")
            return ""

    return translation

def alphabet_to_braille(alphabet):
    # variable to track when we should add the "number follows" braille sequence
    number_mode = False
    translation = ""

    for c in alphabet:
        if c.isnumeric():
            if not number_mode:
                translation = translation + ALPHABET_TO_BRAILLE["other"]["number"]
                number_mode = True
            translation = translation + ALPHABET_TO_BRAILLE["numbers"][c]
        elif c == ' ':
            number_mode = False
            translation = translation + ALPHABET_TO_BRAILLE["letters"][' ']
        elif c.isalpha():
            if c.isupper():
                translation = translation + ALPHABET_TO_BRAILLE["other"]["capital"]
                c = c.lower()
            translation = translation + ALPHABET_TO_BRAILLE["letters"][c]
        else:
            # can only enter here if the character is not a letter or number or space (which should not happen if input is correct)
            print("ERROR")
            return ""

    return translation


if __name__ == '__main__':
    text = " ".join(sys.argv[1:])
    translate(text)
